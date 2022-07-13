from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import View
from django.urls import reverse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from ordering.models import Order
from .utils import generate_payment_url

class PaymentView(View):
    def get(self, request, *args, **kwargs):
        uuid = kwargs.get('uuid')
        order = get_object_or_404(Order, uuid=uuid)
        url = generate_payment_url(order)
        return redirect(url)

@method_decorator(csrf_exempt, name="dispatch")
class CancelView(View):
    template_name = "payment/cancel.html"

    def get(self, request, *args, **kwargs):
        uuid = kwargs.get('uuid')
        order = get_object_or_404(Order, uuid=uuid)
        return render(request, self.template_name, context={
            'object': order
        })

    def post(self, request, *args, **kwargs):   
        uuid = kwargs['uuid']
        to = reverse('cancel-view', kwargs={
            'uuid': uuid
        })
        return redirect(to)

@method_decorator(csrf_exempt, name="dispatch")
class SuccessView(View):
    template_name = "payment/success.html"

    def get(self, request, *args, **kwargs):
        uuid = kwargs.get('uuid')
        order = get_object_or_404(Order, uuid=uuid)
        return render(request, self.template_name, context={
            'object': order
        })

    def post(self, request, *args, **kwargs):
        uuid = kwargs['uuid']
        order = get_object_or_404(Order, uuid=uuid)

        order.is_purchased = True
        order.save()

        to = reverse('success-view', kwargs={
            'uuid': uuid
        })
        return redirect(to)




    