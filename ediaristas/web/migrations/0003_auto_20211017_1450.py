# Generated by Django 3.2.8 on 2021-10-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contratante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratante',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
