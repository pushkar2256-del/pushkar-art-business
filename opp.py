import streamlit as st

st.set_page_config(page_title="Pushkar Verma Art", page_icon="🎨")

# Sidebar
with st.sidebar:
    st.title("Contact Pushkar")
    st.write("📧 pushkar2256@gmail.com")
    st.write("📍 Ambala, Haryana, India")
    st.write("---")
    st.write("Rates vary based on reference complexity.")

# Main Page
st.title("PUSHKAR VERMA")
st.header("Character Illustrator & Concept Artist")

st.markdown("""
### Professional Profile
Concept-driven artist specializing in original character development and visual storytelling. 
I excel at translating complex narratives into high-quality illustrations using a **conceptual artist mind**.
""")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Core Skills")
    st.write("• Character Design\n• Visual Storytelling\n• Digital Illustration")
with col2:
    st.subheader("Experience")
    st.write("• Freelance Illustrator\n• Original IP Development\n• Production-Ready Assets")

st.divider()

st.header("Commission Inquiries")
st.write("Rates are determined by the detail in the picture you provide.")
level = st.select_slider("Select Project Level", ["Basic Sketch", "Standard Render", "Complex Concept"])

if level == "Basic Sketch":
    st.success("Estimated Rate: Request quote via email.")
elif level == "Standard Render":
    st.success("Estimated Rate: Request quote via email.")
else:
    st.success("Estimated Rate: Request quote via email.")

st.write("### Ready to work? Email: pushkar2256@gmail.com")
