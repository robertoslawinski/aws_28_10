import yaml
 
with open("db.yml", "r") as f:
    config = yaml.safe_load(f)

print("📌 Conectando ao Banco de Dados...")
print("Servidor:", config["servidor"])
print("Utilizador:", config["utilizador"])
print("Base de Dados:", config["base_de_dados"])
