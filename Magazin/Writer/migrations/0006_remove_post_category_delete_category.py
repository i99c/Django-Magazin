# Generated by Django 5.0.6 on 2024-07-08 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Writer', '0005_category_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
