def ipranger_api(ip):
    G = "\033[38;5;82m"
    Y = "\033[38;5;226m"
    R2 = "\033[38;5;202m"
    R = "\033[0m"
    
    try:
        parts = ip.split('.')
        base_ip = f'{parts[0]}.{parts[1]}.{parts[2]}.'

        with open('ipranger.txt', 'a', encoding='utf-8') as f:
            for i in range(1, 256):
                f.write(f'{base_ip}{i}\n')
                print(f'[{G}+{R}] {G}{base_ip}{i}{R}')
        
        return

    except Exception as e:
        print(f'[{R2}-{R}] {R2}{ip}{R} {e}')
