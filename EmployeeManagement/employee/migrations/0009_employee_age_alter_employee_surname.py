# Generated by Django 4.1.1 on 2022-09-27 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_employee_data_fixture'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='surname',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]