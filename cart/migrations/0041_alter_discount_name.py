# Generated by Django 4.2.4 on 2023-09-21 09:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0040_alter_discount_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='name',
            field=models.TextField(blank=True, default=uuid.UUID('9657db34-5022-4db7-aaf9-92b2580a8769'), verbose_name='رشته تخفیف'),
        ),
    ]
