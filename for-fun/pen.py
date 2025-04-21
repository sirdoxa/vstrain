import socket
import requests
from datetime import datetime
from bs4 import BeautifulSoup, Comment

domain = "aidinr.ir"
url = f"http://{domain}"
print("=" * 60)
print(f"🎯 Target: {domain}")
print(f"🕒 Started at: {datetime.now()}")
print("=" * 60)

try:
    ip = socket.gethostbyname(domain)
    print(f"🌐 IP Address: {ip}")
    host = socket.gethostbyaddr(ip)[0]
    print(f"📛 Hostname: {host}")
except Exception as e:
    print(f"⚠️ DNS Error: {e}")

try:
    response = requests.get(url, timeout=5)
    print("\n📦 HTTP Headers:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")
except Exception as e:
    print(f"⚠️ Header Error: {e}")

try:
    soup = BeautifulSoup(response.text, "html.parser")
    print("\n🧷 Meta Tags:")
    for tag in soup.find_all("meta"):
        print(f"  {tag}")

    print("\n🕵️ HTML Comments:")
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        print(f"  💬 {comment}")
except Exception as e:
    print(f"⚠️ HTML Parse Error: {e}")

paths = ["/robots.txt", "/sitemap.xml", "/admin", "/login", "/.git", "/.env"]
print("\n🗺️ Common Paths:")
for path in paths:
    full_url = url + path
    try:
        r = requests.get(full_url, timeout=3)
        if r.status_code == 200:
            print(f"  ✅ Found: {full_url}")
        elif r.status_code == 403:
            print(f"  🔒 Forbidden: {full_url}")
    except:
        pass

print("\n✅ Scan Complete.")
print("=" * 60)


robots = requests.get(url + "/robots.txt")
print("\n📄 robots.txt content:")
print(robots.text)
