# Generated by Django 4.1.2 on 2022-10-14 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_shoppingcart_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='client',
        ),
    ]
