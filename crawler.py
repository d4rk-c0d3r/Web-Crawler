import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "rvce.edu.in"
with open("/home/user/Downloads/files-and-dirs-wordlist.txt","r") as wordlist_file:
    try:
        for line in wordlist_file:
            word = line.strip()
            test_url = target_url + "/" + word
            response = request(test_url)
            if response:
                print("[+] Discovered subdomain >> " + test_url)
    except KeyboardInterrupt:
        exit()
