from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
# 4.2 Django ORM (Models)
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    featured = models.BooleanField(default=False, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='menu_items', null=True)

    class Meta:
        constraints = [
            # 4.2 Django ORM (Constraints)
            models.CheckConstraint(condition=models.Q(price__gte=0), name='price_gte_0'),
        ]

    def __str__(self):
        return self.name

class NutritionalInfo(models.Model):
    # 4.2 Django ORM (OneToOne Relationship)
    menu_item = models.OneToOneField(MenuItem, on_delete=models.CASCADE, primary_key=True)
    calories = models.IntegerField()
    protein = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Nutrition for {self.menu_item.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False, db_index=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    date = models.DateField(auto_now_add=True, db_index=True)
    # 4.2 Django ORM (ManyToMany Relationship)
    items = models.ManyToManyField(MenuItem, related_name='orders')

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.TextField(max_length=1000)

    class Meta:
        # 4.2 Django ORM (Indexes)
        indexes = [
            models.Index(fields=['reservation_time']),
        ]

    def __str__(self):
        return f"Reservation for {self.first_name} {self.last_name}"