# Generated by Django 4.2.3 on 2023-07-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=60)),
                ('mname', models.CharField(max_length=60)),
                ('lname', models.CharField(max_length=60)),
                ('gender', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('attach', models.FileField(upload_to='')),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]