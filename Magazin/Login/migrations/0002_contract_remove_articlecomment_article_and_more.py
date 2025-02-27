# Generated by Django 5.0 on 2024-07-03 20:46

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('content', ckeditor.fields.RichTextField()),
                ('is_delete', models.BooleanField(default=False, verbose_name='Silindi')),
                ('delete_date', models.DateTimeField(blank=True, null=True, verbose_name='Silinme Tarihi')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme Tarihi')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='Url')),
            ],
        ),
        migrations.RemoveField(
            model_name='articlecomment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='articlecomment',
            name='reader',
        ),
        migrations.RemoveField(
            model_name='reader',
            name='user',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='user',
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefon')),
                ('is_darkmode', models.BooleanField(default=False, verbose_name='Dark Mode')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme Tarihi')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Silindi')),
                ('delete_date', models.DateTimeField(blank=True, null=True, verbose_name='Silinme Tarihi')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
        migrations.CreateModel(
            name='ContractVerified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme Tarihi')),
                ('contracts', models.ManyToManyField(to='Login.contract', verbose_name='Sözleşmeler')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Login.customer', verbose_name='Müşteri')),
            ],
        ),
        migrations.CreateModel(
            name='ContactVerified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_phone', models.BooleanField(default=False, verbose_name='Telefon Doğrulandı')),
                ('is_mail', models.BooleanField(default=False, verbose_name='Mail Doğrulandı')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme Tarihi')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Silindi')),
                ('delete_date', models.DateTimeField(blank=True, null=True, verbose_name='Silinme Tarihi')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Login.customer', verbose_name='Müşteri')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Backend Developer', 'Backend Developer'), ('Frontend Developer', 'Frontend Developer'), ('Fullstack Developer', 'Fullstack Developer'), ('Web Developer', 'Web Developer'), ('Mobile Developer', 'Mobile Developer'), ('DevOps Engineer', 'DevOps Engineer'), ('UI/UX Designer', 'UI/UX Designer'), ('Graphic Designer', 'Graphic Designer'), ('Quality Assurance Engineer', 'Quality Assurance Engineer'), ('Project Manager', 'Project Manager'), ('Product Manager', 'Product Manager'), ('Scrum Master', 'Scrum Master'), ('Database Administrator', 'Database Administrator'), ('System Administrator', 'System Administrator'), ('Network Administrator', 'Network Administrator'), ('Technical Support', 'Technical Support'), ('Customer Support', 'Customer Support'), ('Sales Manager', 'Sales Manager'), ('HR Manager', 'HR Manager'), ('Finance Manager', 'Finance Manager'), ('Legal Advisor', 'Legal Advisor'), ('Content Writer', 'Content Writer'), ('Marketing Specialist', 'Marketing Specialist'), ('Business Analyst', 'Business Analyst'), ('Data Scientist', 'Data Scientist'), ('Security Specialist', 'Security Specialist'), ('IT Consultant', 'IT Consultant'), ('Trainer / Instructor', 'Trainer / Instructor'), ('Intern', 'Intern')], max_length=50, verbose_name='Görevi')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefon')),
                ('is_darkmode', models.BooleanField(verbose_name='Dark Mode')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Silindi')),
                ('delete_date', models.DateTimeField(blank=True, null=True, verbose_name='Silinme Tarihi')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme Tarihi')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='Url')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='ArticleComment',
        ),
        migrations.DeleteModel(
            name='Reader',
        ),
        migrations.DeleteModel(
            name='Writer',
        ),
    ]
