from django.db import models
from PIL import Image


###   compulsory field in post method (other than these field all are optional)

# title
# address
# city
# state
# pin
# description
# property_type
# available_from
# Furnished
# rent
# owner_name
# owner_phone_no1
# posted_by


class Data(models.Model):
    PROPERTY_TYPE_CHOICE= [
        ('flat','Flat'),
        ('room','Room'),
        ('house','House')
    ]
    property_type=models.CharField(max_length=5,choices=PROPERTY_TYPE_CHOICE,blank=False)

    title = models.CharField(max_length=32,blank=False)
    img1=models.ImageField(upload_to='images/data/', default='images/data/default.png',verbose_name="")
    img2=models.ImageField(upload_to='images/data/', default='images/data/default.png',verbose_name="")
    img3=models.ImageField(upload_to='images/data/', default='images/data/default.png',verbose_name="")
    img4=models.ImageField(upload_to='images/data/', default='images/data/default.png',verbose_name="")


    description = models.TextField(max_length=360,blank=False)
    bedroom = models.IntegerField(null=True,blank=True)
    bathroom = models.IntegerField(null=True,blank=True)
    balconies = models.IntegerField(null=True,blank=True)
    Kitchen = models.IntegerField(null=True,blank=True)
    area = models.IntegerField(null=True,blank=True)

    parking = models.BooleanField(default=False)
    lift=models.BooleanField(default=False)
    swimming_pool=models.BooleanField(default=False)
    gym=models.BooleanField(default=False)
    gas_pipeline=models.BooleanField(default=False)
    electricity_charge=models.IntegerField(default=0,blank=True)
    electricity_supply=models.BooleanField(default=True)
    Power_backup=models.BooleanField(default=False)
    water_charge=models.IntegerField(default=0,blank=True)
    water_supply=models.BooleanField(default=True)
    water_purifier=models.BooleanField(default=False)
    fridge=models.BooleanField(default=False)
    washing_machine=models.BooleanField(default=False)
    CCTV=models.BooleanField(default=False)
    guard=models.BooleanField(default=False)
    medical=models.BooleanField(default=False)
    fire_alarme=models.BooleanField(default=False)

    CLEANING_CHOICES=[
        ('no','No'),
        ('daily','Daily'),
        ('weekly','Weekly')
    ]
    cleaning=models.CharField(max_length=6,choices=CLEANING_CHOICES,blank=True,default='no')

    FURNISHED_CHOICES=[
        ('unfurnished','Unfurnished'),
        ('semifurnished','Semifurnished'),
        ('fullyfurnished','Fullyfurnished')
    ]
    furnished = models.CharField(max_length=20,choices=FURNISHED_CHOICES,blank=False,default='unfurnished')


    AVAILABLE_FOR_CHOICES=[
        ('bachelor','bachelor'),
        ('student','student'),
        ('couple','couple'),
        ('family','family'),
        ('boys','boys'),
        ('girls','girls'),
        ('any','any')
    ]
    available_for = models.CharField(max_length=10,choices=AVAILABLE_FOR_CHOICES,default='any',blank=True)

    available_from=models.DateField(blank=False)
    rent = models.IntegerField(blank=False)
    additional_charge = models.IntegerField(default=0,blank=True)
    security_money = models.IntegerField(default=0,blank=True)
    one_time_charge =models.IntegerField(default=0,blank=True)
    agreement_duration = models.IntegerField(null=True,blank=True)


    owner_name=models.CharField(max_length=40,blank=False)
    owner_phone_no1 = models.CharField(max_length=10,blank=False)
    owner_phone_no2 = models.CharField(max_length=10,blank=True)

    POSTED_BY_CHOICES=[
        ('owner','Owner'),
        ('agent','Agent')
    ]
    posted_by=models.CharField(max_length=5,choices=POSTED_BY_CHOICES)

    posted_on=models.DateField(auto_now_add=True)
    agent_name=models.CharField(max_length=40,blank=True,null=True)
    age_of_property=models.IntegerField(blank=True,null=True)
    locality = models.TextField(max_length=360,null=True,blank=True)
    address = models.TextField(max_length=360,blank=False)
    city = models.TextField(max_length=360,blank=False)
    state= models.TextField(max_length=360,blank=False)
    pin = models.TextField(max_length=360,blank=False)



    # to change image size
    
    def save(self, ** kwargs):
        super().save()
        img_size=(350,300)

        image1=Image.open(self.img1.path)
        image2=Image.open(self.img2.path)
        image3=Image.open(self.img3.path)
        image4=Image.open(self.img4.path)

        new_img1= image1.resize(img_size)
        new_img2= image2.resize(img_size)
        new_img3= image3.resize(img_size)
        new_img4= image4.resize(img_size)

        new_img1.save(self.img1.path)
        new_img2.save(self.img2.path)
        new_img3.save(self.img3.path)
        new_img4.save(self.img4.path)

