import requests
import json

class BumbleAPI:
    def __init__(self, phone, password):
        self.session = requests.Session()
        self.phone = phone
        self.password = password
        self.headers = {
            "X-Desktop-web": "1",
            "Origin": "https://bumble.com",
            "Referer": "https://bumble.com/get-started",
            "Sec-Fetch-Mode": "cors",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
            "x-use-session-cookie": "1"
        }

    def login(self):
        url = "https://bumble.com/mwebapi.phtml?SERVER_LOGIN_BY_PASSWORD"
        payload = {
            "version": 1,
            "message_type": 15,
            "message_id": 12,
            "body": [
                {
                    "message_type": 15,
                    "server_login_by_password": {
                        "remember_me": True,
                        "phone": self.phone,
                        "password": self.password,
                        "stats_data": ""
                    }
                }
            ],
            "is_background": False
        }
        response = self.session.post(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            return "Login Successful"
        else:
            return response.text

    def startup(self):
        url = "https://bumble.com/mwebapi.phtml?SERVER_APP_STARTUP"
        payload = {
            "version": 1,
            "message_type": 2,
            "message_id": 1,
            "body": [
                {
                    "message_type": 2,
                    "server_app_startup": {
                        "app_build": "MoxieWebapp",
                        "app_name": "moxie",
                        "app_version": "1.0.0",
                        "can_send_sms": False,
                        "user_agent": self.headers["User-Agent"],
                        "screen_width": 1680,
                        "screen_height": 1050,
                        "language": 0,
                        "is_cold_start": True,
                        "external_provider_redirect_url": "https://bumble.com/static/external-auth-result.html?",
                        "locale": "en-us",
                        "app_platform_type": 5,
                        "app_product_type": 400,
                        "device_info": {"webcam_available": True, "form_factor": 3},
                        "build_configuration": 2
                    }
                }
            ],
            "is_background": False
        }
        response = self.session.post(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            return "Startup Successful"
        else:
            return response.text

    def get_encounters(self):
        url = "https://bumble.com/mwebapi.phtml?SERVER_GET_ENCOUNTERS"
        payload = {
            "version": 1,
            "message_type": 81,
            "message_id": 3,
            "body": [
                {
                    "message_type": 81,
                    "server_get_encounters": {
                        "number": 50,
                        "context": 1
                    }
                }
            ],
            "is_background": False
        }
        response = self.session.post(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            return response.json()["body"][0]["client_encounters"]
        else:
            return response.text

    def vote_yes_for_encounter(self, encounter_id):
        url = "https://bumble.com/mwebapi.phtml?SERVER_ENCOUNTERS_VOTE"
        payload = {
            "version": 1,
            "message_type": 80,
            "message_id": 14,
            "body": [
                {
                    "message_type": 80,
                    "server_encounters_vote": {
                        "person_id": encounter_id,
                        "vote": 2,
                        "vote_source": 1,
                        "game_mode": 0
                    }
                }
            ],
            "is_background": False
        }
        response = self.session.post(url, headers=self.headers, data=json.dumps(payload))
        return "Voted Yes" if response.status_code == 200 else response.text

    def vote_no_for_encounter(self, encounter_id):
        url = "https://bumble.com/mwebapi.phtml?SERVER_ENCOUNTERS_VOTE"
        payload = {
            "version": 1,
            "message_type": 80,
            "message_id": 14,
            "body": [
                {
                    "message_type": 80,
                    "server_encounters_vote": {
                        "person_id": encounter_id,
                        "vote": 3,
                        "vote_source": 1,
                        "game_mode": 0
                    }
                }
            ],
            "is_background": False
        }
        response = self.session.post(url, headers=self.headers, data=json.dumps(payload))
        return "Voted No" if response.status_code == 200 else response.text

    def get_matches_list(self):
        url = "https://bumble.com/mwebapi.phtml?SERVER_GET_USER_LIST"
        payload = {
            "body": [
                {
                    "message_type": 245,
                    "server_get_user_list": {
                        "preferred_count": 30,
                        "folder_id": 0
                    }
                }
            ],
            "message_id": 5,
            "message_type": 245,
            "version": 1,
            "is_background": False
        }
        response = self.session.post(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            return response.json()["body"][0]["client_user_list"]["section"][1]
        else:
            return response.text

    def get_matches_details(self, user_id):
        url = "https://bumble.com/mwebapi.phtml?SERVER_GET_USER"
        payload = {
            "body": [
                {
                    "message_type": 403,
                    "server_get_user": {
                        "user_id": user_id
                    }
                }
            ],
            "message_id": 8,
            "message_type": 403,
            "version": 1,
            "is_background": False
        }
        response = self.session.post(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            return response.json()["body"][0]["user"]
        else:
            return response.text
