import json
import requests

def revereseip_api(ip):
    G = "\033[38;5;82m"
    Y ="\033[38;5;226m"
    R2 = "\033[38;5;202m"
    R = "\033[0m"
    url = f'https://api.xreverselabs.org/itsuka?apiKey=abe8d9a6a22f9ba33bc0bb0e4ed56624&ip={ip}'
    data = requests.get(url, timeout=10)
    domains = json.loads(data.text)['domains']
    for domain in domains:
        print(f"[{G}+{R}] {G}{domain}{R}")
        with open('revereseip.txt', 'a') as file:
            return file.write(f'{domain}\n')