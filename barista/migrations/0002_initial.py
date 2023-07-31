# Generated by Django 4.2.2 on 2023-07-31 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barista', '0001_initial'),
        ('stuff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='order_contents',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem'),
        ),
        migrations.AddField(
            model_name='order',
            name='work_schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuff.workschedule'),
        ),
        migrations.AddField(
            model_name='menu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem'),
        ),
    ]
