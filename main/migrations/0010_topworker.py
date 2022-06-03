# Generated by Django 4.0 on 2022-06-03 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_blog_remove_seller_user_delete_productdetail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='workers/')),
            ],
        ),
    ]