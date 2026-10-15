# Automação em Python, Excel e Power BI para controle de contratos

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow.svg)

Projeto que substitui a conferência manual de planilhas por três peças:

1. **Planilha Excel** de conferência de horas, com validações e fórmulas protegidas.
2. **Scripts em Python** que cruzam faltas, justificativas e contrato e geram a memória de cálculo do faturamento.
3. **Guia de painel no Power BI** para acompanhar indicadores do setor: telefonia fixa, franquias de telefonia móvel e destinação de resíduos.

> Todos os dados deste projeto são **fictícios**.

## Como rodar

```bash
git clone https://github.com/pazoliveira/admin-workflow-automation.git
cd admin-workflow-automation
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

python src/gerar_dados.py      # (opcional) recria os dados fictícios
python src/main.py             # roda o pipeline e gera data/processed/
python src/gerar_planilha.py   # (opcional) recria a planilha Excel
python -m unittest discover -s tests -v   # testes das regras
```

## Estrutura

```text
admin-workflow-automation/
├── data/
│   ├── raw/          # entradas fictícias (ponto, justificativas, contratos, telefonia, resíduos)
│   └── processed/    # relatórios gerados
├── excel/            # planilha de conferência de horas
├── powerbi/          # guia do painel
├── src/
│   ├── extract.py    # leitura das planilhas
│   ├── transform.py  # validações, cruzamento e cálculo
│   ├── load.py       # exportação
│   ├── main.py       # executa o pipeline
│   ├── gerar_dados.py
│   └── gerar_planilha.py
├── tests/
├── requirements.txt
└── README.md
```

## Roadmap

- [ ] Pipeline em Python (validação, cruzamento e cálculo da glosa)
- [ ] Planilha Excel de conferência
- [ ] Painel no Power BI

## Autor

**Diego Paz** · [LinkedIn](https://linkedin.com/in/pazoliveira) · [GitHub](https://github.com/pazoliveira)

## Licença

MIT

