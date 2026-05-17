# Tech Skills Trend Dashboard

Este projeto é um **dashboard em Streamlit** que analisa descrições de vagas de emprego e identifica as **habilidades (skills) de tecnologia** mais citadas, como Cloud, Data, DevOps e Desenvolvimento.

O objetivo é visualizar quais tecnologias estão sendo mais exigidas no mercado com base em dados de vagas.

## Funcionalidades

- Carrega um dataset de vagas a partir de um arquivo CSV
- Permite filtrar vagas por período (data de postagem)
- Conta quantas vezes cada habilidade aparece nas descrições
- Exibe um gráfico com as 10 skills mais citadas
- Mostra a tabela do dataset filtrado
- Mostra o ranking completo das habilidades analisadas

## Tecnologias Utilizadas

- Python
- Pandas
- Streamlit
- Plotly

## Estrutura do Projeto

```text
tech-skills-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
│
└── data/
    └── jobs.csv
```

## Como Executar

**1. Instalar dependências**

```bash
pip install -r requirements.txt
```

**2. Rodar o dashboard**

```bash
streamlit run app.py
```

O Streamlit abrirá no navegador em:

```
http://localhost:8501
```

## Dataset

Nesta primeira versão, o dataset utilizado é um arquivo CSV de exemplo (`data/jobs.csv`) contendo descrições fictícias de vagas.

Em versões futuras, o projeto será expandido para utilizar datasets reais (ex: Kaggle) e automatizar a coleta de dados.

## Próximas Melhorias (Roadmap)

- Utilizar um dataset real do Kaggle
- Criar categorias de skills (Cloud / Data / Backend / DevOps)
- Adicionar gráficos de tendência ao longo do tempo
- Automatizar atualização do dataset com GitHub Actions
- Fazer deploy do dashboard online

---

Criado por **Taciana Couto**
