from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import django.db
from .models import MenuItem, Category, Reservation, Order
from .serializers import MenuItemSerializer, CategorySerializer, ReservationSerializer, OrderSerializer

# 4.3 Django REST Framework (DRF) - Views (Generics)
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

# 4.3 Django REST Framework (DRF) - ViewSets
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    # 4.3 Django REST Framework (DRF) - Pagination, filtering, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'featured']
    search_fields = ['name']
    ordering_fields = ['price']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('items').all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    # 4.2 Django ORM (Transactions & atomic blocks)
    @django.db.transaction.atomic
    def perform_create(self, serializer):
        # Example of atomic transaction: save order and potentially decrease stock or something
        # For now just save, but wrapped in atomic block
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Users see only their own orders
        if self.request.user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)
