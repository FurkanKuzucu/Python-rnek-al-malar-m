from django.db import models

class book(models.Model):
    title=models.CharField(max_length=50,verbose_name="İsim")
    typ=models.CharField(max_length=50,verbose_name="Yazarı")
    categr=models.CharField(max_length=50,verbose_name="Kategori")
    
    def __str__(self):
        return self.title
