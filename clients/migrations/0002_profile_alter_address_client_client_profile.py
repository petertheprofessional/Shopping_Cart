# Generated by Django 4.1.2 on 2022-10-14 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.URLField()),
                ('about_me', models.TextField()),
                ('settings', models.JSONField()),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='addresses', to='clients.client'),
        ),
        migrations.AddField(
            model_name='client',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.profile', unique=True),
        ),
    ]
