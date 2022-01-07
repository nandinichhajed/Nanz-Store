from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializers
from .models  import Order
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True 
        return False
    except UserModel.DoseNotExsist:
        return False
    
@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'please re-login', 'code':'1'})
    
    if request.method == 'POST':
        user_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']
        
        total_pro = len(products.split(',')[:-1])
        
        UserModel = get_user_model()
        
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return JsonResponse({'error':'User dose not exsist'})
        
        ordr = Order(user=user, product_name=products, total_products=total_pro, transaction_id=transaction_id, total_amount=total_amount)
        ordr.save()
        return JsonResponse({'success': True, 'error': False, 'msg': 'Order placed successfully'})

class OrderViewSet(viewsets.ModelViewSet):
    quaryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializers        
    