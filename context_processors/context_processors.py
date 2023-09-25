from save.models import SaveModel
from like.models import LikeModel
from dislike.models import DislikeModel
from account.models import CustomerService
from product.models import Product
def user_is_authenticate(requset):
    is_authenticated = requset.user.is_authenticated
    return {'is_authenticated': is_authenticated}
def last_service_number(request):
    service = CustomerService.objects.all().last()
    return {'service': service}
