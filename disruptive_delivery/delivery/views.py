from django.shortcuts import render, redirect
from django.http import request, HttpResponse, JsonResponse
import requests
from datetime import *
from .forms import *
from django.contrib import messages
import json
# Create your views here.

def offer_delivery(date, time, price, id):
    dt = datetime.combine(date, time)
    h = {
        'Content-Type': 'application/json',
        'x-api-key': '57xzYFk9GgJNFnUjQKc9'
    }

    body = {
        "price_in_cents": price,
        "expected_delivery_datetime": dt.isoformat('T', 'milliseconds') + 'Z',
        "order_id": id
    }
    r = requests.post(
        'https://pasd-webshop-api.onrender.com/api/delivery/', headers=h, json=body)

    try:
        return (JsonResponse(r.json(), status=r.status_code))
    except ValueError:
        return HttpResponse(status=r.status_code)


def render_home(request):
    return render(request, 'home.html', {})

def render_driver_home(request):
    return render(request, 'delivery-driver.html', {})
    
def render_offer(request):
    h = {
        'x-api-key': '57xzYFk9GgJNFnUjQKc9'
    }
    r = requests.get(
        'https://pasd-webshop-api.onrender.com/api/order/', headers=h)

    orders = r.json()
    filtered_orders = []
    for order in orders['orders']:
        if order['last_delivery'] == None:
            filtered_orders.append((order['id'], order['id']))
        elif order['last_delivery']['status'] == 'REJ':
            filtered_orders.append((order['id'], order['id']))
    if request.method == 'POST':
        form = OrderOfferFormID(request.POST)
        form.fields['id'].choices = filtered_orders
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            price = form.cleaned_data['price']
            id = form.cleaned_data['id']
            response = offer_delivery(date, time, price, id)
            if response.status_code == 400:
                content = json.loads(response.content)
                messages.error(request, content['detail'])
            elif response.status_code == 422:
                messages.error(request, 'Invalid input.')
            elif response.status_code == 404:
                messages.error(request, 'Order not found')
            elif response.status_code == 500:
                messages.error(
                    request, 'Internal server error, please try again later.')
            elif response.status_code == 200:
                content = json.loads(response.content)
                if content['status'] == "REJ":
                    messages.warning(request, 'Offer rejected.')
                elif content['status'] == "EXP":
                    messages.success(
                        request, 'Offer accepted.')

        return redirect('offer')
    else:
        form = OrderOfferFormID()
        form.fields['id'].choices = filtered_orders

    return render(request, 'offer.html', {'form': form})


def get_orders(request):
    h = {
        'x-api-key': '57xzYFk9GgJNFnUjQKc9'
    }
    r = requests.get(
        'https://pasd-webshop-api.onrender.com/api/order/', headers=h)

    orders = r.json()
    filtered_orders = []
    for order in orders['orders']:
        if order['last_delivery'] == None:
            filtered_orders.append(order)
        elif order['last_delivery']['status'] == 'REJ':
            filtered_orders.append(order)

    if request.method == 'POST':
        form = OrderOfferForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            price = form.cleaned_data['price']
            id = request.POST.get('order_id')
            response = offer_delivery(date, time, price, id)
            if response.status_code == 400:
                content = json.loads(response.content)
                messages.error(request, content['detail'])
            elif response.status_code == 422:
                messages.error(request, 'Invalid input.')
            elif response.status_code == 404:
                messages.error(request, 'Order not found')
            elif response.status_code == 500:
                messages.error(
                    request, 'Internal server error, please try again later.')
            elif response.status_code == 200:
                content = json.loads(response.content)
                if content['status'] == "REJ":
                    messages.warning(request, 'Offer rejected.')
                elif content['status'] == "EXP":
                    messages.success(
                        request, 'Offer accepted.')
        return redirect('orders')
    else:
        form = OrderOfferForm()

    return render(request, 'orders.html', {'form': form, 'deliveries': {'orders': filtered_orders}})
# 7551


def get_delivery_by_id(id):
    h = {
        'x-api-key': '57xzYFk9GgJNFnUjQKc9'
    }
    r = requests.get(
        f'https://pasd-webshop-api.onrender.com/api/delivery/{id}', headers=h)

    return JsonResponse(r.json(), status=r.status_code)


def render_delivery(request):

    delivery = None
    if request.method == 'POST':
        form = GetDeliveryForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            response = get_delivery_by_id(id)
            if response.status_code == 400:
                content = json.loads(response.content)
                messages.error(request, content['detail'])
            elif response.status_code == 422:
                content = json.loads(response.content)
                messages.error(request, content['detail'])
            elif response.status_code == 404:
                messages.error(request, 'Delivery not found')
            elif response.status_code == 500:
                messages.error(
                    request, 'Internal server error, please try again later.')
            elif response.status_code == 200:
                delivery = json.loads(response.content)
    else:
        form = GetDeliveryForm()

    return render(request, 'delivery.html', {'form': form, 'delivery': delivery})


