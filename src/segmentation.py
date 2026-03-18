def classify_segment(score):

    if score >= 100:
        return "Hot"
    elif score >= 60:
        return "Warm"
    else:
        return "Cold"


def apply_segmentation(df):
    df["segmento"] = df["score"].apply(classify_segment)
    return df