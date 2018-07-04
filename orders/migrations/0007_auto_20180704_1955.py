# Generated by Django 2.0.7 on 2018-07-04 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180704_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Замовлений товар', 'verbose_name_plural': 'Замовлені товари'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус замовлення', 'verbose_name_plural': 'Статуси замовлень'},
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_comment',
            field=models.TextField(blank=True, default=None, max_length=300, null=True, verbose_name='Комментар до замовлення'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, verbose_name='Електронна пошта покупця'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(max_length=64, verbose_name='Имя покупця'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=models.CharField(blank=True, default=None, max_length=40, null=True, verbose_name='Телефон покупця'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.Status', verbose_name='Статус замовлення'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Назва статуса'),
        ),
    ]
