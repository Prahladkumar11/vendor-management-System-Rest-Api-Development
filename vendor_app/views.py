# Import necessary modules from Django and third-party packages
from django.shortcuts import render, redirect
from .models import *
from rest_framework import viewsets, status
from .serializers import vendorSerializer, purchaseOrderSerializer, PerformanceSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime


# Define a ViewSet for the 'vendor' model
class vendorViewset(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD operations on the 'vendor' model.
    """

    # Set the queryset to include all objects of the 'vendor' model
    queryset = vendor.objects.all()
    
    # Specify the serializer class to be used for the 'vendor' model
    serializer_class = vendorSerializer

    # Define a custom action to retrieve all purchase orders associated with a specific vendor
    @action(detail=True, methods=["get"])
    def purchaseOrders(self, request, pk=None):
        """
        Retrieve all purchase orders associated with a specific vendor.
        """
        vendorObj = self.get_object()
        purchaseOrders = purchaseOrder.objects.filter(vendor=vendorObj)
        serializer = purchaseOrderSerializer(
            purchaseOrders, many=True, context={"request": request}
        )
        return Response(serializer.data)

    # Define a custom action to retrieve performance data for a specific vendor
    @action(detail=True, methods=["get"])
    def performance(self, request, pk=None):
        """
        Retrieve historical performance data for a specific vendor.
        """
        vendor_obj = self.get_object()

        try:
            historical_performances = Performance.objects.filter(vendor=vendor_obj)
            serializer = PerformanceSerializer(
                historical_performances, many=True, context={"request": request}
            )
            return Response(serializer.data)

        except Performance.DoesNotExist:
            return Response(
                {"error": "No historical performance data exists for this vendor."}
            )


# Define a ViewSet for the 'purchaseOrder' model
class purchaseOrderViewset(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD operations on the 'purchaseOrder' model.
    """

    # Set the queryset to include all objects of the 'purchaseOrder' model
    queryset = purchaseOrder.objects.all()
    
    # Specify the serializer class to be used for the 'purchaseOrder' model
    serializer_class = purchaseOrderSerializer

    # Define a custom action to acknowledge a purchase order
    @action(detail=True, methods=["post"])
    def acknowledge(self, request, pk=None):
        """
        Acknowledge a purchase order.
        """
        purchase_order = self.get_object()

        if purchase_order.acknowledgementDate is None:
            purchase_order.acknowledgementDate = datetime.now()
            purchase_order.save()

            # Trigger recalculation of average_response_time
            update_average_response_time(purchase_order)

            return Response(
                {"detail": "Acknowledgment successful."}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "Purchase order already acknowledged."},
                status=status.HTTP_400_BAD_REQUEST,
            )


# Define a ViewSet for the 'Performance' model
class performanceViewset(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD operations on the 'Performance' model.
    """

    # Set the queryset to include all objects of the 'Performance' model
    queryset = Performance.objects.all()
    
    # Specify the serializer class to be used for the 'Performance' model
    serializer_class = PerformanceSerializer
