# Generated by Django 2.2.5 on 2019-09-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todoitem_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='done',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='done_date',
            field=models.DateTimeField(null=True),
        ),
    ]
