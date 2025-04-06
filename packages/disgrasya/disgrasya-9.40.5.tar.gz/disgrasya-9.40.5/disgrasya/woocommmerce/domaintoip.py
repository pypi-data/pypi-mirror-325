import socket

def domaintoip_api(domain):
    G = "\033[38;5;82m"
    Y ="\033[38;5;226m"
    R2 = "\033[38;5;202m"
    R = "\033[0m"
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"[{G}+{R}] {G}{domain}{R} {ip_address}")
        with open("domaintoip.txt", "a") as file:
            return file.write(f"{ip_address}\n")
    except socket.gaierror as e:
        return print(f"[{Y}!{R}] {Y}{domain}{R} {e}")