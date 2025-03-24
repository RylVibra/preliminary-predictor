import streamlit as st
import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner


st.header("QR Code Scanner")

enable = st.checkbox("Enable camera")

camera = st.camera_input("Show QR code")