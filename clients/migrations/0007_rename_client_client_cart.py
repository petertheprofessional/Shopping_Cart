# Generated by Django 4.1.2 on 2022-10-14 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_client_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client',
            new_name='cart',
        ),
    ]
