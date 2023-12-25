from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, select
from sqlalchemy import inspect
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"
    # atributos
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(20))

    # conta relaciona com cliente
    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    # representando cliente
    def __repr__(self):
        return f"cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})"


class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(String(30), nullable=False, default='Conta Corrente')
    agencia = Column(String)
    numero = Column(Integer)

    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)

    # cliente relaciona com conta
    cliente = relationship("Cliente", back_populates="conta")

    # representando conta
    def __repr__(self):
        return f"Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, numero={self.numero})"


print(Cliente.__tablename__)


# conexao com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("cliente"))

print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    lucas = Cliente(
        nome='Lucas C',
        cpf='123456789',
        endereco='Rua Sao Paulo'
    )

    conta_lucas = Conta(tipo='Conta Salario', agencia='2699', numero=12345)
    lucas.conta = [conta_lucas]

    joao = Cliente(
        nome='Joao A',
        cpf='789654321',
        endereco='Rua Rio Janeiro'
    )

    conta_joao = Conta(tipo='Conta Corrente', agencia='6288', numero=54321)
    joao.conta = [conta_joao]

# enviando para o BD
session.add_all([lucas, joao])

session.commit()

stmt = select(Cliente).where(Cliente.nome.in_(['lucas', 'joao']))
for cliente in session.scalars(stmt):
    print(cliente)

stmt_conta = select(Conta).where(Conta.id_cliente.in_([2]))
for conta in session.scalars(stmt_conta):
    print(conta)

stmt_order = select(Cliente).order_by(Cliente.nome.desc())
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(Cliente.nome, Conta.tipo).join_from(Conta, Cliente)
for result in session.scalars(stmt_join):
    print(result)

    
