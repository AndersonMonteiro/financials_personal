# Generated by Django 3.2.7 on 2022-01-10 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20220110_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
