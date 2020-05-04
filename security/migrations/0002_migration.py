# Generated by Django 2.2.12 on 2020-05-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_migration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputloggedrequest',
            name='user',
        ),
        migrations.AddField(
            model_name='inputloggedrequest',
            name='user_id',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='user ID'),
        ),
    ]
