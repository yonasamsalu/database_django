# Generated by Django 5.0.6 on 2024-05-16 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_rename_member_membertable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membertable',
            name='joined_date',
        ),
        migrations.RemoveField(
            model_name='membertable',
            name='phone',
        ),
    ]