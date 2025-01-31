# Generated by Django 5.1.3 on 2025-01-06 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_layer', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='donation',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donor',
            field=models.CharField(max_length=255),
        ),
    ]
