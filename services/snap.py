import requests

def send(number):
    try:
        r = requests.post(
            url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
            json={"cellphone": f"+98{number}"},
            timeout=5,
            verify=False
        )
        return r
    except Exception as e:
        raise Exception(f"Snapp API error: {str(e)}")
