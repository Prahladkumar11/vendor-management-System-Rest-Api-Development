from django.urls import path,include
from . views import *
from .models import *
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'vendors', vendorViewset)
router.register(r'purchaseOrders', purchaseOrderViewset)
router.register(r'performances', performanceViewset)

urlpatterns = [    
    path('',include(router.urls))
      
]