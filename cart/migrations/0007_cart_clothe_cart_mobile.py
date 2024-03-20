# Generated by Django 4.0 on 2024-03-17 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothe', '0001_initial'),
        ('mobile', '0002_remove_mobile_categories_delete_category_mobile'),
        ('cart', '0006_delete_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='clothe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothe.clothe'),
        ),
        migrations.AddField(
            model_name='cart',
            name='mobile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mobile.mobile'),
        ),
    ]