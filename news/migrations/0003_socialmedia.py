# Generated by Django 4.2 on 2024-08-01 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_subscribe'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('instagram', models.URLField()),
            ],
            options={
                'verbose_name': 'SocialMedia',
                'verbose_name_plural': 'SocialMedia',
            },
        ),
    ]
