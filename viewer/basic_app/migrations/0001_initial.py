# Generated by Django 4.0.3 on 2022-11-17 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('designation', models.CharField(max_length=50)),
                ('faculty_id', models.CharField(blank=True, max_length=5)),
                ('photo', models.ImageField(default='default_pic.jpg', upload_to='photos')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=10)),
                ('dob', models.DateField(default=datetime.date.today)),
                ('blood_group', models.CharField(blank=True, choices=[('A+ve', 'A+ve'), ('B+ve', 'B+ve'), ('A-ve', 'A-ve'), ('B-ve', 'B-ve'), ('O+ve', 'O+ve'), ('AB-ve', 'A-ve')], max_length=5)),
                ('aadhar_no', models.CharField(blank=True, max_length=12)),
                ('pan_no', models.CharField(blank=True, max_length=10)),
                ('mobile', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
