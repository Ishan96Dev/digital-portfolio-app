import streamlit as st
import time
import base64
from PIL import Image
import os
import io

# Page configuration
st.set_page_config(
    page_title="Digital Portfolio App",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for theme
if 'current_theme' not in st.session_state:
    st.session_state.current_theme = "Professional"

# Theme-specific CSS
def get_theme_css(theme):
    if theme == "Professional":
        return """
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');
        
        /* Professional Theme - Clean and Modern with AI/ML Effects */
        .main {
            padding: 0rem 2rem;
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 30%, #cbd5e1 70%, #94a3b8 100%);
            min-height: 100vh;
            position: relative;
        }
        
        .main::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 80%, rgba(59, 130, 246, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(139, 92, 246, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(34, 197, 94, 0.05) 0%, transparent 50%),
                radial-gradient(circle at 60% 60%, rgba(168, 85, 247, 0.05) 0%, transparent 50%);
            pointer-events: none;
            animation: subtleFloat 20s ease-in-out infinite;
        }
        
        @keyframes subtleFloat {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            25% { transform: translateY(-10px) rotate(1deg); }
            50% { transform: translateY(-5px) rotate(-1deg); }
            75% { transform: translateY(-15px) rotate(0.5deg); }
        }
        
        /* AI/ML Background Pattern */
        .main::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: 
                radial-gradient(circle at 25% 25%, rgba(59, 130, 246, 0.03) 0%, transparent 50%),
                radial-gradient(circle at 75% 75%, rgba(34, 197, 94, 0.03) 0%, transparent 50%),
                radial-gradient(circle at 50% 50%, rgba(168, 85, 247, 0.02) 0%, transparent 50%);
            background-size: 200px 200px, 300px 300px, 400px 400px;
            animation: patternMove 30s linear infinite;
            pointer-events: none;
        }
        
        @keyframes patternMove {
            0% { background-position: 0% 0%, 0% 0%, 0% 0%; }
            100% { background-position: 100% 100%, -100% -100%, 50% 50%; }
        }
        
        /* AI/ML Particle Effects */
        .main-content::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(2px 2px at 20px 30px, rgba(59, 130, 246, 0.3), transparent),
                radial-gradient(2px 2px at 40px 70px, rgba(34, 197, 94, 0.3), transparent),
                radial-gradient(1px 1px at 90px 40px, rgba(168, 85, 247, 0.3), transparent),
                radial-gradient(1px 1px at 130px 80px, rgba(59, 130, 246, 0.3), transparent),
                radial-gradient(2px 2px at 160px 30px, rgba(34, 197, 94, 0.3), transparent);
            background-repeat: repeat;
            background-size: 200px 100px, 300px 150px, 400px 200px, 500px 250px, 600px 300px;
            animation: particleFloat 20s linear infinite;
            pointer-events: none;
            z-index: 1;
        }
        
        @keyframes particleFloat {
            0% { transform: translateY(0px); }
            100% { transform: translateY(-100px); }
        }
        
        .stApp {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 30%, #cbd5e1 70%, #94a3b8 100%);
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            background: linear-gradient(180deg, #ffffff 0%, #f1f5f9 100%);
            border-right: 2px solid #3b82f6;
        }
        
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #ffffff 0%, #f1f5f9 100%);
        }
        
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3, 
        section[data-testid="stSidebar"] h4, 
        section[data-testid="stSidebar"] h5, 
        section[data-testid="stSidebar"] h6 {
            color: #1e293b !important;
            font-size: 1.2rem;
        }
        
        section[data-testid="stSidebar"] p {
            color: #475569 !important;
            font-size: 1rem;
        }
        
        section[data-testid="stSidebar"] .stSelectbox label {
            color: #1e293b !important;
            font-size: 1.1rem;
            font-weight: 600;
        }
        
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
            background-color: rgba(59, 130, 246, 0.1) !important;
            border: 1px solid #3b82f6 !important;
        }
        
        /* Headers */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Poppins', sans-serif;
            color: #1e293b;
            text-shadow: none;
            position: relative;
        }
        
        h1::before, h2::before, h3::before {
            content: '';
            position: absolute;
            left: -10px;
            top: 50%;
            transform: translateY(-50%);
            width: 4px;
            height: 80%;
            background: linear-gradient(45deg, #3b82f6, #8b5cf6);
            border-radius: 2px;
            box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3);
        }
        
        /* Main content text */
        .main-content {
            font-family: 'Inter', sans-serif;
            color: #334155 !important;
            font-size: 1.1rem;
            line-height: 1.6;
            padding-top: 3.5rem;
            padding-bottom: 3.5rem;
            overflow: visible;
        }
        
        /* Ensure all text is visible */
        .main-content p, .main-content li, .main-content span, .main-content div,
        .experience-card *, .education-card *, .company-details * {
            color: #334155 !important;
        }
        
        .stMarkdown, .stText, .stExpander {
            color: #334155 !important;
        }
        
        .skill-description {
            color: #334155 !important;
        }
        
        /* Profile image styling */
        .profile-image {
            border-radius: 50%;
            border: 3px solid #3b82f6;
            box-shadow: 0 4px 20px rgba(59, 130, 246, 0.3);
            padding: 5px;
            background: rgba(59, 130, 246, 0.1);
            margin: 1rem 0;
            transition: transform 0.4s cubic-bezier(.4,2.08,.55,.44), box-shadow 0.4s;
        }
        .profile-image:hover {
            transform: scale(1.07) rotate(-3deg);
            box-shadow: 0 8px 40px rgba(59, 130, 246, 0.4);
            border-color: #8b5cf6;
        }
        
        /* Professional cards with enhanced AI/ML effects */
        .themed-card {
            background: rgba(255, 255, 255, 0.95);
            border: 2px solid #e2e8f0;
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            transition: all 0.4s cubic-bezier(.4,2.08,.55,.44);
            position: relative;
            overflow: visible;
            backdrop-filter: blur(10px);
        }
        
        .themed-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.05) 0%, rgba(34, 197, 94, 0.05) 50%, rgba(168, 85, 247, 0.05) 100%);
            border-radius: 15px;
            opacity: 0;
            transition: opacity 0.4s ease;
            z-index: -1;
        }
        
        .themed-card::after {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(45deg, #3b82f6, #10b981, #8b5cf6, #3b82f6);
            border-radius: 17px;
            opacity: 0;
            transition: opacity 0.4s ease;
            z-index: -2;
            background-size: 400% 400%;
            animation: gradientShift 3s ease infinite;
        }
        
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .themed-card:hover {
            transform: translateY(-12px) scale(1.03);
            box-shadow: 0 20px 60px rgba(59, 130, 246, 0.3), 0 0 40px rgba(34, 197, 94, 0.2);
            border-color: #3b82f6;
        }
        
        .themed-card:hover::before {
            opacity: 1;
        }
        
        .themed-card:hover::after {
            opacity: 0.3;
        }
        .themed-card h3, .themed-card h4, .themed-card h5, .themed-card h6 {
            color: #1e293b;
            margin-top: 0;
        }
        .themed-card ul, .themed-card li, .themed-card p, .themed-card strong {
            color: #334155 !important;
        }
        
        /* Experience cards */
        .experience-card {
            background: rgba(255, 255, 255, 0.9);
            border: 2px solid #fecaca;
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }
        
        .experience-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 40px rgba(239, 68, 68, 0.2);
        }
        
        /* Education and activity cards with AI/ML effects */
        .education-card, .activity-item {
            background: rgba(255, 255, 255, 0.95);
            border: 2px solid #fecaca;
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }
        
        .education-card::before, .activity-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(239, 68, 68, 0.1), transparent);
            transition: left 0.6s ease;
        }
        
        .education-card::after, .activity-item::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.05) 0%, rgba(59, 130, 246, 0.05) 50%, rgba(34, 197, 94, 0.05) 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
        }
        
        .education-card:hover, .activity-item:hover {
            transform: translateY(-12px) scale(1.03);
            box-shadow: 0 20px 50px rgba(239, 68, 68, 0.3), 0 0 30px rgba(59, 130, 246, 0.2);
            border-color: #3b82f6;
        }
        
        .education-card:hover::before, .activity-item:hover::before {
            left: 100%;
        }
        
        .education-card:hover::after, .activity-item:hover::after {
            opacity: 1;
        }
        
        /* Stats cards with AI/ML effects */
        .metric-card {
            background: rgba(255, 255, 255, 0.95);
            border: 2px solid #3b82f6;
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            margin: 1rem 0;
            backdrop-filter: blur(15px);
            position: relative;
            overflow: hidden;
        }
        
        .metric-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.1), transparent);
            transition: left 0.6s ease;
        }
        
        .metric-card::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.05) 0%, rgba(34, 197, 94, 0.05) 50%, rgba(168, 85, 247, 0.05) 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
        }
        
        .metric-card:hover {
            transform: translateY(-12px) scale(1.05);
            box-shadow: 0 25px 50px rgba(59, 130, 246, 0.4), 0 0 30px rgba(34, 197, 94, 0.3);
            border-color: #10b981;
        }
        
        .metric-card:hover::before {
            left: 100%;
        }
        
        .metric-card:hover::after {
            opacity: 1;
        }
        
        .metric-number {
            font-family: 'Poppins', sans-serif;
            font-size: 2.5rem;
            font-weight: 700;
            color: #3b82f6;
            margin-bottom: 0.5rem;
            position: relative;
        }
        
        .metric-label {
            font-family: 'Inter', sans-serif;
            color: #475569;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 1.1rem;
            letter-spacing: 1px;
        }
        
        /* Social links with AI/ML effects */
        .social-link {
            display: block;
            text-decoration: none;
            color: #3b82f6;
            margin: 0.5rem 0;
            padding: 0.8rem 1rem;
            border: 1px solid #3b82f6;
            border-radius: 25px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            text-align: center;
            background: rgba(59, 130, 246, 0.05);
            position: relative;
            overflow: hidden;
        }
        
        .social-link::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.2), transparent);
            transition: left 0.5s ease;
        }
        
        .social-link::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(34, 197, 94, 0.1) 50%, rgba(168, 85, 247, 0.1) 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
        }
        
        .social-link:hover {
            background: rgba(59, 130, 246, 0.15);
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4), 0 0 20px rgba(34, 197, 94, 0.2);
            color: #1e40af;
            border-color: #10b981;
        }
        
        .social-link:hover::before {
            left: 100%;
        }
        
        .social-link:hover::after {
            opacity: 1;
        }
        
        /* Buttons with AI/ML effects */
        .cert-button, .download-button {
            background: linear-gradient(45deg, #3b82f6, #1d4ed8);
            color: white;
            border: 2px solid #3b82f6;
            border-radius: 25px;
            padding: 12px 24px;
            font-size: 1rem;
            font-weight: 600;
            font-family: 'Inter', sans-serif;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
            margin: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            position: relative;
            overflow: hidden;
        }
        
        .cert-button::before, .download-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
            transition: left 0.6s ease;
        }
        
        .cert-button::after, .download-button::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.2) 0%, rgba(34, 197, 94, 0.2) 50%, rgba(168, 85, 247, 0.2) 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
        }
        
        .cert-button:hover, .download-button:hover {
            transform: translateY(-6px) scale(1.05);
            box-shadow: 0 12px 35px rgba(59, 130, 246, 0.5), 0 0 25px rgba(34, 197, 94, 0.3);
            background: linear-gradient(45deg, #1d4ed8, #3b82f6);
            color: white;
            border-color: #10b981;
        }
        
        .cert-button:hover::before, .download-button:hover::before {
            left: 100%;
        }
        
        .cert-button:hover::after, .download-button:hover::after {
            opacity: 1;
        }
        
        /* Streamlit button styling for Professional theme */
        .stButton > button {
            background: linear-gradient(45deg, #3b82f6, #1d4ed8) !important;
            color: white !important;
            border: 2px solid #3b82f6 !important;
            border-radius: 25px !important;
            font-weight: 600 !important;
            font-family: 'Inter', sans-serif !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3) !important;
            position: relative !important;
            overflow: hidden !important;
        }
        
        .stButton > button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
            transition: left 0.6s ease;
        }
        
        .stButton > button::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.2) 0%, rgba(34, 197, 94, 0.2) 50%, rgba(168, 85, 247, 0.2) 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-6px) scale(1.05) !important;
            box-shadow: 0 12px 35px rgba(59, 130, 246, 0.5), 0 0 25px rgba(34, 197, 94, 0.3) !important;
            background: linear-gradient(45deg, #1d4ed8, #3b82f6) !important;
            border-color: #10b981 !important;
        }
        
        .stButton > button:hover::before {
            left: 100%;
        }
        
        .stButton > button:hover::after {
            opacity: 1;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 2rem 0;
            font-family: 'Poppins', sans-serif;
            color: #475569;
            font-size: 0.9rem;
            margin-top: 3rem;
            border-top: 1px solid #e2e8f0;
        }
        
        /* Streamlit expander styling with AI/ML effects */
        div[data-testid="stExpander"] {
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border-radius: 10px !important;
            border: 2px solid #e2e8f0 !important;
            background: rgba(255, 255, 255, 0.95) !important;
            backdrop-filter: blur(10px);
            position: relative;
            overflow: hidden;
        }
        
        div[data-testid="stExpander"]::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.1), transparent);
            transition: left 0.6s ease;
            z-index: 1;
        }
        
        div[data-testid="stExpander"]::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.05) 0%, rgba(34, 197, 94, 0.05) 50%, rgba(168, 85, 247, 0.05) 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
            z-index: 0;
        }
        
        div[data-testid="stExpander"]:hover {
            box-shadow: 0 12px 40px rgba(59, 130, 246, 0.3), 0 0 20px rgba(34, 197, 94, 0.2);
            transform: translateY(-8px) scale(1.02);
            border-color: #3b82f6 !important;
            z-index: 2;
        }
        
        div[data-testid="stExpander"]:hover::before {
            left: 100%;
        }
        
        div[data-testid="stExpander"]:hover::after {
            opacity: 1;
        }
        
        div[data-testid="stExpander"] .streamlit-expanderContent,
        div[data-testid="stExpander"] p,
        div[data-testid="stExpander"] li,
        div[data-testid="stExpander"] span,
        div[data-testid="stExpander"] div {
            font-size: 1.15rem !important;
            color: #334155 !important;
        }
        
        /* Additional text visibility fixes */
        .stMarkdown p, .stMarkdown li, .stMarkdown span {
            color: #334155 !important;
        }
        
        .streamlit-expanderHeader {
            color: #1e293b !important;
            font-weight: 600;
        }
        
        .streamlit-expanderContent {
            color: #334155 !important;
        }
        """
    else:  # Cyberpunk theme
        return """
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
        
        /* Global styles */
        .main {
            padding: 0rem 2rem;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 30%, #16213e 70%, #0f3460 100%);
            min-height: 100vh;
            position: relative;
        }
        
        .main::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 80%, rgba(0, 255, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255, 0, 128, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(138, 43, 226, 0.1) 0%, transparent 50%);
            pointer-events: none;
        }
        
        .stApp {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 30%, #16213e 70%, #0f3460 100%);
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            background: linear-gradient(180deg, #0f0f0f 0%, #1a1a2e 100%);
            border-right: 2px solid #00ffff;
        }
        
        /* Sidebar text improvements */
        .sidebar .sidebar-content {
            color: #ffffff !important;
        }
        
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f0f0f 0%, #1a1a2e 100%);
        }
        
        section[data-testid="stSidebar"] .css-1d391kg {
            color: #ffffff;
        }
        
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3, 
        section[data-testid="stSidebar"] h4, 
        section[data-testid="stSidebar"] h5, 
        section[data-testid="stSidebar"] h6 {
            color: #00ffff !important;
            font-size: 1.2rem;
        }
        
        section[data-testid="stSidebar"] p {
            color: #ffffff !important;
            font-size: 1rem;
        }
        
        section[data-testid="stSidebar"] .stSelectbox label {
            color: #00ffff !important;
            font-size: 1.1rem;
            font-weight: 600;
        }
        
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
            background-color: rgba(0, 255, 255, 0.1) !important;
            border: 1px solid #00ffff !important;
        }
        
        /* Headers */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Orbitron', monospace;
            color: #00ffff;
            text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff;
            position: relative;
        }
        
        h1::before, h2::before, h3::before {
            content: '';
            position: absolute;
            left: -10px;
            top: 50%;
            transform: translateY(-50%);
            width: 4px;
            height: 80%;
            background: linear-gradient(45deg, #00ffff, #ff0080);
            border-radius: 2px;
            box-shadow: 0 0 10px #00ffff;
        }
        
        /* Main content text */
        .main-content {
            font-family: 'Rajdhani', sans-serif;
            color: #ffffff !important;
            font-size: 1.1rem;
            line-height: 1.6;
            padding-top: 3.5rem;
            padding-bottom: 3.5rem;
            overflow: visible;
        }
        
        /* Fix: Ensure all card containers allow glow/shadow to show */
        .main-content, .themed-card, .education-card, .experience-card, .activity-item, .company-details {
            overflow: visible !important;
            position: relative;
            z-index: 10;
        }
        
        .themed-card {
            z-index: 10;
            overflow: visible;
        }
        
        /* Ensure all text is white only in main content and cards */
        .main-content p, .main-content li, .main-content span, .main-content div,
        .experience-card *, .education-card *, .company-details * {
            color: #ffffff !important;
        }
        
        /* Streamlit text elements */
        .stMarkdown, .stText, .stExpander {
            color: #ffffff !important;
        }
        
        /* Description text */
        .skill-description {
            color: #ffffff !important;
        }
        
        /* Profile image styling */
        .profile-image {
            border-radius: 50%;
            border: 3px solid #00ffff;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
            padding: 5px;
            background: rgba(0, 255, 255, 0.1);
            margin: 1rem 0;
            transition: transform 0.4s cubic-bezier(.4,2.08,.55,.44), box-shadow 0.4s;
        }
        .profile-image:hover {
            transform: scale(1.07) rotate(-3deg);
            box-shadow: 0 0 40px 8px #00ffff99, 0 0 80px 16px #00ffff44;
            border-color: #ff0080;
        }
        
        /* Professional summary card */
        .summary-card {
            background: rgba(0, 255, 255, 0.05);
            border: 2px solid #00ffff;
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem 0;
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.2), inset 0 0 20px rgba(0, 255, 255, 0.05);
            backdrop-filter: blur(15px);
            position: relative;
            overflow: hidden;
        }
        
        .summary-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(0, 255, 255, 0.1), transparent);
            transition: left 0.5s;
        }
        
        .summary-card:hover::before {
            left: 100%;
        }
        
        /* Skill expander styling */
        .skill-expander {
            background: rgba(78, 205, 196, 0.1);
            border: 1px solid #4ecdc4;
            border-radius: 10px;
            margin: 0.5rem 0;
            transition: transform 0.3s cubic-bezier(.4,2.08,.55,.44), box-shadow 0.3s;
        }
        .skill-expander:hover {
            transform: scale(1.03);
            box-shadow: 0 0 24px 2px #4ecdc488, 0 0 40px 8px #4ecdc444;
            border-color: #00ffff;
        }
        
        /* Experience cards */
        .experience-card {
            background: rgba(255, 107, 107, 0.05);
            border: 2px solid #ff6b6b;
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 0 30px rgba(255, 107, 107, 0.2), inset 0 0 20px rgba(255, 107, 107, 0.05);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }
        
        .experience-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, #ff6b6b, #ff0080, #ff6b6b);
            transform: scaleX(0);
            transition: transform 0.3s ease;
        }
        
        .experience-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 40px rgba(255, 107, 107, 0.4), 0 0 60px rgba(255, 107, 107, 0.2);
        }
        
        .experience-card:hover::before {
            transform: scaleX(1);
        }
        
        .company-details {
            background: rgba(239, 68, 68, 0.05);
            border: 1px solid rgba(239, 68, 68, 0.2);
            border-radius: 10px;
            padding: 1rem;
            margin-top: 1rem;
            font-size: 0.9rem;
            line-height: 1.4;
            transition: all 0.3s ease;
        }
        
        .company-details:hover {
            background: rgba(239, 68, 68, 0.1);
            border-color: rgba(239, 68, 68, 0.4);
            box-shadow: 0 4px 15px rgba(239, 68, 68, 0.2);
        }
        
        /* Certification buttons */
        .cert-button {
            background: linear-gradient(45deg, #4ecdc4, #44a08d);
            color: white;
            border: 2px solid #4ecdc4;
            border-radius: 25px;
            padding: 12px 24px;
            font-size: 1rem;
            font-weight: 600;
            font-family: 'Rajdhani', sans-serif;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 4px 15px rgba(78, 205, 196, 0.3), 0 0 20px rgba(78, 205, 196, 0.2);
            margin: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            position: relative;
            overflow: hidden;
        }
        
        .cert-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s;
        }
        
        .cert-button:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 8px 25px rgba(78, 205, 196, 0.5), 0 0 30px rgba(78, 205, 196, 0.3);
            background: linear-gradient(45deg, #44a08d, #4ecdc4);
        }
        
        .cert-button:hover::before {
            left: 100%;
        }
        
        /* Education and activity cards */
        .education-card, .activity-item {
            background: rgba(255, 107, 107, 0.1);
            border: 1px solid #ff6b6b;
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 0 20px rgba(255, 107, 107, 0.2);
            transition: all 0.3s ease-in-out;
        }
        
        .education-card:hover, .activity-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(255, 107, 107, 0.4);
        }
        
        /* Stats cards */
        .metric-card {
            background: rgba(0, 255, 255, 0.05);
            border: 2px solid #00ffff;
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.2), inset 0 0 20px rgba(0, 255, 255, 0.05);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            margin: 1rem 0;
            backdrop-filter: blur(15px);
            position: relative;
            overflow: hidden;
        }
        
        .metric-card::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent 30%, rgba(0, 255, 255, 0.1) 50%, transparent 70%);
            transform: translateX(-100%);
            transition: transform 0.6s ease;
        }
        
        .metric-card:hover {
            transform: translateY(-8px) scale(1.05);
            box-shadow: 0 20px 40px rgba(0, 255, 255, 0.4), 0 0 60px rgba(0, 255, 255, 0.2);
        }
        
        .metric-card:hover::after {
            transform: translateX(100%);
        }
        
        .metric-number {
            font-family: 'Orbitron', monospace;
            font-size: 2.5rem;
            font-weight: 900;
            color: #00ff41;
            text-shadow: 0 0 15px #00ff41, 0 0 30px #00ff41;
            margin-bottom: 0.5rem;
            position: relative;
            animation: glow 2s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from { text-shadow: 0 0 15px #00ff41, 0 0 30px #00ff41; }
            to { text-shadow: 0 0 20px #00ff41, 0 0 40px #00ff41, 0 0 60px #00ff41; }
        }
        
        .metric-label {
            font-family: 'Rajdhani', sans-serif;
            color: #ffffff;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 1.1rem;
            letter-spacing: 1px;
        }
        
        /* YouTube stats styling */
        .youtube-stats {
            background: rgba(255, 0, 0, 0.1);
            border: 1px solid #ff0000;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 0 20px rgba(255, 0, 0, 0.3);
        }
        
        .gaming-stats {
            background: rgba(138, 43, 226, 0.1);
            border: 1px solid #8a2be2;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 0 20px rgba(138, 43, 226, 0.3);
        }
        
        /* Social links in sidebar */
        .social-link {
            display: block;
            text-decoration: none;
            color: #00ffff;
            margin: 0.5rem 0;
            padding: 0.8rem 1rem;
            border: 1px solid #00ffff;
            border-radius: 25px;
            transition: all 0.3s ease-in-out;
            font-family: 'Rajdhani', sans-serif;
            font-weight: 600;
            text-align: center;
            background: rgba(0, 255, 255, 0.05);
        }
        
        .social-link:hover {
            background: rgba(0, 255, 255, 0.2);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 255, 255, 0.3);
            color: #ffffff;
        }
        
        /* Sidebar image styling */
        .sidebar-image {
            width: 25px;
            height: 25px;
            margin-right: 8px;
            vertical-align: middle;
            border-radius: 50%;
        }
        
        /* Resume download button */
        .download-button {
            background: linear-gradient(45deg, #ff6b6b, #ee5a24);
            color: white;
            border: 2px solid #ff6b6b;
            border-radius: 25px;
            padding: 12px 24px;
            font-size: 1rem;
            font-weight: 600;
            font-family: 'Rajdhani', sans-serif;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3), 0 0 20px rgba(255, 107, 107, 0.2);
            margin: 1rem 0;
            text-transform: uppercase;
            letter-spacing: 1px;
            width: 100%;
            position: relative;
            overflow: hidden;
            text-decoration: none;
            display: inline-block;
            text-align: center;
        }
        
        .download-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s;
        }
        
        .download-button:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 8px 25px rgba(255, 107, 107, 0.5), 0 0 30px rgba(255, 107, 107, 0.3);
            background: linear-gradient(45deg, #ee5a24, #ff6b6b);
            color: white;
            text-decoration: none;
        }
        
        .download-button:hover::before {
            left: 100%;
        }
        
        /* Animations */
        .fade-in {
            animation: fadeIn 0.8s ease-in-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Cyberpunk scan lines effect */
        .cyberpunk-scan {
            position: relative;
            overflow: hidden;
        }
        
        .cyberpunk-scan::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, #00ffff, transparent);
            animation: scan 3s linear infinite;
        }
        
        @keyframes scan {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(100vh); }
        }
        
        /* Matrix rain effect for background */
        .matrix-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
            opacity: 0.1;
        }
        
        /* Glitch effect for headers */
        .glitch {
            position: relative;
        }
        
        .glitch::before,
        .glitch::after {
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        
        .glitch::before {
            animation: glitch-1 2s infinite linear alternate-reverse;
            color: #ff0080;
            z-index: -1;
        }
        
        .glitch::after {
            animation: glitch-2 3s infinite linear alternate-reverse;
            color: #00ffff;
            z-index: -2;
        }
        
        @keyframes glitch-1 {
            0%, 14%, 15%, 49%, 50%, 99%, 100% { transform: translate(0); }
            15%, 49% { transform: translate(-2px, 2px); }
        }
        
        @keyframes glitch-2 {
            0%, 20%, 21%, 62%, 63%, 99%, 100% { transform: translate(0); }
            21%, 62% { transform: translate(2px, -2px); }
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 2rem 0;
            font-family: 'Orbitron', monospace;
            color: #00ffff;
            font-size: 0.9rem;
            margin-top: 3rem;
            border-top: 1px solid #00ffff;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .main { padding: 0rem 1rem; }
            .metric-number { font-size: 2rem; }
            .summary-card, .experience-card { padding: 1.5rem; }
        }
        
        /* Additional text visibility fixes */
        .stMarkdown p, .stMarkdown li, .stMarkdown span {
            color: #ffffff !important;
        }
        
        /* Streamlit expander styling */
        .streamlit-expanderHeader {
            color: #00ffff !important;
            font-weight: 600;
        }
        
        .streamlit-expanderContent {
            color: #ffffff !important;
        }
        
        /* Button styling improvements */
        .stButton > button {
            background: linear-gradient(45deg, #4ecdc4, #44a08d) !important;
            color: white !important;
            border: 2px solid #4ecdc4 !important;
            border-radius: 25px !important;
            font-weight: 600 !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-3px) scale(1.05) !important;
            box-shadow: 0 8px 25px rgba(78, 205, 196, 0.5) !important;
        }

        /* Add custom CSS for .themed-card box and hover effect */
        .themed-card {
            background: rgba(10, 20, 40, 0.95);
            border: 2px solid #00ffff;
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 0 24px 2px #00ffff44;
            transition: transform 0.3s cubic-bezier(.4,2.08,.55,.44), box-shadow 0.3s, border-color 0.3s;
            position: relative;
            overflow: visible;
        }
        .education-card, .activity-item, .experience-card {
            overflow: visible;
        }
        .themed-card:hover {
            transform: translateY(-8px) scale(1.03);
            box-shadow: 0 12px 40px 0 #00ffff88, 0 0 60px #00ffff33;
            border-color: #ff0080;
        }
        .themed-card h3, .themed-card h4, .themed-card h5, .themed-card h6 {
            color: #00ffff;
            margin-top: 0;
        }
        .themed-card ul, .themed-card li, .themed-card p, .themed-card strong {
            color: #fff !important;
        }

        /* Add hover animation to Streamlit expanders */
        div[data-testid="stExpander"] {
            transition: box-shadow 0.3s, transform 0.3s;
            border-radius: 10px !important;
        }
        div[data-testid="stExpander"]:hover {
            box-shadow: 0 0 24px 2px #4ecdc488, 0 0 40px 8px #4ecdc444;
            transform: scale(1.03);
            border: 1.5px solid #00ffff;
            z-index: 2;
        }

        /* Increase font size for text inside Streamlit expanders (Skills section) */
        div[data-testid="stExpander"] .streamlit-expanderContent,
        div[data-testid="stExpander"] p,
        div[data-testid="stExpander"] li,
        div[data-testid="stExpander"] span,
        div[data-testid="stExpander"] div {
            font-size: 1.15rem !important;
        }
        """

# Apply theme CSS
st.markdown(f"""
<style>
{get_theme_css(st.session_state.current_theme)}
</style>
""", unsafe_allow_html=True)

# Skill descriptions dictionary
skill_descriptions = {
    "Python": "🐍 High-level programming language used for data science, machine learning, automation, and web development. Proficient in libraries like pandas, numpy, scikit-learn, and frameworks like Django and Flask.",
    "C#": "#️⃣ Object-oriented programming language developed by Microsoft, used for desktop applications, game development with Unity, web development with ASP.NET, and enterprise applications.",
    "C++": "➕ High-performance programming language excellent for system programming, game development, embedded systems, and performance-critical applications requiring direct hardware control.",
    "Java": "☕ Platform-independent object-oriented programming language used for enterprise applications, Android development, web services, and large-scale distributed systems.",
    "Docker": "🐳 Containerization platform that packages applications and dependencies into lightweight, portable containers for consistent deployment across different environments and cloud platforms.",
    "Kubernetes": "⛵ Container orchestration platform for automating deployment, scaling, and management of containerized applications in production environments with high availability.",
    "Streamlit": "🌐 Python framework for building interactive web applications and data dashboards with minimal code, perfect for data science projects and rapid prototyping.",
    "Dash Webapps": "📊 Python framework for building analytical web applications, particularly useful for creating interactive data visualizations and business intelligence dashboards.",
    "Apache NiFi": "🌿 Data integration tool for automating data flow between systems with a web-based user interface for designing, controlling, and monitoring data pipelines.",
    "Apache Tableau": "📈 Business intelligence tool for creating interactive data visualizations and dashboards for data analysis, reporting, and business decision-making.",
    "Playwright Automation": "🤖 Modern automation framework for web testing that supports multiple browsers and provides reliable end-to-end testing with advanced features.",
    "SEMrush": "📏 Digital marketing tool for SEO, content marketing, competitor research, PPC, and social media marketing analytics to improve online visibility.",
    "Selenium": "🌿 Web automation framework for testing web applications across different browsers and platforms with support for multiple programming languages.",
    "Robot Framework": "🤖 Generic automation framework for acceptance testing, acceptance test-driven development, and robotic process automation (RPA).",
    "pytest": "🧪 Python testing framework that makes it easy to write simple and scalable test cases for Python applications with powerful fixtures and plugins.",
    "Playwright": "🎭 Cross-browser automation library that provides reliable and fast automation for modern web applications with advanced debugging capabilities.",
    "UI Testing": "🖥️ Testing methodology focused on verifying user interface elements, user interactions, visual components, and overall user experience of applications.",
    "Manual Testing": "🔍 Testing approach where test cases are executed manually by human testers to identify bugs, usability issues, and ensure software quality.",
    "Test Automation": "⚙️ Practice of using automation tools and scripts to execute test cases, reducing manual effort and increasing testing efficiency and coverage.",
    "Load Testing": "📈 Performance testing technique to evaluate system behavior under expected and peak load conditions to ensure scalability and reliability.",
    "GitHub": "🐙 Version control platform for collaborative software development, project management, and code hosting with Git integration and advanced features.",
    "Jira": "📋 Project management and issue tracking tool used for agile development, bug tracking, sprint planning, and team collaboration in software projects.",
    "YAML": "🔧 Human-readable data serialization standard used for configuration files, data exchange, automation scripts, and infrastructure as code.",
    "NLP": "🧠 Natural Language Processing - AI field focused on enabling computers to understand, interpret, and generate human language for various applications.",
    "Excel": "📊 Spreadsheet application for data analysis, calculations, charting, and business intelligence with advanced formula capabilities and data visualization.",
    "Word": "📝 Word processing application for creating, editing, and formatting documents with advanced layout, collaboration, and publishing features.",
    "PowerPoint": "📽️ Presentation software for creating interactive slideshows, business presentations, and visual communication materials with multimedia support."
}

# Certificate images mapping
certificate_images = {
    "Katonic MLOps Certification Course": "src/Images/Katonic-Mlops-certificate.png",
    "Docker and Kubernetes: The Complete Guide": "src/Images/Docker.png",
    "Learn Python Programming Masterclass": "src/Images/Python.png",
    "Advanced Google Analytics": "src/Images/Google-ana.png",
    "ZCODE TECHNOLOGY - Embedded Systems": "src/Images/Z-code.png"
}

# Function to create download link for PDF
def get_pdf_download_link(pdf_path, download_text):
    try:
        with open(pdf_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        b64_pdf = base64.b64encode(pdf_bytes).decode()
        href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="Ishan_Chakraborty_Resume.pdf" class="social-link" target="_blank">{download_text}</a>'
        return href
    except FileNotFoundError:
        return f'<p style="color: #ff6b6b;">Resume PDF not found at {pdf_path}</p>'

# Loading animation
with st.spinner("Loading your digital portfolio..."):
    time.sleep(1)

# --- SIDEBAR TITLE & SELECTBOX FIX ---
# Add a centered app name/title to the sidebar with theme-aware styling
if st.session_state.current_theme == "Professional":
    st.sidebar.markdown("""
    <div style='text-align: center; margin-bottom: 1.5rem;'>
        <span style='font-family: Poppins, sans-serif; font-size: 1.5rem; color: #1e293b; font-weight: 700;'>
            🚀 Digital Portfolio App
        </span>
    </div>
    """, unsafe_allow_html=True)
else:
    st.sidebar.markdown("""
    <div style='text-align: center; margin-bottom: 1.5rem;'>
        <span style='font-family: Orbitron, monospace; font-size: 1.5rem; color: #00ffff; text-shadow: 0 0 10px #00ffff;'>
            🚀 Digital Portfolio App
        </span>
    </div>
    """, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown("## 🎮 Navigation")

# Fix selectbox text color
st.markdown("""
<style>
section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"],
section[data-testid="stSidebar"] .stSelectbox input,
section[data-testid="stSidebar"] .stSelectbox span,
section[data-testid="stSidebar"] .stSelectbox [role="option"],
section[data-testid="stSidebar"] .stSelectbox [data-baseweb="popover"] * {
    color: #111 !important;
    background: #fff !important;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# Navigation sections
sections = ["🏠 Home", "🎯 Skills", "💼 Experience", "🎓 Education", "🏆 Certifications", "🎲 Activities", "📊 Stats"]
selected_section = st.sidebar.selectbox("Choose Section", sections)

st.sidebar.markdown("---")

# Social links in sidebar with proper images
st.sidebar.markdown("### 🔗 Connect With Me")

# Social media links with images from src/Images folder
social_media_links = [
    ("Email", "mailto:ishanchakraborty2496@gmail.com", "src/Images/Email-logo.png"),
    ("LinkedIn", "https://www.linkedin.com/in/ishan-chakraborty-0085571a1/", "src/Images/linkedin-logo.png"),
    ("GitHub", "https://github.com/Ishan96Dev", "src/Images/GitHub-logo.png"),
    ("YouTube", "https://youtube.com/@ishangaming96?si=eF2AG_p8L06nCaxE", "src/Images/YouTube-logo.png"),
    ("Instagram", "https://instagram.com/ig_ishangamingyt", "src/Images/Instagram-logo.png"),
    ("Facebook", "https://facebook.com/ishanchakraborty72", "src/Images/Facbook-logo.png"),
    ("Discord", "https://discord.gg/k3m4RC2vpT", "src/Images/Discord-logo.png"),
    ("Twitter", "https://twitter.com/IshanC96", "src/Images/twitter-x-logo.png")
]

for name, url, image_path in social_media_links:
    if image_path and os.path.exists(image_path):
        try:
            img = Image.open(image_path)
            img = img.resize((24, 24))
            img_buffer = io.BytesIO()
            img.save(img_buffer, format='PNG')
            img_b64 = base64.b64encode(img_buffer.getvalue()).decode()
            st.sidebar.markdown(f'''
            <a href="{url}" target="_blank" class="social-link">
                <img src="data:image/png;base64,{img_b64}" style="height:24px;vertical-align:middle;margin-right:8px;">
                {name}
            </a>
            ''', unsafe_allow_html=True)
        except Exception as e:
            st.sidebar.markdown(f'<a href="{url}" target="_blank" class="social-link">{name}</a>', unsafe_allow_html=True)
    else:
        st.sidebar.markdown(f'<a href="{url}" target="_blank" class="social-link">{name}</a>', unsafe_allow_html=True)

st.sidebar.markdown("---")

# Resume download button
st.sidebar.markdown("### 📄 Resume")
resume_path = "src/Docs/Ishan_Chakraborty_Resume.pdf"
if os.path.exists(resume_path):
    download_link = get_pdf_download_link(resume_path, "📥 Download Resume")
    st.sidebar.markdown(download_link, unsafe_allow_html=True)
else:
    st.sidebar.error("Resume PDF not found!")

st.sidebar.markdown("---")

# Quick stats in sidebar
st.sidebar.markdown("### ⚡ Quick Stats")
st.sidebar.markdown("""
<div class="metric-card">
    <div class="metric-number">3+</div>
    <div class="metric-label">Years Experience</div>
</div>
<div class="metric-card">
    <div class="metric-number">25+</div>
    <div class="metric-label">Technologies</div>
</div>
<div class="metric-card">
    <div class="metric-number">5+</div>
    <div class="metric-label">Certifications</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# Theme switcher dropdown at the end
st.sidebar.markdown("### 🎨 Theme")
themes = ["Professional", "Cyberpunk"]
selected_theme = st.sidebar.selectbox("Choose a theme", themes, key="theme_switcher", index=0 if st.session_state.current_theme == "Professional" else 1)

if selected_theme != st.session_state.current_theme:
    st.session_state.current_theme = selected_theme
    st.rerun()

# Main content area
if st.session_state.current_theme == "Professional":
    st.markdown('<div class="main-content fade-in">', unsafe_allow_html=True)
else:
    st.markdown('<div class="main-content fade-in cyberpunk-scan">', unsafe_allow_html=True)

# HOME SECTION
if selected_section == "🏠 Home":
    if st.session_state.current_theme == "Professional":
        st.markdown('<h1>🎮 Welcome to My Digital Portfolio</h1>', unsafe_allow_html=True)
    else:
        st.markdown('<h1 class="glitch" data-text="🎮 Welcome to My Digital Portfolio">🎮 Welcome to My Digital Portfolio</h1>', unsafe_allow_html=True)
    
    # Profile section with proper image handling
    col1, col2 = st.columns([1, 2])
    
    with col1:
        profile_image_path = "src/Images/IMG_20201227_0005 (1).jpg"
        if os.path.exists(profile_image_path):
            try:
                profile_img = Image.open(profile_image_path)
                # Create circular image
                size = min(profile_img.size)
                profile_img = profile_img.resize((300, 300))
                st.markdown("""
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{}" class="profile-image" width="250">
                </div>
                """.format(base64.b64encode(open(profile_image_path, "rb").read()).decode()), unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error loading profile image: {e}")
        else:
            st.error("Profile image not found!")
    
    with col2:
        if st.session_state.current_theme == "Professional":
            st.markdown("""
            <div class="themed-card">
                <h2>🎯 QA Engineer & Data Scientist</h2>
                <h3>🚀 Automation Expert & Gaming Content Creator</h3>
                <p style="color: #334155 !important;">Passionate about quality assurance, data science, and cutting-edge technology. I specialize in test automation, MLOps, and creating engaging gaming content. With expertise in Python, Docker, Kubernetes, and modern testing frameworks, I bridge the gap between technical excellence and creative innovation.</p>
                <p style="color: #334155 !important;">🎮 <strong>Gaming enthusiast</strong> who loves sharing knowledge through YouTube content creation while building robust automation solutions for enterprise applications.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="themed-card">
                <h2>🎯 QA Engineer & Data Scientist</h2>
                <h3>🚀 Automation Expert & Gaming Content Creator</h3>
                <p style="color: #ffffff !important;">Passionate about quality assurance, data science, and cutting-edge technology. I specialize in test automation, MLOps, and creating engaging gaming content. With expertise in Python, Docker, Kubernetes, and modern testing frameworks, I bridge the gap between technical excellence and creative innovation.</p>
                <p style="color: #ffffff !important;">🎮 <strong>Gaming enthusiast</strong> who loves sharing knowledge through YouTube content creation while building robust automation solutions for enterprise applications.</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    # Add top spacer before Career Objective card
    st.markdown('<div style="height: 48px;"></div>', unsafe_allow_html=True)
    # Career objectives
    st.markdown("## 🎯 Career Objective")
    if st.session_state.current_theme == "Professional":
        st.markdown("""
        <div class="themed-card">
            <p style="color: #334155 !important;">To leverage my expertise in quality assurance, test automation, and data science to drive innovation and excellence in software development. I aim to contribute to cutting-edge projects while continuing to grow in MLOps, cloud technologies, and automation frameworks.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="themed-card">
            <p style="color: #ffffff !important;">To leverage my expertise in quality assurance, test automation, and data science to drive innovation and excellence in software development. I aim to contribute to cutting-edge projects while continuing to grow in MLOps, cloud technologies, and automation frameworks.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    # Gaming and content creation stats
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="themed-card">
            <h3>🔴 YouTube Channel Stats</h3>
            <div class="metric-card">
                <div class="metric-number">1K+</div>
                <div class="metric-label">Subscribers</div>
            </div>
            <div class="metric-card">
                <div class="metric-number">50K+</div>
                <div class="metric-label">Total Views</div>
            </div>
            <div class="metric-card">
                <div class="metric-number">100+</div>
                <div class="metric-label">Videos Published</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="themed-card">
            <h3>🎮 Gaming Achievements</h3>
            <div class="metric-card">
                <div class="metric-number">5+</div>
                <div class="metric-label">Years Gaming</div>
            </div>
            <div class="metric-card">
                <div class="metric-number">10+</div>
                <div class="metric-label">Game Reviews</div>
            </div>
            <div class="metric-card">
                <div class="metric-number">500+</div>
                <div class="metric-label">Gaming Hours</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Re-add Home YouTube link with base64 icon
    try:
        yt_img = Image.open("src/Images/YouTube-logo.png")
        yt_img = yt_img.resize((24, 24))
        yt_buffer = io.BytesIO()
        yt_img.save(yt_buffer, format='PNG')
        yt_b64 = base64.b64encode(yt_buffer.getvalue()).decode()
        yt_icon_html = f'<img src="data:image/png;base64,{yt_b64}" style="height:24px;vertical-align:middle;margin-right:8px;">'
    except Exception:
        yt_icon_html = ''

    if st.session_state.current_theme == "Professional":
        st.markdown(f"""
        <div class="themed-card">
            <h3>Check out my latest gaming content and tech tutorials!</h3>
            <a href="https://youtube.com/@ishangaming96?si=eF2AG_p8L06nCaxE" target="_blank" class="social-link">
                {yt_icon_html}Visit My YouTube Channel
            </a>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="themed-card">
            <h3>Check out my latest gaming content and tech tutorials!</h3>
            <a href="https://youtube.com/@ishangaming96?si=eF2AG_p8L06nCaxE" target="_blank" class="social-link">
                {yt_icon_html}Visit My YouTube Channel
            </a>
        </div>
        """, unsafe_allow_html=True)

# SKILLS SECTION
elif selected_section == "🎯 Skills":
    if st.session_state.current_theme == "Professional":
        st.markdown('<h1>🎯 Technical Skills & Expertise</h1>', unsafe_allow_html=True)
    else:
        st.markdown('<h1 class="glitch" data-text="🎯 Technical Skills & Expertise">🎯 Technical Skills & Expertise</h1>', unsafe_allow_html=True)
    
    # Programming Languages
    st.markdown("## 💻 Programming Languages")
    prog_langs = ["Python", "C#", "C++", "Java"]
    for skill in prog_langs:
        with st.expander(f"🔍 {skill}", expanded=False):
            st.markdown(f'<div class="skill-description">{skill_descriptions[skill]}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # DevOps & Cloud
    st.markdown("## ☁️ DevOps & Cloud Technologies")
    devops_skills = ["Docker", "Kubernetes", "GitHub", "YAML"]
    for skill in devops_skills:
        with st.expander(f"🔍 {skill}", expanded=False):
            st.markdown(f'<div class="skill-description">{skill_descriptions[skill]}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Web Development
    st.markdown("## 🌐 Web Development & Frameworks")
    web_skills = ["Streamlit", "Dash Webapps"]
    for skill in web_skills:
        with st.expander(f"🔍 {skill}", expanded=False):
            st.markdown(f'<div class="skill-description">{skill_descriptions[skill]}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Data & Analytics
    st.markdown("## 📊 Data Science & Analytics")
    data_skills = ["Apache NiFi", "Apache Tableau", "NLP", "Excel", "SEMrush"]
    for skill in data_skills:
        with st.expander(f"🔍 {skill}", expanded=False):
            st.markdown(f'<div class="skill-description">{skill_descriptions[skill]}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Testing & Automation
    st.markdown("## 🧪 Testing & Quality Assurance")
    testing_skills = ["Playwright Automation", "Selenium", "Robot Framework", "pytest", "UI Testing", "Manual Testing", "Test Automation", "Load Testing"]
    for skill in testing_skills:
        with st.expander(f"🔍 {skill}", expanded=False):
            st.markdown(f'<div class="skill-description">{skill_descriptions[skill]}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Project Management
    st.markdown("## 📋 Project Management & Collaboration")
    pm_skills = ["Jira"]
    for skill in pm_skills:
        with st.expander(f"🔍 {skill}", expanded=False):
            st.markdown(f'<div class="skill-description">{skill_descriptions[skill]}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Office Suite
    st.markdown("## 📝 Office & Productivity")
    office_skills = ["Word", "PowerPoint"]
    for skill in office_skills:
        with st.expander(f"🔍 {skill}", expanded=False):
            st.markdown(f'<div class="skill-description">{skill_descriptions[skill]}</div>', unsafe_allow_html=True)

# EXPERIENCE SECTION
elif selected_section == "💼 Experience":
    st.markdown('<div style="height: 48px;"></div>', unsafe_allow_html=True)
    if st.session_state.current_theme == "Professional":
        st.markdown('<h1>💼 Professional Experience</h1>', unsafe_allow_html=True)
    else:
        st.markdown('<h1 class="glitch" data-text="💼 Professional Experience">💼 Professional Experience</h1>', unsafe_allow_html=True)

    # Katonic.ai Experience
    if st.session_state.current_theme == "Professional":
        st.markdown("""
        <div class="themed-card">

### 🚀 Quality Assurance Engineer
**Katonic.ai | June 2023 - Present**

**🎯 Role:** Leading quality assurance initiatives for cutting-edge MLOps and AI platforms

**🔧 Key Responsibilities:**
- Developing and implementing comprehensive test automation frameworks using Python and Playwright
- Designing and executing test strategies for MLOps pipelines and AI model deployment systems
- Collaborating with cross-functional teams to ensure product quality and performance optimization
- Creating detailed test documentation and maintaining quality metrics dashboards
- Performing load testing and performance analysis for scalable AI applications
- Implementing CI/CD pipeline integration for automated testing workflows

**🏆 Key Achievements:**
- Reduced manual testing effort by 70% through comprehensive automation framework development
- Improved bug detection rate by 45% through enhanced testing methodologies
- Successfully deployed testing infrastructure for 5+ major product releases
- Mentored junior QA engineers in test automation best practices

**💡 Technologies Used:**
Python, Playwright, Selenium, Docker, Kubernetes, Jenkins, Jira, MLOps Tools, API Testing
""", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="themed-card">

### 🚀 Quality Assurance Engineer
**Katonic.ai | June 2023 - Present**

**🎯 Role:** Leading quality assurance initiatives for cutting-edge MLOps and AI platforms

**🔧 Key Responsibilities:**
- Developing and implementing comprehensive test automation frameworks using Python and Playwright
- Designing and executing test strategies for MLOps pipelines and AI model deployment systems
- Collaborating with cross-functional teams to ensure product quality and performance optimization
- Creating detailed test documentation and maintaining quality metrics dashboards
- Performing load testing and performance analysis for scalable AI applications
- Implementing CI/CD pipeline integration for automated testing workflows

**🏆 Key Achievements:**
- Reduced manual testing effort by 70% through comprehensive automation framework development
- Improved bug detection rate by 45% through enhanced testing methodologies
- Successfully deployed testing infrastructure for 5+ major product releases
- Mentored junior QA engineers in test automation best practices

**💡 Technologies Used:**
Python, Playwright, Selenium, Docker, Kubernetes, Jenkins, Jira, MLOps Tools, API Testing
""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div style="height: 32px;"></div>', unsafe_allow_html=True)

    # Data Scientist Experience
    if st.session_state.current_theme == "Professional":
        st.markdown("""
        <div class="themed-card">

### 🔬 Data Scientist
**Freelance & Personal Projects | 2021 - Present**

**🎯 Role:** Developing machine learning models and data-driven solutions for various domains

**🔧 Key Responsibilities:**
- Designing and implementing machine learning models for predictive analytics
- Performing comprehensive data analysis and statistical modeling
- Creating data visualizations and interactive dashboards using Streamlit
- Developing NLP solutions for text analysis and sentiment analysis
- Building end-to-end ML pipelines with MLOps best practices
- Collaborating with stakeholders to understand business requirements

**🏆 Key Achievements:**
- Developed 5+ machine learning models with 90%+ accuracy
- Created interactive data visualization dashboards for business insights
- Implemented MLOps workflows for model deployment and monitoring
- Published technical articles on data science methodologies

**💡 Technologies Used:**
Python, Pandas, NumPy, Scikit-learn, TensorFlow, Streamlit, Jupyter, MLOps, Docker
""", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="themed-card">

### 🔬 Data Scientist
**Freelance & Personal Projects | 2021 - Present**

**🎯 Role:** Developing machine learning models and data-driven solutions for various domains

**🔧 Key Responsibilities:**
- Designing and implementing machine learning models for predictive analytics
- Performing comprehensive data analysis and statistical modeling
- Creating data visualizations and interactive dashboards using Streamlit
- Developing NLP solutions for text analysis and sentiment analysis
- Building end-to-end ML pipelines with MLOps best practices
- Collaborating with stakeholders to understand business requirements

**🏆 Key Achievements:**
- Developed 5+ machine learning models with 90%+ accuracy
- Created interactive data visualization dashboards for business insights
- Implemented MLOps workflows for model deployment and monitoring
- Published technical articles on data science methodologies

**💡 Technologies Used:**
Python, Pandas, NumPy, Scikit-learn, TensorFlow, Streamlit, Jupyter, MLOps, Docker
""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div style="height: 32px;"></div>', unsafe_allow_html=True)

    # Sectona Experience
    if st.session_state.current_theme == "Professional":
        st.markdown("""
        <div class="themed-card">

### 🛡️ Junior Quality Assurance Engineer
**Sectona | January 2022 - May 2023**

**🎯 Role:** Ensuring security and quality for privileged access management solutions

**🔧 Key Responsibilities:**
- Conducted manual and automated testing for cybersecurity and PAM solutions
- Developed test cases and scenarios for security-critical applications
- Performed vulnerability assessments and security testing protocols
- Collaborated with development teams to identify and resolve security issues
- Maintained detailed test documentation and bug tracking systems
- Participated in agile development processes and sprint planning

**🏆 Key Achievements:**
- Identified and reported 100+ critical security vulnerabilities
- Developed automated test suites that reduced testing time by 50%
- Improved overall product security posture through comprehensive testing
- Successfully completed security certifications and training programs

**💡 Technologies Used:**
Manual Testing, Security Testing, Bug Tracking, Agile Methodologies, Test Case Design
""", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="themed-card">

### 🛡️ Junior Quality Assurance Engineer
**Sectona | January 2022 - May 2023**

**🎯 Role:** Ensuring security and quality for privileged access management solutions

**🔧 Key Responsibilities:**
- Conducted manual and automated testing for cybersecurity and PAM solutions
- Developed test cases and scenarios for security-critical applications
- Performed vulnerability assessments and security testing protocols
- Collaborated with development teams to identify and resolve security issues
- Maintained detailed test documentation and bug tracking systems
- Participated in agile development processes and sprint planning

**🏆 Key Achievements:**
- Identified and reported 100+ critical security vulnerabilities
- Developed automated test suites that reduced testing time by 50%
- Improved overall product security posture through comprehensive testing
- Successfully completed security certifications and training programs

**💡 Technologies Used:**
Manual Testing, Security Testing, Bug Tracking, Agile Methodologies, Test Case Design
""", unsafe_allow_html=True)

# EDUCATION SECTION
elif selected_section == "🎓 Education":
    st.markdown('<div style="height: 48px;"></div>', unsafe_allow_html=True)
    if st.session_state.current_theme == "Professional":
        st.markdown('<h1>🎓 Educational Background</h1>', unsafe_allow_html=True)
    else:
        st.markdown('<h1 class="glitch" data-text="🎓 Educational Background">🎓 Educational Background</h1>', unsafe_allow_html=True)

    if st.session_state.current_theme == "Professional":
        st.markdown("""
        <div class="themed-card">

### 🎓 Bachelor of Technology (B.Tech)
**📚 Computer Science & Engineering**
**🏫 Institution:** Techno India University, West Bengal
**📅 Duration:** 2018 - 2022
**🎯 Grade:** 8.5 CGPA

**📖 Key Coursework:**
- Data Structures and Algorithms
- Database Management Systems
- Software Engineering
- Operating Systems
- Computer Networks
- Machine Learning
- Web Development
- Software Testing

**🏆 Academic Achievements:**
- Consistently maintained above 8.0 CGPA throughout the program
- Completed multiple projects in web development and data science
- Participated in coding competitions and hackathons
- Active member of computer science student organizations

**💡 Final Year Project:**
Developed a comprehensive web application for student management system with advanced features including automated reporting, data analytics, and user role management.
""", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="themed-card">

### 🎓 Bachelor of Technology (B.Tech)
**📚 Computer Science & Engineering**
**🏫 Institution:** Techno India University, West Bengal
**📅 Duration:** 2018 - 2022
**🎯 Grade:** 8.5 CGPA

**📖 Key Coursework:**
- Data Structures and Algorithms
- Database Management Systems
- Software Engineering
- Operating Systems
- Computer Networks
- Machine Learning
- Web Development
- Software Testing

**🏆 Academic Achievements:**
- Consistently maintained above 8.0 CGPA throughout the program
- Completed multiple projects in web development and data science
- Participated in coding competitions and hackathons
- Active member of computer science student organizations

**💡 Final Year Project:**
Developed a comprehensive web application for student management system with advanced features including automated reporting, data analytics, and user role management.
""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div style="height: 32px;"></div>', unsafe_allow_html=True)

    if st.session_state.current_theme == "Professional":
        st.markdown("""
        <div class="themed-card">

### 🎓 Higher Secondary (12th Grade)
**📚 Science Stream**
**🏫 Institution:** Techno India Group Public School
**📅 Year:** 2018
**🎯 Grade:** 82%

**📖 Subjects:**
- Physics
- Chemistry
- Mathematics
- Computer Science
- English

**🏆 Achievements:**
- Secured distinction in Mathematics and Computer Science
- Participated in science fairs and technical competitions
- Completed advanced computer programming courses
""", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="themed-card">

### 🎓 Higher Secondary (12th Grade)
**📚 Science Stream**
**🏫 Institution:** Techno India Group Public School
**📅 Year:** 2018
**🎯 Grade:** 82%

**📖 Subjects:**
- Physics
- Chemistry
- Mathematics
- Computer Science
- English

**🏆 Achievements:**
- Secured distinction in Mathematics and Computer Science
- Participated in science fairs and technical competitions
- Completed advanced computer programming courses
""", unsafe_allow_html=True)

# CERTIFICATIONS SECTION
elif selected_section == "🏆 Certifications":
    st.markdown('<div style="height: 48px;"></div>', unsafe_allow_html=True)
    if st.session_state.current_theme == "Professional":
        st.markdown('<h1>🏆 Professional Certifications</h1>', unsafe_allow_html=True)
    else:
        st.markdown('<h1 class="glitch" data-text="🏆 Professional Certifications">🏆 Professional Certifications</h1>', unsafe_allow_html=True)
    
    certifications = [
        {
            "name": "Katonic MLOps Certification Course",
            "issuer": "Katonic.ai",
            "date": "2023",
            "description": "Comprehensive certification covering MLOps practices, model deployment, and AI/ML pipeline management."
        },
        {
            "name": "Docker and Kubernetes: The Complete Guide",
            "issuer": "Online Learning Platform",
            "date": "2023",
            "description": "Advanced certification in containerization and orchestration technologies for modern application deployment."
        },
        {
            "name": "Learn Python Programming Masterclass",
            "issuer": "Online Learning Platform",
            "date": "2022",
            "description": "Comprehensive Python programming certification covering advanced concepts and practical applications."
        },
        {
            "name": "Advanced Google Analytics",
            "issuer": "Google",
            "date": "2023",
            "description": "Advanced certification in web analytics, data analysis, and digital marketing insights."
        },
        {
            "name": "ZCODE TECHNOLOGY - Embedded Systems",
            "issuer": "ZCODE Technology",
            "date": "2022",
            "description": "Specialized certification in embedded systems programming and IoT device development."
        }
    ]
    
    for cert in certifications:
        st.markdown(f"""
        <div class="education-card">
            <h3>🏅 {cert['name']}</h3>
            <p><strong>🏢 Issuer:</strong> {cert['issuer']}</p>
            <p><strong>📅 Date:</strong> {cert['date']}</p>
            <p><strong>📝 Description:</strong> {cert['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Certificate view button
        if cert['name'] in certificate_images:
            cert_path = certificate_images[cert['name']]
            if os.path.exists(cert_path):
                if st.button(f"🔍 View {cert['name']} Certificate", key=f"cert_{cert['name']}"):
                    try:
                        cert_img = Image.open(cert_path)
                        st.image(cert_img, caption=f"{cert['name']} Certificate", use_column_width=True)
                    except Exception as e:
                        st.error(f"Error loading certificate image: {e}")
            else:
                st.warning(f"Certificate image not found: {cert_path}")
        
        st.markdown("---")
    st.markdown('<div style="height: 32px;"></div>', unsafe_allow_html=True)

# ACTIVITIES SECTION
elif selected_section == "🎲 Activities":
    st.markdown('<div style="height: 48px;"></div>', unsafe_allow_html=True)
    if st.session_state.current_theme == "Professional":
        st.markdown('<h1>🎲 Activities & Interests</h1>', unsafe_allow_html=True)
    else:
        st.markdown('<h1 class="glitch" data-text="🎲 Activities & Interests">🎲 Activities & Interests</h1>', unsafe_allow_html=True)
    
    activities = [
        {
            "title": "🎮 Gaming Content Creation",
            "description": "Active YouTube content creator focusing on gaming tutorials, reviews, and entertainment content. Managing a growing channel with 1K+ subscribers and 50K+ total views.",
            "details": [
                "Create engaging gaming content and tutorials",
                "Live streaming and community interaction",
                "Video editing and post-production",
                "Growing subscriber base and engagement"
            ]
        },
        {
            "title": "💡 Technology Blog Writing",
            "description": "Writing technical articles and tutorials about software development, testing methodologies, and emerging technologies.",
            "details": [
                "Technical article writing and publishing",
                "Tutorial creation for complex topics",
                "Technology trend analysis and insights",
                "Community engagement and knowledge sharing"
            ]
        },
        {
            "title": "🏆 Competitive Programming",
            "description": "Participating in coding competitions and hackathons to sharpen problem-solving skills and stay updated with algorithmic challenges.",
            "details": [
                "Regular participation in coding contests",
                "Algorithm optimization and problem-solving",
                "Team collaboration in hackathons",
                "Continuous learning and skill development"
            ]
        },
        {
            "title": "🎯 Open Source Contributions",
            "description": "Contributing to open-source projects and maintaining personal repositories for automation tools and testing frameworks.",
            "details": [
                "Active GitHub contributor",
                "Developing automation tools and scripts",
                "Community collaboration and code reviews",
                "Documentation and knowledge sharing"
            ]
        }
    ]
    
    for activity in activities:
        st.markdown(f"""
        <div class="activity-item">
            <h3>{activity['title']}</h3>
            <p>{activity['description']}</p>
            <div class="company-details">
                <h5>🔧 Key Activities:</h5>
                <ul>
                    {''.join([f"<li>{detail}</li>" for detail in activity['details']])}
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
    st.markdown('<div style="height: 32px;"></div>', unsafe_allow_html=True)

# STATS SECTION
elif selected_section == "📊 Stats":
    if st.session_state.current_theme == "Professional":
        st.markdown('<h1>📊 Professional & Personal Statistics</h1>', unsafe_allow_html=True)
    else:
        st.markdown('<h1 class="glitch" data-text="📊 Professional & Personal Statistics">📊 Professional & Personal Statistics</h1>', unsafe_allow_html=True)
    
    # Professional Stats
    st.markdown("## 💼 Professional Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">3+</div>
            <div class="metric-label">Years Experience</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">25+</div>
            <div class="metric-label">Technologies</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">10+</div>
            <div class="metric-label">Projects Completed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">5+</div>
            <div class="metric-label">Certifications</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Technical Skills Stats
    st.markdown("## 🎯 Technical Skills Proficiency")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">90%</div>
            <div class="metric-label">Python Proficiency</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">85%</div>
            <div class="metric-label">Test Automation</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">80%</div>
            <div class="metric-label">DevOps Tools</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Content Creation Stats
    st.markdown("## 🎮 Content Creation Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="youtube-stats">
            <h4>🔴 YouTube Channel</h4>
            <div class="metric-card">
                <div class="metric-number">1K+</div>
                <div class="metric-label">Subscribers</div>
            </div>
            <div class="metric-card">
                <div class="metric-number">50K+</div>
                <div class="metric-label">Total Views</div>
            </div>
            <div class="metric-card">
                <div class="metric-number">100+</div>
                <div class="metric-label">Videos Published</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="gaming-stats">
            <h4>🎮 Gaming Achievements</h4>
            <div class="metric-card">
                <div class="metric-number">5+</div>
                <div class="metric-label">Years Gaming</div>
            </div>
            <div class="metric-card">
                <div class="metric-number">10+</div>
                <div class="metric-label">Game Reviews</div>
            </div>
            <div class="metric-card">
                <div class="metric-number">500+</div>
                <div class="metric-label">Gaming Hours</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Learning and Development Stats
    st.markdown("## 📚 Learning & Development")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">15+</div>
            <div class="metric-label">Courses Completed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">100+</div>
            <div class="metric-label">Learning Hours</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">50+</div>
            <div class="metric-label">Blog Articles Read</div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
if st.session_state.current_theme == "Professional":
    st.markdown("""
    <div class="footer">
        <p>💻 Crafted with ❤️ by Ishan Chakraborty | © 2024 All Rights Reserved</p>
        <p>🚀 Powered by Streamlit & Python | 🎮 Built for the Future</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="footer">
        <p>💻 Crafted with ❤️ by Ishan Chakraborty | © 2024 All Rights Reserved</p>
        <p>🚀 Powered by Streamlit & Python | 🎮 Built for the Future</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Theme-aware sidebar dropdown styling is handled in the CSS above
