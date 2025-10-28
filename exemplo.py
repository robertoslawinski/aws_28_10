import sys
print("Nome do script:", sys.argv[0])
print("Argumentos:", sys.argv[1:])
print("Número de argumentos:", len(sys.argv) - 1)

if len(sys.argv) < 5:
    print("⚠️ Dica: rode com 4 argumentos: <nome> <apelido> <confirme> <cidade>")
    sys.exit(0)

nome, apelido, confirme, cidade = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
print("nome =", nome)
print("apelido =", apelido)
print("confirme =", confirme)
print("cidade =", cidade)
