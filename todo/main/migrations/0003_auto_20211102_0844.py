# Generated by Django 3.2.8 on 2021-11-02 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tomeet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='test',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='tomeet',
            name='date_of_meeting',
            field=models.DateField(auto_now_add=True),
        ),
    ]
