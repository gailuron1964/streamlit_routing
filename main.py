import streamlit as st

option = st.selectbox('How would you like to be contacted?', ('Email', 'Home phone', 'Mobile phone'))
st.experimental_set_query_params(
  option=option,
)

params = st.experimental_get_query_params()
option = params.get("option", ["None"])[0]
st.write(f"You selected {option}")
