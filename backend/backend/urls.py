from django.contrib import admin
from django.urls import path
from vendor.views import VendorListCreateView, VendorDetailView
from vendor.views import PurchaseOrderListCreateView, PurchaseOrderDetailView,VendorPerformanceView,PurchaseOrderAcknowledgmentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    # vendor profile management ends
    path('api/purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    # purchase order tracking ends
    path('api/vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    # Vendor Performance Evaluation ends
    path('api/purchase_orders/<int:pk>/acknowledge/', PurchaseOrderAcknowledgmentView.as_view(), name='acknowledge-purchase-order'),
    # Vendor Performance API Endpoint ends
]
