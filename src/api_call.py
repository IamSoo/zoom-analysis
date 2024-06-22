import requests

client_id = ""
account_id = ""
client_secret = ""

auth_token_url = "https://zoom.us/oauth/token"
api_base_url = "https://api.zoom.us/v2"
user_id = ""


def get_token():
    token_data = {
        "grant_type": "account_credentials",
        "account_id": account_id,
        "client_secret": client_secret,
    }
    response = requests.post(
        auth_token_url, auth=(client_id, client_secret), data=token_data
    )

    if response.status_code != 200:
        print("Unable to get access token")
    response_data = response.json()
    access_token = response_data["access_token"]
    return access_token


# get list of meetings
def get_list_of_meetings(access_token):

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    resp = requests.get(
        f"{api_base_url}/users/{user_id}/meetings?type=scheduled", headers=headers
    )

    if resp.status_code != 201:
        print("Unable to generate meeting link")
    response_data = resp.json()

    content = {"meetings": response_data["meetings"]}
    print(content)


if __name__ == '__main__':
    token = get_token()
    get_list_of_meetings(token)