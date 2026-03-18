import streamlit as st
import pandas as pd

from src.scoring import apply_scoring
from src.segmentation import apply_segmentation
from src.action import apply_action
from src.messaging import apply_messaging

st.set_page_config(page_title="GrowthFlow AI", layout="wide")

st.title("🚀 GrowthFlow AI - Lead Automation Dashboard")

st.markdown("Sistema de priorização e automação de leads com IA")

uploaded_file = st.file_uploader("📂 Faça upload do CSV de leads", type=["csv"])

# 🔥 NOVO: carregar exemplo automaticamente
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.info("Exibindo exemplo padrão. Faça upload para usar seus dados.")
    df = pd.read_csv("data/leads.csv")

# pipeline
df = apply_scoring(df)
df = apply_segmentation(df)
df = apply_action(df)
df = apply_messaging(df)

df = df.sort_values(by="score", ascending=False)

st.subheader("📊 Leads Processados")
st.dataframe(df, use_container_width=True)

# métricas
st.subheader("📈 Distribuição de Leads")

col1, col2, col3 = st.columns(3)

col1.metric("🔥 Hot", len(df[df["segmento"] == "Hot"]))
col2.metric("🟡 Warm", len(df[df["segmento"] == "Warm"]))
col3.metric("🔵 Cold", len(df[df["segmento"] == "Cold"]))