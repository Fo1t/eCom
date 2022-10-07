import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Manufacturer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    site = models.URLField(max_length=200)

    def __str__(self):
        return self.title+" ("+self.site+")"


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=False)
    price = models.FloatField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    AVAILABILITY_STATUS = (
        ('i', 'In Stock'),
        ('s', 'Available at short notice'),
        ('o', 'Ordered on demand'),
        ('n', 'Not available'),
    )
    availability = models.CharField(max_length=1, choices=AVAILABILITY_STATUS, blank=True, default='n')
    weight = models.FloatField(null=True)
    sale = models.FloatField(null=True, default=0.0)
    discounted_price = models.FloatField(null=True, default=0.0)
    #title_image = models.ForeignKey('TitleImage', on_delete=models.SET_NULL, related_name='titlei', null=True)

    def __str__(self):
        return self.title+" |   "+self.category.__str__()+" |   "+self.manufacturer.__str__()

    class Meta:
        ordering = ['title']

    def availability_verbose(self):
        return dict(Product.AVAILABILITY_STATUS)[self.availability]

class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    file = models.ImageField(upload_to='img', null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, related_name="prodimage")
    #title_status = models.BooleanField(default=False)

# class TitleImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, related_name="titleprod")
#     image = models.ForeignKey(Image, on_delete=models.CASCADE, null=False, related_name="titleimage")
#
# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     phone_num = models.CharField(max_length=11, null=False)
#
#     def __str__(self):
#         return self.user.__str__()

# class Order(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     client = models.ForeignKey("Profile", on_delete=models.CASCADE, null=False)
#     sum_price = models.FloatField(null=False)
#     ORDER_STATUS = (
#         ('w', 'Waiting for payment'),
#         ('i', 'In processing'),
#         ('p', 'Package'),
#         ('t', 'Transmitted to delivery service'),
#         ('r', 'Return'),
#         ('c', 'Canceled by'),
#     )
#     status = models.CharField(max_length=1, choices=ORDER_STATUS, blank=True, default='w')
#     created_date = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.id+"    |   "+self.status+"    |   "+self.created_date
#
#     def status_verbose(self):
#         return dict(Order.ORDER_STATUS)[self.status]
#
# class Delivery(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     price = models.FloatField(null=False, default=0.0)
#     address = models.CharField(max_length=255, null=False)
#     comments = models.CharField(max_length=255)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
#
#     def __str__(self):
#         return self.id
#
# class OrderInstance(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
