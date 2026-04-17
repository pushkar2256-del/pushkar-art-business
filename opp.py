import streamlit as st

st.set_page_config(page_title="Pushkar Verma Art", page_icon="🎨")

# Sidebar
with st.sidebar:
    st.title("Contact Pushkar")
    st.markdown("📧 [pushkar2256@gmail.com](mailto:pushkar2256@gmail.com)")
    st.markdown("📞 [Call: +91 8708775612](tel:+918708775612)")
    st.write("📍 Ambala, Haryana, India")
    st.write("---")
    st.caption("Rates include all taxes.")

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

# Price Calculator Section
st.header("Commission Price Calculator")
st.write("Select your requirements below to see the automatic quote.")

# Level Selection
level = st.select_slider(
    "Select Drawing Level", 
    options=["Basic Drawing", "Moderate", "Intermediate"]
)

# Distance Input
distance = st.number_input("Delivery Distance from Ambala (in KM)", min_value=0, value=0)

# Price Logic
base_price = 0
if level == "Basic Drawing":
    base_price = 129
elif level == "Moderate":
    base_price = 349
else: # Intermediate
    base_price = 589

# Transportation Logic
shipping = 0
if distance > 0:
    if distance <= 200:
        shipping = 50
    else:
        # You didn't specify over 200km, so I set a logical estimate of 100
        shipping = 100 

total_price = base_price + shipping

# Display the Price
st.subheader(f"Total Amount: ₹{total_price}")
st.write(f"*(Base: ₹{base_price} + Shipping: ₹{shipping})*")

st.divider()

# Final Contact Section
st.write("### Ready to place your order?")
btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    contact_link = f'mailto:pushkar2256@gmail.com?subject=Art%20Order:%20{level}'
    st.markdown(f'<a href="{contact_link}" target="_blank" style="text-decoration: none;"><div style="background-color: #ffcc00
