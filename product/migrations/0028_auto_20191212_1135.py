# Generated by Django 2.0.5 on 2019-12-12 09:35

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_auto_20191212_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to=product.models.get_upload_path, verbose_name='фото товару'),
        ),
    ]
