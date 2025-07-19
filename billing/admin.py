from django.contrib import admin
from .models import (
    DemandType, Role, EmployeeType, PaymentMethod, Branch, Employee,
    Customer, NepaliMonth
)

admin.site.register(DemandType)
admin.site.register(Role)
admin.site.register(EmployeeType)
admin.site.register(PaymentMethod)
admin.site.register(Branch)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(NepaliMonth)
