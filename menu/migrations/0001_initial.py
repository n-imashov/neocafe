# Generated by Django 4.2.2 on 2023-08-01 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/menucategory')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/menuitem/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menucategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('weight', models.IntegerField(default=0)),
                ('arrival_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/menuitem/')),
                ('menuitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='menu.menuitem')),
            ],
        ),
        migrations.AddField(
            model_name='menuitem',
            name='products',
            field=models.ManyToManyField(to='menu.product'),
        ),
    ]
