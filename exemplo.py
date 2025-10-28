import os, sys

print("Nome do script:", sys.argv[0])
print("Argumentos:", sys.argv[1:])
print("Número de argumentos:", len(sys.argv) - 1)

if len(sys.argv) >= 4:
    nome, apelido, cidade, ambiente = sys.argv[1:5]
    print(f"nome={nome}, apelido={apelido}, cidade={cidade}, ambiente={ambiente}")
else:
    print("⚠️ Dica: rode com 4 argumentos: <nome> <apelido> <cidade> <ambiente>")
