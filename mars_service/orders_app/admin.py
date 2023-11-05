from django.contrib import admin

# Register your models here.
from .models import Device, Customer, DeviceInField, Order


class DeviceAdmin(admin.ModelAdmin):
    '''Класс для описания админки модели Device'''
    list_display = ('manufacturer', 'model', 'id')
    

class CustomerAdmin(admin.ModelAdmin):
    '''Класс для описания админки модели Customer'''
    list_display = ('customer_name', 'customer_address', 'customer_cuty', 'id')
    

class DeviceInFieldAdmin(admin.ModelAdmin):
    '''Класс для описания админки модели DeviceInField'''
    list_display = ('serial_number', 'customer_id', 'analyzer_id', 'owner_status', 'id')
    

class OrderAdmin(admin.ModelAdmin):
    '''Класс для описания админки модели Order'''
    list_display = ('id', 'device', 'customer', 'order_description', 'created', 'last_update', 'order_status')

admin.site.register(Device, DeviceAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(DeviceInField, DeviceInFieldAdmin)
admin.site.register(Order, OrderAdmin)