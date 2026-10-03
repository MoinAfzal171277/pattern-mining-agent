import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Pattern Mining Agent",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 Pattern Mining Agent")
st.write(
    "Discover potentially meaningful patterns, relationships, "
    "and unusual observations in your dataset."
)

st.info(
    "Upload a CSV or Excel file to begin your analysis."
)

uploaded_file = st.file_uploader(
    "Upload your dataset",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("Dataset uploaded successfully!")

        st.subheader("1. Dataset Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric(
            "Missing Values",
            int(df.isna().sum().sum())
        )

        st.subheader("2. Data Preview")
        st.dataframe(df.head(20), use_container_width=True)

        st.subheader("3. Column Information")

        profile = pd.DataFrame({
            "Data Type": df.dtypes.astype(str),
            "Missing Values": df.isna().sum(),
            "Unique Values": df.nunique()
        })

        st.dataframe(profile, use_container_width=True)

        st.subheader("4. Descriptive Statistics")

        st.dataframe(
            df.describe(include="all").T,
            use_container_width=True
        )

        numeric_df = df.select_dtypes(include=np.number)

        if numeric_df.shape[1] >= 2:
            st.subheader("5. Correlation Analysis")

            correlation = numeric_df.corr(
                method="pearson"
            )

            st.dataframe(
                correlation.round(3),
                use_container_width=True
            )

            st.caption(
                "Correlation indicates association, not necessarily causation."
            )
        else:
            st.warning(
                "At least two numeric columns are needed "
                "for correlation analysis."
            )

        st.subheader("6. Download Dataset Profile")

        csv_data = profile.to_csv().encode("utf-8")

        st.download_button(
            label="Download Column Profile",
            data=csv_data,
            file_name="dataset_profile.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"Could not analyze the uploaded file: {e}")
