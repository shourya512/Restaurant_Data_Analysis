# Restaurant Data Analysis Dashboard

An interactive data analysis dashboard built with **Streamlit** that explores restaurant data, visualizes trends, and demonstrates end-to-end data analysis and feature engineering skills.

---

## 🚀 Live Demo

👉 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/Shourya512/Restaurant_Data_Analysis)

---

## 📌 Features

- **Data Exploration** — Check missing values and data types across the dataset
- **Descriptive Analysis** — View summary statistics (mean, median, std, min, max) for all numeric columns
- **Geospatial Analysis** — Map restaurants by city using Latitude and Longitude
- **Table Booking Analysis** — Percentage breakdown of restaurants offering table booking
- **Price Range Analysis** — Bar chart showing distribution across price tiers
- **Feature Engineering** — Create new features like restaurant name length from existing data

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading and manipulation |
| Matplotlib | Charts and visualizations |
| Streamlit | Interactive web dashboard |
| Jupyter Notebook | Exploratory data analysis (6 notebooks) |
| Hugging Face Spaces | Deployment platform |

---

## 📁 Project Structure

```
Restaurant_Data_Analysis/
│
├── Dataset.csv                          # Restaurant dataset (source data)
├── app.py                               # Streamlit dashboard
├── Data_Exploration.ipynb               # Missing values, data types
├── Descriptive_Analysis.ipynb           # Statistical summary
├── Geospatial_Analysis.ipynb            # Location-based analysis
├── Table_Booking_Online_Delivery.ipynb  # Booking and delivery trends
├── Price_Range_Analysis.ipynb           # Price distribution
├── Feature_Engineering.ipynb           # New feature creation
└── requirment.txt                       # Project dependencies
```

---

## 📊 Dataset

The dashboard uses `Dataset.csv` included in this repository. Key columns:

| Column | Description |
|---|---|
| `Restaurant Name` | Name of the restaurant |
| `City` | City where the restaurant is located |
| `Latitude` & `Longitude` | Geographic coordinates for mapping |
| `Has Table booking` | Whether the restaurant offers table booking |
| `Price range` | Affordability tier (1–4) |

No upload needed — the dataset is fully integrated into the dashboard.

---

## ⚙️ Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/shourya512/Restaurant_Data_Analysis.git
cd Restaurant_Data_Analysis
```

**2. Install dependencies**
```bash
pip install -r requirment.txt
```

**3. Run the dashboard**
```bash
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
pandas
matplotlib
```

---

## 🌐 Deployment

Deployed on **Hugging Face Spaces** for stable hosting with no setup required. All sections are preloaded — open the live link and explore instantly.

---

## 🙋 Author

**Shourya Parashar** — [GitHub](https://github.com/shourya512)
