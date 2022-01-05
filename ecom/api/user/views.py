from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserSerializer
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
import random
import re
# Create your views here.

def generate_session_token(length=10):
    return ''.join(random.SystemRndom().choice([char(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length)) 

@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'send a POST request with valid parameters only'})
    
    username = request.POST['email']
    username = request.POST['password']

# validation part
    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
        return    JsonResponse({'error': 'enter avalid email'})
    
    if len(password) < 3:
        return JsonResponse({'error': 'passwords need to be atlist of 3 char'})
    
    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(email=username)
        
        if user.check_password(password):
            usr_dict = UserModel.objects.get(email=username).values().first()
            usr_dict.pop('password')
           
            if user.session_token !="0":
               user.session_token = "0"
               user.save()
               return JsonResponse({'error': 'previous session exsists!'})
           
            token = generate_session_token()
            user.session_token = token
            user.save()
            return JsonResponse({'token': token, 'user': user_dict})
        else:
            return JsonResponse({'error': 'Invalid Password!'})
               
           
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Email'})

def signout(request, id):
    logout(request)
    
    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoseNotExsist:
        return JsonResponse({'error': 'Invalid user ID'})
    
    return JsonResponse({'success': 'Logout success'})   
        
class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action  = {'create': [AllowAny]}
    
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class =  UserSerializer
    
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        
        except KeyError:
            return [permission() for permission in self.permission_classes]