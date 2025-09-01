import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Análisis de Videojuegos", layout="wide")

st.title("Análisis de Videojuegos para la Tienda Ice")

df = pd.read_csv("games.csv")

df.columns = df.columns.str.lower()

df['year_of_release'] = pd.to_numeric(df['year_of_release'], errors='coerce')

df['total_sales'] = df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

st.sidebar.header("Filtro por año de lanzamiento")
years = sorted(df['year_of_release'].dropna().unique())
years_int = [int(year) for year in years]
selected_year = st.sidebar.selectbox("Selecciona un año", years_int)

filtered_df = df[df['year_of_release'] == float(selected_year)]

st.subheader(f"Juegos lanzados en {selected_year}")
st.dataframe(
    filtered_df[['name', 'platform', 'genre', 'total_sales']]
    .sort_values(by='total_sales', ascending=False)
    .reset_index(drop=True)
)

st.subheader("Ventas por plataforma")
sales_by_platform = filtered_df.groupby('platform')['total_sales'].sum().sort_values(ascending=False)

fig, ax = plt.subplots()
sales_by_platform.plot(kind='bar', ax=ax, color='skyblue')
ax.set_ylabel("Ventas (millones)")
ax.set_xlabel("Plataforma")
ax.set_title(f"Ventas por plataforma en {selected_year}")
st.pyplot(fig)





