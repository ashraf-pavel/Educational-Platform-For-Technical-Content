# Generated by Django 4.0.6 on 2022-08-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_coursequiz_options_remove_coursequiz_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attemptquiz',
            name='right_ans',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
