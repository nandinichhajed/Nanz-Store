from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category
# Create your views here.

# A ViewSet class is simply a type of class-based View, 
# that does not provide any method handlers such as .get() or .post(), 
# and instead provides actions such as .list() and .create().

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    
# Using ViewSet you don't have to create separate views for getting a list of 
# objects and detail of one object. 
# ViewSet will handle for you in a consistent way both list and detail.