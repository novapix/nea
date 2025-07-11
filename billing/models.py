from django.db import models

class Customer(models.Model):
    SC_NO = models.CharField(max_length=20, null=True, blank=True)
    Name = models.CharField(max_length=100, null=False, blank=False)
    Address = models.TextField(null=False, blank=False)
    DOB = models.DateField(null=False, blank=False)
    ContactNo = models.CharField(max_length=20, null=False, blank=False)
    CitizenshipNo = models.CharField(max_length=50, unique=True, null=False, blank=False)
    LocationCitizenship = models.CharField(max_length=100, null=False, blank=False)
    PropertyFileLocation = models.CharField(max_length=255, null=False, blank=False)
    BranchID = models.IntegerField(null=False, blank=False)
    DemandTypeID = models.IntegerField(null=False, blank=False)
    Status = models.BooleanField(default=True)


    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'customer'
