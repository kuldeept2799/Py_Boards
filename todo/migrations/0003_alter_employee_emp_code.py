# Generated by Django 3.2.4 on 2021-07-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_code',
            field=models.CharField(help_text='emp code ex. LTPL - 4 digit', max_length=10, unique=True),
        ),
    ]