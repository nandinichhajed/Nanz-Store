from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_excempt
# Create your views here.
import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="yttk4qxd48g2phxm",
        public_key="nty8qkp4rv29qtjx",
        private_key="d59ab95a587f4603b8451b512c365daa"
    )
)

def validate_user_session(id, token):
    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoseNotExsist:
        return False
    
@csrf_excempt
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Invalid Session, Please login again!'})
    
    return JsonResponse({'clientToken': gateway.client_token.generate, 'success': True})

@csrf_excempt
def process_payement(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Invalid Session, Please login again!'})
    
    nonce_from_the_client = request.form["payment_method_nonce"]
    amount_from_the_client = request.form["amount"]
    
    result = gateway.transaction.sale({
    "amount": amount_from_the_client,
    "payment_method_nonce": nonce_from_the_client,
    "options": {
      "submit_for_settlement": True
        }
    })
    
    if result.is_success:
        return JsonResponse({"success": result.is_success, 
                             'transaction': {'id': result.transaction.id, 
                                             'amount': result.transaction.amount
                                             }})
    else:
        return JsonResponse({'success': False, 'error': True})