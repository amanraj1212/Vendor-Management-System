from rest_framework import generics
from .models import Vendor
from .serializers import VendorSerializer,VendorPerformanceSerializer
# vendor profile management ends
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
# purchase order tracking ends
from rest_framework.response import Response
# Vendor Performance Evaluation ends
from .models import PurchaseOrder
from django.utils import timezone
from .models import Vendor, PurchaseOrder
# Vendor Performance API Endpoint ends

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
# vendor profile management ends

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()
        vendor_id = self.request.query_params.get('vendor_id')
        if vendor_id:
            queryset = queryset.filter(vendor__id=vendor_id)
        return queryset

class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
# purchase order tracking ends

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        #print(instance)
        performance_metrics = {
            'on_time_delivery_rate': instance.calculate_on_time_delivery_rate,
            'quality_rating_avg': instance.calculate_quality_rating,
            'average_response_time': instance.calculate_response_time,
            'fulfilment_rate': instance.calculate_fulfilment_rate,
        }
        serializer = VendorPerformanceSerializer(performance_metrics)
        return Response(serializer.data)
    # Vendor Performance API Endpoint ends
    
class PurchaseOrderAcknowledgmentView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Check if the purchase order has already been acknowledged
        if instance.acknowledgment_date is not None:
            return Response({"error": "Purchase order has already been acknowledged."}, status=400)

        instance.acknowledgment_date = timezone.now()
        instance.save()

        # Recalculate average_response_time for the vendor
        vendor = instance.vendor
        vendor.average_response_time = vendor.calculate_response_time()
        vendor.save()

        return Response({'acknowledgment_date': instance.acknowledgment_date})
# Vendor Performance API Endpoint ends