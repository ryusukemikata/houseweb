# Generated by Django 3.2.3 on 2023-01-01 04:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('housework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseworkmodel',
            name='postdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]