import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# --------------------------
# Styling
# --------------------------
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Restaurant Analytics", layout="wide")

st.title("🍽️ Restaurant Data Analysis Dashboard")

# --------------------------
# Load default dataset
# --------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(BASE_DIR, "dataset.csv")

try:
    df = pd.read_csv(dataset_path)
    st.success("Default dataset loaded ✅")
except FileNotFoundError:
    df = None
    st.error(f"Default dataset not found at {dataset_path}")

if df is not None:
    st.subheader("📊 Dataset Overview")
    st.write(df.head())
    st.write("Shape:", df.shape)

    # --------------------------
    # Expandable Sections
    # --------------------------

    # 1️⃣ Data Exploration
    with st.expander("🔍 Data Exploration"):
        st.write("Missing Values:")
        st.write(df.isnull().sum())
        st.write("Data Types:")
        st.write(df.dtypes)

    # 2️⃣ Descriptive Analysis
    with st.expander("📈 Descriptive Analysis"):
        st.write(df.describe())

    # 3️⃣ Geospatial Analysis
    with st.expander("🌍 Geospatial Analysis"):
        if "Latitude" in df.columns and "Longitude" in df.columns and "City" in df.columns:
            city = st.selectbox("Select City", df["City"].dropna().unique())
            filtered_df = df[df["City"] == city]
            map_data = filtered_df.rename(columns={"Latitude": "lat", "Longitude": "lon"})
            st.map(map_data)
        else:
            st.warning("Latitude/Longitude or City columns not found.")

    # 4️⃣ Table Booking Analysis
    with st.expander("📦 Table Booking Analysis"):
        if "Has Table booking" in df.columns:
            st.write(df["Has Table booking"].value_counts(normalize=True) * 100)
        else:
            st.warning("'Has Table booking' column not found.")

    # 5️⃣ Price Range Analysis
    with st.expander("💰 Price Range Analysis"):
        if "Price range" in df.columns:
            st.bar_chart(df["Price range"].value_counts())
        else:
            st.warning("'Price range' column not found.")

    # 6️⃣ Feature Engineering
    with st.expander("⚙️ Feature Engineering"):
        if "Restaurant Name" in df.columns:
            df["Name Length"] = df["Restaurant Name"].astype(str).apply(len)
            st.write(df[["Restaurant Name", "Name Length"]].head())
        else:
            st.warning("'Restaurant Name' column not found.")