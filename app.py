    # ---- AUTHENTICATED USER INTERFACE ----
    st.sidebar.success(f"Logged in as: **{st.session_state.username}**")
    
    # Tool Navigation Menu - Added a "Home / Dashboard" option as the default
    tool_choice = st.sidebar.selectbox(
        "Select AI Tool", 
        ["Home Dashboard", "AI CV Builder", "Cover Letter Generator", "Interview Coach"]
    )
    
    # Logout Button at the bottom of sidebar
    st.sidebar.markdown("---")
    if st.sidebar.button("Log Out"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    # ---- MAIN APP INTERACTION PAGES ----
    st.title("🚀 MT Graduate Career Launchpad")
    st.caption("Powered by Qwen 3.7 Plus AI Architecture")
    st.markdown("---")

    # NEW: Welcoming, content-rich Home Dashboard
    if tool_choice == "Home Dashboard":
        st.subheader(f"Welcome back, {st.session_state.username}! 👋")
        st.markdown("""
        Welcome to your intelligent career acceleration suite. This platform is specifically tailored to help 
        graduates refine their professional branding, optimize application assets, and ace competitive interviews.
        
        ### 💡 Available Intelligence Tools:
        """)
        
        # Displaying features in clear, clickable-looking info blocks
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("### 📝 AI CV Builder\n\nTailor your current resume against any target job description. Uncover skill gaps and instantly optimize your keywords.")
        with col2:
            st.success("### ✉️ Cover Letter Builder\n\nGenerate high-impact, completely bespoke cover letters highlighting your unique background for specific employers.")
        with col3:
            st.warning("### 🎙️ Interview Coach\n\nPractice tough behavioral interview questions and receive structured feedback utilizing the STAR methodology.")
            
        st.markdown("---")
        st.markdown("""
        ### 📱 Mobile User Tip:
        If you are on a mobile device, **tap the small arrow icon (`>`) at the top-left corner** of your screen to open the navigation menu and launch a specific tool!
        """)

    # TOOL 1: AI CV Builder
    elif tool_choice == "AI CV Builder":
        st.header("📝 AI CV Builder & Tailoring Tool")
        st.write("Paste your current CV text and target job description to optimize your content.")
        
        col1, col2 = st.columns(2)
        with col1:
            cv_input = st.text_area("Your Current CV Text", height=250, placeholder="Paste your resume details here...")
        with col2:
            jd_input = st.text_area("Target Job Description", height=250, placeholder="Paste the job advertisement requirements here...")
            
        if st.button("Analyze & Optimize CV"):
            if cv_input and jd_input:
                with st.spinner("Qwen AI is reviewing your layout and syntax..."):
                    feedback = generate_cv_critique(cv_input, jd_input)
                    st.markdown(feedback)
            else:
                st.warning("Please provide both your CV and the Job Description to continue.")

    # TOOL 2: Cover Letter Generator
    elif tool_choice == "Cover Letter Generator":
        st.header("✉️ Cover Letter Generator")
        st.write("Generate a bespoke, professional cover letter tailored to your dream organization.")
        
        comp_name = st.text_input("Company Name", placeholder="e.g., Google, McKinsey, Stripe")
        j_title = st.text_input("Job Title", placeholder="e.g., Management Trainee, Associate Consultant")
        u_profile = st.text_area("Key Highlights of Your Profile", height=150, placeholder="e.g., Computer Science honors graduate with 2 internships in data analysis and agile scrum experience.")
        
        if st.button("Generate Cover Letter"):
            if comp_name and j_title and u_profile:
                with st.spinner("Drafting high-impact cover letter via Qwen AI..."):
                    letter = generate_cover_letter(u_profile, comp_name, j_title)
                    st.success("Cover letter generated successfully!")
                    st.text_area("Generated Output", value=letter.strip(), height=350)
            else:
                st.warning("Please fill out all the input fields.")

    # TOOL 3: Interview Coach
    elif tool_choice == "Interview Coach":
        st.header("🎙️ AI Interactive Interview Coach")
        st.write("Practice answering challenging behavioral or technical questions and receive immediate smart feedback.")
        
        mock_question = "Tell me about a time you had to deal with a conflict within a cross-functional team, and how you resolved it."
        st.info(f"**Practice Question:** \n\n {mock_question}")
        
        user_ans = st.text_area("Your Response (Use the STAR Method: Situation, Task, Action, Result)", height=200, placeholder="Type your answer here...")
        
        if st.button("Submit Response for Feedback"):
            if user_ans:
                with st.spinner("Analyzing communication frameworks and metrics..."):
                    coach_feedback = generate_interview_feedback(mock_question, user_ans)
                    st.markdown(coach_feedback)
            else:
                st.warning("Please type an answer before requesting feedback.")

if __name__ == '__main__':
    main()
