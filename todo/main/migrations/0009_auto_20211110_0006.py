# Generated by Django 3.2.8 on 2021-11-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_habits_today'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habits',
            name='done_for',
        ),
        migrations.RemoveField(
            model_name='habits',
            name='today',
        ),
        migrations.AddField(
            model_name='habits',
            name='done_for_today',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='habits',
            name='comment',
            field=models.CharField(max_length=100),
        ),
    ]
