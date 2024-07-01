from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    posting_date = models.DateField()
    salary = models.CharField(max_length=256)
    hours = models.CharField(max_length=50)
    closing_date = models.DateField()
    location = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    company = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    job_reference = models.CharField(max_length=100)
    additional_salary_info = models.TextField(null=True, blank=True)
    min_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_type = models.CharField(max_length=50)
    avg_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
