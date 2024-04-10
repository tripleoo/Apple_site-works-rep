# Generated by Django 5.0.2 on 2024-04-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iphone', '0006_review_iphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='vidtovara',
            name='slug',
            field=models.SlugField(default='default-slug-value', max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='nikname',
            field=models.CharField(max_length=50, verbose_name='Введите ваше имя'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rev',
            field=models.CharField(max_length=500, verbose_name='Оставьте свой комментарий'),
        ),
    ]
