# Generated by Django 3.1.3 on 2020-12-12 08:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201212_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(default=1, unique=True, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
