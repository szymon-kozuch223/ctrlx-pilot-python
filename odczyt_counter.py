import time
import requests
import urllib3

urllib3.disable_warnings()  # certyfikat sterownika jest samopodpisany

IP = "192.168.1.1"
USER = "boschrexroth"
PASSWORD = "boschrexroth"  # jeśli zmieniałeś hasło, wpisz nowe
BASE = f"https://{IP}"
NODE = "plc/app/Application/sym/PLC_PRG/counter"


def get_token():
    r = requests.post(
        f"{BASE}/identity-manager/api/v1/auth/token",
        json={"name": USER, "password": PASSWORD},
        verify=False, timeout=5,
    )
    r.raise_for_status()
    return r.json()["access_token"]


def get(token, path, **params):
    return requests.get(
        f"{BASE}/automation/api/v2/nodes/{path}",
        headers={"Authorization": f"Bearer {token}"},
        params=params, verify=False, timeout=5,
    )


token = get_token()

for _ in range(5):
    r = get(token, NODE)
    if r.status_code == 200:
        print("counter =", r.json().get("value"))
    else:
        print("Błąd", r.status_code, "- węzły pod sym/:")
        print(get(token, "plc/app/Application/sym", type="browse").text)
        break
    time.sleep(1)