# Generated by Django 3.2.6 on 2021-08-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('Stationary', 'Stationary'), ('Electronices', 'Electronices'), ('food', 'food')], max_length=20)),
                ('quantity', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]