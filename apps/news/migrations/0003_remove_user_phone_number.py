# Generated by Django 5.1.2 on 2025-01-02 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_todo_user_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]