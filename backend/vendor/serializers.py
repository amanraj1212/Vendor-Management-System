from rest_framework import serializers
from .models import Vendor
# vendor profile management ends
from .models import PurchaseOrder
# purchase order tracking ends

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'contact_details', 'address', 'vendor_code']
# vendor profile management ends

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['id', 'vendor', 'po_number', 'vendor_reference', 'order_date', 'delivery_date', 'items', 'quantity', 'status', 'quality_rating', 'issue_date', 'acknowledgment_date']  # Add other fields here like 'total_amount', 'status', 'created_at'
# purchase order tracking ends

class VendorPerformanceSerializer(serializers.Serializer):
    on_time_delivery_rate = serializers.FloatField()
    quality_rating_avg = serializers.FloatField()
    average_response_time = serializers.FloatField()
    fulfilment_rate = serializers.FloatField()
# Vendor Performance API Endpoint ends