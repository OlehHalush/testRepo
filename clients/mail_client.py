import os
import re
import time
import uuid

import allure

from models.mail_client_models.account_models import AccountRequest
from models.mail_client_models.domains_models import DomainsResponse
from models.mail_client_models.message_details_models import MessageDetailsResponse
from models.mail_client_models.messages_models import MessagesResponse
from models.mail_client_models.token_models import TokenRequest, TokenResponse
from utils.allure_log_helper import allure_log

BASE_URL = "https://api.mail.tm"
TOKEN_URL = f"{BASE_URL}/token"
DOMAINS_URL = f"{BASE_URL}/domains"
ACCOUNTS_URL = f"{BASE_URL}/accounts"
MESSAGES_URL = f"{BASE_URL}/messages"


class MailClient:
    @staticmethod
    @allure.step("create email inbox")
    def create_account():
        domains_response = allure_log("GET", DOMAINS_URL, "Get domains")

        if domains_response.status_code != 200:
            raise Exception(f"Domains fetching failed: {domains_response.text}")

        domains = DomainsResponse(**domains_response.json())
        domain = domains.hydra_member[0].domain
        worker_id = os.getenv("PYTEST_XDIST_WORKER", "worker0")
        unique_suffix = f"{worker_id}-{uuid.uuid4().hex[:6]}"
        email = f"testuser-{unique_suffix}@{domain}"
        password = "P@ssw0rd123"
        account_request = AccountRequest(address=email, password=password).model_dump()
        accounts_response = allure_log("POST", ACCOUNTS_URL, "Create account inbox", json=account_request)

        if accounts_response.status_code != 201:
            raise Exception(f"Registration failed: {accounts_response.text}")

        return email, password

    @staticmethod
    @allure.step("get token for email '{0}' and password '{1}'")
    def get_token(email, password):
        token_request = TokenRequest(address=email, password=password).model_dump()
        token_response = allure_log("POST", TOKEN_URL, "Get token", json=token_request)

        if token_response.status_code != 200:
            raise Exception(f"Login failed: {token_response.text}")

        return TokenResponse(**token_response.json()).token

    @staticmethod
    @allure.step("wait for email with subject '{2}' in inbox '{0}'")
    def wait_for_email(email, password, subject: str, timeout=60):
        token = MailClient.get_token(email, password)
        headers = {"Authorization": f"Bearer {token}"}

        for _ in range(timeout):
            messages_response = allure_log("GET", MESSAGES_URL, "Get emails", headers=headers)

            if messages_response.status_code != 200:
                raise Exception(f"Messages fetching failed: {messages_response.text}")

            messages = MessagesResponse(**messages_response.json()).hydra_member
            for msg in messages:
                if msg.subject == subject:
                    return msg

            time.sleep(2)

        raise TimeoutError(f"No email with subject '{subject}' received within {timeout} seconds.")

    @staticmethod
    @allure.step("get link containing '{3}' from email with message_id '{2}'")
    def get_link_from_email(email, password, message_id, link):
        token = MailClient.get_token(email, password)
        headers = {"Authorization": f"Bearer {token}"}
        response = allure_log("GET", f"{MESSAGES_URL}/{message_id}", "Get email details", headers=headers)

        if response.status_code != 200:
            raise Exception(f"Email details fetching failed: {response.text}")

        body = MessageDetailsResponse(**response.json()).text
        urls = re.findall(r"https?://[^\s\]]+", body)
        activation_links = [url for url in urls if link in url]

        if not activation_links:
            raise Exception("No activation link found.")

        activation_link = activation_links[0]
        return activation_link
