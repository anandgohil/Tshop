# Generated by Django 2.2.4 on 2020-10-24 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0006_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('PENDING', 'Pending'), ('PLACED', 'Placed'), ('CANCELED', 'Canceled'), ('COMPLITED', 'Complited')], max_length=15)),
                ('payment_method', models.CharField(choices=[('CASH_ON_DELIVERY', 'cash_On_Delivery'), ('ONLINE', 'Online')], max_length=30)),
                ('total', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('shipping_addres', models.CharField(max_length=200)),
                ('contact', models.IntegerField(max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Payment_status', models.CharField(default='FAILED', max_length=15)),
                ('payment_id', models.CharField(max_length=60)),
                ('payment_request_id', models.CharField(max_length=60, unique=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.SizeVarient')),
                ('tshirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Tshirt')),
            ],
        ),
    ]