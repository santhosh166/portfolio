# Generated by Django 4.0.1 on 2022-01-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_remove_certifications_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='certifications',
            name='logo',
            field=models.ImageField(default=None, upload_to='pics'),
            preserve_default=False,
        ),
    ]