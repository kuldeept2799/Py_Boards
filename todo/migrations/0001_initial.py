# Generated by Django 3.2.4 on 2021-06-26 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_code', models.CharField(max_length=10, unique=True)),
                ('emp_name', models.CharField(max_length=40)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmpDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_code', models.CharField(max_length=10)),
                ('dept_name', models.CharField(max_length=30)),
                ('emp_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.employee')),
            ],
        ),
    ]
