from django.contrib.auth.models import User
from django.db import models


# Base Table with no Foreign Keys

class DemandType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    rate_per_unit = models.FloatField(null=False, blank=False)
    minimum_charge = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'demand_types'


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


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    logo = models.TextField(null=False, blank=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'payment_method'


class Branch(models.Model):
    branch_code = models.CharField(max_length=20, unique=True, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    contact = models.CharField(max_length=50, null=False, blank=False)
    status = models.BooleanField(default=True)
    # this is set to null to prevent circular dependency as branch has branch_admin(emp) and emp has branch so well...
    branch_incharge = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='branches_incharge_of'
    )

    def __str__(self):
        return f"{self.branch_code} - {self.name}"

    class Meta:
        db_table = 'branch'
        ordering = ['branch_code']


class Employee(models.Model):
    contact_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    employee_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    address = models.TextField(null=False, blank=False)
    citizenship_no = models.CharField(max_length=50, unique=True)
    citizenship_file_location = models.CharField(max_length=255, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    employee_type = models.ForeignKey(EmployeeType, on_delete=models.PROTECT)
    status = models.BooleanField(default=False,help_text="Approved status")  # False until approved
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Linked after approval
    date_joined = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.employee_code})"

    class Meta:
        db_table = 'employee'
        ordering = ['name']


class Customer(models.Model):
    sc_no = models.CharField(max_length=20, null=True, blank=True, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    dob = models.DateField(null=False, blank=False)
    contact_no = models.CharField(max_length=20, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    citizenship_no = models.CharField(max_length=50, unique=True, null=False, blank=False)
    location_citizenship = models.CharField(max_length=100, null=False, blank=False)
    property_file_location = models.CharField(max_length=255, null=False, blank=False)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT,null=False, blank=False)
    demand_type = models.ForeignKey(DemandType, on_delete=models.PROTECT,null=False, blank=False)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=False,help_text="Approved status")
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customer'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    employee = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.OneToOneField(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture = models.TextField(null=True, blank=True)
    last_seen = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.employee and self.customer:
            raise ValidationError("UserProfile can be linked to either an Employee or a Customer, not both.")

    class Meta:
        db_table = 'user_profile'
