# Generated by Django 5.1 on 2024-09-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poste', models.CharField(max_length=300)),
                ('course_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tutor_name', models.CharField(max_length=100)),
                ('duration', models.FloatField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
