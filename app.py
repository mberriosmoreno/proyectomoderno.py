import streamlit as st
from PIL import Image
import base64

# Configuración inicial
st.set_page_config(
    page_title="Innovación Digital 2024",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar estilos CSS
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
load_css()

# Sidebar con navegación
def sidebar():
    with st.sidebar:
        st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
        logo = Image.open("assets/images/logo.png")
        st.image(logo, use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.title("Navegación")
        st.page_link("app.py", label="Inicio", icon="🏠")
        st.page_link("pages/1_🏠_Inicio.py", label="Visión General", icon="🌐")
        st.page_link("pages/2_📄_Proyecto.py", label="Detalles Técnicos", icon="📊")
        st.page_link("pages/3_👥_Equipo.py", label="Equipo", icon="👨💻")
        st.page_link("pages/4_📚_Docs.py", label="Documentación", icon="📖")
        st.page_link("pages/5_📧_Contacto.py", label="Contacto", icon="📩")
        
        st.divider()
        st.markdown("**Versión:** 2.1.0 | **Última actualización:** Julio 2024")
        st.caption("© 2024 Innovación Digital. Todos los derechos reservados.")

# Página principal
def main_page():
    st.title("Transformando el Futuro Digital")
    st.subheader("Una solución integral para la nueva era tecnológica")
    
    with st.container():
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("""
            ### Características Clave
            <div class="feature-card">
                <h4>🔄 Procesamiento en Tiempo Real</h4>
                <p>Tecnología de vanguardia para análisis instantáneo</p>
            </div>
            
            <div class="feature-card">
                <h4>🔐 Seguridad Cuántica</h4>
                <p>Encriptación post-cuántica de última generación</p>
            </div>
            
            <div class="feature-card">
                <h4>🤖 IA Adaptativa</h4>
                <p>Sistemas de aprendizaje automático auto-optimizables</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.image("assets/images/hero.png", use_column_width=True)

if __name__ == "__main__":
    sidebar()
    main_page()
