# Generated by Django 4.0.6 on 2022-07-25 16:39

import api.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(blank=True, default='Not Available', max_length=32, null=True)),
                ('mobile', models.CharField(blank=True, default='Not Available', max_length=10, null=True)),
                ('dp', models.ImageField(blank=True, default='images/dp/default.jpg', upload_to='images/dp/')),
                ('age', models.CharField(blank=True, default='Not Available', max_length=3, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Not available', max_length=10)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='about')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60, validators=[api.models.WhitelistEmailValidator(whitelist=['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'])])),
                ('mobile', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\ \\d+)*\\Z'), code='invalid', message=None), django.core.validators.MinLengthValidator(10)], verbose_name='Phone Number')),
                ('detail', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(choices=[('Flat', 'Flat'), ('Room', 'Room'), ('House', 'House')], max_length=5)),
                ('title', models.CharField(max_length=32)),
                ('img1', models.ImageField(blank=True, default='images/default/1.jpg', upload_to='images/product/')),
                ('img2', models.ImageField(blank=True, default='images/default/2.jpg', upload_to='images/product/')),
                ('img3', models.ImageField(blank=True, default='images/default/3.jpg', upload_to='images/product/')),
                ('img4', models.ImageField(blank=True, default='images/default/4.jpg', upload_to='images/product/')),
                ('description', models.TextField(max_length=360)),
                ('bhk', models.CharField(blank=True, choices=[('1RK/1BHK', '1RK/1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK'), ('4BHK', '4BHK'), ('5+BHK', '5+BHK'), ('No', 'No')], max_length=10, null=True)),
                ('bedroom', models.IntegerField(blank=True, default=0, null=True)),
                ('bathroom', models.IntegerField(blank=True, default=0, null=True)),
                ('balconies', models.IntegerField(blank=True, default=0, null=True)),
                ('Kitchen', models.IntegerField(blank=True, default=0, null=True)),
                ('area', models.IntegerField(blank=True, default=0, null=True)),
                ('parking', models.BooleanField(default=False)),
                ('lift', models.BooleanField(default=False)),
                ('swimming_pool', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
                ('gas_pipeline', models.BooleanField(default=False)),
                ('electricity_charge', models.IntegerField(blank=True, default=0)),
                ('electricity_supply', models.BooleanField(default=True)),
                ('Power_backup', models.BooleanField(default=False)),
                ('water_charge', models.IntegerField(blank=True, default=0)),
                ('water_supply', models.BooleanField(default=True)),
                ('water_purifier', models.BooleanField(default=False)),
                ('fridge', models.BooleanField(default=False)),
                ('washing_machine', models.BooleanField(default=False)),
                ('CCTV', models.BooleanField(default=False)),
                ('guard', models.BooleanField(default=False)),
                ('medical', models.BooleanField(default=False)),
                ('fire_alarme', models.BooleanField(default=False)),
                ('cleaning', models.CharField(blank=True, choices=[('No', 'No'), ('Daily', 'Daily'), ('Weekly', 'Weekly')], default='No', max_length=6)),
                ('furnished', models.CharField(choices=[('Unfurnished', 'Unfurnished'), ('SemiFurnished', 'Semifurnished'), ('FullyFurnished', 'Fullyfurnished')], default='Unfurnished', max_length=20)),
                ('available_for', models.CharField(blank=True, choices=[('Student', 'Student'), ('GovernmentEmployee', 'GovernmentEmployee'), ('Bachelor', 'Bachelor'), ('Couple', 'Couple'), ('Family', 'Family'), ('Boy', 'Boy'), ('Girl', 'Girl'), ('Any', 'Any')], default='Any', max_length=20)),
                ('available_from', models.DateField()),
                ('rent', models.IntegerField()),
                ('additional_charge', models.IntegerField(blank=True, default=0)),
                ('security_money', models.IntegerField(blank=True, default=0)),
                ('one_time_charge', models.IntegerField(blank=True, default=0)),
                ('agreement_duration', models.IntegerField(blank=True, default=12, null=True)),
                ('owner_name', models.CharField(max_length=40)),
                ('owner_phone_no1', models.CharField(max_length=10)),
                ('owner_phone_no2', models.CharField(blank=True, max_length=10)),
                ('posted_by', models.CharField(choices=[('Owner', 'Owner'), ('Agent', 'Agent')], max_length=5)),
                ('posted_on', models.DateField(auto_now_add=True)),
                ('agent_name', models.CharField(blank=True, max_length=40, null=True)),
                ('age_of_property', models.IntegerField(blank=True, default=0, null=True)),
                ('locality', models.TextField(blank=True, max_length=360, null=True)),
                ('address', models.TextField(max_length=360)),
                ('city', models.TextField(max_length=360)),
                ('state', models.TextField(max_length=360)),
                ('pin', models.TextField(max_length=360)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
