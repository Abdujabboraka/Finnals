# Generated by Django 5.1.2 on 2024-12-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_ratelesson_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratelesson',
            name='rate',
            field=models.CharField(choices=[('like', 'like'), ('dislike', 'dislike')], max_length=8),
        ),
    ]