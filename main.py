import requests

# suppply okta issuer, client id, and secret
OKTA_ISSUER = ""
OKTA_CLIENT_ID = ""
OKTA_CLIENT_SECRET = ""


def is_token_active(_token: str) -> bool:
    """
    This function will call oktas endpoint to check if the access token you provided is valid or not

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
        return True
    else:
        print(f"Introspection failed: {response.status_code}, {response.text}")
        return False


if __name__ == "__main__":
    token = ""
    res = is_token_active(token)
    print(f"{res=}")
