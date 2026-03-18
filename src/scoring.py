def calculate_score(row):

    score = 0

    # Interesse
    interesse_score = {
        "Alto": 50,
        "Médio": 30,
        "Baixo": 10
    }

    score += interesse_score.get(row["interesse"], 0)

    # Orçamento
    if row["orcamento"] > 50000:
        score += 50
    elif row["orcamento"] > 20000:
        score += 30

    # Origem (intenção)
    if row["origem"] in ["Google", "WhatsApp"]:
        score += 20

    return score


def apply_scoring(df):
    df["score"] = df.apply(calculate_score, axis=1)
    return df