from import_export import resources,fields,widgets
from .models import OilOrder,Order
from .widgets import PaymentWidget

class TireOrderResource(resources.ModelResource):
    payment = fields.Field(
        attribute="payment_type",
        widget=PaymentWidget(Order.PAYMENT_CHOICES)
    )

    class Meta:
        model = Order
        fields = ("id","phone",'name','product_title','email','order_date')
        export_order = ("id","phone",'name','product_title','email','payment','order_date')

class OilOrderResource(resources.ModelResource):
    payment = fields.Field(
        attribute="payment_type",
        widget=PaymentWidget(OilOrder.PAYMENT_CHOICES)
    )

    vol = fields.Field(
        attribute="oil__volume",
        column_name="volume",
        widget=widgets.CharWidget()
    )

    class Meta:
        model = OilOrder
        fields = ("id","phone",'name','product_title','email','order_date')
        export_order = ("id","phone",'name','product_title','vol','email','payment','order_date')