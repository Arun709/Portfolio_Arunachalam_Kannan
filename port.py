import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Arunachalam Kannan | Data Scientist",
    page_icon="🚀",
    layout="wide"
)

# ---------- VIBRANT PURPLE CSS ----------
PURPLE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* Global Styles */
html, body, [data-testid="stAppViewContainer"] {
    background: #0d0221;
    color: #f0e7ff;
    font-family: 'Poppins', -apple-system, sans-serif;
}

[data-testid="stAppViewContainer"] > .main {
    background: linear-gradient(135deg, #0d0221 0%, #1a0b3f 25%, #2d1b69 50%, #1a0b3f 75%, #0d0221 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a0b3f 0%, #0d0221 100%);
    border-right: 2px solid rgba(168, 85, 247, 0.3);
}

[data-testid="stSidebar"] .css-1d391kg {
    padding-top: 2rem;
}

/* Typography */
.hero-title {
    font-size: 4rem;
    font-weight: 900;
    line-height: 1.1;
    margin-bottom: 1rem;
    font-family: 'Space Grotesk', sans-serif;
    background: linear-gradient(135deg, #c084fc 0%, #e879f9 30%, #fbbf24 60%, #f472b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.03em;
    text-shadow: 0 0 80px rgba(168, 85, 247, 0.5);
    animation: glow 3s ease-in-out infinite;
}

@keyframes glow {
    0%, 100% { filter: brightness(1) drop-shadow(0 0 20px rgba(168, 85, 247, 0.6)); }
    50% { filter: brightness(1.2) drop-shadow(0 0 40px rgba(168, 85, 247, 0.9)); }
}

.hero-subtitle {
    font-size: 1.4rem;
    color: #e9d5ff;
    font-weight: 500;
    margin-bottom: 1.5rem;
    line-height: 1.6;
    font-family: 'Space Grotesk', sans-serif;
}

.hero-description {
    font-size: 1.05rem;
    line-height: 1.8;
    color: #ddd6fe;
    margin-bottom: 2rem;
}

/* Cards with Glass Effect */
.modern-card {
    background: linear-gradient(135deg, rgba(88, 28, 135, 0.3) 0%, rgba(59, 7, 100, 0.4) 100%);
    border: 2px solid rgba(168, 85, 247, 0.3);
    border-radius: 24px;
    padding: 2.5rem;
    margin-bottom: 2rem;
    backdrop-filter: blur(16px);
    box-shadow: 
        0 8px 32px rgba(168, 85, 247, 0.2),
        inset 0 1px 0 rgba(255, 255, 255, 0.1);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.modern-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(168, 85, 247, 0.1) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.4s ease;
}

.modern-card:hover::before {
    opacity: 1;
}

.modern-card:hover {
    transform: translateY(-8px);
    border-color: rgba(192, 132, 252, 0.6);
    box-shadow: 
        0 20px 60px rgba(168, 85, 247, 0.4),
        0 0 80px rgba(168, 85, 247, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.project-card {
    background: linear-gradient(135deg, rgba(88, 28, 135, 0.25) 0%, rgba(76, 29, 149, 0.35) 100%);
    border: 2px solid rgba(168, 85, 247, 0.25);
    border-radius: 28px;
    padding: 2.5rem;
    margin-bottom: 2rem;
    backdrop-filter: blur(16px);
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.project-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, transparent, #c084fc, #e879f9, transparent);
    transition: left 0.5s ease;
}

.project-card:hover::before {
    left: 100%;
}

.project-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(192, 132, 252, 0.6);
    box-shadow: 
        0 30px 80px rgba(168, 85, 247, 0.5),
        0 0 100px rgba(232, 121, 249, 0.3);
}

/* Section Headers */
.section-header {
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 1rem;
    font-family: 'Space Grotesk', sans-serif;
    background: linear-gradient(135deg, #f0e7ff 0%, #c084fc 50%, #e879f9 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.02em;
    text-shadow: 0 0 40px rgba(168, 85, 247, 0.5);
}

.section-description {
    font-size: 1.15rem;
    color: #e9d5ff;
    margin-bottom: 3rem;
    line-height: 1.6;
}

/* Tech Stack Icons */
.tech-icon {
    width: 48px;
    height: 48px;
    padding: 8px;
    background: rgba(168, 85, 247, 0.15);
    border: 2px solid rgba(168, 85, 247, 0.3);
    border-radius: 12px;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

.tech-icon:hover {
    background: rgba(168, 85, 247, 0.3);
    border-color: rgba(192, 132, 252, 0.6);
    transform: translateY(-4px) rotate(5deg);
    box-shadow: 0 8px 24px rgba(168, 85, 247, 0.4);
}

.tech-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

/* Skill Pills with Glow */
.skill-container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin-top: 1.5rem;
}

.skill-pill {
    padding: 0.75rem 1.5rem;
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.2) 0%, rgba(139, 92, 246, 0.2) 100%);
    border: 2px solid rgba(192, 132, 252, 0.4);
    border-radius: 50px;
    font-size: 0.95rem;
    font-weight: 600;
    color: #e9d5ff;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(168, 85, 247, 0.2);
}

.skill-pill:hover {
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.35) 0%, rgba(139, 92, 246, 0.35) 100%);
    border-color: rgba(232, 121, 249, 0.7);
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(168, 85, 247, 0.5);
}

