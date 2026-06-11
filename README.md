# 📊 Automacao-Excel

## 📋 Sobre o Projeto

Projeto desenvolvido em Python para automatizar a análise de dados de presença de funcionários armazenados em uma planilha do Google Sheets.

O sistema identifica automaticamente o funcionário com maior número de faltas e o funcionário com melhor frequência, enviando e-mails personalizados para cada um através da automação do Gmail.

Este projeto foi criado com o objetivo de praticar automação de tarefas, manipulação de planilhas, análise de dados e integração entre diferentes ferramentas.

## 🚀 Tecnologias Utilizadas

* Python
* Pandas
* Google Sheets API
* Gspread
* Google Service Account
* PyAutoGUI
* Pyperclip

## ⚙️ Funcionalidades

* Leitura automática de dados em uma planilha do Google Sheets
* Conversão dos dados para DataFrame utilizando Pandas
* Identificação do funcionário mais faltoso
* Identificação do funcionário mais presente
* Busca automática dos e-mails cadastrados
* Abertura automática do Gmail
* Envio automático de mensagem de advertência
* Envio automático de mensagem de reconhecimento

## 📊 Regras de Negócio

### Funcionário mais faltoso

O sistema localiza o colaborador com maior quantidade de registros de falta e envia uma mensagem solicitando melhoria na frequência.

### Funcionário mais presente

O sistema identifica o colaborador com melhor presença e envia uma mensagem de reconhecimento pelo desempenho.

## 🛠️ Como Executar

### Instalar Dependências

```bash
pip install pandas
pip install gspread
pip install google-auth
pip install pyautogui
pip install pyperclip
```

### Configurar Credenciais

1. Criar um projeto no Google Cloud.
2. Ativar a Google Sheets API.
3. Criar uma Service Account.
4. Baixar o arquivo JSON de credenciais.
5. Salvar o arquivo na raiz do projeto.

### Executar

```bash
python main.py
```

## 📚 Conceitos Praticados

* Automação de Processos
* Manipulação de Planilhas
* Integração com APIs
* Tratamento de Dados com Pandas
* Automação de Navegador
* Envio Automatizado de E-mails
* Leitura e Escrita de Dados

## 🎯 Objetivo do Projeto

Projeto desenvolvido para praticar automação de tarefas corporativas utilizando Python, reduzindo atividades manuais relacionadas ao acompanhamento de frequência de colaboradores.

## 📷 Demonstração

Adicionar aqui um print da planilha utilizada no projeto.

## 👨‍💻 Autor

André Felipe da Silva Leal

Estudante de Análise e Desenvolvimento de Sistemas.
