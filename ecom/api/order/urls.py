from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/<str:id>/<str:token>/', views.add, name='order.add'),    
]