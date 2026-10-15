# Automação em Python para relatórios administrativos

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow.svg)](https://github.com/pazoliveira/admin-workflow-automation)

> Automação em Python desenvolvida para substituir a consolidação manual de planilhas administrativas por um pipeline automatizado de ingestão, limpeza, cruzamento de dados e geração de relatórios.

---

## Sobre o projeto

Este projeto automatiza rotinas administrativas e operacionais: ele lê planilhas brutas de registro de horas e justificativas, valida regras lógicas para evitar erros de cálculo, cruza informações de faltas com faturamento contratual e exporta dados prontos para análise e relatórios.

---

## Perguntas

- Quanto tempo de trabalho manual de consolidação de planilhas conseguimos economizar?
- Qual a taxa de registros incompletos ou com inconsistências nas planilhas de entrada?
- Quais ocorrências de faltas ou lançamentos requerem atenção e ajuste no faturamento?

---

## Fontes de dados 

| Fonte | Descrição | 
| --- | --- |
| `data/raw/ponto.csv` | Registros brutos de horas de trabalho, presença e faltas |
| `data/raw/justificativas.csv` | Justificativas de faltas enviadas pela supervisão |

---

## Metodologia

O projeto é dividido em 3 etapas simples:

1. **Leitura dos Dados (`extract.py`):** Ingestão automatizada das planilhas brutas de entrada.
2. **Limpeza e Validação (`transform.py`):** Aplicação de regras lógicas de horas, validação de dados e cruzamento de faltas com justificativas.
3. **Geração do Relatório (`load.py`):** Exportação dos relatórios consolidados de faturamento e base de indicadores (KPIs).

---

## Tecnologias utilizadas

- **Linguagem:** Python 3.10+
- **Bibliotecas principais:** `pandas` (manipulação de planilhas e dados)
- **Visualização:** Relatórios em CSV/Excel e suporte a dashboards (Power BI)

---

## Estrutura do repositório

```text
admin-workflow-automation/
├── data/
│   ├── raw/                 # Planilhas brutas de entrada
│   └── processed/           # Relatórios consolidados gerados
├── src/
│   ├── __init__.py          # Identificador de pacote Python
│   ├── extract.py           # Módulo de leitura de planilhas
│   ├── transform.py         # Módulo de limpeza e validação
│   ├── load.py              # Módulo de exportação de relatórios
│   └── main.py              # Script principal (orquestrador)
├── .gitignore
├── README.md
└── requirements.txt

```

---

## Como rodar

```bash
git clone [https://github.com/pazoliveira/admin-workflow-automation.git](https://github.com/pazoliveira/admin-workflow-automation.git)
cd admin-workflow-automation
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/main.py

```

---

## Roadmap

* [x] **1. Extração:** Leitura automatizada das planilhas brutas de entrada (`.csv` / `.xlsx`).
* [ ] **2. Tratamento:** Limpeza de dados, validação de horas e cruzamento de faltas x justificativas.
* [ ] **3. Visualização e Exportação:** Geração do relatório final consolidado e base de indicadores.

---

## Autor

**Diego Paz** — [LinkedIn](https://linkedin.com/in/pazoliveira) — [GitHub](https://github.com/pazoliveira)

---

## Licença

MIT License

```


