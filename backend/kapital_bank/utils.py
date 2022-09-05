from django.urls import reverse
from django.conf import settings

from .models import KapitalPaymentSecurity
from secure_sites.models import SecureSite

import requests
import os
import xmltodict


def generate_payment_url(order):
    secure_site = SecureSite.objects.filter(active=True).first()
    site_url = secure_site.get_address() if secure_site else ""

    success_url = site_url + reverse('success-view', kwargs={
        "uuid": order.uuid,
    })

    cancel_url = site_url + reverse('cancel-view', kwargs={
        "uuid": order.uuid,
    })

    if order.is_purchased and not settings.DEBUG:
        return cancel_url

    security = KapitalPaymentSecurity.objects.filter(active=True).first()

    if not security:
        return cancel_url

    data = generate_data(order, security, success_url, cancel_url)

    host_path = os.getcwd() if settings.DEBUG else "/vol/web"

    crt_file = host_path + security.crt_file.url
    key_file = host_path + security.key_file.url

    headers = {'Content-Type': 'application/xml'}

    response = requests.post(
        security.service_link,
        data=data.encode('utf-8'),
        headers=headers,
        verify=security.verify,
        cert=(crt_file, key_file)
    )

    if response.status_code >= 400:
        return cancel_url

    xml = response.text

    create_order_dict = xmltodict.parse(xml, process_namespaces=True)

    # try:
    order_dict = create_order_dict['TKKPG']['Response']['Order']
    order_id = order_dict['OrderID']
    session_id = order_dict['SessionID']
    # except KeyError:
    #     return cancel_url

    payment_url = security.payment_link.replace(
        "{{ORDERID}}", order_id).replace("{{SESSIONID}}", session_id)

    return payment_url


def generate_data(order, security, success_url, cancel_url):
    data = f"""<?xml version="1.0" encoding="UTF-8"?>
    <TKKPG>
        <Request>
            <Operation>CreateOrder</Operation>
            <Language>{order.get_lang_code()}</Language>
            <Order> 
                <OrderType>Purchase</OrderType>
                <Merchant>{security.merchant_id}</Merchant>
                <Amount>{order.get_total_price() * 100}</Amount>
                <Currency>944</Currency>
                <Description>{order.get_description()}</Description>
                <ApproveURL>{success_url}</ApproveURL>
                <CancelURL>{cancel_url}</CancelURL>
                <DeclineURL>{cancel_url}</DeclineURL>
            </Order>
        </Request>
    </TKKPG>
    """

    return data
