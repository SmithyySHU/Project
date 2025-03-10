# Generated by Django 5.0.6 on 2024-07-01 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('posting_date', models.DateField()),
                ('salary', models.CharField(max_length=256)),
                ('hours', models.CharField(max_length=50)),
                ('closing_date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=255)),
                ('job_type', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('job_reference', models.CharField(max_length=100)),
                ('additional_salary_info', models.TextField(blank=True, null=True)),
                ('min_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('max_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('salary_type', models.CharField(max_length=50)),
                ('avg_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
