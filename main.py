import sys
from os import environ

import requests
from dotenv import load_dotenv

load_dotenv(".env")

OKTA_ISSUER = environ["OKTA_ISSUER"]
OKTA_CLIENT_ID = environ["OKTA_CLIENT_ID"]
OKTA_CLIENT_SECRET = environ["OKTA_CLIENT_SECRET"]


def is_token_active(_token: str) -> bool:
    """
    This function will call okta's endpoint to check if the access token you provided is valid or not

    :_token: Your okta access token as a string
    :return: If the token is valid true, else false
    """

    introspection_url = f"{OKTA_ISSUER}/v1/introspect"
    response = requests.post(
        introspection_url,
        auth=(OKTA_CLIENT_ID, OKTA_CLIENT_SECRET),
        data={"token": _token, "token_type_hint": "access_token"},
    )

    if response.status_code == 200:
        data = response.json()
        print(f"{data=}")
        if data["active"]:
            return True
        if not data["active"]:
            return False
    else:
        print(f"Introspection failed: {response.status_code}, {response.text}")
        return False


if __name__ == "__main__":
    token = sys.argv[1]
    res = is_token_active(token)
    print(f"{res=}")
