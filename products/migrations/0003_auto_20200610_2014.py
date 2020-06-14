# Generated by Django 3.0.7 on 2020-06-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productimage_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]