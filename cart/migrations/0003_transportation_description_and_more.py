# Generated by Django 4.2.4 on 2023-09-10 13:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_order_transport'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportation',
            name='description',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='توضیحات'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transportation',
            name='coast',
            field=models.FloatField(verbose_name='هزینه'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='title',
            field=models.CharField(max_length=20, verbose_name='عنوان'),
        ),
    ]
