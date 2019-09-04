# Generated by Django 2.0.6 on 2019-09-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0040_auto_20190309_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_removed',
            field=models.BooleanField(default=False, verbose_name='Видалене'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_address',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Адреса (вулиця, будинок) покупця'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_city',
            field=models.CharField(default=None, max_length=80, null=True, verbose_name='Місто покупця'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_email',
            field=models.EmailField(default=None, max_length=70, null=True, verbose_name='Електронна пошта покупця'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(default=None, max_length=80, null=True, verbose_name="Ім'я покупця"),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=models.CharField(default=None, max_length=40, null=True, verbose_name='Телефон покупця'),
        ),
    ]