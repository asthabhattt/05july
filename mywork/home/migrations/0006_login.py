# Generated by Django 3.2.5 on 2021-07-19 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210719_0022'),
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
