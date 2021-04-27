# Generated by Django 3.2 on 2021-04-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1)),
                ('age', models.IntegerField()),
                ('medicinename', models.CharField(max_length=100)),
                ('empname', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('prescription_date', models.DateField()),
            ],
            options={
                'db_table': 'prescription',
            },
        ),
    ]
