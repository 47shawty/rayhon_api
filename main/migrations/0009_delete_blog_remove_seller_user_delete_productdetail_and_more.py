# Generated by Django 4.0 on 2022-06-03 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_main_image_product_image_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProductDetail',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]