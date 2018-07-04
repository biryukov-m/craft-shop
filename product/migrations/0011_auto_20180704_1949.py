# Generated by Django 2.0.7 on 2018-07-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20180702_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='cosmeticbag',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='dress',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='dresspattern',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='mobilecase',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='shirt',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='shirtpattern',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='skirt',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='skirtpattern',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='tablecloth',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='tshirt',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='tshirtpattern',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='tunic',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='tunicpattern',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, verbose_name='ціна'),
        ),
    ]
