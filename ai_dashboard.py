import pandas as pd
import streamlit as st
import plotly.express as px
from io import StringIO

st.set_page_config(layout="wide")
file_path = 'ai.csv'

# === Load Data ===
@st.cache_data
def load_data(path):
    import csv
    with open(path, 'r', encoding='utf-8-sig') as f:
        sample = f.read(2048)
        delimiter = csv.Sniffer().sniff(sample).delimiter
    df = pd.read_csv(path, delimiter=delimiter, encoding='utf-8-sig', engine='python', on_bad_lines='skip')
    df.columns = df.columns.str.strip().str.replace(r'\s+', ' ', regex=True)
    return df

df = load_data(file_path)

st.title("📊 AI & Agile Strategy Dashboard")
st.markdown("Explore insights from survey data on AI, Agile, and company strategy.")

# === Sidebar Filters & Navigation ===
st.sidebar.header("🔎 Filters")
company_size_col = 'What is the size of your company?'
company_sizes = df[company_size_col].dropna().unique().tolist() if company_size_col in df else []
selected_size = st.sidebar.selectbox("Select Company Size:", options=["All"] + company_sizes)

# New: Sidebar menu for sections
page = st.sidebar.radio(
    "Navigate",
    options=["Charts", "Benefits", "Challenges", "Raw Data"]
)

filtered_df = df.copy()
if selected_size != "All":
    filtered_df = filtered_df[filtered_df[company_size_col] == selected_size]

# === Show content based on sidebar selection ===

if page == "Charts":
    # AI Usage in Strategic Planning
    ai_usage_col = 'To what extent is AI currently used in your company’s strategic planning?'
    if ai_usage_col in filtered_df.columns:
        filtered_df[ai_usage_col] = pd.to_numeric(filtered_df[ai_usage_col], errors='coerce')
        usage_counts = filtered_df[ai_usage_col].dropna().value_counts().sort_index()
        fig1 = px.bar(
            x=usage_counts.index,
            y=usage_counts.values,
            labels={'x': 'AI Usage Level (1–5)', 'y': 'Number of Companies'},
            title='AI Usage in Strategic Planning',
            text=usage_counts.values
        )
        fig1.update_layout(xaxis=dict(dtick=1), yaxis_title="Number of Companies")
        st.plotly_chart(fig1, use_container_width=True)

    # Agile Frameworks Used
    agile_col = 'Which Agile framework(s) does your organization follow?'
    if agile_col in filtered_df.columns:
        frameworks = filtered_df[agile_col].dropna().str.split(',').explode().str.strip()
        counts = frameworks.value_counts().sort_values(ascending=True)
        fig2 = px.bar(
            x=counts.values,
            y=counts.index,
            orientation='h',
            labels={'x': 'Mentions', 'y': 'Agile Framework'},
            title='Agile Frameworks Used',
            text=counts.values
        )
        st.plotly_chart(fig2, use_container_width=True)

    # AI Technologies Used
    ai_tech_col = 'Which AI technologies are used in your company?'
    if ai_tech_col in filtered_df.columns:
        techs = filtered_df[ai_tech_col].dropna().str.split(',').explode().str.strip()
        tech_counts = techs.value_counts().sort_values(ascending=True)
        fig3 = px.bar(
            x=tech_counts.values,
            y=tech_counts.index,
            orientation='h',
            labels={'x': 'Mentions', 'y': 'AI Technology'},
            title='AI Technologies in Use',
            text=tech_counts.values
        )
        st.plotly_chart(fig3, use_container_width=True)

elif page == "Benefits":
    st.header("💬 Greatest Benefits of Using AI")
    benefit_col = 'In your opinion, what is the greatest benefit of using AI in strategy development?'
    if benefit_col in filtered_df.columns:
        responses = filtered_df[benefit_col].dropna().astype(str).reset_index(drop=True)
        for i, response in responses.items():
            st.markdown(f"**{i+1}.** {response}")
    else:
        st.info("No benefit responses available.")

elif page == "Challenges":
    st.header("💬 Challenges in Implementing AI into Agile")
    challenges_col = 'Have you encountered any challenges when implementing AI into your Agile processes? Please describe.'
    if challenges_col in filtered_df.columns:
        responses = filtered_df[challenges_col].dropna().astype(str).reset_index(drop=True)
        for i, response in responses.items():
            st.markdown(f"**{i+1}.** {response}")
    else:
        st.info("No challenge responses available.")

elif page == "Raw Data":
    st.header("📄 Filtered Data Table")
    st.dataframe(filtered_df)

    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv_data,
        file_name='filtered_data.csv',
        mime='text/csv'
    )
