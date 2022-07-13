from import_export import widgets

class PaymentWidget(widgets.Widget):
    def __init__(self,payment_choices):
        self.payment_choices = payment_choices

    def render(self, value, obj=None):
        paymant_choice = self.payment_choices[value - 1][1] 
        return paymant_choice