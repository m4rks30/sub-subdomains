#pip install tldextract
import requests
import tldextract

def check_subdomains(domain, subdomains_list):
    for subdomain in subdomains_list:
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[+] {url} is up!")
        except requests.ConnectionError:
            pass

if __name__ == '__main__':
    domain = input("Enter the domain: ")
    subdomains_list = ['www', 'mail', 'ftp', 'blog', 'test']
    check_subdomains(domain, subdomains_list)
