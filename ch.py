import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160') # ripemd160 e um algoritmo de hash de 160bits

hash1.update(open(arquivo1, 'rb').read())


hash2 = hashlib.new('ripemd160') # ripemd160 e um algoritmo de hash de 160bits

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} difere do arquivo: {arquivo2}')
    print('O hash do aquivo a.txt: ', hash1.hexdigest())
    print('O hash do arquivo b.txt:', hash2.hexdigest())
else:
    print(f'O arquivo: {arquivo1} e igual ao arquivo: {arquivo2}')
    print('O hash do aquivo a.txt: ', hash1.hexdigest())
    print('O hash do arquivo b.txt:', hash2.hexdigest())
