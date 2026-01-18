# Python Data Ingestion to AWS S3

## 📌 Visão Geral
Este projeto demonstra um pipeline simples de **ingestão de dados**, desenvolvido com foco em **Engenharia de Dados**.

O pipeline realiza:
- Consumo de dados a partir de uma **API pública**
- Transformação básica utilizando **Pandas**
- Persistência local em formato **CSV**
- Upload dos dados para a **AWS S3**, organizados em uma estrutura de Data Lake

O objetivo é demonstrar conceitos fundamentais de ingestão, organização de dados e integração com serviços cloud.

---

## 🧱 Arquitetura do Pipeline

API Pública  
↓  
Python (requests + pandas)  
↓  
CSV (local)  
↓  
AWS S3 (camada raw)


## 🧱 Os dados são armazenados no S3 seguindo o padrão:
s3://<bucket-name>/raw/users/dt=YYYY-MM-DD/users_YYYYMMDD_HHMMSS.csv



---

## 🛠️ Tecnologias Utilizadas
- Python 3.10+
- Pandas
- Requests
- Boto3
- AWS S3
- AWS IAM
- Git / GitHub

---

## 📂 Estrutura do Projeto

├── src/  
│ ├── ingest.py  
│ └── config.py  
├── data/  
├── requirements.txt  
└── README.md


---

## ⚙️ Pré-requisitos
- Python 3.10 ou superior
- Conta AWS
- AWS CLI configurado (`aws configure`)
- Permissões para escrita em bucket S3

---

## 🚀 Como Executar o Projeto

### 1 Clonar o repositório
```bash
git clone https://github.com/al-ma-ab/python-data-ingestion.git
cd python-data-ingestion
```
### 2 Clonar o repositório
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3 Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4 Configurar o bucket S3
-- Edite o arquivo src/config.py
```bash
S3_BUCKET = "nome-do-seu-bucket"
```
### 5 Executar ingestão
```bash
python -m src.ingest
```
### ✅ Resultado Esperado

- Um arquivo CSV será criado localmente no diretório data/  
- O mesmo arquivo será enviado para o bucket S3 na camada raw/  
- O caminho completo do arquivo será exibido no terminal após a execução


### 🔒 Segurança

- As credenciais AWS não estão versionadas
- O acesso à AWS é realizado via AWS CLI e IAM
- Nenhuma chave sensível é armazenada no código

### 🎯 Próximos Passos

- Evoluir o pipeline para salvar dados em formato Parquet
- Introduzir logging estruturado
- Implementar tratamento de falhas e retries
- Processar os dados utilizando PySpark
- Criar camada processed no Data Lake


## 👤 Autor

Alexandre Martins  
Engenheiro de Dados
