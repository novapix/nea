from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('status', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    objects = UserManager()
    
    # Remove default fields
    first_name = None
    last_name = None
    is_staff = None
    is_superuser = None
    
    # Custom fields
    email = models.EmailField(unique=True)
    last_seen = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False, help_text="Approved status")
    
    # Relationships
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_username(self):
        return self.username

    def __str__(self):
        return self.username

    def is_superadmin(self):
        try:
            return self.employee.employee_type.name.lower() == 'superadmin'
        except (AttributeError, Employee.DoesNotExist):
            return False

    @property
    def is_staff(self):
        """For Django admin compatibility"""
        return self.is_superadmin()

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        swappable = 'AUTH_USER_MODEL'


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
    date_joined = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.employee_code})"

    class Meta:
        db_table = 'employee'
        ordering = ['name']


class Customer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    sc_number = models.CharField(max_length=50, unique=True,null=True,blank=True)
    address = models.TextField(null=False, blank=False)
    contact = models.CharField(max_length=50, null=True, blank=True,unique=True)
    email = models.EmailField(null=True, blank=True,unique=True)
    dob = models.DateField(null=True, blank=True)
    demand_type = models.ForeignKey(DemandType, on_delete=models.PROTECT, null=False, blank=False)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="Approved status")
    citizenship_no = models.CharField(max_length=50, unique=True)
    citizenship_file_location = models.CharField(max_length=255, null=True, blank=True)
    property_file_location = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customer'


class NepaliMonth(models.Model):
    month_number = models.PositiveSmallIntegerField(unique=True, help_text="Month number 1-12")
    name_en = models.CharField(max_length=50, unique=True, help_text="English month name")
    name_np = models.CharField(max_length=50, unique=True, help_text="Nepali month name (in Nepali script)")
    abbreviation = models.CharField(max_length=10, blank=True, null=True, help_text="Optional short form")

    def __str__(self):
        return f"{self.month_number} - {self.name_en} ({self.name_np})"

    class Meta:
        db_table = 'nepali_months'
        ordering = ['month_number']


from django.core.validators import FileExtensionValidator

class Avatar(models.Model):
    """Model to store user profile pictures"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar')
    image = models.ImageField(
        upload_to='avatars/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Avatar for {self.user.email}"

    class Meta:
        verbose_name = 'Avatar'
        verbose_name_plural = 'Avatars'
