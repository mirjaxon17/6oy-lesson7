# Generated by Django 5.0.3 on 2024-04-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_remove_bookingbook_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1, upload_to='book'),
            preserve_default=False,
        ),
    ]
