# 🧩 Estudo de Microserviços - Bootcamp Luizalabs

Este projeto foi desenvolvido como parte dos estudos sobre **arquitetura de microserviços**, no **Bootcamp Luizalabs**.  
O objetivo é entender o fluxo de comunicação assíncrona entre serviços usando **RabbitMQ**, **FastAPI** e **SQLite3**.

---

## 🚀 Visão Geral

O sistema é composto por dois microserviços principais:

1. **API Producer (FastAPI)**  
   Responsável por receber requisições HTTP e enviar mensagens (dicts JSON) para uma fila do **RabbitMQ**.

2. **Worker Consumer (Python)**  
   Responsável por consumir as mensagens da fila, processá-las e armazenar os dados em um banco de dados **SQLite3**.

---

## 🧠 Tecnologias Utilizadas

- 🐍 **Python 3.12+**
- ⚡ **FastAPI**
- 🐇 **RabbitMQ**
- 🗃️ **SQLite3**
- 🔄 **pika** (para comunicação com o RabbitMQ)
- 📦 **Docker** *(opcional para subir o RabbitMQ)*
