# Generated by Django 2.1.3 on 2018-11-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0012_delete_recibo'),
    ]

    operations = [
        migrations.CreateModel(
            name='recibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.IntegerField(blank=True, null=True)),
                ('mes', models.CharField(max_length=100)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]