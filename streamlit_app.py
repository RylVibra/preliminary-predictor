import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner


st.header("QR Code Scanner")

# camera = st.camera_input("Show QR code")

def run_scanner():
    qr_code = qrcode_scanner()

if st.button("Scan", key="QRscan"):
    qr_code = qrcode_scanner()
    if qr_code:
        st.write(f"# {qr_code}")

