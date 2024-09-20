from django.db import models


class CategoryDB(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    Category_Description = models.CharField(max_length=100, null=True, blank=True)
    Category_Image = models.ImageField(upload_to="Category Images", null=True, blank=True)


class Sub_CategoryDB(models.Model):
    Category_St = models.CharField(max_length=100, null=True, blank=True)
    Sub_Category_Name = models.CharField(max_length=100, null=True, blank=True)
    Sub_Category_Description = models.CharField(max_length=100, null=True, blank=True)
    Sub_Category_Image = models.ImageField(upload_to="Sub-Category Images", null=True, blank=True)


class ProductDB(models.Model):
    Cat_Select = models.CharField(max_length=100, null=True, blank=True)
    Sub_Cat_Select = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Product_About = models.CharField(max_length=100, null=True, blank=True)
    Product_Price = models.IntegerField(null=True, blank=True)
    Product_Description = models.CharField(max_length=100, null=True, blank=True)
    Product_Image = models.ImageField(upload_to="Product Images", null=True, blank=True)


class Workout_Cat_DB(models.Model):
    Workout_Cat = models.CharField(max_length=100, null=True, blank=True)
    Workout_desc = models.CharField(max_length=100, null=True, blank=True)
    Workout_Cat_Image = models.ImageField(upload_to="Workout_Category Images", null=True, blank=True)


class Daily_Workout_Cat_DB(models.Model):
    Daily_Workout_Cat = models.CharField(max_length=100, null=True, blank=True)
    Daily_Workout_desc = models.CharField(max_length=100, null=True, blank=True)
    Daily_Workout_Cat_Image = models.ImageField(upload_to="Daily_Workout_Category Images", null=True, blank=True)


class Single_WorkoutsDB(models.Model):
    Cat_Name = models.CharField(max_length=100, null=True, blank=True)
    Workout_Name = models.CharField(max_length=100, null=True, blank=True)
    Sets = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Workout_Image = models.ImageField(upload_to="Workout Images/", null=True, blank=True)
    Video = models.FileField(upload_to='Videos/')


class DayDB(models.Model):
    Day_Cat = models.CharField(max_length=100, null=True, blank=True)
    Day = models.CharField(max_length=100, null=True, blank=True)


class Daily_WorkoutsDB(models.Model):
    Day_Cat = models.CharField(max_length=100, null=True, blank=True)
    Workout_Name = models.CharField(max_length=100, null=True, blank=True)
    Sets = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Workout_Image = models.ImageField(upload_to="Workout Images/", null=True, blank=True)
    Video = models.FileField(upload_to='Videos/')


class Membership_PlansDB(models.Model):
    Plan_Name = models.CharField(max_length=100, null=True, blank=True)
    Plan_Price = models.IntegerField(null=True, blank=True)
    Plan_Description = models.CharField(max_length=100, null=True, blank=True)
