# Generated by Django 5.0.3 on 2024-04-06 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_remove_comments_book_bookingbook_comments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comments',
            field=models.ManyToManyField(to='library.comments'),
        ),
    ]
