from api813bet import Bet813API

# Configurações
email = "seu_email_aqui"
senha = "sua_senha_aqui"

# Inicializar API
api = Bet813API(username=email, password=senha)

# Autenticar
print("Autenticando...")
auth = api.auth()
print(f"Status da autenticação: {auth}")

# Obter doubles
print("\nObtendo últimos doubles...")
doubles = api.get_last_doubles()
print(f"Doubles: {doubles}")

# Obter crashes
print("\nObtendo últimos crashes...")
crashes = api.get_last_crashs()
print(f"Crashes: {crashes}") 