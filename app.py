"""
MT Graduate Career Launchpad
Enterprise SaaS Dashboard - Production Build
"""

import streamlit as st
import os

# =============================================================================
# ENTERPRISE UI/UX CSS INJECTION (HIDES BRANDING & ENFORCES THEME)
# =============================================================================
def inject_enterprise_styles():
    st.markdown("""
        <style>
        /* Hide Streamlit Branding */
        #MainMenu, footer, header, .stDeployButton {visibility: hidden !important;}
        
        /* Layout & Theme */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
        .stApp {background-color: #F8FAFC !important; font-family: 'Plus Jakarta Sans', sans-serif !important;}
        
        /* Glassmorphism & Cards */
        .glass-card {background: #ffffff; border: 1px solid #E2E8F0; border-radius: 16px; padding: 24px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);}
        
        /* Analytics Grid */
        .saas-grid {display: flex; gap: 15px; margin-bottom: 25px; flex-wrap: wrap;}
        .saas-card {flex: 1; min-width: 150px; background: #ffffff; border: 1px solid #E2E8F0; padding: 20px; border-radius: 12px; text-align: center; border-top: 4px solid #0B6B3A;}
        
        /* Status Badges */
        .b-green {background: #DCFCE7; border-left: 5px solid #22C55E; color: #14532D; padding: 10px; border-radius: 8px; margin-bottom: 5px;}
        .b-blue {background: #DBEAFE; border-left: 5px solid #3B82F6; color: #1E3A8A; padding: 10px; border-radius: 8px; margin-bottom: 5px;}
        .b-orange {background: #FFEDD5; border-left: 5px solid #F97316; color: #7C2D12; padding: 10px; border-radius: 8px; margin-bottom: 5px;}
        .b-red {background: #FEE2E2; border-left: 5px solid #EF4444; color: #7F1D1D; padding: 10px; border-radius: 8px; margin-bottom: 5px;}
        </style>
    """, unsafe_allow_html=True)

# =============================================================================
# MAIN DASHBOARD
# =============================================================================
def main():
    st.set_page_config(page_title="Launchpad", layout="wide")
    inject_enterprise_styles()

    # 1. Career Readiness Score
    st.markdown('<div class="glass-card" style="border-top: 4px solid #0B6B3A;">', unsafe_allow_html=True)
    st.markdown("<h3>Career Readiness Score</h3>", unsafe_allow_html=True)
    st.markdown("<h1 style='color:#0B6B3A;'>82%</h1>", unsafe_allow_html=True)
    st.progress(0.82)
    st.markdown("Profile Strength: 90% | Skills Match: 78% | CV Quality: 88% | Interview Readiness: 72%", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. Analytics Cards
    st.markdown("""
        <div class="saas-grid">
            <div class="saas-card"><h2>88%</h2><div style='color:#64748B;'>ATS SCORE</div></div>
            <div class="saas-card"><h2>54</h2><div style='color:#64748B;'>JOBS FOUND</div></div>
            <div class="saas-card"><h2>3</h2><div style='color:#64748B;'>INTERVIEWS</div></div>
            <div class="saas-card"><h2>2</h2><div style='color:#64748B;'>SKILLS GAP</div></div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        # 4. Employability Prediction
        st.markdown('<div class="glass-card"><h3>Employment Probability</h3><h2 style="color:#0B6B3A;">87%</h2>', unsafe_allow_html=True)
        st.markdown("<div class='b-green'>✓ Strong Communication</div><div class='b-green'>✓ High ATS Score</div><div class='b-red'>⚠ Need More Projects</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 5. Job Matching
        st.markdown('<div class="glass-card"><h3>Recommended Jobs</h3>', unsafe_allow_html=True)
        st.markdown("Project Coordinator (94% Match) | Business Analyst (89% Match)")
        st.button("Apply / Save")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # 3. AI Career Copilot
        st.markdown('<div class="glass-card"><h3>AI Career Copilot</h3>', unsafe_allow_html=True)
        st.text_input("How do I improve my CV?")
        st.button("Analyze")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 11. MT Employability Score
        st.markdown('<div class="glass-card" style="background:#F0FDF4; border: 2px solid #0B6B3A;"><h3>🏆 MT Employability Score™</h3><h2>84/100</h2>', unsafe_allow_html=True)
        st.markdown('Career Match: 92% | CV: 88% | Skills: 79%', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 10. Impact Section
    st.markdown("<br><hr><h3>Graduate Career Launchpad Impact</h3>", unsafe_allow_html=True)
    st.columns(4)[0].metric("Registered", "1,250")
    st.columns(4)[1].metric("CVs Optimized", "3,800")
    st.columns(4)[2].metric("Interviews", "940")
    st.columns(4)[3].metric("Success Rate", "76%")

if __name__ == '__main__':
    main()
