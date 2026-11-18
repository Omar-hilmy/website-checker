import urllib.request

def check_website(url):
    if not url.startswith("http"):
        url = "https://" + url
    try:
        print(f"Checking {url} ...")
        response = urllib.request.urlopen(url, timeout=5)
        print(f"✅ {url} is ONLINE - Status: {response.status}")
    except Exception as e:
        print(f"❌ {url} is DOWN - Error: {e}")

site = input("Enter website (example: google.com): ")
check_website(site)
