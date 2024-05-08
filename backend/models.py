from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
    UserID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=100)
    RegistrationDate = models.DateTimeField(auto_now_add=True)


class Customers(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    registration_id = models.IntegerField(null=True)

class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Registration = models.ForeignKey(Registration, on_delete=models.CASCADE)


class Products(models.Model):
    ProductID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Size = models.CharField(max_length=20)
    Category = models.CharField(max_length=100,
                                choices=[('Women Clothing', 'Women Clothing'), ('Men Clothing', 'Men Clothing')])
    Available = models.IntegerField(default=0)  # Added Available field


class ShoppingCart(models.Model):
    CartID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Size = models.CharField(max_length=20)


class Orders(models.Model):
    OrderID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    OrderDate = models.DateTimeField(auto_now_add=True)
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    Status = models.CharField(max_length=100,
                              choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Shipped', 'Shipped'),
                                       ('Delivered', 'Delivered')])


class OrderDetails(models.Model):
    OrderDetailID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Size = models.CharField(max_length=20)
    Price = models.DecimalField(max_digits=10, decimal_places=2)


class Delivery(models.Model):
    DeliveryID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    DeliveryDate = models.DateTimeField()
    ShippingAddress = models.CharField(max_length=255)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    ZipCode = models.CharField(max_length=20)
    UserID = models.ForeignKey(Registration, on_delete=models.CASCADE)
