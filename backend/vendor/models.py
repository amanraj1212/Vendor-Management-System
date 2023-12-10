from django.db import models
from django.utils.timezone import now
from django.db.models import Count, Avg, F, ExpressionWrapper, DurationField
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=200)
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    # Additional fields for performance metrics Vendor Performance Evaluation: START
    on_time_delivery_rate = models.FloatField()
    quality_rating = models.FloatField()
    response_time = models.FloatField()
    fulfilment_rate = models.FloatField()
    # Additional fields for performance metrics Vendor Performance Evaluation: END

    def __str__(self):
        return self.name
    
    # Backend logic for performance metric:START
    def calculate_on_time_delivery_rate(self):
        completed_orders = self.purchaseorder_set.filter(status='completed')
        total_completed_orders = completed_orders.count()
        on_time_delivered_orders = completed_orders.filter(delivery_date__lte=F('acknowledgment_date'))
        on_time_delivery_rate = on_time_delivered_orders.count() / total_completed_orders if total_completed_orders else 0.0
        #print(on_time_delivery_rate)
        return on_time_delivery_rate

    def calculate_quality_rating(self):
        completed_orders_with_rating = self.purchaseorder_set.filter(status='completed', quality_rating__isnull=False)
        quality_rating_avg = completed_orders_with_rating.aggregate(avg_rating=Avg('quality_rating'))['avg_rating'] or 0.0
        #print(quality_rating_avg)
        return quality_rating_avg

    def calculate_response_time(self):
        acknowledged_orders = self.purchaseorder_set.filter(acknowledgment_date__isnull=False)
        response_times = [
            ack_order.acknowledgment_date - ack_order.issue_date
            for ack_order in acknowledged_orders
        ]
        total_response_time = sum(response_times, timezone.timedelta())  # Initialize as timedelta
        average_response_time = total_response_time / len(response_times) if response_times else timezone.timedelta()
        #print(average_response_time.total_seconds() / 60)
        return average_response_time.total_seconds() / 60  # Convert to minutes

    def calculate_fulfilment_rate(self):
        all_orders = self.purchaseorder_set.all()
        fulfilled_orders = all_orders.filter(status='completed', quality_rating__isnull=False)
        fulfilment_rate = fulfilled_orders.count() / all_orders.count() if all_orders.count() else 0.0
        #print(fulfilment_rate)
        return fulfilment_rate
    # Backend logic for performance metric:END
    
# vendor profile management ends
    
class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50)
    vendor_reference = models.CharField(max_length=100)
    order_date = models.DateField()
    # Add fields for performance metrics Vendor Performance Evaluation: START
    delivery_date = models.DateTimeField(default=now)
    items = models.JSONField(default=list)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=50, default='Pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(default=now)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    # Add fields for performance metrics Vendor Performance Evaluation: END

    def __str__(self):
        return f"PO-{self.po_number}"    
# purchase order tracking ends

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"  
# Historical Performance Model ends