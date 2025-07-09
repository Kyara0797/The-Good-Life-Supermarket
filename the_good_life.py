import streamlit as st
import pandas as pd

def calculate_subtotal(product_name, product_price, product_quantity):
    subtotal = float(product_price) * float(product_quantity)
    new_row = {
        "Product": product_name,
        "Price": product_price, 
        "Quantity": product_quantity, 
        "Subtotal": subtotal
    }

    st.session_state.table_data = pd.concat(
        [st.session_state.table_data, pd.DataFrame([new_row])],
        ignore_index=True
    )

# Initialize the table if not already in session state
if "table_data" not in st.session_state:
    st.session_state.table_data = pd.DataFrame(
        columns=["Product", "Price", "Quantity", "Subtotal"]
    )

col1, col2 = st.columns([1, 3])
with col1:
    st.image("images/logo.png", width=100)  # Ajusta el tamaño si lo ves muy grande
with col2:
    st.markdown(
        "<h1 style='color: #4CAF50; padding-top: 20px;'>The Good Life Supermarket</h1>",
        unsafe_allow_html=True
    )

with st.form("product_form"):
    product_name = st.text_input("Enter the product name")
    product_price = st.number_input("Enter the product price")
    product_quantity = st.number_input("Enter the quantity")
    
    submit_button = st.form_submit_button("Add Product")

if submit_button:
    calculate_subtotal(product_name, product_price, product_quantity)

st.subheader("Shopping Cart")
st.dataframe(st.session_state.table_data)

if st.button("Calculate Total"):
    total = (st.session_state.table_data["Price"]
             * st.session_state.table_data["Quantity"]).sum()
    
    st.subheader("Total Price")
    st.write("The total price is: $" + str(total))
