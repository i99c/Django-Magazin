# Generated by Django 5.0.6 on 2024-07-10 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Writer', '0009_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
    ]
