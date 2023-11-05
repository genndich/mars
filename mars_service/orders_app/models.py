from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError


class Device(models.Model):
    '''Модели оборудования'''
   
    manufacturer = models.CharField(max_length=50, verbose_name='Производитель')
    model = models.CharField(max_length=50, verbose_name='Модель')
    
    
    class Meta:
        db_table = 'devices'
        verbose_name = 'Доступное оборудование'
        verbose_name_plural = 'Доступное оборудование'        
        
    def __str__(self):
        return f'{self.manufacturer} {self.model}'


class Customer(models.Model):
    '''Конечные пользователи оборудования'''
    
    customer_name = models.CharField(max_length=50, verbose_name='Наименование организации')
    customer_address = models.CharField(max_length=50, verbose_name='Адрес')
    customer_cuty = models.CharField(max_length=50, verbose_name='Город')
    
    class Meta:
        db_table = 'customers'
        verbose_name = 'Описание контрагента'
        verbose_name_plural = 'Описание контрагентов'
    
    def __str__(self):
        return f'{self.customer_name}'
    

class DeviceInField(models.Model):
    '''Модель оборудования в полях'''
    
    serial_number = models.CharField(max_length=50, verbose_name='Серийный номер')
    customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name='Идентификатор контрагента')
    analyzer_id = models.ForeignKey(Device, on_delete=models.RESTRICT, verbose_name='Идентификатор оборудования')
    owner_status = models.CharField(max_length=50, verbose_name='Статус принедлежности')
    
    class Meta:
        db_table = 'devices_in_field'
        verbose_name = 'Оборудование в полях'
        verbose_name_plural = 'Оборудование в полях'
        
    def __str__(self):
        return f'{self.serial_number} {self.analyzer_id}'
    

def status_validator(order_status):
    if order_status not in ['open', 'closed', 'in_progress', 'need_info']:
        raise ValidationError('Неверный статус заказа')
    

class Order(models.Model):
    '''Класс для описания заявки'''
    
    device = models.ForeignKey(DeviceInField, on_delete=models.RESTRICT, verbose_name='Оборудование')
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name='Конечный пользователь')
    order_description = models.TextField(verbose_name='Описание заявки')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_update = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Дата последнего обновления')
    order_status = models.CharField(max_length=50, verbose_name='Статус заявки', validators=[status_validator])
    
    class Meta:
        db_table = 'orders'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        
    def save(self, *args, **kwargs):
        self.last_update = datetime.now()
        super().save(*args, **kwargs)
                                
    def __str__(self):
        return f'{self.device} {self.customer} {self.order_status}'