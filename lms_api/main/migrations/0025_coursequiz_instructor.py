# Generated by Django 4.0.6 on 2022-08-22 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_chapter_options_alter_course_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursequiz',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.instructor'),
        ),
    ]