import requests
from django.http import JsonResponse
from django.shortcuts import *

def create_payment(request):
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"
    headers = {
        "Tbk-Api-Key-Id": "597055555532",
        "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
        "Content-Type": "application/json"
    }
    content = {
        "buy_order": "ordenCo3",
        "session_id": "sesi23456",
        "amount": 9999999999,
        "return_url": "http://localhost:8000/",
    }
    response = requests.post(url, headers=headers, json=content)
    response_json = response.json()
    token = response_json.get("token")
    url = response_json.get("url")
    return render(request, "webpay/pay.html", {"token": token, "url": url})