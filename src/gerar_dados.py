""" Geração de dados para testes """

from pathlib import Path
import pandas as pd

PASTA = Path("data/raw")

FALTAS = [
    ("P001", "2026-09-18"),
    ("P001", "2026-09-15"),
    ("P002", "2026-09-30"),
    ("P002", "2026-09-02")
]

PROBLEMAS = {
    ("P001", "2026-09-14"): ("08:00", "07:00"),  # Saída antes da entrada
    ("P002", "2026-09-15"): ("08:00", "21:00"),  # Jornada acima do limite
    ("P001", "2026-09-25"): ("08:00", "08:00"),  # Entrada e saída no mesmo horário
    ("P002", "2026-09-28"): ("08:00", ""),       # Sem saída registrada
}

def gerar_contratos():
    """ Gera dados de contratos """
    linhas = [
        ["P001", "Serviços gerais", 2200, 22, 8],
        ["P002", "Manutenção", 2420, 22, 8]
    ]
    colunas = ["id_posto", "posto", "valor_mensal", "dias_uteis_mes", "horas_dia"]
    return pd.DataFrame(linhas, columns=colunas)

def gerar_ponto():
    """ Gera dados de ponto """
    linhas = []
    for posto in ["P001", "P002"]:
        for dia in pd.bdate_range("2026-09-01", "2026-09-30"):
            data = dia.strftime("%Y-%m-%d")
            if (posto, data) in FALTAS:
                linhas.append([posto, data, "", "", "falta"])
            else:
                entrada, saida = PROBLEMAS.get((posto, data), ("08:00", "16:00"))
                linhas.append([posto, data, entrada, saida, "presente"])
    linhas.append(["P001", "2026-09-01", "08:00", "16:00", "presente"])  # Registro duplicado
    colunas = ["id_posto", "data", "entrada", "saida", "status"]
    return pd.DataFrame(linhas, columns=colunas)

def gerar_justificativas():
    """ Gera dados de justificativas """
    linhas = [
        ["P001", "2026-09-18", "Atestado médico", "sim"],
        ["P002", "2026-09-30", "Licença médica", "sim"],
        ["P001", "2026-09-15", "Motivo pessoal", "nao"]
    ]
    colunas = ["id_posto", "data", "motivo", "aceita"]
    return pd.DataFrame(linhas, columns=colunas)

def main():
    """ Gera os arquivos de dados """
    PASTA.mkdir(parents=True, exist_ok=True)
    tabelas = {
        "contratos": gerar_contratos(),
        "ponto": gerar_ponto(),
        "justificativas": gerar_justificativas(),
    }
    for nome, df in tabelas.items():
        df.to_csv(PASTA / f"{nome}.csv", index=False)
        print(f"{nome}.csv: {len(df)} linhas")

if __name__ == "__main__":
    main()