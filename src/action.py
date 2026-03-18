def define_action(segmento):

    if segmento == "Hot":
        return "Contato imediato (time de vendas)"

    elif segmento == "Warm":
        return "Follow-up em até 24h"

    else:
        return "Fluxo de nutrição (marketing)"


def apply_action(df):
    df["acao"] = df["segmento"].apply(define_action)
    return df