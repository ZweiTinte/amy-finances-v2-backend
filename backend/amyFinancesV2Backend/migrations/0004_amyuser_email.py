# Generated by Django 4.2.4 on 2023-08-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amyFinancesV2Backend', '0003_amyuser_account_user_category_user_dividend_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='amyuser',
            name='email',
            field=models.CharField(default='', max_length=120),
        ),
    ]
