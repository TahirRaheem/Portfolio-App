import streamlit as st

# Personal Information
st.title("Tahir Raheem's Portfolio")
st.write("""
### About Me
I am a passionate developer with expertise in AI, real-time applications, and civil engineering. I have experience in creating innovative apps using cutting-edge technologies like GPT, OpenAI Whisper, Groq API, and more.
""")

st.write("---")

# Projects Section
st.header("Projects")
st.write("Below are some of the projects I have worked on:")

# Add your project samples here
st.write("### 1. Real-time Question Answering Chatbot")
st.write("""
- **Description**: A chatbot that provides real-time answers using the deepset/roberta-base-squad2 model and Groq API for interaction.
- [View Project](https://github.com/your-github-username/your-chatbot-project)
""")

st.write("### 2. BOQ Estimation App")
st.write("""
- **Description**: A cost and duration estimation app for construction activities built using Python and Streamlit.
- [View Project](https://github.com/your-github-username/your-boq-estimation-project)
""")

st.write("### 3. Monte Carlo Simulation App")
st.write("""
- **Description**: A Python-based app for performing Monte Carlo simulations, deployed using Streamlit.
- [View Project](https://github.com/your-github-username/your-monte-carlo-project)
""")

# Contact Section
st.write("---")
st.header("Contact Me")
st.write("""
- **Email**: tahirraheem313@gmail.com
- **Phone**: 03053327174
- [LinkedIn Profile](https://www.linkedin.com/in/your-linkedin-profile)
""")

# Footer
st.write("---")
st.write("Powered by Streamlit | Built with 💻 by Tahir Raheem")

