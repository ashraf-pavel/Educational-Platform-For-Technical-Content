# Generated by Django 4.0.6 on 2022-08-24 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_rename_right_ans_attemptquiz_given_ans'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.instructor')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
            options={
                'verbose_name_plural': '12. Post',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.instructor')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.post')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
            options={
                'verbose_name_plural': '13. Post Reply',
            },
        ),
    ]