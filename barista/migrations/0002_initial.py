# Generated by Django 4.2.2 on 2023-08-02 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barista', '0001_initial'),
        ('stuff', '0001_initial'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='work_schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuff.workschedule'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_contents',
            field=models.ManyToManyField(to='menu.menuitem'),
        ),
        migrations.AddField(
            model_name='menu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem'),
        ),
    ]
