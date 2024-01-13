# Generated by Django 4.0.6 on 2022-08-03 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_chapter_options_remove_chapter_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.RemoveField(
            model_name='course',
            name='techs',
        ),
        migrations.AlterField(
            model_name='chapter',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module_chapters', to='main.module'),
        ),
        migrations.AlterField(
            model_name='module',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_modules', to='main.course'),
        ),
        migrations.DeleteModel(
            name='CourseCategory',
        ),
    ]
