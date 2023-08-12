from rest_framework import serializers
from .models import Account, Transaction, Order, Stock, Dividend, Category

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name', 'iban', 'balance', 'accountType')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'name', 'transactionType', 'amount', 'date', 'recurringEnd', 'recurringPeriod', 'recurringGap')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'amount', 'date', 'price', 'sum', 'cost', 'orderType')

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'name', 'watchlisted', 'link', 'price', 'isin', 'amount')

class DividendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dividend
        fields = ('id', 'amountBeforeTax', 'payDate', 'taxAmount', 'exDate')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'type')
