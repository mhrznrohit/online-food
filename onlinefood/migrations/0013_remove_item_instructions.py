# Generated by Django 4.0.1 on 2022-09-04 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinefood', '0012_cartitems_itemtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='instructions',
        ),
    ]