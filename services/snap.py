import requests
from user_agent import generate_user_agent
import urllib3

# Suppress SSL warning if verify=False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def send(number, proxy=None):
    try:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': generate_user_agent()
        }

        proxies = proxy if proxy else {}

        response = requests.post(
            url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
            headers=headers,
            json={"cellphone": f"+98{number}"},
            timeout=5,
            verify=False,
            proxies=proxies
        )
        return response
    except Exception as e:
        raise Exception(f"Snapp API error: {str(e)}")
