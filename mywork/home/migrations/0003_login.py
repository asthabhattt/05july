# Generated by Django 3.2.5 on 2021-07-17 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginusername', models.CharField(max_length=122)),
                ('loginpassword', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]
