# Generated by Django 2.1.3 on 2018-11-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0006_auto_20181122_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista_registro',
            name='fecha_realizado',
            field=models.DateField(null=True),
        ),
    ]
