# Generated by Django 4.2.4 on 2023-08-14 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amyFinancesV2Backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dividend',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amyFinancesV2Backend.stock'),
        ),
        migrations.AddField(
            model_name='dividend',
            name='toAccount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amyFinancesV2Backend.account'),
        ),
        migrations.AddField(
            model_name='order',
            name='fromAccount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderFromAccount', to='amyFinancesV2Backend.account'),
        ),
        migrations.AddField(
            model_name='order',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amyFinancesV2Backend.stock'),
        ),
        migrations.AddField(
            model_name='order',
            name='toAccount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderToAccount', to='amyFinancesV2Backend.account'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amyFinancesV2Backend.category'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='fromAccount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactionFromAccount', to='amyFinancesV2Backend.account'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='toAccount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactionToAccount', to='amyFinancesV2Backend.account'),
        ),
    ]
