# Generated by Django 3.2.6 on 2021-08-30 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20210830_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
    ]
