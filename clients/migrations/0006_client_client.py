# Generated by Django 4.1.2 on 2022-10-14 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_remove_shoppingcart_client'),
        ('clients', '0005_remove_client_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart', to='shopping.shoppingcart', unique=True),
        ),
    ]