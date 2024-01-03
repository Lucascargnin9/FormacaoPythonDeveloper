import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print(endereco)

rede = '192.168.0.0/4'

enderecor = ipaddress.ip_network(rede,strict= False)

for ip in enderecor:
    print(rede)

