from django.db import models

# Create your models here.
class Account(models.Model):
    iban = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    balance = models.DecimalField(max_digits=20, decimal_places=3)
    accountType = models.CharField(max_length=120)

    def _str_(self):
        return self.name
    
class Category(models.Model):
    type = models.IntegerField()
    name = models.CharField(max_length=120)

    def _str_(self):
        return self.name
    
class Transaction(models.Model):
    transactionType = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    date = models.CharField(max_length=120)
    recurringEnd = models.CharField(max_length=120)
    recurringPeriod = models.CharField(max_length=120)
    recurringGap = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank = True, null = True)
    fromAccount = models.ForeignKey(Account, on_delete = models.CASCADE, blank = True, null = True)
    toAccount = models.ForeignKey(Account, on_delete = models.CASCADE, blank = True, null = True)

    def _str_(self):
        return self.name
    
class Stock(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    isin = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    link = models.TextField()
    name = models.CharField(max_length=120)
    watchlisted = models.BooleanField(default=False)

    def _str_(self):
        return self.name
    
class Order(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    date = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    sum = models.DecimalField(max_digits=20, decimal_places=3)
    cost = models.DecimalField(max_digits=20, decimal_places=3)
    orderType = models.CharField(max_length=120)
    fromAccount = models.ForeignKey(Account, on_delete = models.CASCADE, blank = True, null = True)
    toAccount = models.ForeignKey(Account, on_delete = models.CASCADE, blank = True, null = True)
    fromAccount = models.ForeignKey(Account, on_delete = models.CASCADE, blank = True, null = True)
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, blank = True, null = True)

    def _str_(self):
        return self.date
    
class Dividend(models.Model):
    amountBeforeTax = models.DecimalField(max_digits=20, decimal_places=3)
    payDate = models.CharField(max_length=120)
    taxAmount = models.DecimalField(max_digits=20, decimal_places=3)
    exDate = models.CharField(max_length=120)
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, blank = True, null = True)
    toAccount = models.ForeignKey(Account, on_delete = models.CASCADE, blank = True, null = True)

    def _str_(self):
        return self.payDate
    