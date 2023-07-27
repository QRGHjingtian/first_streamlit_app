import streamlit

streamlit.title("My Parents New Healthy Dinner")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
