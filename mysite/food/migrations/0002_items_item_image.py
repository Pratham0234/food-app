# Generated by Django 2.2.12 on 2023-02-24 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_image',
            field=models.CharField(default='https://www.everestkitchenpa.com/assets/images/menuShortCuts/momoShortCut.jpg', max_length=500),
            preserve_default=False,
        ),
    ]