/* Buttons with Gradient */
.cta-button {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem 2rem;
    background: linear-gradient(135deg, #8b5cf6 0%, #a855f7 50%, #c084fc 100%);
    border: none;
    border-radius: 50px;
    color: white;
    font-weight: 700;
    font-size: 1rem;
    text-decoration: none;
    transition: all 0.4s ease;
    box-shadow: 0 8px 24px rgba(168, 85, 247, 0.4);
    position: relative;
    overflow: hidden;
}

.cta-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
    transition: left 0.5s ease;
}

.cta-button:hover::before {
    left: 100%;
}

.cta-button:hover {
    transform: translateY(-4px) scale(1.05);
    box-shadow: 0 12px 40px rgba(168, 85, 247, 0.6);
}

.link-button {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem 2rem;
    background: rgba(168, 85, 247, 0.15);
    border: 2px solid rgba(192, 132, 252, 0.5);
    border-radius: 50px;
    color: #e9d5ff;
    font-size: 1rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
}

.link-button:hover {
    background: rgba(168, 85, 247, 0.25);
    border-color: rgba(232, 121, 249, 0.8);
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(168, 85, 247, 0.4);
}

/* Profile Image with Glow */
.profile-container {
    position: relative;
    border-radius: 28px;
    overflow: hidden;
    border: 3px solid rgba(192, 132, 252, 0.5);
    box-shadow: 
        0 20px 60px rgba(168, 85, 247, 0.4),
        0 0 80px rgba(168, 85, 247, 0.3);
    transition: all 0.4s ease;
}

.profile-container:hover {
    border-color: rgba(232, 121, 249, 0.8);
    box-shadow: 
        0 30px 80px rgba(168, 85, 247, 0.6),
        0 0 120px rgba(232, 121, 249, 0.5);
    transform: scale(1.02);
}

/* Glowing Orbs */
.bg-gradient-orb {
    position: fixed;
    border-radius: 50%;
    filter: blur(100px);
    opacity: 0.3;
    z-index: -1;
    pointer-events: none;
    animation: float 20s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translate(0, 0); }
    25% { transform: translate(50px, -50px); }
    50% { transform: translate(-30px, 30px); }
    75% { transform: translate(30px, 50px); }
}

.orb-1 {
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, #8b5cf6 0%, transparent 70%);
    top: -100px;
    left: -100px;
    animation-delay: 0s;
}

.orb-2 {
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, #c084fc 0%, transparent 70%);
    bottom: -150px;
    right: -150px;
    animation-delay: 5s;
}

