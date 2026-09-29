# Automação em Python para relatórios administrativos

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow.svg)](https://github.com/pazoliveira/admin-workflow-automation)

> Automação em Python desenvolvida para substituir a consolidação manual de planilhas administrativas por um pipeline automatizado de ingestão, limpeza e geração de relatórios

---

## Sobre o projeto

Este projeto automatiza a burocracia: ele lê planilhas brutas de tarefas e finanças, limpa inconsistências e exporta relatórios pronto para auxiliar na tomada de uma decisão administrativa.

---

## Perguntas

* Quanto tempo de trabalho manual de consolidação de planilhas conseguimos economizar por semana?
* Qual a taxa de registros incompletos ou formatados incorretamente nas planilhas administrativas de entrada?
* Quais tarefas ou lançamentos requerem atenção imediata devido a pendências ou erros?

---

## Fontes de dados 
| Fonte | Descrição | 
| --- | --- |
| `data/raw/dados_brutos.csv` | Planilhas brutas contendo registros de tarefas administrativas, custos e status 

---

## Metodologia

O projeto de automação dividido em 3 etapas:

1. **Leitura dos Dados: ** Ingestão automatizada das planilhas brutas recebidas.
2. **Limpeza: ** Preenchimento de células vazias, padronização de textos e identificação de inconsistências.
3. **Geração do Relatório: ** Exportação dos relatórios administrativos consolidados e salvamento na pasta final.

---

## Tecnologias utilizadas

* **Linguagem:** Python 3.10+
* **Bibliotecas principais:** `pandas` (manipulação de planilhas e dados)
* **Visualização:** Relatórios em CSV e registros de status no terminal

---

## Estrutura do repositório

```text
admin-workflow-automation/
├── data/
│   ├── raw/                  # Planilhas brutas de entrada
│   └── processed/            # Relatórios consolidados gerados
├── src/
│   ├── __init__.py           # Identificador de pacote Python
│   ├── extract.py            # Módulo de leitura de planilhas
│   ├── transform.py          # Módulo de limpeza e tratamento
│   ├── load.py               # Módulo de exportação de relatórios
│   └── main.py               # Script principal (orquestrador)
├── .gitignore
├── README.md
└── requirements.txt

```
---

## Como rodar

```bash
git clone https://github.com/pazoliveira/admin-workflow-automation.git
cd admin-workflow-automation
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py

```

## Roadmap

- [x] **1. Extração:** Leitura automatizada das planilhas brutas de entrada (`.csv` / `.xlsx`).
- [ ] **2. Tratamento:** Limpeza de dados, preenchimento de nulos e aplicação de regras de negócio.
- [ ] **3. Visualização e Exportação:** Geração do relatório final consolidado e exibição de métricas operacionais.


## Autor

**Paulo Oliveira** — [LinkedIn](https://www.google.com/search?q=https://linkedin.com/in/pazoliveira) — [GitHub](https://www.google.com/search?q=https://github.com/pazoliveira)

---

## Licença

MIT License
