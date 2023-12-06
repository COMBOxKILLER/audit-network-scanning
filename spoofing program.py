import requests

def spoof_user_agent(url, user_agent):
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    return response.text

spoofed_html = spoof_user_agent('https://example.com', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
print(spoofed_html)