.orb-3 {
    width: 450px;
    height: 450px;
    background: radial-gradient(circle, #e879f9 0%, transparent 70%);
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    animation-delay: 10s;
}

/* Stats Box */
.stat-box {
    text-align: center;
    padding: 2rem;
    background: linear-gradient(135deg, rgba(88, 28, 135, 0.3) 0%, rgba(76, 29, 149, 0.3) 100%);
    border: 2px solid rgba(168, 85, 247, 0.3);
    border-radius: 20px;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
}

.stat-box:hover {
    background: linear-gradient(135deg, rgba(88, 28, 135, 0.5) 0%, rgba(76, 29, 149, 0.5) 100%);
    border-color: rgba(192, 132, 252, 0.6);
    transform: scale(1.05);
    box-shadow: 0 8px 32px rgba(168, 85, 247, 0.4);
}

.stat-number {
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #c084fc 0%, #e879f9 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
    font-family: 'Space Grotesk', sans-serif;
}

.stat-label {
    font-size: 0.95rem;
    color: #e9d5ff;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 600;
}

/* Icon Container */
.icon-badge {
    display: inline-block;
    padding: 0.5rem;
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.2) 0%, rgba(139, 92, 246, 0.2) 100%);
    border: 2px solid rgba(192, 132, 252, 0.4);
    border-radius: 12px;
    margin-right: 1rem;
    transition: all 0.3s ease;
}

.icon-badge:hover {
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.35) 0%, rgba(139, 92, 246, 0.35) 100%);
    border-color: rgba(232, 121, 249, 0.7);
    transform: scale(1.1) rotate(5deg);
}

/* Remove default padding */
.main > div {
    padding-top: 2rem !important;
}

/* Streamlit overrides */
.stMarkdown {
    color: inherit;
}

h1, h2, h3 {
    color: #f0e7ff;
    font-family: 'Space Grotesk', sans-serif;
}

/* Certificate Card Styling */
.cert-card {
    background: linear-gradient(135deg, rgba(88, 28, 135, 0.3) 0%, rgba(76, 29, 149, 0.35) 100%);
    border: 2px solid rgba(168, 85, 247, 0.3);
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(16px);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    height: 100%;
    display: flex;
    flex-direction: column;
}

.cert-card:hover {
    transform: translateY(-6px);
    border-color: rgba(192, 132, 252, 0.6);
    box-shadow: 
        0 16px 48px rgba(168, 85, 247, 0.4),
        0 0 60px rgba(168, 85, 247, 0.25);
}

.cert-title {
    color: #e9d5ff;
    font-size: 1.15rem;
    font-weight: 600;
    margin-bottom: 0.75rem;
    line-height: 1.4;
}

.cert-issuer {
    color: #c084fc;
    font-weight: 500;
    font-size: 0.95rem;
    margin-bottom: 0.5rem;
}

.cert-year {
    color: #a78bfa;
    font-size: 0.85rem;
    margin-top: auto;
}
</style>

