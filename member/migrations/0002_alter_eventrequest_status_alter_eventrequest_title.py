# Generated by Django 5.1.3 on 2024-12-08 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventrequest',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='eventrequest',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
