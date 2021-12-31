from rest_framework.views import APIView
from rest_framework import permissions,response,status
from rest_framework.generics import CreateAPIView

from . import serializers
# from .models import Cart
from tireapp.models import Tire


class TireOrderAPIView(CreateAPIView):
    serializer_class = serializers.TireOrderSerializer
    permission_classes = [permissions.AllowAny]
    

class OilOrderAPIView(CreateAPIView):
    serializer_class = serializers.OilOrderSerializer
    permission_classes = [permissions.AllowAny]


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

         