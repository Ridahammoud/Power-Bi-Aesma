import streamlit as st

# ------------------------------------------------------------
# ⚙️ Configuration de la page
# ------------------------------------------------------------
st.set_page_config(page_title="Tableau de bord Power BI", layout="wide")

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
    st.stop()  # 👈 Empêche d'exécuter le reste du script si non connecté
else:
    st.sidebar.button(
        "Se déconnecter",
        on_click=lambda: st.session_state.update({"authenticated": False})
    )

    st.title("Bienvenue dans ton application sécurisée 🚀")
    st.write("Voici le contenu de ton app Streamlit privée.")

    # --------------------------------------------------------
    # 📊 Tableau de bord Power BI
    # --------------------------------------------------------
    powerbi_iframe = """
        <style>
            iframe {
                position: fixed;
                top: 70px; /* espace pour le titre */
                left: 0;
                width: 100%;
                height: calc(100vh - 70px);
                border: none;
            }
        </style>
        <iframe title="Dashboard_AESMA_daily_New_Released" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=24e1ad7f-1036-4b67-ab7b-6e766bf2eb55&autoAuth=true&ctid=70c9c52f-2483-473b-afd8-1627b7563e5b" frameborder="0" allowFullScreen="true"></iframe>
    """
    st.markdown(powerbi_iframe, unsafe_allow_html=True)
