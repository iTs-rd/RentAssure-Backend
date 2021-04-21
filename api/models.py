from django.db import models
from PIL import Image

# test model to upload images

# class Image(models.Model):
#     img1=models.ImageField(upload_to='images/', null=True, verbose_name="")
#     img2=models.ImageField(upload_to='images/', null=True, verbose_name="")


class House(models.Model):
    title = models.CharField(max_length=32)

    img1=models.ImageField(upload_to='images/house/', null=True, verbose_name="")
    img2=models.ImageField(upload_to='images/house/', null=True, verbose_name="")
    img3=models.ImageField(upload_to='images/house/', null=True, verbose_name="")
    img4=models.ImageField(upload_to='images/house/', null=True, verbose_name="")

    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    balconies = models.IntegerField()
    area = models.IntegerField()        # sq. ft.
    furnished = models.BooleanField()
    price = models.IntegerField()
    additional_charge = models.IntegerField()
    security_money = models.IntegerField()
    locality = models.TextField(max_length=360)
    address = models.TextField(max_length=360)
    city = models.TextField(max_length=360)
    state= models.TextField(max_length=360)
    pin = models.TextField(max_length=360)
    phone = models.TextField(max_length=10)
    # Facing = models.TextField()
    available = models.TextField(max_length=360)       #  Ex. family
    parking = models.BooleanField()
    agreement_duration = models.IntegerField()     # no of months
    description = models.TextField(max_length=360)

    def save(self, ** kwargs):
        super().save()
        image1=Image.open(self.img1.path)
        new_img1= image1.resize((350,300))
        print(image1.size)
        print(new_img1.size)
        new_img1.save(self.img1.path)

        image2=Image.open(self.img2.path)
        new_img2= image2.resize((350,300))
        new_img2.save(self.img2.path)

        image3=Image.open(self.img3.path)
        new_img3= image3.resize((350,300))
        new_img3.save(self.img3.path)

        image4=Image.open(self.img4.path)
        new_img4= image4.resize((350,300))
        new_img4.save(self.img4.path)



class Room(models.Model):
    title = models.CharField(max_length=32)

    img1=models.ImageField(upload_to='images/room/', null=True, verbose_name="")
    img2=models.ImageField(upload_to='images/room/', null=True, verbose_name="")
    img3=models.ImageField(upload_to='images/room/', null=True, verbose_name="")
    img4=models.ImageField(upload_to='images/room/', null=True, verbose_name="")

    bathroom = models.IntegerField()
    balconies = models.IntegerField()
    area = models.IntegerField()
    furnished = models.BooleanField()
    ac = models.BooleanField()
    water = models.IntegerField()
    electricity = models.IntegerField()
    price = models.IntegerField()
    additional_charge = models.IntegerField()
    security_money = models.IntegerField()
    locality = models.TextField(max_length=360)
    address = models.TextField(max_length=360)
    city = models.TextField(max_length=360)
    state= models.TextField(max_length=360)
    pin = models.TextField(max_length=360)
    phone = models.TextField(max_length=10)
    # Facing = models.TextField()
    available = models.TextField(max_length=360)       #  Ex. family
    parking = models.BooleanField()
    agreement_duration = models.IntegerField()     # no of months
    description = models.TextField(max_length=360)


    def save(self, ** kwargs):
        super().save()
        image1=Image.open(self.img1.path)
        new_img1= image1.resize((350,300))
        print(image1.size)
        print(new_img1.size)
        new_img1.save(self.img1.path)

        image2=Image.open(self.img2.path)
        new_img2= image2.resize((350,300))
        new_img2.save(self.img2.path)

        image3=Image.open(self.img3.path)
        new_img3= image3.resize((350,300))
        new_img3.save(self.img3.path)

        image4=Image.open(self.img4.path)
        new_img4= image4.resize((350,300))
        new_img4.save(self.img4.path)



class Flat(models.Model):
    title = models.CharField(max_length=32)

    img1=models.ImageField(upload_to='images/flat/', null=True, verbose_name="")
    img2=models.ImageField(upload_to='images/flat/', null=True, verbose_name="")
    img3=models.ImageField(upload_to='images/flat/', null=True, verbose_name="")
    img4=models.ImageField(upload_to='images/flat/', null=True, verbose_name="")

    floor=models.IntegerField()
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    balconies = models.IntegerField()
    area = models.IntegerField()
    furnished = models.BooleanField()
    price = models.IntegerField()
    additional_charge = models.IntegerField()
    security_money = models.IntegerField()
    locality = models.TextField(max_length=360)
    address = models.TextField(max_length=360)
    city = models.TextField(max_length=360)
    state= models.TextField(max_length=360)
    pin = models.TextField(max_length=360)
    phone = models.TextField(max_length=10)
    # Facing = models.TextField()
    available = models.TextField(max_length=360)       #  Ex. family
    parking = models.BooleanField()
    agreement_duration = models.IntegerField()     # no of months
    description = models.TextField(max_length=360)


    def save(self, ** kwargs):
        super().save()
        image1=Image.open(self.img1.path)
        new_img1= image1.resize((350,300))
        print(image1.size)
        print(new_img1.size)
        new_img1.save(self.img1.path)

        image2=Image.open(self.img2.path)
        new_img2= image2.resize((350,300))
        new_img2.save(self.img2.path)

        image3=Image.open(self.img3.path)
        new_img3= image3.resize((350,300))
        new_img3.save(self.img3.path)

        image4=Image.open(self.img4.path)
        new_img4= image4.resize((350,300))
        new_img4.save(self.img4.path)




