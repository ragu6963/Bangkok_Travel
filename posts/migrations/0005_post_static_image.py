# Generated by Django 3.1.7 on 2021-03-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210321_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='static_image',
            field=models.ImageField(default='img/default.png', upload_to=''),
        ),
    ]