import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Tech Skills Dashboard", layout="wide")

st.title("Tech Skills Trend Dashboard")
st.write("Dashboard simples para analisar habilidades mais citadas em descrições de vagas.")

df = pd.read_csv("data/jobs.csv")
df["date_posted"] = pd.to_datetime(df["date_posted"])

skills = [
    "python", "sql", "power bi", "excel", "aws", "azure", "docker", "kubernetes",
    "terraform", "c#", ".net", "linux", "git", "github actions", "react",
    "node.js", "javascript", "java", "spring boot", "postgresql", "machine learning",
    "pandas", "scikit-learn"
]

st.sidebar.header("Filtros")

min_date = df["date_posted"].min()
max_date = df["date_posted"].max()

date_range = st.sidebar.date_input(
    "Selecione o período:",
    [min_date, max_date]
)

filtered_df = df.copy()

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = filtered_df[
        (filtered_df["date_posted"] >= pd.to_datetime(start_date)) &
        (filtered_df["date_posted"] <= pd.to_datetime(end_date))
    ]

skill_counts = {}

for skill in skills:
    skill_counts[skill] = filtered_df["description"].str.lower().str.contains(skill).sum()

skills_df = pd.DataFrame({
    "skill": list(skill_counts.keys()),
    "count": list(skill_counts.values())
}).sort_values("count", ascending=False)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Principais habilidades")
    fig = px.bar(
        skills_df.head(10),
        x="skill",
        y="count",
        title="As principais habilidades mais citadas"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Dataset filtrado")
    st.dataframe(filtered_df)

st.subheader("Ranking completo")
st.dataframe(skills_df)