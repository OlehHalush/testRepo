import json

import allure
import requests


def allure_log(method, url, description, **kwargs):
    response = requests.request(method, url, **kwargs)

    # Build nicely formatted log with method & URL outside JSON body
    body = kwargs.get("json") or kwargs.get("data")
    try:
        body_pretty = json.dumps(body, indent=2) if body else ""
    except (TypeError, ValueError):
        body_pretty = str(body) if body else ""

    request_log = f'"method": "{method.upper()}",\n"url": "{url}",\n\n"body": {body_pretty}'

    allure.attach(
        request_log,
        name=f"{description} request",
        attachment_type=allure.attachment_type.TEXT
    )

    # Attach response as usual
    try:
        response_json = response.json()
        allure.attach(
            json.dumps(response_json, indent=2),
            name=f"{description} response",
            attachment_type=allure.attachment_type.JSON)
    except ValueError:
        allure.attach(
            f"Status: {response.status_code}\nHeaders: {dict(response.headers)}\nBody: {response.text}",
            name=f"{description} response",
            attachment_type=allure.attachment_type.TEXT
        )

    return response
