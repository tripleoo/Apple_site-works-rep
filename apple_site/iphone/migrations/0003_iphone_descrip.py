# Generated by Django 5.0.2 on 2024-03-24 19:12

import django.db.models.deletion
import iphone.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iphone', '0002_description_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='iphone',
            name='descrip',
            field=models.ForeignKey(default=iphone.models.default_description, on_delete=django.db.models.deletion.PROTECT, related_name='des', to='iphone.description'),
        ),
    ]
