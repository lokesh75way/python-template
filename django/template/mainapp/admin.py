from django.contrib import admin
from .models import MenuItem, Category, Reservation, Order

# 4.6 Admin Customization (Custom actions)
@admin.action(description='Mark selected items as featured')
def make_featured(modeladmin, request, queryset):
    queryset.update(featured=True)

# 4.6 Admin Customization (ModelAdmin)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'featured')
    list_filter = ('category', 'featured')
    search_fields = ('name',)
    actions = [make_featured]

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'reservation_time', 'guest_count')
    list_filter = ('reservation_time',)
    search_fields = ('first_name', 'last_name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'status', 'date')
    list_filter = ('status', 'date')

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Category)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Order, OrderAdmin)