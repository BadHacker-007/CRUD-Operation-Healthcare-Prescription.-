# Generated by Django 3.2 on 2021-05-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_empmodel_patientpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empmodel',
            name='patientpic',
            field=models.ImageField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
    ]