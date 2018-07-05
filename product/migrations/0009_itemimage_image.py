# Generated by Django 2.0.6 on 2018-07-02 10:53

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_itemimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemimage',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to=product.models.get_upload_path, verbose_name='фото товару'),
        ),
    ]