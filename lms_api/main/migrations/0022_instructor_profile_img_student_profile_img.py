# Generated by Django 4.0.6 on 2022-08-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_favouritecourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='profile_photos/'),
        ),
        migrations.AddField(
            model_name='student',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='profile_photos/'),
        ),
    ]