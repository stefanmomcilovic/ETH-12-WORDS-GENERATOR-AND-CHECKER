import requests
import mnemonic
import secrets
from eth_account import Account


INFURA_API_KEY = ""

def generate_seed_phrase():
    entropy = secrets.token_bytes(16)
    m = mnemonic.Mnemonic("english")
    return m.to_mnemonic(entropy)

def get_balance(address):
    url = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}/eth/balance/{address}?tag=latest"
    response = requests.get(url)

    if response.status_code == 200:
        balance = int(response.json(), 16) / 10**18
        return float(balance)
    else:
        return 0.00

def generate_and_check_balance():
    seed_phrase = generate_seed_phrase()
    acct = Account.create(seed_phrase)
    address = acct.address
    balance = get_balance(address)
    return address, balance, acct._private_key, seed_phrase

while True:
    address, balance, private_key, seed_phrase = generate_and_check_balance()
    if balance > 0.00:
        print('Found Balance!!!')
        print("Address:", address)
        print("Balance: {:.3f} ETH".format(balance))
        print("Private Key:", private_key.hex())
        print("Seed phrase:", seed_phrase)
        break
    else:
        print("Address:", address)
        print("Balance: {:.3f} ETH".format(balance))
        print("Private Key:", private_key.hex())
        print("Seed phrase:", seed_phrase)
