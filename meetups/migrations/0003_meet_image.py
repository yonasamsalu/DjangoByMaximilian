# Generated by Django 5.0.6 on 2024-06-03 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_meet_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='image',
            field=models.ImageField(default='test', upload_to='images'),
            preserve_default=False,
        ),
    ]
