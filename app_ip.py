import streamlit as st
import requests
from streamlit_js import st_js

st.title("Fetch Client and Server IP Addresses")

# Get the server IP address
server_ip = requests.get("https://api.ipify.org/?format=json").json()["ip"]
st.write(f'Server IP: {server_ip}')

# Get the client IP address using JavaScript
client_ip = st_js("""
    async function getClientIP() {
        const response = await fetch('https://api.ipify.org/?format=json');
        const data = await response.json();
        return data.ip;
    }
    getClientIP();
""")
st.write(f'Client IP: {client_ip}')

# Get user's geolocation
location = st_js("""
    async function getLocation() {
        return new Promise((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(
                position => {
                    resolve({
                        latitude: position.coords.latitude,
                        longitude: position.coords.longitude
                    });
                },
                error => {
                    resolve('Geolocation permission denied or unavailable');
                }
            );
        });
    }
    getLocation();
""")
st.write(f'Location: {location}')

# Get the URL parts of the page
page_location = st_js('window.location.href')
st.write(f'Page Location: {page_location}')