<div class="bg-gradient-orb orb-1"></div>
<div class="bg-gradient-orb orb-2"></div>
<div class="bg-gradient-orb orb-3"></div>
"""

st.markdown(PURPLE_CSS, unsafe_allow_html=True)

# ---------- CONSTANTS ----------
GITHUB_URL = "https://github.com/Arun709"
LINKEDIN_URL = "https://www.linkedin.com/in/arunachalam-kannan-data-scientist/"
EMAIL = "mailto:arunchlmk@gmail.com"

# Tech stack icons (using emoji as placeholders)
TECH_ICONS = {
    "Python": "🐍",
    "SQL": "💾",
    "Pandas": "🐼",
    "NumPy": "🔢",
    "Scikit-learn": "🤖",
    "TensorFlow": "🧠",
    "PyTorch": "🔥",
    "Streamlit": "⚡",
    "Power BI": "📊",
    "LangChain": "⛓️",
    "YOLO": "👁️",
    "OpenCV": "📷"
}

# ---------- SIDEBAR NAV ----------
st.sidebar.markdown("### ✨ Navigation")
pages = ["🏠 Home", "🚀 Projects", "💡 Skills", "📚 Experience", "🏆 Certifications"]
selection = st.sidebar.radio("", pages, label_visibility="collapsed")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Connect")
st.sidebar.markdown(f"🔗 [GitHub]({GITHUB_URL})")
st.sidebar.markdown(f"💼 [LinkedIn]({LINKEDIN_URL})")
st.sidebar.markdown(f"✉️ [Email](mailto:arunchlmk@gmail.com)")

# ---------- PAGE: HOME ----------
if selection == "🏠 Home":
    col1, col2 = st.columns([1.2, 2])

    with col1:
        st.markdown('<div class="profile-container">', unsafe_allow_html=True)
        # Note: Replace with actual profile image path if available
        st.image("profile_bw.png", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Quick stats
        stat_col1, stat_col2 = st.columns(2)
        with stat_col1:
            st.markdown("""
                <div class="stat-box">
                    <div class="stat-number">7+</div>
                    <div class="stat-label">Projects</div>
                </div>
            """, unsafe_allow_html=True)
        with stat_col2:
            st.markdown("""
                <div class="stat-box">
                    <div class="stat-number">15+</div>
                    <div class="stat-label">Skills</div>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="hero-title">Arunachalam Kannan</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="hero-subtitle">Data Scientist • Machine Learning Engineer • AI Enthusiast</div>',
            unsafe_allow_html=True
        )
        
        st.markdown(
            '<div class="hero-description">'
            'Results-driven Data Scientist and Machine Learning Engineer with hands-on experience in '
            'developing and deploying ML models, data pipelines, and analytics solutions. Proven expertise '
            'in Python, SQL, and machine learning algorithms with a track record of achieving 96%+ accuracy '
            'in production environments. Skilled in end-to-end ML lifecycle from data preprocessing to model monitoring.'
            '</div>',
            unsafe_allow_html=True
        )

        # CTA buttons
        st.markdown(
            f'<a class="cta-button" href="{LINKEDIN_URL}" target="_blank">🚀 Let\'s Connect</a> '
            f'<a class="link-button" href="{GITHUB_URL}" target="_blank">💻 View Projects</a>',
            unsafe_allow_html=True
        )

        st.markdown("<br><br>", unsafe_allow_html=True)

        # Tech showcase
        st.markdown("""
            <div class="modern-card">
                <h3 style="margin-top: 0; color: #f0e7ff; font-family: 'Space Grotesk', sans-serif;">🔮 Currently Building</h3>
                <p style="color: #ddd6fe; line-height: 1.8; font-size: 1.05rem;">
                    Developing next-generation intelligent applications using <strong>Streamlit</strong>, <strong>LangChain</strong>, 
                    and <strong>YOLO</strong> for real-time computer vision. Mastering AI/ML at <strong>IIT Madras</strong> with focus on 
                    NLP, Time Series Forecasting, and Generative AI. Building production-ready ML solutions and exploring sustainable energy analytics.
                </p>
        """, unsafe_allow_html=True)
        
        # Tech icons grid
        tech_icons_html = '<div class="tech-grid">'
        for tech, icon in list(TECH_ICONS.items())[:8]:
            tech_icons_html += f'<div class="tech-icon" title="{tech}" style="font-size: 2rem;">{icon}</div>'
        tech_icons_html += '</div>'
        
        st.markdown(tech_icons_html + "</div>", unsafe_allow_html=True)

