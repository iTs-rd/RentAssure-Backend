# Generated by Django 3.1.7 on 2021-04-10 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210410_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img1',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img2',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
