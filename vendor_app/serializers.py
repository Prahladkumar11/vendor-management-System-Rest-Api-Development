from rest_framework import serializers
from .models import *

class vendorSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=vendor
        fields=('id','name','address','vendor_code','contact_details')
        
        
class purchaseOrderSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=purchaseOrder
        fields=('id','poNumber','vendor','orderDate','issueDate','deliveryDate','items','quantity','status','quantityRating')
        
class PerformanceSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    vendor = serializers.HyperlinkedRelatedField(view_name='vendor-detail', read_only=True)
    class Meta:
        model=Performance
        fields="__all__"
        