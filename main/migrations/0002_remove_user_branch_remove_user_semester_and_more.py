# Generated by Django 5.0.7 on 2024-07-20 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='user',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='user',
            name='take_personality_test',
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
