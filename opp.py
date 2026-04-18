import streamlit as st

st.set_page_config(page_title="Pushkar Verma Art", page_icon="🎨")

# Sidebar
with st.sidebar:
    st.title("Contact Pushkar")
    st.markdown("📧 [Email Me](mailto:pushkar2256@gmail.com)")
    st.markdown("📞 [Call: +91 8708775612](tel:+918708775612)")
    
    st.write("---")
    st.subheader("Follow My Work")
    # YouTube Channel Link
    st.markdown("📺 [YouTube: ytug116](https://www.youtube.com/@ytug116)")
    
    st.write("---")
    st.success("🟢 Accepting Commissions")
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
st.write("Select your drawing level and delivery distance to see the total price.")

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
    # Clicking this opens Gmail automatically
    contact_link = f'mailto:pushkar2256@gmail.com?subject=Art%20Order:%20{level}'
    st.markdown(f'<a href="{contact_link}" target="_blank" style="text-decoration: none;"><div style="background-color: #ffcc00; color: black; padding: 15px; text-align: center; border-radius: 5px; font-weight: bold;">EMAIL ORDER</div></a>', unsafe_allow_html=True)

with btn_col2:
    # Clicking this opens the Phone Dialer
    st.markdown(f'<a href="tel:+918708775612" style="text-decoration: none;"><div style="background-color: #25d366; color: white; padding: 15px; text-align: center; border-radius: 5px; font-weight: bold;">CALL TO ORDER</div></a>', unsafe_allow_html=True)

# YouTube Footer
st.write("---")
st.write("Check out my latest speedpaints and designs on [YouTube](https://www.youtube.com/@ytug116)")
