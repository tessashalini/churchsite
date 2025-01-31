# Generated by Django 5.1.3 on 2025-01-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_communitymessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='submitted_at',
        ),
        migrations.AddField(
            model_name='donation',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donation',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='donation',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='donation',
            name='receipt',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='donation',
            name='receipt_file',
            field=models.FileField(upload_to='receipts/'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='transfer_method',
            field=models.CharField(max_length=50),
        ),
    ]
