from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from PIL import Image
from django.utils.deconstruct import deconstructible
from django.core.validators import MinLengthValidator, int_list_validator, EmailValidator


class BaseUserManager(models.Manager):

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by lowercasing the domain part of it.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = email_name + '@' + domain_part.lower()
        return email

    def make_random_password(self, length=10,
                             allowed_chars='abcdefghjkmnpqrstuvwxyz'
                                           'ABCDEFGHJKLMNPQRSTUVWXYZ'
                                           '23456789'):
        """
        Generate a random password with the given length and given
        allowed_chars. The default value of allowed_chars does not have "I" or
        "O" or letters and digits that look similar -- just to avoid confusion.
        """
        return get_random_string(length, allowed_chars)

    def get_by_natural_key(self, email):
        return self.get(**{self.model.USERNAME_FIELD: email})


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, firstname, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, firstname, password, **other_fields)

    def create_user(self, email, username, firstname, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))
        other_fields.setdefault('is_active', True)

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          firstname=firstname, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    firstname = models.CharField(max_length=150, blank=False)
    lastname = models.CharField(
        max_length=32, blank=True, null=True, default="Not Available")
    mobile = models.CharField(
        max_length=10, blank=True, null=True, default="Not Available")
    dp = models.ImageField(upload_to='images/dp/',
                           default='images/dp/default.jpg', blank=True)
    age = models.CharField(max_length=3,  blank=True,
                           null=True, default="Not Available")

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, blank=True, default="Not available")

    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    EMAIL_FIELD = 'email'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname']

    def __str__(self):
        return self.username

    def save(self, ** kwargs):
        super().save()
        img_size = (200, 200)
        image1 = Image.open(self.dp.path)
        new_img1 = image1.resize(img_size)
        new_img1.save(self.dp.path)


class DataModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=False)
    PROPERTY_TYPE_CHOICE = [
        ('Flat', 'Flat'),
        ('Room', 'Room'),
        ('House', 'House')
    ]
    property_type = models.CharField(
        max_length=5, choices=PROPERTY_TYPE_CHOICE, blank=False)

    title = models.CharField(max_length=32, blank=False)
    img1 = models.ImageField(upload_to='images/product/',
                             default='images/default/1.jpg', blank=True)
    img2 = models.ImageField(upload_to='images/product/',
                             default='images/default/2.jpg', blank=True)
    img3 = models.ImageField(upload_to='images/product/',
                             default='images/default/3.jpg', blank=True)
    img4 = models.ImageField(upload_to='images/product/',
                             default='images/default/4.jpg', blank=True)

    description = models.TextField(max_length=360, blank=False)

    BHK_CHOICES = [
        ('1RK/1BHK', '1RK/1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
        ('4BHK', '4BHK'),
        ('5+BHK', '5+BHK'),
        ('No', 'No'),
    ]
    bhk = models.CharField(
        max_length=10, choices=BHK_CHOICES, blank=True, null=True)

    bedroom = models.IntegerField(null=True, blank=True, default=0)
    bathroom = models.IntegerField(null=True, blank=True, default=0)
    balconies = models.IntegerField(null=True, blank=True, default=0)
    Kitchen = models.IntegerField(null=True, blank=True, default=0)
    area = models.IntegerField(null=True, blank=True, default=0)

    parking = models.BooleanField(default=False)
    lift = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    gas_pipeline = models.BooleanField(default=False)
    electricity_charge = models.IntegerField(default=0, blank=True)
    electricity_supply = models.BooleanField(default=True)
    Power_backup = models.BooleanField(default=False)
    water_charge = models.IntegerField(default=0, blank=True)
    water_supply = models.BooleanField(default=True)
    water_purifier = models.BooleanField(default=False)
    fridge = models.BooleanField(default=False)
    washing_machine = models.BooleanField(default=False)
    CCTV = models.BooleanField(default=False)
    guard = models.BooleanField(default=False)
    medical = models.BooleanField(default=False)
    fire_alarme = models.BooleanField(default=False)

    CLEANING_CHOICES = [
        ('No', 'No'),
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly')
    ]
    cleaning = models.CharField(
        max_length=6, choices=CLEANING_CHOICES, blank=True, default='No')

    FURNISHED_CHOICES = [
        ('Unfurnished', 'Unfurnished'),
        ('SemiFurnished', 'Semifurnished'),
        ('FullyFurnished', 'Fullyfurnished')
    ]
    furnished = models.CharField(
        max_length=20, choices=FURNISHED_CHOICES, blank=False, default='Unfurnished')

    AVAILABLE_FOR_CHOICES = [
        ('Student', 'Student'),
        ('GovernmentEmployee', 'GovernmentEmployee'),
        ('Bachelor', 'Bachelor'),
        ('Couple', 'Couple'),
        ('Family', 'Family'),
        ('Boy', 'Boy'),
        ('Girl', 'Girl'),
        ('Any', 'Any')
    ]
    available_for = models.CharField(
        max_length=20, choices=AVAILABLE_FOR_CHOICES, default='Any', blank=True)

    available_from = models.DateField(blank=True)
    rent = models.IntegerField(blank=False)
    additional_charge = models.IntegerField(default=0, blank=True)
    security_money = models.IntegerField(default=0, blank=True)
    one_time_charge = models.IntegerField(default=0, blank=True)
    agreement_duration = models.IntegerField(null=True, blank=True, default=12)

    owner_name = models.CharField(max_length=40, blank=False)
    owner_phone_no1 = models.CharField(max_length=10, blank=False)
    owner_phone_no2 = models.CharField(max_length=10, blank=True)

    POSTED_BY_CHOICES = [
        ('Owner', 'Owner'),
        ('Agent', 'Agent')
    ]
    posted_by = models.CharField(max_length=5, choices=POSTED_BY_CHOICES)

    posted_on = models.DateField(auto_now_add=True)
    agent_name = models.CharField(max_length=40, blank=True, null=True)
    age_of_property = models.IntegerField(blank=True, null=True, default=0)
    locality = models.TextField(max_length=360, null=True, blank=True)
    address = models.TextField(max_length=360, blank=False)
    city = models.TextField(max_length=360, blank=False)
    state = models.TextField(max_length=360, blank=False)
    pin = models.TextField(max_length=360, blank=False)

    def __str__(self):
        return self.user.username + " itemID: "+str(self.id)

    # to change image size

    def save(self, ** kwargs):
        super().save()
        img_size = (350, 300)

        image1 = Image.open(self.img1.path)
        image2 = Image.open(self.img2.path)
        image3 = Image.open(self.img3.path)
        image4 = Image.open(self.img4.path)

        new_img1 = image1.resize(img_size)
        new_img2 = image2.resize(img_size)
        new_img3 = image3.resize(img_size)
        new_img4 = image4.resize(img_size)

        new_img1.save(self.img1.path)
        new_img2.save(self.img2.path)
        new_img3.save(self.img3.path)
        new_img4.save(self.img4.path)


@ deconstructible
class WhitelistEmailValidator(EmailValidator):

    def validate_domain_part(self, domain_part):
        return False

    def __eq__(self, other):
        return isinstance(other, WhitelistEmailValidator) and super().__eq__(other)


class ContactData(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=60, validators=[WhitelistEmailValidator(
        whitelist=['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'])])
    mobile = models.CharField(max_length=10, verbose_name='Phone Number', validators=[int_list_validator(sep=' '),
                                                                                      MinLengthValidator(10)])
    detail = models.TextField(max_length=300, blank=False)
# 00747686 ludo code
