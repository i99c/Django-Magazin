# Generated by Django 5.0.6 on 2024-07-07 21:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_article_remove_contractverified_contracts_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='writers', to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
    ]
