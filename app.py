"""
MT Graduate Career Launchpad
Enterprise AI Agent Edition - Middle Technology Branding Build
"""

import streamlit as st
import json
import hashlib
import os

# --- INITIALIZE BACKEND ---
# (Keep your existing hash_password, load_users, save_users, register_user, authenticate_user functions here)

# --- PREMIUM STYLING ENGINE (Updated for Middle Technology Branding) ---
def inject_premium_styles():
    st.markdown("""
        <style>
        /* Remove default branding */
        #MainMenu, footer, header {visibility: hidden !important;}
        .stDeployButton {display:none !important;}
        
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        
        .stApp {
            background-color: #121212 !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #E2E8F0 !important;
        }
        
        h1, h2, h3, h4, h5, h6, p, span, label { color: #E2E8F0 !important; }

        .premium-hero {
            background: linear-gradient(135deg, #2D2D2D 0%, #1A1A1A 100%);
            text-align: center;
            padding: 35px 20px;
            border-radius: 20px;
            margin-bottom: 25px;
            border-bottom: 3px solid #C5A059;
            box-shadow: 0 10px 25px rgba(197, 160, 89, 0.15);
        }
        
        .premium-hero h1 { color: #C5A059 !important; font-weight: 800 !important; }

        .premium-card {
            background: #1E1E1E;
            padding: 24px;
            border-radius: 16px;
            border: 1px solid #333;
            margin-bottom: 20px;
        }
        
        .premium-card h3 { color: #C5A059 !important; }

        div.stButton > button {
            background: linear-gradient(90deg, #8B6B23 0%, #C5A059 100%) !important;
            color: #000 !important;
            font-weight: 700 !important;
            border: none !important;
            border-radius: 8px !important;
        }
        
        .system-footer {
            background-color: #1A1A1A;
            border-top: 2px solid #C5A059;
            padding: 30px;
            border-radius: 16px;
            text-align: center;
            color: #ffffff !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- MAIN INTERFACE ---
def main():
    st.set_page_config(page_title="MT Career Launchpad", page_icon="🎓", layout="wide")
    inject_premium_styles()
    
    # ... [Keep your Session State init logic here] ...

    # Display Hero Header
    st.markdown("""
        <div class="premium-hero">
            <h1>Graduate Career Launchpad</h1>
            <p>Empowering Innovation - Reshaping The Future</p>
        </div>
    """, unsafe_allow_html=True)

    # ... [Keep your login/routing logic here] ...

    render_footer()

def render_footer():
    st.markdown("""
        <div class="system-footer">
            <h4>MIDDLE TECHNOLOGY</h4>
            <p>Graphic Design, Empower, Innovation, Reshaping The Future.</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
