from django.core.mail import send_mail, EmailMultiAlternatives, get_connection
from django.conf import settings
from django.template.loader import render_to_string

from pathlib import Path
from email.mime.image import MIMEImage

import os

from rest_framework.views import APIView
from rest_framework import permissions,response,status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from . import serializers
from .models import Order
from tireapp.models import Tire
from emailapp.models import AuthUser
from kapital_bank.models import KapitalPaymentSecurity

from social.models import Phone
from navigation.models import Logo


class TireOrderAPIView(CreateAPIView):
    serializer_class = serializers.TireOrderSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        data = { "lang_code": request.LANGUAGE_CODE, **request.data }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class OilOrderAPIView(CreateAPIView):
    serializer_class = serializers.OilOrderSerializer
    permission_classes = [permissions.AllowAny]


class EmailSenderAPIView(APIView):
    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()

        if not order:
            return response.Response(
                status=status.HTTP_404_NOT_FOUND
            )

        if not order.email:
            return response.Response(
                status=status.HTTP_400_BAD_REQUEST, 
                data={
                    "message": "Email is not provided!"
                }
            )

        auth_user = AuthUser.objects.filter(active=True).first()
        if not auth_user:
            return response.Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "messagee": "Auth user is not available!"
                }
            )

        security = KapitalPaymentSecurity.objects.filter(active=True).first()


        logo = Logo.objects.filter(active=True).first()
        logo_image = None
        
        if logo:
            logo_image = logo.logo
            

        phone = Phone.objects.filter(active=True).first()
        phone_number = ""

        if phone:
            phone_number = phone.number

        html_message = render_to_string('emails/payment-email.html',{
            "object":order,
            "phone": phone_number,
            "online_payment": security
        })

        subject = "Payment"
        recipient_list = [order.email]
        fail_silently = settings.DEBUG == False

        connection = get_connection(
            username=auth_user.email, 
            password=auth_user.password, 
            fail_silently=fail_silently
        )

        msg = EmailMultiAlternatives(subject, "...", auth_user.email, recipient_list, connection=connection)
        msg.mixed_subtype = 'related' 
        msg.attach_alternative(html_message, "text/html")

        if logo_image:
            image = MIMEImage(logo_image.read())
            msg.attach(image)
            image.add_header('Content-ID', "<logo>")

        if order.tire.brand and order.tire.brand.image:
            image = MIMEImage(order.tire.brand.image.read())
            msg.attach(image)
            image.add_header("Content-ID", "<brand>")
        
        msg.send()

        

        return response.Response()


# class CartItemAPIView(APIView):
#     product_models = [Tire]
#     permission_classes = [permissions.AllowAny]

#     def post(self,request,*args,**kwargs):
#         model = self.get_model(**kwargs)
#         product = self.get_product(**kwargs)
#         cart, cart_item, new = Cart.objects.get_or_create_cart_item(request,product)
#         self.manage_cart_item(request, cart_item, new, **kwargs)
#         return response.Response(data={
#             'totalQuantity': cart.quantity,
#             'quantity': cart_item.quantity,
#             'totalPrice': cart.update_total_price()
#         },status=status.HTTP_201_CREATED)


#     def manage_cart_item(self, request, cart_item, new, action, **kwargs):
#         quantity = request.data.get('quantity', 1)
        
#         if action == 'increment':
#             cart_item.increment(quantity)
#         else:
#             cart_item.decrement()

#         if cart_item.quantity == 0:
#             cart_item.delete()


#     def get_model(self,**kwargs):
#         try:
#             index = kwargs.get('index', 1)
#             return self.product_models[index]
#         except ValueError:
#             return Tire

#     def get_product(self, model, **kwargs):
#         pk = kwargs['pk']
#         return model.objects.filter(pk=pk).first()

         