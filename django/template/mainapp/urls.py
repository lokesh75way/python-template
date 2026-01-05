from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import api_views

# 4.3 Django REST Framework (DRF) - Routers
router = DefaultRouter()
router.register(r'menu-items', api_views.MenuItemViewSet)
router.register(r'reservations', api_views.ReservationViewSet)
router.register(r'orders', api_views.OrderViewSet)

urlpatterns = [
    path("function", views.hello_world),
    path('class', views.HelloView.as_view()),
    path('reservation', views.home),
    path('categories', api_views.CategoryView.as_view()),
    path('api/', include(router.urls)),
]