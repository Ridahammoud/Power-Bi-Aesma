import streamlit as st

st.set_page_config(page_title="Tableau de bord Power BI", layout="wide")

st.title("Mon tableau de bord Power BI")

# Lien Power BI public ou iframe
powerbi_iframe = """
<iframe title="Dashboard_AESMA_daily_New" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=ce04f5e8-9e59-4f46-aaac-8178ca8f8136&autoAuth=true&ctid=70c9c52f-2483-473b-afd8-1627b7563e5b&actionBarEnabled=true&reportCopilotInEmbed=true" frameborder="0" allowFullScreen="true"></iframe>
"""

# Affichage dans Streamlit
st.markdown(powerbi_iframe, unsafe_allow_html=True)
