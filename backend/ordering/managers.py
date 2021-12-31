from django.db.models import Manager


class CartManager(Manager):
    def get_cart(self, request):
        if not request.session.session_key:
            request.session.save()
        user_key = request.session.session_key

        if not user_key:
            return None

        cart, _ = self.get_or_create(user_key=user_key)
        return cart

    def get_or_create_cart_item(self, request, product):
        cart = self.get_cart(request)

        if not cart:
            return None, None, False

        cart_item, new = cart.cart_items.get_or_create(
            product=product
        )

        return cart, cart_item, new