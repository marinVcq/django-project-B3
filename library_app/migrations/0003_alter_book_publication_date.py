# Generated by Django 4.2.7 on 2023-12-19 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.TextField(),
        ),
    ]