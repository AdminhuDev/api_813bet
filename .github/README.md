# 🎲 API 813bet

[![GitHub](https://img.shields.io/badge/GitHub-AdminhuDev-blue?style=flat-square&logo=github)](https://github.com/AdminhuDev)
[![Telegram](https://img.shields.io/badge/Telegram-@Analista__Adminhu-blue?style=flat-square&logo=telegram)](https://t.me/Analista_Adminhu)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

> 🎮 API não oficial para a plataforma 813bet - Acesse dados de Doubles e Crashes de forma automatizada

## 🌟 Destaques

- ✨ Interface Python simples e intuitiva
- 🔄 Retry automático em falhas de conexão
- 🔒 Headers personalizados para segurança
- 🌐 Suporte a proxy
- 📊 Dados em tempo real

## 🎯 Recursos

### 🎲 Double
- 🔴 Vermelho (1-7)
- ⚫️ Preto (8-14)
- ⚪️ Branco (15)

### 📈 Crash
- ⬛️ Abaixo de 2x
- 🟩 2x ou maior

## 💻 Instalação

```bash
# Clone o repositório
git clone https://github.com/AdminhuDev/api_813bet.git
cd api_813bet

# Método 1: Pip Install Local
pip install -e .

# Método 2: Requirements
pip install -r requirements.txt
```

## 🚀 Uso Rápido

```python
from api813bet import Bet813API

# Inicializar e autenticar
api = Bet813API("seu_email", "sua_senha")
api.auth()

# Obter resultados
doubles = api.get_last_doubles()
crashes = api.get_last_crashs()
```

## 🤖 Robô de Sinais

Entre em contato para um robô personalizado:
- ✨ Sinais de Double e Crash
- 🎯 Estratégias personalizadas
- 📱 Integração com Telegram
- 🛠️ Suporte 24/7

## 📞 Contato

- 📱 **Telegram:** [@Analista_Adminhu](https://t.me/Analista_Adminhu)
- 💼 **GitHub:** [AdminhuDev](https://github.com/AdminhuDev)

## 📝 Licença

MIT © [AdminhuDev](https://github.com/AdminhuDev) 