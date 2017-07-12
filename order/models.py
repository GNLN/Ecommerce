from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import uuid

class Inventory(models.Model):
    ProdId = models.CharField(max_length=100, primary_key=True, verbose_name="Product ID")
    PName = models.CharField(max_length=100, verbose_name="Product Name")
    PType = models.CharField(max_length=250, verbose_name="Product Type")
    PCat = models.CharField(max_length=100, verbose_name="Product Category")
    PPrice = models.CharField(max_length=250, verbose_name="Price")
    Prourl = models.CharField(max_length=500, verbose_name="Product Image URL")
    def __str__(self):
        return self.PName

    def get_absolute_url(self):
        return reverse('onlinepurchases:index')

    class Meta:
        db_table = "Inventory"

# class Product(models.Model):
#     productID = models.CharField(max_length=250)
#     title = models.CharField(max_length=500)
#     price = models.CharField(max_length=100)
#     picture = models.CharField(max_length=1000)
#     productQuantity = models.CharField(max_length=10)
#     description = models.CharField(max_length=500)
#
#     def __str__(self):
#         return self.title + "-" + "price=" + self.price + " Quantity=" + self.productQuantity + " Description:" + self.description

class Payment(models.Model):
    creditCardNo = models.CharField(max_length=100, primary_key=True)
    cName = models.CharField(max_length=100)
    expirationMonth = models.CharField(max_length=100)
    expirationYear = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    bAddress = models.CharField(max_length=1000)
    purchaser = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.creditCardNo

    class Meta:
        db_table = "Payment"

class Order(models.Model):
    orderID = models.CharField(max_length=250,primary_key=True, default=uuid.uuid4)
    date = models.DateField()
    oPurchaser = models.ForeignKey(User,on_delete=models.CASCADE)
    oCreditCard = models.ForeignKey(Payment,on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.orderID
    def get_absolute_url(self):
        return reverse('onlinepurchases:place-order')

    class Meta:
        db_table = "Order"

class Product(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ProdId = models.ForeignKey(Inventory, on_delete=models.SET_NULL, null=True, blank=True)
    ProBuyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    OrderQuantity = models.IntegerField(verbose_name="Quantity")
    sAddress = models.CharField(max_length=1000, verbose_name="Shipping Address")
    def __str__(self):
        return "Product: "+ self.ProdId.PName + "\n" + "Order: "+self.order.orderID

    def get_absolute_url(self):
        return reverse('onlinepurchases:thankyou')

    class Meta:
        db_table = "Product"

class Category(models.Model):
    categoryID = models.CharField(max_length=250)
    categoryName = models.CharField(max_length=250)

    class Meta:
        db_table = "Category"

class return_order(models.Model):
    ReturnId = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)
    RTimeStamp = models.DateTimeField(auto_now_add=True)
    orderid = models.ManyToManyField(Order)
    ReturnReason_choices = (
        ('Product Damaged','Product Damaged'),
        ('Item arrived too late','Item arrived too late'),
        ('Missing Parts or accesories','Missing Parts or accesories'),
        ('Product and shipping box both damaged','Product and shipping box both damaged'),
        ('Wrong item sent','Wrong item sent'),
        ('Item defective', 'Item defective'),
        ('Item no longer needed','Item no longer needed'),
    )
    ReturnReason = models.CharField(max_length=500, choices=ReturnReason_choices)
    ReturnOption_choices = (
        ('Cashback','Cashback'),
        ('Replacement','Replacement'),
        ('EKart Credits','EKart Credits'),
    )
    ReturnOptions = models.CharField(max_length=500, choices=ReturnOption_choices)
    #ReturnFeedback = models.CharField(max_length=500)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    #ProductName = models.CharField(max_length=500)
    ProductQuality_choices = (
        ('Excellent - Unopened','Excellent - Unopened'),
        ('Good - Slightly Used','Good - Slightly Used'),
        ('Poor - Broken','Poor - Broken')
    )
    ProductQuality = models.CharField(max_length=500, choices=ProductQuality_choices)

    def get_absolute_url(self):
        return reverse ('order:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.ReturnId + "-" + str(self.RTimeStamp)

    class Meta:
        db_table = "Return Order"

class Track(models.Model):
    unique_together = ("tOrder","tPurchaser","tProduct")
    tOrder = models.ForeignKey(Order,on_delete=models.CASCADE)
    tPurchaser = models.ForeignKey(User,on_delete=models.CASCADE)
    tProduct = models.ForeignKey(Inventory,on_delete=models.CASCADE)
    shipmentNo = models.BigIntegerField()

    def __str__(self):
        return self.shipmentNo

    class Meta:
        db_table = "Track Order"