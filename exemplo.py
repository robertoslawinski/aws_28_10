# exemplo.py
import os, sys

print("Nome do script:", sys.argv[0])
print("Argumentos:", sys.argv[1:])
print("Número de argumentos:", len(sys.argv) - 1)

# Inputs vindos da linha de comando (passados pelo workflow)
# Ex.: python exemplo.py <NOME> <APELIDO> <CONFIRME> <CIDADE>
if len(sys.argv) >= 5:
    nome, apelido, confirme, cidade = sys.argv[1:5]
    print(f"nome={nome}, apelido={apelido}, confirme={confirme}, cidade={cidade}")
else:
    print("⚠️ Dica: rode com 4 argumentos: <nome> <apelido> <confirme> <cidade>")

# Também mostramos variáveis de ambiente (se precisar no futuro)
print("ENV_GITHUB_ENVIRONMENT =", os.getenv("GITHUB_ENVIRONMENT"))
