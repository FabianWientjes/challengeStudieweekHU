from pathlib import Path
import pandas as pd
import streamlit as st
from loguru import logger
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Company info", layout="wide", page_icon=":bar_chart:")
st.title("Look alike companies")


df=  st.session_state.dataframe

distinct_uuids = df['uuid'].unique()
# Get the first 15 distinct UUIDs
first_15_uuids = distinct_uuids[:15]

options_companies = st.selectbox(
        "Select the reference company",
        first_15_uuids
    )

# Define features
features = ['start_year', 'company_type', 'nace1']  # Replace with actual feature names

# Prepare and standardize features
X = df[features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply k-means clustering
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Identify the reference company
reference_company_id = options_companies #'9ceb2787-7cf3-41d6-b073-c85a5571210d'  # Replace with actual reference company ID
reference_company = df[df['uuid'] == reference_company_id]
reference_features = reference_company[features]

# Standardize reference features
reference_features_scaled = scaler.transform(reference_features)

# Predict the cluster for the reference company
reference_cluster = kmeans.predict(reference_features_scaled)

# Retrieve similar companies
similar_companies = df[df['cluster'] == reference_cluster[0]]

# Output similar companies
#st.text(similar_companies)
st.data_editor(similar_companies)


