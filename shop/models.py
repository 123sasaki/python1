from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=250, )
    slug = models.SlugField(max_length=250, )


    def get_url(self):
        return reverse('shop:products_by_category', args=[self.slug])

    def __str__(self):
         return self.name



class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name

    
    # name = models.CharField(max_length=250)
    # slug = models.SlugField(max_length=250)
    # description = models.TextField(blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # price = models.IntegerField()
    # image = models.ImageField(upload_to='product', blank=True)
    # stock = models.IntegerField()
    # available = models.BooleanField(default=True)

