# Generated by Django 4.1.7 on 2023-03-09 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_author_publisher_alter_book_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
