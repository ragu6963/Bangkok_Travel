# Generated by Django 3.1.7 on 2021-03-21 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_static_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='static_image',
            field=models.ImageField(default='static/img/default.png', upload_to=''),
        ),
    ]
