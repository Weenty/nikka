from django.db import models
from django.contrib.auth.models import AbstractUser
from goods.models import products, package
from django.db.models import Sum

class users(AbstractUser):
    phone_number = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    basket = models.OneToOneField('basket', on_delete=models.PROTECT, default='', null=True)
<<<<<<< HEAD
    # orders = models.ForeignKey('order', on_delete=models.CASCADE, default='', null=True)
=======
    orders = models.ForeignKey('orders', on_delete=models.CASCADE, default='', null=True)
>>>>>>> fa624badf8fe4786d7c2ec3ce20398ac2f1a89aa
    def __str__(self):
        return self.username

class basket(models.Model):
    id = models.AutoField(unique=False, primary_key=True)
    products = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    ordered = models.IntegerField(default=0)

class paymant_method(models.Model):
    name = models.CharField(max_length=45)

class receiving_method(models.Model):
    name = models.CharField(max_length=45) 

class point_of_issue(models.Model):
    index = models.CharField(max_length=45)
    sity = models.CharField(max_length=45)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=45)
    
# class order(models.Model):
#     id_basket = models.ForeignKey('basket', on_delete=models.CASCADE)
#     final_cost = models.DecimalField(max_digits=7, decimal_places=0)
#     order_list = models.ManyToManyField(products, through='order_list')
#     comment = models.TextField()
#     payment_method = models.OneToOneField(paymant_method, on_delete=models.PROTECT)
#     receiving_method = models.OneToOneField(receiving_method, on_delete=models.PROTECT)
#     point_of_issue = models.OneToOneField(point_of_issue, on_delete=models.PROTECT)

<<<<<<< HEAD
# class orders_list(models.Model):
#     cost = models.DecimalField(max_digits=7, decimal_places=0)
#     order = models.ForeignKey(order, on_delete=models.PROTECT)
#     product = models.ForeignKey(products, on_delete=models.PROTECT)
=======
class order(models.Model):
    id_basket = models.ForeignKey('basket', on_delete=models.CASCADE)
    final_cost = models.DecimalField(max_digits=7, decimal_places=0, null=True)
    order_list = models.ManyToManyField(products, through='order_list')
    comment = models.TextField()
    payment_method = models.OneToOneField(paymant_method, on_delete=models.PROTECT)
    receiving_method = models.OneToOneField(receiving_method, on_delete=models.PROTECT)
    point_of_issue = models.OneToOneField(point_of_issue, on_delete=models.PROTECT)
   
    # def sum_cost(self):
    #    return package.objects.aggregate(Sum('cost'))
    
    def calculate_final_cost(self):
        return self.final_cost.forcehash(self.sum_cost())
    
    def save(self, *args, **kwargs):
        self.final_cost = self.calculate_final_cost()
        super(order, self).save(*args, **kwargs)

class order_list(models.Model):
    cost = models.DecimalField(max_digits=7, decimal_places=0)
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    
>>>>>>> fa624badf8fe4786d7c2ec3ce20398ac2f1a89aa
