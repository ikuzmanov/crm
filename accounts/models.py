from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length=254, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag (models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Food', 'Food'),
        ('Drink', 'Drink'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=50, null=True)
    price = models.FloatField()
    tags = models.ManyToManyField(Tag)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    description = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('For delivery', 'For delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return "Order #" + str(self.id)
