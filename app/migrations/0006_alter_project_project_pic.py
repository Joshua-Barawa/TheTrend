# Generated by Django 4.0.3 on 2022-03-25 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]