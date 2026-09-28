import streamlit as st

pages = {
    "Main": [
        st.Page("Overview.py", title="Overview", icon="🏠"),
    ],
    "Analysis": [
        st.Page("pages/1_Dataset.py", title="Dataset", icon="📂"),
        st.Page("pages/2_AI_Analysis.py", title="AI Analysis", icon="🤖"),
        st.Page("pages/3_Data_Quality.py", title="Data Quality", icon="🧹"),
        st.Page("pages/4_Anomaly_Insights.py", title="Anomaly Insights", icon="🔍"),
        st.Page("pages/5_Visualization.py", title="Visualization", icon="📊"),
        st.Page("pages/6_AI_Insights.py", title="AI Insights", icon="💡"),
    ],
}

pg = st.navigation(pages)

pg.run()