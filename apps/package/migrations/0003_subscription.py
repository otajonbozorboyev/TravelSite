# Generated by Django 5.1.1 on 2024-10-05 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0002_bookingtour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('is_published', models.BooleanField(default=False)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
