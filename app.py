import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Data Cleaner & Visualizer", layout="wide")

st.title("🧹 Data Cleaner & 📊 Visualizer")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("🔍 Raw Data")
    st.dataframe(df)

    st.markdown("---")
    
    # Cleaning Options
    st.subheader("🧼 Data Cleaning")
    if st.checkbox("Drop duplicates"):
        df = df.drop_duplicates()
        st.success("Duplicates dropped!")

    if st.checkbox("Drop rows with missing values"):
        df = df.dropna()
        st.success("Missing values removed!")

    st.markdown("### Cleaned Data Preview")
    st.dataframe(df)

    # Data Summary
    st.markdown("### 🧾 Data Summary")
    st.write(df.describe())

    st.markdown("---")
    
    # Visualizations
    st.subheader("📊 Visualizations")

    columns = df.columns.tolist()

    plot_type = st.selectbox("Choose a plot type", ["Histogram", "Bar Chart", "Box Plot", "Heatmap", "Scatter Plot"])

    if plot_type == "Histogram":
        col = st.selectbox("Choose column", columns)
        fig = px.histogram(df, x=col)
        st.plotly_chart(fig)

    elif plot_type == "Bar Chart":
        col = st.selectbox("Choose categorical column", columns)
        fig = px.bar(df[col].value_counts().reset_index(), x="index", y=col)
        st.plotly_chart(fig)

    elif plot_type == "Box Plot":
        col = st.selectbox("Choose numeric column", columns)
        fig = px.box(df, y=col)
        st.plotly_chart(fig)

    elif plot_type == "Heatmap":
        st.write("Correlation Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    elif plot_type == "Scatter Plot":
        x = st.selectbox("X axis", columns)
        y = st.selectbox("Y axis", columns, index=1)
        fig = px.scatter(df, x=x, y=y)
        st.plotly_chart(fig)
