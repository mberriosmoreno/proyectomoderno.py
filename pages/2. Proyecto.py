import streamlit as st
import plotly.express as px

st.title("📊 Arquitectura Técnica")

# Diagrama de arquitectura interactivo
with st.expander("🏗️ Diagrama del Sistema", expanded=True):
    fig = px.sunburst(
        names=["Plataforma", "Frontend", "Backend", "IA", "DB"],
        parents=["", "Plataforma", "Plataforma", "Plataforma", "Backend"],
        values=[100, 30, 40, 20, 10],
        color=["Plataforma", "Frontend", "Backend", "IA", "DB"],
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig, use_container_width=True)

# Sección de línea de tiempo mejorada
st.header("🚀 Cronograma de Desarrollo")
st.markdown("""
<div class="modern-timeline">
    <div class="timeline-item">
        <div class="timeline-marker"></div>
        <div class="timeline-content">
            <h4>Fase 1: Diseño Conceptual</h4>
            <p class="timeline-date">Q1 2024</p>
            <ul>
                <li>Investigación de mercado</li>
                <li>Prototipado inicial</li>
            </ul>
        </div>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-marker"></div>
        <div class="timeline-content">
            <h4>Fase 2: Desarrollo Nucleo</h4>
            <p class="timeline-date">Q2 2024</p>
            <ul>
                <li>Implementación backend</li>
                <li>Integración IA</li>
            </ul>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
