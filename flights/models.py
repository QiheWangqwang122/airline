from django.db import models
# models is the class table for the database
# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3) #charfile is a build in jango element
    city = models.CharField(max_length=64)

    def __str__(self): #create string representation of the object
        return f"{self.city} ({self.code})"
    
class Flight(models.Model):
    #models.ForeignKey 是连接另一个class的方法，然后Airport是classname
    #on_delete = models.CASCADE 是删除的方法，如果删除了airport，那么flight也会被删除
    #models.CASCADE 是删除的方法，如果删除了airport，那么flight也会被删除
    #related_name 就是找到链接别的class 这个参数的所有信息
    origin = models.ForeignKey(Airport,on_delete = models.CASCADE,related_name = "departures") #charfile is a build in jango element
    destination = models.ForeignKey(Airport,on_delete = models.CASCADE,related_name = "arrivals") #charfile is a build in jango element
    duration = models.IntegerField()

    def __str__(self): #create string representation of the object
        return f"{self.id} : {self.origin} to {self.destination}"   
    
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    #every passger can have multiple flights many class is used to connect the 2 class
    #blank = True is used to make the field optional maybe didnt have any flights.
    flights = models.ManyToManyField(Flight,blank=True,related_name="passengers")
    
    def __str__(self):
        return f"{self.first} {self.last}"