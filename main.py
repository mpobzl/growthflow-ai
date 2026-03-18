from src.utils import load_data, save_data
from src.scoring import apply_scoring
from src.segmentation import apply_segmentation
from src.action import apply_action
from src.messaging import apply_messaging


def run_pipeline():

    print("Carregando dados...")
    df = load_data("data/leads.csv")

    print("\nAplicando scoring...")
    df = apply_scoring(df)

    print("\nAplicando segmentação...")
    df = apply_segmentation(df)

    print("\nDefinindo ações...")
    df = apply_action(df)

    print("\nGerando mensagens personalizadas...")
    df = apply_messaging(df)

    # 🔥 Ordenar por prioridade (score)
    df = df.sort_values(by="score", ascending=False)

    print("\nResultado final:\n")
    print(df)

    save_data(df, "outputs/leads_final.csv")


if __name__ == "__main__":
    run_pipeline()