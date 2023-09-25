from product.models import Product

DISLIKE_SESSION_ID = 'dislike'

class Dislike:
    def __init__(self, request):
        self.session = request.session
        dislike = self.session.get(DISLIKE_SESSION_ID)

        if not dislike:
            dislike = self.session[DISLIKE_SESSION_ID] = {}

        self.dislike = dislike

    def unique_id_generator(self, id_user, slug_product):
        """ make the unique id as the id of
        the goods that insert into the dislike session """
        return f'{id_user}-{slug_product}'

    def save(self):
        """ save the all modified in session """
        self.session.modified = True

    def add(self, product, user):
        """ create the item in the dislike session
            if is not exists we add it
            if is exists we just increase the quantity"""
        unique = self.unique_id_generator(user.id, product.slug)
        if unique not in self.dislike:
            self.dislike[unique] = {'product_id': str(product.id), 'user_id': str(user.id)}
            self.save()

    def __iter__(self):
        """iterate all the item that exists in the dislike session"""
        dislike = self.dislike.copy()
        # l = []
        for item in dislike.values():
            product = Product.objects.get(id=int(item['product_id']))
            item['product'] = product
            yield item

    def delete(self, id):
        if id in self.dislike:
            del self.dislike[id]
            self.save()
