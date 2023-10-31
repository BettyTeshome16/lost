from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser

class MyCustomUsers(AbstractUser):
    is_lostuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='UserProfilePhoto', null=True, blank=True)

    Email_Field = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

class Sing(models.Model):
    name = models.CharField(max_length=200)
    fathername = models.CharField(max_length=200)
    Gfathername = models.CharField(max_length=200)
    ID = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    cofirmpassword = models.CharField(max_length=200)
    choosefile = models.FileField(upload_to='documents/')
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Contact(models.Model):
    sing = models.ForeignKey(Sing, on_delete=models.CASCADE)
    ID = models.CharField(max_length=200)
    data = models.DateField(auto_now_add=True)
    messages = models.TextField()

    def __str__(self):
        return self.messages


class Log(models.Model):
    sing = models.OneToOneField(Sing, on_delete=models.CASCADE)
    email1 = models.EmailField()
    password2 = models.CharField(max_length=200)

    def __str__(self):
        return self.email1


class LostItem1(models.Model):
    
    sic = models.IntegerField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    pd = models.TextField()
    lost_img = models.ImageField(upload_to='lost_images/')
    reward = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.sing.name


class FoundItem(models.Model):
    
    sic = models.IntegerField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    pd = models.TextField()
    image = models.ImageField(upload_to='found_items/')

    def __str__(self):
        return self.sing.name


class PostNews(models.Model):
    
    title = models.CharField(max_length=100)
    addressed_to = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    sing = models.ForeignKey(Sing, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
   
    selling_item = models.CharField(max_length=255)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_date = models.DateField()
    image1 = models.ImageField(upload_to='images/', default='default_image.jpg')
    image2 = models.ImageField(upload_to='images/', default='default_image.jpg')

    def __str__(self):
        return self.selling_item


class Bid(models.Model):
    price = models.IntegerField()

    def __str__(self):
        return f"Bid: {self.price}"  

class BiddingItem(models.Model):
    bid_id = models.CharField(max_length=20)
    product_description = models.CharField(max_length=100)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.bid_amount            