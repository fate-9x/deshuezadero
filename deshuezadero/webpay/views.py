import requests
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import *


def create_payment(request):
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"
    headers = {
        "Tbk-Api-Key-Id": settings.WEBPAY_API_KEY,
        "Tbk-Api-Key-Secret": settings.WEBPAY_API_SECRET,
        "Content-Type": "application/json"
    }
    content = {
        "buy_order": "123asd",
        "session_id": "123cafk",
        "amount": 100000,
        "return_url": "http://localhost:8000/",
    }
    response = requests.post(url, headers=headers, json=content)
    response_json = response.json()
    token = response_json.get("token")
    url = response_json.get("url")
    return render(request, "webpay/pay.html", {"token": token, "url": url})
