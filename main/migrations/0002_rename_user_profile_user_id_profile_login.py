# Generated by Django 5.0.7 on 2024-08-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='profile',
            name='login',
            field=models.CharField(default=1, max_length=55),
            preserve_default=False,
        ),
    ]
