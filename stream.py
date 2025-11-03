import streamlit as st

# ------------------------------------------------------------
# 🔐 Authentification basique avec Streamlit Secrets
# ------------------------------------------------------------
def login():
    st.title("🔐 Connexion")

    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if (
            username == st.secrets["auth"]["USERNAME"]
            and password == st.secrets["auth"]["PASSWORD"]
        ):
            st.session_state["authenticated"] = True
            st.success("Connexion réussie 🎉")
            st.rerun()
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")

# ------------------------------------------------------------
# 🚀 Application principale
# ------------------------------------------------------------
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    st.sidebar.button("Se déconnecter", on_click=lambda: st.session_state.update({"authenticated": False}))
    st.title("Bienvenue dans ton application sécurisée 🚀")
    st.write("Voici le contenu de ton app Streamlit privée.")

st.set_page_config(page_title="Tableau de bord Power BI", layout="wide")

st.title("Mon tableau de bord Power BI")

# Lien Power BI public ou iframe
powerbi_iframe = """
<iframe title="Dashboard_AESMA_daily_New" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=ce04f5e8-9e59-4f46-aaac-8178ca8f8136&autoAuth=true&ctid=70c9c52f-2483-473b-afd8-1627b7563e5b&actionBarEnabled=true&reportCopilotInEmbed=true" frameborder="0" allowFullScreen="true"></iframe>
"""

# Affichage dans Streamlit
st.markdown(powerbi_iframe, unsafe_allow_html=True)
