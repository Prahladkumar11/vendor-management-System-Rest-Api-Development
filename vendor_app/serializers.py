# Import necessary modules from Django REST Framework
from rest_framework import serializers

# Import models from the current application
from .models import *

# Define a serializer for the 'vendor' model
class vendorSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the 'vendor' model.

    Serializes the 'vendor' model fields to be used in API responses.
    """
    id = serializers.ReadOnlyField()

    class Meta:
        model = vendor
        fields = ('id', 'name', 'address', 'vendor_code', 'contact_details')
        

# Define a serializer for the 'purchaseOrder' model
class purchaseOrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the 'purchaseOrder' model.

    Serializes the 'purchaseOrder' model fields to be used in API responses.
    """
    id = serializers.ReadOnlyField()

    class Meta:
        model = purchaseOrder
        fields = ('id', 'poNumber', 'vendor', 'orderDate', 'issueDate', 'deliveryDate', 'items', 'quantity', 'status', 'quantityRating')


# Define a serializer for the 'Performance' model
class PerformanceSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the 'Performance' model.

    Serializes the 'Performance' model fields to be used in API responses.
    """
    id = serializers.ReadOnlyField()
    
    # Use a HyperlinkedRelatedField to represent the 'vendor' relationship as a hyperlink
    vendor = serializers.HyperlinkedRelatedField(view_name='vendor-detail', read_only=True)

    class Meta:
        models=Performance
        fields="__all__"
        
     
