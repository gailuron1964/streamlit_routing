import streamlit as st

options = ['Email', 'Home phone', 'Mobile phone']

params = st.experimental_get_query_params()
option = params.get("option", ["Email"])[0]

def navigate():
  st.experimental_set_query_params(
    option=st.session_state.selected_option,
  )

st.selectbox(
  'How would you like to be contacted?', 
  options,
  index=options.index(option),
  on_change=navigate,
  key="selected_option"
)

st.write(f"You selected {option}")