# ---------- PAGE: PROJECTS ----------
elif selection == "🚀 Projects":
    st.markdown('<div class="section-header">✨ Featured Projects</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-description">Real-world solutions showcasing data science, ML engineering, and deployment expertise</div>',
        unsafe_allow_html=True
    )

    projects = [
        {
            "title": "👁️ SmartVision – Real-time Object Detection System",
            "description": "Developed end-to-end real-time object detection system processing video streams at 30 FPS with 94% detection accuracy. Implemented YOLO v5 model with custom training on 5,000+ labeled images for multi-class object detection. Built interactive Streamlit web application for live video inference with confidence score visualization and optimized inference pipeline reducing latency by 35% through batch processing and GPU acceleration.",
            "tech": ["YOLO 👁️", "OpenCV 📷", "TensorFlow 🧠", "Streamlit ⚡"],
            "link": "https://arunsmartvisionai.streamlit.app/"
        },
        {
            "title": "🚔 PatrolIQ – Crime Hotspot Prediction with Geospatial Analysis",
            "description": "Built predictive model using Random Forest and XGBoost algorithms to forecast crime hotspots with 89% accuracy. Processed and analyzed 100K+ geospatial crime records using pandas and SQL, engineering 15+ location-based features. Created interactive geospatial dashboards with Folium and Power BI for law enforcement decision-making with time series analysis for temporal crime patterns.",
            "tech": ["Random Forest 🌲", "XGBoost 🚀", "GeoPandas 🗺️", "Folium 📍", "Power BI 📊"],
            "link": "https://chicagocrimepatroliq-h4ytwrdu8jbxmjmeqsnbtk.streamlit.app/"
        },
        {
            "title": "💰 EMIPredict AI – Loan Default Prediction System",
            "description": "Developed classification model to predict loan defaults achieving 97% accuracy using ensemble methods (Random Forest, XGBoost, Gradient Boosting). Performed comprehensive EDA and feature engineering on 50K+ customer records, creating 20+ predictive features. Built automated data preprocessing pipeline handling missing values, outliers, and feature scaling. Deployed model as REST API using Flask with user-friendly Streamlit interface.",
            "tech": ["XGBoost 🚀", "Scikit-learn 🤖", "Flask 🌐", "SQL 💾", "Streamlit ⚡"],
            "link": "https://emipridictionproject-9zcck5xfgrlampdfphlnul.streamlit.app/"
        },
        {
            "title": "🛒 E-Commerce Sales Analytics – 10-Year Trend Analysis",
            "description": "Analyzed 10 years of e-commerce sales data (1M+ transactions) using Python and SQL to identify revenue trends and customer behavior patterns. Built comprehensive ETL pipeline to extract, transform, and load data from multiple sources with 99% data accuracy. Created interactive Power BI dashboards visualizing sales performance, inventory metrics, and seasonal trends. Performed cohort analysis and customer segmentation using clustering algorithms.",
            "tech": ["Python 🐍", "SQL 💾", "Power BI 📊", "Pandas 🐼", "NumPy 🔢"],
            "link": "https://github.com/Arun709/Amazon-India-Sales-Analytics-Project"
        },
        {
            "title": "🏏 Cricbuzz LiveStats – Real-time Cricket Analytics",
            "description": "Real-time cricket analytics platform leveraging Cricbuzz API to deliver live match statistics, score progression tracking, and player performance metrics in an interactive web application. Features include real-time score updates, player statistics, match summaries, and historical data analysis with intuitive visualizations.",
            "tech": ["Python 🐍", "REST API 🌐", "Streamlit ⚡", "Data Viz 📈"],
            "link": "https://cricbuzz-livestats-kjvfexh5z4a35dyn69cfap.streamlit.app/"
        },
        {
            "title": "🤖 Customer Support Assistant AI – RAG-Powered Chatbot",
            "description": "RAG-powered intelligent chatbot that retrieves relevant knowledge base articles and generates accurate responses using GPT, deployed with an intuitive Streamlit interface. Leverages LangChain for document processing and vector databases for efficient semantic search, providing context-aware customer support automation.",
            "tech": ["LangChain ⛓️", "Vector DB 🗄️", "OpenAI 🧠", "Streamlit ⚡"],
            "link": "https://customersupportassistantai.streamlit.app/"
        },
        {
            "title": "⚙️ RUL Prediction – Remaining Useful Life Forecasting",
            "description": "Advanced predictive maintenance system utilizing machine learning to forecast Remaining Useful Life (RUL) of industrial equipment. Implemented time series analysis and regression models to predict equipment failure, enabling proactive maintenance scheduling and reducing downtime. Features comprehensive sensor data analysis, feature engineering, and model evaluation with interactive visualizations.",
            "tech": ["Scikit-learn 🤖", "Time Series 📈", "Pandas 🐼", "Streamlit ⚡"],
            "link": "https://rulpredictionproject.streamlit.app/"
        }
    ]

    for project in projects:
        link = project["link"]
        tech_pills = "".join([f'<div class="skill-pill">{tech}</div>' for tech in project["tech"]])
        
        st.markdown(f"""
            <div class="project-card">
                <h3 style="margin-top: 0; color: #f0e7ff; font-size: 1.75rem; font-family: 'Space Grotesk', sans-serif;">{project["title"]}</h3>
                <p style="color: #ddd6fe; line-height: 1.8; margin-bottom: 2rem; font-size: 1.05rem;">
                    {project["description"]}
                </p>
                <div class="skill-container">
                    {tech_pills}
                </div>
                <br>
                <a class="link-button" href="{link}" target="_blank">View Project →</a>
            </div>
        """, unsafe_allow_html=True)

