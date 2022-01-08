from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.template.defaultfilters import slugify

# Create your models here.
class Worker(models.Model):
    
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    
    slug = models.SlugField(max_length=200, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=('-create_at',)
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        to_assign = slugify(self.name)
        
        if Worker.objects.filter(slug=to_assign).exists():
            to_assign =to_assign+str(Worker.objects.all().count())
            
        self.slug= to_assign
        
        super().save(*args, **kwargs)
        

    
class Store(models.Model):
    
    title = models.CharField(max_length=200)
    worker= models.ForeignKey(to=Worker, on_delete=models.CASCADE)
    
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    
    class Meta:
        ordering=('-create_at',)
        
        
    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     to_assign = slugify(self.title)
        
    #     if Worker.objects.filter(slug=to_assign).exists():
    #         to_assign =to_assign+str(Worker.objects.all().count())
            
    #     self.slug= to_assig
        
    # super().save(*args, **kwargs)
    


    
    
    
class Visit(models.Model):
    
    date = models.DateTimeField(auto_now=True)
    store = models.ForeignKey(Store, on_delete=DO_NOTHING)
    long = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    
    def __str__(self):
        return str(self.date) + "  " + str(self.store) + "  " + str(self.lat)+ str(self.long)

