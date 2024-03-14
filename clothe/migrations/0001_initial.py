# Generated by Django 4.0 on 2024-03-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('brand', models.CharField(max_length=255, verbose_name='Brand')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='clothes/')),
            ],
        ),
    ]
