# Generated by Django 4.0.3 on 2022-03-04 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='teste', max_length=30),
            preserve_default=False,
        ),
    ]
