# Generated by Django 4.0.6 on 2022-08-03 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_chapter_options_alter_student_options_module'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'verbose_name_plural': '5. Module Chapter'},
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='course',
        ),
        migrations.AddField(
            model_name='chapter',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.module'),
        ),
    ]
