import random
import string

tamanho = int(input('Digite a quantidade de caracteres desejada: '))

chars = string.ascii_letters + string.digits + '!@#$%&*()-=?'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
