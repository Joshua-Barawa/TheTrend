# Generated by Django 4.0.3 on 2022-03-25 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
