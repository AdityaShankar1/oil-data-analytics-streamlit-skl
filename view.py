# view.py
import streamlit as st
import pandas as pd
import streamlit as st

def set_background():
    encoded_string = """
    XFFFFBgwYPRjGJEgg/wDBFRRQEsWLFFFFFFHFKG5iV4Xf3mN/xgVQAGD6gKcUUUWLGO31CBAgQQQX58DzGDZVtZrxKgmiXDy4JQOczKy1i5j9SxYxs2w6BBBAQgveDLvoUHqEGKKDCECEOuJcuXL6rgw6h1KFDKjQDbDudL7+Tx8QEZdmX29Do/QP+If5H2QJ+u7Lm1+6aL2mB/UBGfuQ/V9qw5p6UgUz/EX6X5jwj2R1vmjsD5iHSfWgxjGPR+gAoCdmBr7Zr7Ri7fcJQDhuVJyXCEGD0Ibh0roxSPclxSkPBc0xfJUt2YyyIhAdCRIIkSMZlCHQYMUfUNHX9Ezhh8T9A2xA5PCNQ23FFFFFBgwel9GMEEEH+Qquu7+prFFiii6Cij6SjmaYRfHGJH/EEAAGzqT6TiixejOA6EEEEEAFuAit4AmnEpDEoQO9SzTRglq9pYseY/Q9GPWvoOly4PQh9IHQEIEIQZcGWS5ZL+ip7yqGHU0GKuMvmbLb+Wh8TuEhGX27YfSfqBOS8IJfYTh/bUHfiqiWHyCwN+Mb+2Wf2KTi74p+p+ddTKO9txEcIm4m8xka94oMj9vodZXMp5gXL7zzp54rmow+EW4xj9ZCYSksl58Bp+IUDJgTSRYh0DBgwZcslJZFJZPMuU6IhbF3q4yUsU5YtO4isWL9IPUYzugwgwYMUfUMnXaiD5Ixh2dTv8KxlSFpQ7MLX4ooooMUGDBl9GMYkEEExQ/5Kqme/9k=
    """
    page_bg_img = f'''
    <style>
    .stApp {{
        position: relative;
        z-index: 0;
    }}
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0;
        width: 100vw;
        height: 100vh;
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        opacity: 0.07;
        z-index: -1;
        pointer-events: none;
    }}
    .css-1d391kg {{
        background-color: rgba(255, 255, 255, 0.9) !important;
        border-radius: 10px;
        padding: 1rem;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

def render_header():
    st.title("Oil & Gas Supply Chain Dashboard")
    st.markdown("### Phase 1 - Data Simulation and Industry Trends")

def color_status(val):
    if val == "Critical":
        color = 'background-color: #ff4c4c'  # red
    elif val == "Warning":
        color = 'background-color: #ffeb3b'  # yellow
    elif val == "Normal":
        color = 'background-color: #c8e6c9'  # light green (pista)
    else:
        color = ''
    return color

def render_sensor_data_table(sensor_data: list[dict]):
    st.subheader("Simulated Sensor Data")
    if not sensor_data:
        st.write("No sensor data available.")
        return
    df = pd.DataFrame(sensor_data)
    styled_df = df.style.applymap(color_status, subset=['status'])
    st.dataframe(styled_df)

def render_industry_trends(df: pd.DataFrame):
    st.subheader("Industry Trends")
    if df.empty:
        st.write("Industry trends data not available.")
        return
    st.line_chart(df.set_index("Year"))

def render_state_wise_consumption(df: pd.DataFrame):
    st.subheader("State-wise Consumption and Production")
    if df.empty:
        st.write("State-wise data not available.")
        return
    st.bar_chart(df.set_index("State"))

def render_auth_input():
    st.sidebar.header("Authentication")
    key = st.sidebar.text_input("Enter Access Key to view advanced data", type="password")
    return key

def render_auth_message(has_access: bool):
    if not has_access:
        st.warning("You do not have access to advanced data. Please enter the correct key.")

# code for ML component rendering:

def render_auth_message(has_access: bool):
    if not has_access:
        st.warning("You do not have access to advanced data. Please enter the correct key.")

def render_ml_predictions(df: pd.DataFrame):
    st.subheader("Predicted Crude Oil Production for Next Years")
    if df.empty:
        st.write("No predictions available.")
        return
    st.write(df)