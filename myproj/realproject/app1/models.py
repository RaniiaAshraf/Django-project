from django.db import models

# Create your models here.
class Donation(models.Model):
    id=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50 , default= "Donation" , verbose_name="Name     " )
    Targetprice = models.DecimalField(max_digits=7, decimal_places=2 , verbose_name="Price    ")
    image = models.ImageField(upload_to='media/%y/%m/%d' , verbose_name="Image     ")
    Description = models.TextField(null = True , blank= True , verbose_name="Description     ")
    def __str__(self):
        return self.Name
    
    
