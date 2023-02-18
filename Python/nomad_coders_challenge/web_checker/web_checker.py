from requests import get

websites = {
    "google.com",
    "https://naver.com",
    "twitter.com",
    "facebook.com",
    "https://airbnb.com"
}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    print(response)