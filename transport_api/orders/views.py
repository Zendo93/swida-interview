from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        order_number = self.request.query_params.get('order_number')
        customer_name = self.request.query_params.get('customer_name')

        if order_number:
            queryset = queryset.filter(order_number__icontains=order_number)
        if customer_name:
            queryset = queryset.filter(customer_name__icontains=customer_name)

        return queryset

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer