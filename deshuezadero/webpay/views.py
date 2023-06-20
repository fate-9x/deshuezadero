import requests
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import *
from appDeshuezadero.models import *


def create_payment(request, amount):
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"
    headers = {
        "Tbk-Api-Key-Id": settings.WEBPAY_API_KEY,
        "Tbk-Api-Key-Secret": settings.WEBPAY_API_SECRET,
        "Content-Type": "application/json"
    }
    content = {
        "buy_order": "123asd",
        "session_id": "123cafk",
        "amount": amount,
        "return_url": "http://localhost:8000/webpay/transaction",
    }
    response = requests.post(url, headers=headers, json=content)
    response_json = response.json()
    token = response_json.get("token")
    url = response_json.get("url")
    return token, url


def checkout(request):

    carrito = Carrito.objects.filter(user_id=request.user.id)
    ammount = 0

    for producto in carrito:
        ammount += int(producto.suma)

    token, url = create_payment(request, ammount)

    return render(request, "webpay/checkout.html", {'token': token, 'url': url, 'carrito': carrito, 'total': ammount})


def transaction(request):

    token = request.GET.get('token_ws')

    url = f"https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{token}"
    headers = {
        "Tbk-Api-Key-Id": settings.WEBPAY_API_KEY,
        "Tbk-Api-Key-Secret": settings.WEBPAY_API_SECRET,
        "Content-Type": "application/json"
    }

    return render(request, "webpay/pago_exitoso.html")

    response = requests.put(url, headers=headers)
    response_json = response.json()
    status = response_json.get("status")
    payment_method = response_json.get("payment_type_code")
    monto = response_json.get("amount")

    payment_method_id = TipoPago.objects.filter(tipo=payment_method).get().id

    if status == 'AUTHORIZED':

        HistorialPago.objects.create(
            token=token, cliente_id=request.user.id, tipo_pago_id=payment_method_id, valor_neto=monto)

        Carrito.objects.filter(user_id=request.user.id).delete()

        return render(request, "webpay/pago_exitoso.html", {'token': token, 'status': status})

    elif status == 'FAILED':

        return render(request, "webpay/pago_rechazado.html", {'token': token, 'status': status})
