from django.contrib import admin
from .models import Account, Transaction, Order, Stock, Dividend, Category, AmyUser

class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'iban', 'balance', 'accountType')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'transactionType', 'amount', 'date', 'recurringEnd', 'recurringPeriod', 'recurringGap')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'price', 'sum', 'cost', 'orderType')

class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'watchlisted', 'link', 'price', 'isin', 'amount')

class DividendAdmin(admin.ModelAdmin):
    list_display = ('amountBeforeTax', 'payDate', 'taxAmount', 'exDate')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

class AmyUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Dividend, DividendAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AmyUser, AmyUserAdmin)