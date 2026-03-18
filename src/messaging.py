def generate_message(row):

    nome = row["nome"]
    segmento = row["segmento"]

    if segmento == "Hot":
        return f"{nome}, vi que você demonstrou bastante interesse. Vamos conversar hoje?"

    elif segmento == "Warm":
        return f"{nome}, tenho uma oportunidade que pode fazer sentido para você. Quer saber mais?"

    else:
        return f"{nome}, separei um conteúdo que pode te ajudar. Posso te enviar?"


def apply_messaging(df):
    df["mensagem"] = df.apply(generate_message, axis=1)
    return df