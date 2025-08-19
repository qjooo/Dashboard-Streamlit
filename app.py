import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]

# Paleta de tons de rosa 
rose_colors = ["#EEC9D2", "#E7BFC8", "#D9A7B5", "#C98DA1", "#B97C8A", "#A86A7A"]
# Paleta de tons de azul
blue_cyan_palette = ["#B3E5FC", "#81D4FA", "#4FC3F7", "#29B6F6", "#03A9F4", "#0288D1"]


col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(
    df_filtered,
    x="Date",
    y="Total",
    color="City",
    title="Faturamento por dia",
    color_discrete_sequence=blue_cyan_palette # rose_colors
)
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(
    df_filtered,
    x="Date",
    y="Product line",
    color="City",
    title="Faturamento por tipo de produto",
    orientation="v",
    color_discrete_sequence=blue_cyan_palette # rose_colors
)
col2.plotly_chart(fig_prod, use_container_width=True)

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(
    city_total,
    x="City",
    y="Total",
    color="City",
    title="Faturamento por filial",
    color_discrete_sequence=blue_cyan_palette # rose_colors
)
col3.plotly_chart(fig_city, use_container_width=True)

fig_kind = px.pie(
    df_filtered,
    values="Total",
    names="Payment",
    title="Faturamento por tipo de pagamento",
    color_discrete_sequence=blue_cyan_palette # rose_colors
)
col4.plotly_chart(fig_kind, use_container_width=True)

city_total_rating = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(
    city_total_rating,
    y="Rating",
    x="City",
    color="City",
    title="Avaliação",
    color_discrete_sequence=blue_cyan_palette # rose_colors
)
col5.plotly_chart(fig_rating, use_container_width=True)
