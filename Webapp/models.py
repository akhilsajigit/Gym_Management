from django.db import models


# Create your models here.
class ContactDB(models.Model):
    fd_Name = models.CharField(max_length=100, null=True, blank=True)
    fd_Email = models.EmailField(max_length=100, null=True, blank=True)
    fd_Subject = models.CharField(max_length=100, null=True, blank=True)
    fd_Message = models.CharField(max_length=100, null=True, blank=True)


class RegisterDB(models.Model):
    User_Name = models.CharField(max_length=100, null=True, blank=True)
    User_Email = models.EmailField(max_length=100, null=True, blank=True)
    User_Password = models.CharField(max_length=100, null=True, blank=True)


class CartDB(models.Model):
    Ct_User = models.CharField(max_length=100, null=True, blank=True)
    Ct_Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Ct_Product_Price = models.IntegerField(null=True, blank=True)
    Ct_Quantity = models.IntegerField(null=True, blank=True)
    Ct_Total_price = models.IntegerField(null=True, blank=True)
    Ct_Image = models.ImageField(upload_to="Cart Images", null=True, blank=True)


class OrderDB(models.Model):
    Customer_Name = models.CharField(max_length=100, null=True, blank=True)
    Customer_State = models.CharField(max_length=100, null=True, blank=True)
    Customer_Address = models.CharField(max_length=100, null=True, blank=True)
    Customer_City = models.CharField(max_length=100, null=True, blank=True)
    Customer_Mobile = models.IntegerField(null=True, blank=True)
    Customer_Email = models.EmailField(max_length=100, null=True, blank=True)
    Order_Price = models.IntegerField(null=True, blank=True)


class TrainerRequest(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=100, null=True, blank=True)
    certification = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="Trainer requests", null=True, blank=True)
    approved = models.BooleanField(default=False)


class Gym_MemberDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Joining_Date = models.DateField(max_length=100, null=True, blank=True)
    Select_Trainer = models.CharField(max_length=100, null=True, blank=True)
    Select_Course = models.CharField(max_length=100, null=True, blank=True)
    Select_Plan = models.CharField(max_length=100, null=True, blank=True)
    Amount = models.IntegerField(null=True, blank=True)
    Gender = models.CharField(max_length=100, null=True, blank=True)
    Height = models.CharField(max_length=100, null=True, blank=True)
    Weight = models.CharField(max_length=100, null=True, blank=True)
    Medical = models.CharField(max_length=100, null=True, blank=True)
    Emergency_Name = models.CharField(max_length=100, null=True, blank=True)
    Emergency_Phone = models.IntegerField(null=True, blank=True)
    User_Session = models.CharField(max_length=100, null=True, blank=True)
    Profile_Image = models.ImageField(upload_to="Gym Members", null=True, blank=True)
    Payment_approved = models.BooleanField(default=False)
