from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import requests

# Function to get public IP address using httpbin
def get_public_ip():
    response = requests.get("https://httpbin.org/ip")
    return response.json()["origin"]

# Get the IP address before using Tor
initial_ip = get_public_ip()
print("Initial IP Address:", initial_ip)

# Set up Tor proxy
tor_proxy = "http://localhost:8118"
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = tor_proxy
proxy.ssl_proxy = tor_proxy

# Set up Chrome with the Tor proxy
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server=http://localhost:8118")
driver = webdriver.Chrome(options=chrome_options)

# Get the Tor IP address
tor_ip = get_public_ip()
print("Tor IP Address:", tor_ip)

# Your Selenium code goes here

# Close the browser
driver.quit()

# Get the IP address after using Tor
final_ip = get_public_ip()
print("Final IP Address:", final_ip)
