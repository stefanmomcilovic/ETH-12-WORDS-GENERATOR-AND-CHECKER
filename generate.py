import requests
import random
import hashlib
from english_words import get_english_words_set
INFURA_API_KEY = ""

def generate_seed_phrase():
    word_list = get_english_words_set(['web2'], lower=True)
    seed_phrase = []
    for i in range(12):
        seed_phrase.append(random.choice(list(word_list)))
    return " ".join(seed_phrase)


def get_balance(address):
    url = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}/eth/balance/{address}?tag=latest"
    response = requests.get(url)

    if response.status_code == 200:
        balance = float(response.json(), 16) / 10**18
        return balance
    else:
        return 0

def generate_and_check_balance():
    seed_phrase = generate_seed_phrase()
    address = f"0x{hashlib.sha3_256(seed_phrase.encode()).hexdigest()[24:]}"
    balance = get_balance(address)
    return address, balance, seed_phrase

while True:
    address, balance, seed_phrase = generate_and_check_balance()
    if balance > 0.00:
        print('Found Balance!!!')
        print("Address:", address)
        print("Balance:", balance, "ETH")
        print("Seed phrase:", seed_phrase)
        break
    else:
        print("Address:", address)
        print("Balance:", balance, "ETH")
        print("Seed phrase:", seed_phrase)
