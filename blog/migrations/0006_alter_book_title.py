# Generated by Django 4.2.3 on 2023-07-30 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