# ---------- PAGE: SKILLS ----------
elif selection == "💡 Skills":
    st.markdown('<div class="section-header">⚡ Technical Arsenal</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-description">Tools and technologies powering production-ready solutions</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="modern-card">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <div class="icon-badge" style="font-size: 2rem;">🤖</div>
                    <h3 style="margin: 0; color: #f0e7ff; font-family: 'Space Grotesk', sans-serif;">Machine Learning & AI</h3>
                </div>
                <p style="color: #ddd6fe; line-height: 2; font-size: 1.05rem;">
                    • <strong>Supervised Learning</strong>: Classification, Regression, Ensemble Methods<br>
                    • <strong>Unsupervised Learning</strong>: Clustering, Dimensionality Reduction<br>
                    • <strong>Deep Learning</strong>: Neural Networks, CNNs, Transfer Learning<br>
                    • <strong>NLP</strong>: Text Classification, NLTK, spaCy, Transformers<br>
                    • <strong>Computer Vision</strong>: YOLO, OpenCV, Image Processing<br>
                    • <strong>Time Series</strong>: Forecasting, Trend Analysis<br>
                    • <strong>Model Optimization</strong>: Hyperparameter Tuning, Cross-validation<br>
                    • <strong>A/B Testing</strong>: Statistical Hypothesis Testing
                </p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="modern-card">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <div class="icon-badge" style="font-size: 2rem;">🐍</div>
                    <h3 style="margin: 0; color: #f0e7ff; font-family: 'Space Grotesk', sans-serif;">Programming & Development</h3>
                </div>
                <p style="color: #ddd6fe; line-height: 2; font-size: 1.05rem;">
                    • <strong>Python</strong>: pandas, NumPy, scikit-learn, TensorFlow, PyTorch<br>
                    • <strong>SQL</strong>: PostgreSQL, MySQL, Complex Queries, Optimization<br>
                    • <strong>Git & GitHub</strong>: Version Control, Collaboration<br>
                    • <strong>REST APIs</strong>: Flask, FastAPI, Integration<br>
                    • <strong>OOP</strong>: Object-Oriented Programming Principles
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="modern-card">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <div class="icon-badge" style="font-size: 2rem;">⚙️</div>
                    <h3 style="margin: 0; color: #f0e7ff; font-family: 'Space Grotesk', sans-serif;">Data Engineering & MLOps</h3>
                </div>
                <p style="color: #ddd6fe; line-height: 2; font-size: 1.05rem;">
                    • <strong>ETL/ELT Pipelines</strong>: Data Extraction, Transformation, Loading<br>
                    • <strong>Data Modeling</strong>: Schema Design, Data Warehousing<br>
                    • <strong>Data Quality</strong>: Validation, Quality Management<br>
                    • <strong>Model Deployment</strong>: MLflow, Docker (Learning), CI/CD<br>
                    • <strong>Model Monitoring</strong>: Performance Metrics, Debugging<br>
                    • <strong>Cloud Platforms</strong>: AWS (Learning), Azure (Learning), GCP (Learning)
                </p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="modern-card">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <div class="icon-badge" style="font-size: 2rem;">📊</div>
                    <h3 style="margin: 0; color: #f0e7ff; font-family: 'Space Grotesk', sans-serif;">Visualization & BI</h3>
                </div>
                <p style="color: #ddd6fe; line-height: 2; font-size: 1.05rem;">
                    • <strong>BI Tools</strong>: Power BI, Tableau, Interactive Dashboards<br>
                    • <strong>Python Viz</strong>: Matplotlib, Seaborn, Plotly<br>
                    • <strong>Web Apps</strong>: Streamlit Applications<br>
                    • <strong>Geospatial</strong>: Folium, GeoPandas Visualization
                </p>
            </div>
        """, unsafe_allow_html=True)

# ---------- PAGE: EXPERIENCE ----------
elif selection == "📚 Experience":
    st.markdown('<div class="section-header">🛠️ Professional Journey</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-description">Transforming data into actionable insights and intelligent solutions</div>',
        unsafe_allow_html=True
    )

    experience = [
        {
            "role": "Data Science Intern",
            "company": "HCL GUVI",
            "period": "Jun 2025 – Dec 2025",
            "location": "Chennai, Tamil Nadu, India (Remote)",
            "highlights": [
                "Developed and validated machine learning models achieving 96%+ accuracy across 1,000+ test cases using Python, scikit-learn, and TensorFlow",
                "Built ETL pipelines to process and analyze large datasets (500K+ records) using pandas and SQL, identifying 25+ critical data quality issues and improving data integrity by 30%",
                "Designed and deployed real-time performance monitoring dashboards using Tableau and Power BI, tracking model metrics and KPIs for stakeholder reporting",
                "Performed systematic data validation and quality assurance on image-based datasets using computer vision techniques (YOLO, OpenCV), reducing misclassification errors by 22%",
                "Collaborated with cross-functional teams to optimize data processing workflows, reducing processing time by 18% while maintaining accuracy standards",
                "Documented ML model architecture, data pipelines, and audit procedures, ensuring reproducibility and compliance with project benchmarks",
                "Conducted exploratory data analysis (EDA) and statistical testing to identify patterns, trends, and anomalies in complex datasets"
            ]
        }
    ]

    for exp in experience:
        st.markdown(f"""
            <div class="modern-card">
                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 1rem;">
                    <h3 style="margin: 0; color: #e9d5ff; font-size: 1.8rem;">{exp['role']}</h3>
                    <span style="color: #c084fc; font-weight: 600; font-size: 1.1rem;">{exp['period']}</span>
                </div>
                <p style="color: #a78bfa; margin: 0.4rem 0 0.2rem 0; font-weight: 500;">{exp['company']}</p>
                <p style="color: #9d7bde; margin: 0 0 1.2rem 0; font-size: 0.95rem;">{exp['location']}</p>
                <ul style="color: #ddd6fe; line-height: 1.8; margin-left: 1.2rem; padding-left: 0;">
        """, unsafe_allow_html=True)

        for point in exp["highlights"]:
            st.markdown(f"<li>{point}</li>", unsafe_allow_html=True)

        st.markdown("</ul></div>", unsafe_allow_html=True)

    # Education Section
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header" style="font-size: 2.5rem;">🎓 Education</div>', unsafe_allow_html=True)
    
    education = [
        {
            "degree": "Master's in Data Science",
            "institution": "Indian Institute of Technology, Madras Pravartak Technologies Foundation",
            "period": "Jul 2025 – Present",
            "details": "Specialization: AI/ML, NLP, Time Series Forecasting, Generative AI"
        },
        {
            "degree": "Bachelor of Commerce",
            "institution": "Madras University",
            "period": "Jul 2019 – Jul 2022",
            "details": "Specialization: Accounting & Finance, Business Analytics"
        }
    ]

    for edu in education:
        st.markdown(f"""
            <div class="modern-card">
                <h3 style="margin: 0; color: #e9d5ff; font-size: 1.6rem;">{edu['degree']}</h3>
                <p style="color: #a78bfa; margin: 0.4rem 0; font-weight: 500;">{edu['institution']}</p>
                <p style="color: #c084fc; font-size: 0.95rem; margin: 0.4rem 0;">{edu['period']}</p>
                <p style="color: #ddd6fe; margin-top: 1rem;">{edu['details']}</p>
            </div>
        """, unsafe_allow_html=True)

# ---------- PAGE: CERTIFICATIONS ----------
elif selection == "🏆 Certifications":
    st.markdown('<div class="section-header">🏅 Certifications & Professional Development</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-description">Continuous learning in data science, ML engineering & AI technologies</div>',
        unsafe_allow_html=True
    )

    # Certifications from resume
    certs = [
        {
            "name": "Master Data Science Program",
            "issuer": "GUVI Institute",
            "year": "2024–2025",
            "category": "core"
        },
        {
            "name": "PostgreSQL for Data Analysis and Data Science",
            "issuer": "Udemy",
            "year": "2024",
            "category": "technical"
        },
        {
            "name": "Excel for Data Analytics",
            "issuer": "Simplilearn",
            "year": "2024",
            "category": "technical"
        },
        {
            "name": "Excel for Data Analysis",
            "issuer": "Great Learning",
            "year": "2024",
            "category": "technical"
        },
        {
            "name": "Certification Program in Banking and Finance Operations and Sales",
            "issuer": "Edu Bridge India",
            "year": "2023",
            "category": "domain"
        },
        {
            "name": "Statistics 101",
            "issuer": "United Latino Students Association",
            "year": "2024",
            "category": "technical"
        }
    ]

    # Display certifications in a grid
    cols = st.columns(2)
    for i, cert in enumerate(certs):
        with cols[i % 2]:
            st.markdown(f"""
                <div class="cert-card">
                    <div class="cert-title">{cert['name']}</div>
                    <div class="cert-issuer">{cert['issuer']}</div>
                    <div class="cert-year">Issued • {cert['year']}</div>
                </div>
            """, unsafe_allow_html=True)

    # Additional Information Section
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div class="modern-card">
            <h3 style="margin-top: 0; color: #f0e7ff; font-family: 'Space Grotesk', sans-serif;">📚 Additional Information</h3>
            <div style="color: #ddd6fe; line-height: 2; font-size: 1.05rem;">
                <p><strong>🌐 Languages:</strong> English (Fluent) • Tamil (Native) • German (Learning)</p>
                <p><strong>💼 Work Authorization:</strong> Available to work in India • Open to relocation opportunities (Germany, Europe)</p>
                <p><strong>⏰ Availability:</strong> Immediate • Flexible for rotational shifts and remote work</p>
                <p><strong>🎯 Professional Interests:</strong> Sustainable Energy Analytics • Generative AI • MLOps • Real-time Data Processing</p>
                <p><strong>💻 GitHub:</strong> Active contributor with 15+ repositories showcasing ML projects, data analysis, and automation scripts</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ---------- FOOTER (appears on all pages) ----------
st.markdown("---")

footer_html = f"""
<div style="text-align: center; color: #a78bfa; padding: 2rem 0 1.5rem; font-size: 0.95rem;">
    <p>Built with ❤️ using Streamlit • © 2026 Arunachalam Kannan</p>
    <p style="margin-top: 0.8rem;">
        <a href="{GITHUB_URL}" target="_blank" style="color: #c084fc; text-decoration: none; margin: 0 1rem;">GitHub</a> • 
        <a href="{LINKEDIN_URL}" target="_blank" style="color: #c084fc; text-decoration: none; margin: 0 1rem;">LinkedIn</a> • 
        <a href="{EMAIL}" style="color: #c084fc; text-decoration: none; margin: 0 1rem;">Email</a>
    </p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
