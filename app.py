import sys
print("Nome do script:", sys.argv[0])
print("Argumentos:", sys.argv[1:])
print("Número de argumentos:", len(sys.argv) - 1)
if len(sys.argv) < 3:
    print("⚠️ Passe ao menos 2 argumentos. Ex.: python app.py 'Alice' 42")
    sys.exit(1)
for i, v in enumerate(sys.argv[1:], start=1):
    print(f"arg{i} = {v}")
