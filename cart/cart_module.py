from product.models import Product

CART_SESSION_ID = 'cart'

class Cart:
    """this class use for the add the goods that customer select it for buying"""

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)

        if not cart:
            cart = self.session[CART_SESSION_ID] = {}

        self.cart = cart



    def unique_id_generator(self, id, color, size):
        """ make the unique id as the id of
        the goods that insert into the cart session """
        return f'{id}-{color}-{size}'

    def save(self):
        """ save the all modified in session """
        self.session.modified = True

    def __iter__(self):
        """iterate all the item that exists in the cart session"""
        cart = self.cart.copy()
        # l = []
        for item in cart.values():
            product = Product.objects.get(id=int(item['product_id']))
            item['product'] = product
            item['total'] = float(item['price']) * int(item['quantity'])
            item['unique_id'] = self.unique_id_generator(item['product_id'], item['color'], item['size'])
            yield item

    def add(self, product, quantity, color, size):
        """ create the item in the cart session
            if is not exists we add it
            if is exists we just increase the quantity"""
        print(quantity)
        unique = self.unique_id_generator(product.id, color, size)
        if unique not in self.cart:
            self.cart[unique] = {'product_id': str(product.id), 'quantity': str(quantity), 'color': color, 'size': size,
                                 'price': product.price}
        else:
            self.cart[unique]['quantity'] = str(int(self.cart[unique]['quantity']) + int(quantity))
        self.save()
        print(self.cart.values())

    def total_price(self):
        tot_of_order = 0
        for item in self.cart.values():
            tot_of_order += float(item['price']) * int(item['quantity'])
        return tot_of_order
    def delete(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()


    def clear(self):
        del self.session[CART_SESSION_ID]
