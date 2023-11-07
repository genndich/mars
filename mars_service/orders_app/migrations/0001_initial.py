# Generated by Django 4.2 on 2023-11-05 13:08

from django.db import migrations, models
import django.db.models.deletion
import orders_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50, verbose_name='Наименование организации')),
                ('customer_address', models.CharField(max_length=50, verbose_name='Адрес')),
                ('customer_cuty', models.CharField(max_length=50, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Описание контрагента',
                'verbose_name_plural': 'Описание контрагентов',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=50, verbose_name='Производитель')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Доступное оборудование',
                'verbose_name_plural': 'Доступное оборудование',
                'db_table': 'devices',
            },
        ),
        migrations.CreateModel(
            name='DeviceInField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50, verbose_name='Серийный номер')),
                ('owner_status', models.CharField(max_length=50, verbose_name='Статус принедлежности')),
                ('analyzer_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.device', verbose_name='Идентификатор оборудования')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.customer', verbose_name='Идентификатор контрагента')),
            ],
            options={
                'verbose_name': 'Оборудование в полях',
                'verbose_name_plural': 'Оборудование в полях',
                'db_table': 'devices_in_field',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_description', models.TextField(verbose_name='Описание заявки')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('last_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата последнего обновления')),
                ('order_status', models.CharField(max_length=50, verbose_name='Статус заявки')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.customer', verbose_name='Конечный пользователь')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.deviceinfield', verbose_name='Оборудование')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'db_table': 'orders',
            },
        ),
    ]
