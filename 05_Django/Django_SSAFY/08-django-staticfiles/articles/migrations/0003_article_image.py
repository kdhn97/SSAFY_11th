# Generated by Django 4.2.11 on 2024-03-28 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_created_at_article_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
