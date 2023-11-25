from django.shortcuts import render, redirect
from .models import *
from rest_framework import viewsets, status
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime


class vendorViewset(viewsets.ModelViewSet):
    queryset = vendor.objects.all()
    serializer_class = vendorSerializer

    @action(detail=True, methods=["get"])
    def purchaseOrders(self, request, pk=None):
        vendorObj = self.get_object()
        purchaseOrders = purchaseOrder.objects.filter(vendor=vendorObj)
        serializer = purchaseOrderSerializer(
            purchaseOrders, many=True, context={"request": request}
        )
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def performance(self, request, pk=None):
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


class purchaseOrderViewset(viewsets.ModelViewSet):
    queryset = purchaseOrder.objects.all()
    serializer_class = purchaseOrderSerializer

    @action(detail=True, methods=["post"])
    def acknowledge(self, request, pk=None):
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


class performanceViewset(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
