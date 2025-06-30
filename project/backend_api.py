import streamlit as st
from medical_knowledge import get_disease_predictions

st.set_page_config(page_title="HealthAI Pro", layout="centered")

st.sidebar.title("📋 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "💬 Patient Chat", "ℹ️ About", "💡 Health Tips", "📞 Contact"])

st.markdown("""
    <style>
        .remedy-box {
            background-color: #fff;
            padding: 1.2rem;
            margin-bottom: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# ========== Home Page ==========
if page == "🏠 Home":
    st.title("🤖 HealthAI Pro")
    st.subheader("AI-powered Disease & Remedy Advisor")
    st.write("Enter your symptoms to get real-time predictions, home remedies, doctor tips & alerts.")

    with st.form("diagnosis_form"):
        symptoms_input = st.text_input("📝 Enter symptoms (comma-separated):", placeholder="e.g. fever, cough")
        submitted = st.form_submit_button("🔍 Diagnose")

    if submitted:
        if not symptoms_input.strip():
            st.warning("⚠️ Please enter at least one symptom.")
        else:
            symptoms = symptoms_input.split(",")
            results = get_disease_predictions(symptoms)

            if results:
                for item in results:
                    st.markdown("<div class='remedy-box'>", unsafe_allow_html=True)
                    st.subheader(f"🦠 {item['Disease']} (Confidence: {item['Confidence']})")
                    st.markdown("### 🌿 Home Remedies")
                    for remedy in item["Remedies"]:
                        st.markdown(f"- {remedy}")
                    st.markdown(f"**💡 Doctor Tip:** {item['Tip']}")
                    if item["Alert"]:
                        st.error(item["Alert"])
                    st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.info("❗ No disease matched. Try rephrasing your symptoms.")

# ========== Patient Chat ==========
elif page == "💬 Patient Chat":
    st.title("💬 Patient Chat Assistant")
    st.write("Ask anything about your health or symptoms.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    with st.form("chat_form"):
        user_input = st.text_input("👤 You:", placeholder="e.g. I have stomach pain", key="chat_input")
        chat_submitted = st.form_submit_button("Send")

    if chat_submitted and user_input:
        if "stomach pain" in user_input.lower():
            bot_response = "It may be gas or indigestion. Try warm water and rest."
        elif "fever" in user_input.lower():
            bot_response = "Check temperature. Drink fluids. Visit a clinic if high."
        else:
            bot_response = "Thank you. Please consult a doctor for serious issues."

        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("HealthAI", bot_response))

    for sender, message in st.session_state.chat_history:
        st.markdown(f"**{sender}:** {message}")

# ========== About ==========
elif page == "ℹ️ About":
    st.title("📘 About HealthAI Pro")
    st.write("""
    HealthAI Pro is an AI-powered healthcare assistant that:
    - Predicts possible diseases
    - Suggests home remedies
    - Warns in serious cases
    - Built with Streamlit, Python for SmartInternz + IBM Granite program
    """)

# ========== Tips ==========
elif page == "💡 Health Tips":
    st.title("💡 Daily Health Tips")
    st.success("🥗 Eat fruits and vegetables daily.")
    st.info("💧 Drink 8+ glasses of water.")
    st.warning("🧼 Wash hands frequently.")
    st.success("🚶 Walk at least 30 minutes.")
    st.info("🛌 Sleep 7-8 hours every night.")

# ========== Contact ==========
elif page == "📞 Contact":
    st.title("📞 Contact & Support")
    st.write("Need help? Reach out to our team:")
    st.markdown("""
    👨‍⚕️ Dr. Mahendra Reddy  
    Email: healthai.support@example.com  
    Phone: +91-90145-05291  
    Office: RISE Krishna Sai Prakasam Group, Andhra Pradesh  
    """)

st.markdown("---")
st.markdown("🧠 Built with ❤️ by HealthAI Team | SmartInternz + IBM Granite")
