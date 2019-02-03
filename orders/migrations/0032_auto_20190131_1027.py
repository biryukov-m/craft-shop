# Generated by Django 2.0.6 on 2019-01-31 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_auto_20190128_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='session_key',
            field=models.CharField(max_length=128, null=True, verbose_name='Ключ сесії покупця'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='order',
            field=models.OneToOneField(blank=True, default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='Належність до замовлення'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_address',
            field=models.CharField(max_length=20, null=True, verbose_name='Адреса (вулиця, будинок) покупця'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_city',
            field=models.CharField(max_length=20, null=True, verbose_name='Місто покупця'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_email',
            field=models.EmailField(max_length=30, null=True, verbose_name='Електронна пошта покупця'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=models.CharField(max_length=40, null=True, verbose_name='Телефон покупця'),
        ),
    ]