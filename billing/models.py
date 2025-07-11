from django.db import models

class Customer(models.Model):
    sc_no = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    dob = models.DateField(null=False, blank=False)
    contact_no = models.CharField(max_length=20, null=False, blank=False)
    citizenship_no = models.CharField(max_length=50, unique=True, null=False, blank=False)
    location_citizenship = models.CharField(max_length=100, null=False, blank=False)
    property_file_location = models.CharField(max_length=255, null=False, blank=False)
    branch_id = models.IntegerField(null=False, blank=False)
    demand_type_id = models.IntegerField(null=False, blank=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customer'


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    logo = models.TextField(null=False, blank=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'payment_method'


class Role(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'roles'

class EmployeeType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee_types'
#
# class Branch(models.Model):
#     branch_code = models.CharField(max_length=20, null=False, blank=False)
#     name = models.CharField(max_length=100, null=False, blank=False)
#     address = models.TextField(null=False, blank=False)
#     contact = models.TextField(null=False, blank=False)
#     status = models.BooleanField(default=True)