# Generated by Django 2.0 on 2017-12-31 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(upload_to='static/upload/other'),
        ),
        migrations.AlterField(
            model_name='noteuser',
            name='photo',
            field=models.ImageField(default='static/upload/head_photo/default.jpg', upload_to='static/upload/head_photo'),
        ),
    ]
