import os #importar o modulo ou bibioteca os (integra os programas e recursos do s.o)

# imprimimndo "#" 60 vezes
print("#" * 60)

ip_ou_host = input("Digite o IP ou Host a ser verificado: ")
print("-" * 60)

os.system('ping -n 4 {}'.format(ip_ou_host)) ## chamando system da bibioteca os - comando ping


