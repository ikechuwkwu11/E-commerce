# Generated by Django 5.1.7 on 2025-06-19 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('is_customer', models.BooleanField(default=True)),
                ('is_seller', models.BooleanField(default=False)),
                ('address', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
