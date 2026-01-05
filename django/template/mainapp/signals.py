from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Order

# 4.5 Middleware & Signals (Signals)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(f"Signal: New user created: {instance.username}")
        # Logic to create profile would go here

@receiver(pre_save, sender=Order)
def check_order_status(sender, instance, **kwargs):
    if instance.id:  # existing object
        old_order = Order.objects.get(pk=instance.id)
        if old_order.status != instance.status:
           print(f"Signal: Order {instance.id} status changed from {old_order.status} to {instance.status}")
