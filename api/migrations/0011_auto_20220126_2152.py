# Generated by Django 3.2 on 2022-01-26 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20220126_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartao',
            old_name='uuid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='historical_cartao',
            old_name='uuid',
            new_name='id',
        ),
    ]