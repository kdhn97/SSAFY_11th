# Generated by Django 4.2.2 on 2023-06-30 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_product_created_at_product_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]