# Generated by Django 2.2.5 on 2019-11-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_post_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.ImageField(default='images/404image.jpg', upload_to='images/'),
        ),
    ]