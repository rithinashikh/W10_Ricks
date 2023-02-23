# Generated by Django 4.1.4 on 2023-02-13 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phase', '0009_address_selected'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('ordertype', models.CharField(choices=[('Cash on delivery', 'Cash on delivery'), ('UPI', 'UPI'), ('Razorpay', 'Razorpay')], default='Cash on delivery', max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=50)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phase.product')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phase.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phase.userdetail')),
            ],
        ),
    ]