def render_update_delivery(request):
    h = {
        'x-api-key': '57xzYFk9GgJNFnUjQKc9'
    }
    r = requests.get(
        'https://pasd-webshop-api.onrender.com/api/order/', headers=h)

    try:
        orders = r.json()
    except ValueError:
        orders = []

    deliveries = []
    for order in orders['orders']:
        if order['last_delivery'] == None:
            continue
        elif order['last_delivery']['status'] != 'REJ':
            if order['last_delivery']['status'] != 'EXP':
                deliveries.append((order['last_delivery']['id'], order['last_delivery']['id']))
                
    if request.method == 'POST':
        form = UpdateDeliveryForm(request.POST)
        form.fields['id'].choices = deliveries
        if form.is_valid():
            status = form.cleaned_data['status']
            id = form.cleaned_data['id']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            response = update_delivery(id, status, date, time)
            if response.status_code == 400:
                content = json.loads(response.content)
                messages.error(request, content['detail'])
            elif response.status_code == 422:
                content = json.loads(response.content)
                messages.error(request, content['detail'])
            elif response.status_code == 404:
                messages.error(request, 'Delivery not found')
            elif response.status_code == 500:
                messages.error(
                    request, 'Internal server error, please try again later.')
            elif response.status_code == 200:
                messages.success(request, 'Successfully updated')
        return redirect('update_delivery')
    else:
        form = UpdateDeliveryForm()
        form.fields['id'].choices = deliveries

    return render(request, 'update_delivery.html', {'form': form})


def update_delivery(id, status, date=None, time=None):
    h = {
        'Content-Type': 'application/json',
        'x-api-key': '57xzYFk9GgJNFnUjQKc9'
    }
    body = {
        "status": status
    }
    if status == "DEL" and date is not None and time is not None:
        dt = datetime.combine(date, time)
        body['actual_deliver_datetime'] = dt.isoformat(
            'T', 'milliseconds') + 'Z'

    r = requests.patch(
        f'https://pasd-webshop-api.onrender.com/api/delivery/{id}', headers=h, json=body)

    return JsonResponse(r.json(), status=r.status_code)


def post_label(id, label):
    h = {'x-api-key': '57xzYFk9GgJNFnUjQKc9'}
    body = {
        'labelFile': label
    }
    r = requests.post(
        f'https://pasd-webshop-api.onrender.com/api/label?delivery_id={id}', headers=h, files=body)

    return JsonResponse(r.json(), status=r.status_code)


def render_post_label(request):
    h = {
        'x-api-key': '57xzYFk9GgJNFnUjQKc9'
    }
    r = requests.get(
        'https://pasd-webshop-api.onrender.com/api/order/', headers=h)

    try:
        orders = r.json()
    except ValueError:
        orders = []
    expected_deliveries = []
    for order in orders['orders']:
        if order['last_delivery'] == None:
            continue
        elif order['last_delivery']['status'] != 'REJ':
            if order['last_delivery']['status'] == 'EXP':
                expected_deliveries.append((order['last_delivery']['id'], (order['last_delivery']['id'])))

    if request.method == 'POST':
        form = UploadLabelForm(request.POST, request.FILES)
        form.fields['id'].choices = expected_deliveries
        if form.is_valid():
            label = request.FILES['label']
            id = form.cleaned_data['id']
            response = post_label(id, label)
            if response.status_code == 200:
                messages.success(request, 'Successfully uploaded the label')
            elif response.status_code == 422:
                messages.error(request, 'Invalid input.')
            elif response.status_code == 404:
                messages.error(request, 'Delivery not found')
            elif response.status_code == 500:
                messages.error(
                    request, 'Internal server error, please try again later.')
            elif response.status_code == 400:
                messages.error(request, 'Delivery already has a label.')
        return redirect('label')
    else:
        form = UploadLabelForm()
        form.fields['id'].choices = expected_deliveries

    return render(request, 'label.html', {'form': form})


def get_deliveries(request):
    h = {
        'x-api-key': '57xzYFk9GgJNFnUjQKc9'
    }
    r = requests.get(
        'https://pasd-webshop-api.onrender.com/api/order/', headers=h)

    try:
        orders = r.json()
    except ValueError:
        orders = []

    expected_deliveries = []
    deliveries = []
    for order in orders['orders']:
        if order['last_delivery'] == None:
            continue
        elif order['last_delivery']['status'] != 'REJ':
            if order['last_delivery']['status'] == 'EXP':
                expected_deliveries.append(order)
            else:
                deliveries.append(order)

    if request.method == 'POST':
        if 'update' in request.POST:
            form = UpdateDeliveryFormNoID(request.POST, prefix = 'update')
            if form.is_valid():
                status = form.cleaned_data['status']
                id = request.POST.get('update')
                date = form.cleaned_data['date']
                time = form.cleaned_data['time']
                response = update_delivery(id, status, date, time)
                if response.status_code == 400:
                    content = json.loads(response.content)
                    messages.error(request, content['detail'])
                elif response.status_code == 422:
                    content = json.loads(response.content)
                    messages.error(request, content['detail'])
                elif response.status_code == 404:
                    messages.error(request, 'Delivery not found')
                elif response.status_code == 500:
                    messages.error(
                        request, 'Internal server error, please try again later.')
                elif response.status_code == 200:
                    messages.success(request, 'Successfully updated')
        elif 'label_id' in request.POST:
            label_form = UpLoadLabelFormNoID(request.POST, request.FILES, prefix = 'label')
            if label_form.is_valid():
                label = request.FILES['label-label']
                id = request.POST.get('label_id')
                response = post_label(id, label)
                if response.status_code == 200:
                    messages.success(request, 'Successfully uploaded the label')
                elif response.status_code == 422:
                    messages.error(request, 'Invalid input.')
                elif response.status_code == 404:
                    messages.error(request, 'Delivery not found')
                elif response.status_code == 500:
                    messages.error(
                        request, 'Internal server error, please try again later.')
                elif response.status_code == 400:
                    messages.error(request, 'Delivery already has a label.')

        return redirect('deliveries')
    else:
        form = UpdateDeliveryFormNoID(prefix = 'update')
        label_form = UpLoadLabelFormNoID(prefix = 'label')

    return render(
        request,
        'deliveries.html',
        {
            'form': form,
            'label_form': label_form,
            'deliveries': {'orders': deliveries},
            'expected_deliveries': {'orders': expected_deliveries}
        }
    )
