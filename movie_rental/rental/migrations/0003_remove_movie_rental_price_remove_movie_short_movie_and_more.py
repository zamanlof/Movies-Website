# Generated by Django 5.0.4 on 2024-08-20 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_movie_image_alter_movie_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='rental_price',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='short_movie',
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
    ]
