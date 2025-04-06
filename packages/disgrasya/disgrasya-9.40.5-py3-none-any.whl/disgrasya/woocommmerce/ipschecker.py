import socket

def ipschecker_api(ip):
    G = "\033[38;5;82m"
    Y ="\033[38;5;226m"
    R2 = "\033[38;5;202m"
    R = "\033[0m"
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 443))
        s.close()
        with open('ipschecker.txt', 'a') as file:
            file.write(f'{ip}\n')
        return print(f"[{G}+{R}] {G}{ip}{R}")
    except Exception as e:
        return print(f"[{R2}-{R}] {R2}{ip}{R} {e}")