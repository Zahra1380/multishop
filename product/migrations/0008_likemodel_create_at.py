# Generated by Django 4.2.4 on 2023-09-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_likemodel_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='likemodel',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]