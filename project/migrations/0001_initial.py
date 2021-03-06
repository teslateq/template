# Generated by Django 2.1.3 on 2018-11-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('name_project', models.CharField(max_length=50)),
                ('email_company', models.EmailField(max_length=20)),
                ('logo_company', models.CharField(default='', max_length=20)),
                ('web_company', models.URLField(default='')),
            ],
        ),
    ]
