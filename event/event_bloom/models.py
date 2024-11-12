from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Story(models.Model):
    image=models.ImageField(upload_to='media/image',blank=True,null=True)
    name=models.CharField(max_length=50)
    outline =  models.TextField()
    desc = models.TextField()
    def __str__(self):
        return self.name


class Service(models.Model):
    image=models.ImageField(upload_to='media/image',blank=True,null=True)
    name=models.CharField(max_length=50)
    outline = models.TextField()
    desc = models.TextField()
    advance_amt=models.IntegerField(max_length=30)
    def __str__(self):
        return self.name

class Inform(models.Model):
    name=models.CharField(max_length=50)
    number=models.IntegerField(max_length=10)
    email=models.TextField(max_length=50)
    message=models.TextField(max_length=200)
    def __str__(self):
        return self.name

class Wedding(models.Model):
    image = models.ImageField(upload_to='media/image', blank=True, null=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Weddingdetail(models.Model):
    name=models.CharField(max_length=50)
    number=models.IntegerField(max_length=10)
    email=models.TextField(max_length=50)
    message=models.TextField(max_length=200)
    def __str__(self):
        return self.name

class Booking(models.Model):
    cus_name=models.CharField(max_length=55)
    cus_ph=models.CharField(max_length=12)
    name=models.ForeignKey(Service,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)


class Event(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advance_amt=models.IntegerField(max_length=30)
    data_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.service.name



class Book_event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Service, on_delete=models.CASCADE)
    no_of_events = models.IntegerField()
    phone = models.CharField(max_length=30)


    ordered_date = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=100, blank=True)
    payment_status = models.CharField(default="pending", max_length=30)

    def __str__(self):
        return self.user.username

class Payment(models.Model):
    name=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    book_id=models.CharField(max_length=100,blank=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return self.name
