# API OneBra

API não oficial para interagir com a plataforma OneBra. Esta API permite acessar dados de jogos como Doubles e Crashes de forma automatizada.

## Características

- ✅ Autenticação automática com email/senha ou token
- 📊 Histórico de Doubles (🔴 1-7 | ⚫️ 8-14 | ⚪️ 15)
- 📈 Histórico de Crashes (⬛️ <2x | 🟩 >=2x)
- 🔄 Sistema de retry automático para falhas de conexão
- 🔒 Headers personalizados para segurança
- 🌐 Suporte a proxy

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/AdminhuDev/api_onebra.git
cd api_onebra
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

### Exemplo Básico

```python
from api_onebra import OnebraAPI

# Configuração inicial
token = "SEU_TOKEN_ONEBRA_AQUI"
email = "SEU_EMAIL_ONEBRA_AQUI"
password = "SUA_SENHA_ONEBRA_AQUI"

# Inicializar API
api = OnebraAPI(email, password, token)

# Autenticar
authentication = api.auth()

# Obter últimos doubles
doubles = api.get_last_doubles()
print("Últimos doubles:", doubles)

# Obter últimos crashes
crashes = api.get_last_crashs()
print("Últimos crashes:", crashes)
```

### Retorno dos Dados

#### Doubles
```python
{
    "items": [
        {"color": "🔴", "value": "5"},  # Vermelho (1-7)
        {"color": "⚫️", "value": "9"},  # Preto (8-14)
        {"color": "⚪️", "value": "15"}  # Branco (15)
    ]
}
```

#### Crashes
```python
{
    "items": [
        {"color": "⬛️", "value": 1.39},  # Abaixo de 2x
        {"color": "🟩", "value": 2.33}   # 2x ou maior
    ]
}
```

### Configurações Avançadas

- **Retry Automático**: 
  - 3 tentativas automáticas
  - Backoff factor: 1
  - Status codes: 429, 500, 502, 503, 504, 104

- **Headers Personalizados**:
  - User-Agent padrão configurado
  - Possibilidade de adicionar headers customizados

- **Proxy**:
  - Suporte a proxy via atributo `proxies`
  - Configurável por instância

## Contribuindo

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes. 

