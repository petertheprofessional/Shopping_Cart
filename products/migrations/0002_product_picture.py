# Generated by Django 4.1.2 on 2022-10-13 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.URLField(default='https://img.freepik.com/free-vector/digital-device-mockup_53876-89354.jpg?w=826&t=st=1665647104~exp=1665647704~hmac=7acb146d6df6054b016bb1d9d70b2f2083eefaac4683cb3082cd8b4c1715ea60'),
        ),
    ]
