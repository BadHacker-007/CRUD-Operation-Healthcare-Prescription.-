# Generated by Django 3.2 on 2021-05-02 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('crud', '0008_alter_empmodel_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='empmodel',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
    ]
