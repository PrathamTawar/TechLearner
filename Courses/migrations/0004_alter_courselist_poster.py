# Generated by Django 5.1 on 2024-09-09 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0003_rename_duration_courselist_duration_months_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselist',
            name='poster',
            field=models.ImageField(blank=True, default='', upload_to='posters/'),
        ),
    ]
