# Generated by Django 5.1.2 on 2024-12-01 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_ratelesson_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratelesson',
            name='rate',
            field=models.CharField(max_length=10),
        ),
    ]
