# Generated by Django 5.0.6 on 2024-05-15 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='age',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
    ]
