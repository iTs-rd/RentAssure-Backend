# Generated by Django 3.1.7 on 2021-05-01 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(choices=[('flat', 'Flat'), ('room', 'Room'), ('house', 'House')], max_length=5)),
                ('title', models.CharField(max_length=32)),
                ('img1', models.ImageField(blank=True, default='images/house/default.png', upload_to='images/house/')),
                ('img2', models.ImageField(blank=True, default='images/house/default.png', upload_to='images/house/')),
                ('img3', models.ImageField(blank=True, default='images/house/default.png', upload_to='images/house/')),
                ('img4', models.ImageField(blank=True, default='images/house/default.png', upload_to='images/house/')),
                ('description', models.TextField(max_length=360)),
                ('bedroom', models.IntegerField(blank=True, null=True)),
                ('bathroom', models.IntegerField(blank=True, null=True)),
                ('balconies', models.IntegerField(blank=True, null=True)),
                ('Kitchen', models.IntegerField(blank=True, null=True)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('furnished', models.CharField(choices=[('unfurnished', 'Unfurnished'), ('semifurnished', 'Semifurnished'), ('fullyfurnished', 'Fullyfurnished')], default='unfurnished', max_length=20)),
                ('available_for', models.CharField(blank=True, choices=[('bachelor', 'bachelor'), ('student', 'student'), ('couple', 'couple'), ('family', 'family'), ('boys', 'boys'), ('girls', 'girls'), ('any', 'any')], default='any', max_length=10)),
                ('available_from', models.DateField()),
                ('rent', models.IntegerField()),
                ('additional_charge', models.IntegerField(blank=True, default=0)),
                ('security_money', models.IntegerField(blank=True, default=0)),
                ('one_time_charge', models.IntegerField(blank=True, default=0)),
                ('agreement_duration', models.IntegerField(blank=True, null=True)),
                ('owner_name', models.CharField(max_length=40)),
                ('owner_phone_no1', models.CharField(max_length=10)),
                ('owner_phone_no2', models.CharField(blank=True, max_length=10)),
                ('locality', models.TextField(blank=True, max_length=360, null=True)),
                ('address', models.TextField(max_length=360)),
                ('city', models.TextField(max_length=360)),
                ('state', models.TextField(max_length=360)),
                ('pin', models.TextField(max_length=360)),
                ('parking', models.BooleanField(default=False)),
                ('lift', models.BooleanField(default=False)),
                ('swimming_pool', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
                ('gas_pipeline', models.BooleanField(default=False)),
                ('Power_backup', models.BooleanField(default=False)),
                ('electricity_charge', models.IntegerField(blank=True, default=0)),
                ('electricity_supply', models.BooleanField(default=True)),
                ('water_charge', models.IntegerField(blank=True, default=0)),
                ('water_supply', models.BooleanField(default=True)),
                ('posted_by', models.CharField(choices=[('owner', 'Owner'), ('agent', 'Agent')], max_length=5)),
                ('posted_on', models.DateField(auto_now_add=True)),
                ('agent_name', models.CharField(blank=True, max_length=40, null=True)),
                ('age_of_property', models.IntegerField(blank=True, null=True)),
                ('fridge', models.BooleanField(default=False)),
                ('washing_machine', models.BooleanField(default=False)),
                ('cleaning', models.CharField(blank=True, choices=[('no', 'No'), ('daily', 'Daily'), ('weekly', 'Weekly')], default='no', max_length=6)),
                ('CCTV', models.BooleanField(default=False)),
                ('guard', models.BooleanField(default=False)),
                ('medical', models.BooleanField(default=False)),
                ('fire_alarme', models.BooleanField(default=False)),
                ('water_purifier', models.BooleanField(default=False)),
            ],
        ),
    ]
