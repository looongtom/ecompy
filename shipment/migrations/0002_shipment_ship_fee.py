# Generated by Django 4.0 on 2024-03-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='ship_fee',
            field=models.DecimalField(db_column='ship_fee', decimal_places=2, default=20.0, max_digits=10),
        ),
    ]