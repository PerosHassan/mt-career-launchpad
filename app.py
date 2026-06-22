def inject_premium_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700;800&display=swap');
        
        /* Force App Base Background & Universal Inheritance */
        .stApp {
            background: linear-gradient(180deg, #063c22 0%, #0d6137 50%, #114d2e 100%) !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #ffffff !important;
        }
        
        /* AGGRESSIVE WHITE CONTRAST OVERRIDE FOR ALL TEXT/LABELS ON MOBILE */
        h1, h2, h3, h4, h5, h6, p, span, li, label, div, select {
            color: #ffffff !important;
        }

        /* Target Streamlit widget text input fields & titles natively */
        div[data-testid="stWidgetLabel"] p, 
        .stSelectbox label p, 
        .stTextInput label p, 
        .stTextArea label p,
        .stWidgetFormModifier label {
            color: #ffffff !important;
            font-weight: 700 !important;
            font-size: 16px !important;
        }
        
        /* Branding Element Geometry */
        .brand-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 14px;
            margin-bottom: 5px;
        }
        .logo-mark {
            background: linear-gradient(135deg, #2ae083 0%, #198754 100%);
            width: 48px;
            height: 48px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 8px 16px rgba(42, 224, 131, 0.25);
            font-weight: 800;
            color: white !important;
            font-size: 22px;
        }
        
        /* Layout Hero Presentation */
        .premium-hero {
            text-align: center;
            padding: 20px 10px;
            color: white;
        }
        .premium-hero h1 {
            font-size: 36px !important;
            font-weight: 800 !important;
            margin: 0 !important;
        }
        .premium-hero p.tagline {
            color: #a3e6be !important;
            font-size: 18px !important;
            margin-top: 4px !important;
        }
        
        /* Safe Form Text Styling (Inputs remain legible inside fields) */
        .stTextInput input, .stTextArea textarea {
            color: #1f2937 !important;
            font-weight: 500 !important;
            background-color: #ffffff !important;
            border-radius: 12px !important;
        }
        
        /* FIX FOR SELECTBOX DROPDOWN TEXT INVISIBILITY */
        /* Forces deep dark text color inside the selection tray and lists */
        div[data-baseweb="select"] *, 
        ul[role="listbox"] *, 
        li[role="option"] * {
            color: #1f2937 !important;
            font-weight: 500 !important;
        }
        
        /* Premium Translucent System Cards */
        .premium-card {
            background: rgba(255, 255, 255, 0.12);
            padding: 20px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            margin-bottom: 20px;
        }
        .premium-card h3 {
            font-size: 22px !important;
            font-weight: 700 !important;
            margin-top: 0 !important;
            color: #ffffff !important;
        }
        
        /* Global Navigation/Action Button Interface Engine */
        div.stButton > button {
            background: linear-gradient(90deg, #2ae083 0%, #198754 100%) !important;
            color: #ffffff !important;
            border-radius: 12px !important;
            border: none !important;
            padding: 12px 24px !important;
            font-weight: 700 !important;
            width: 100%;
        }
        div.stButton > button:hover {
            color: #063c22 !important;
            background: #ffffff !important;
        }
        </style>
    """, unsafe_allow_html=True)
