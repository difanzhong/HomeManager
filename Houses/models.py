from django.db import models


class House(models.Model):
    name = models.CharField(max_length=200)
    rate = models.DecimalField(max_digits=7, decimal_places=2)
    max_guests = models.IntegerField()
    parking = models.IntegerField()
    num_of_bathroom = models.IntegerField()
    area = models.IntegerField()  # in square meters
    description = models.TextField()
    owner = models.CharField(max_length=100)  # email address or username of the owner
    type = models.CharField(max_length=50)  # apartment, houses ...
    #min_days = models.IntegerField() # min days to book

    def __str__(self):
        return self.name + " (" + self.type + ")"


class Bedroom(models.Model):
    bedroom_no = models.IntegerField()
    description = models.CharField(max_length=500)
    house = models.ForeignKey(House, on_delete=models.CASCADE)


class Image(models.Model):
    IMAGE_TYPE_CHOICES = (
        ('T', 'Thumbnail'),
        ('E', 'Exterior'),
        ('I', 'Interior'),
    )
    img_name = models.CharField(max_length=500)
    img_type = models.CharField(max_length=20, choices=IMAGE_TYPE_CHOICES)
    house = models.ForeignKey(House, on_delete=models.CASCADE)


class Bed(models.Model):
    BED_TYPE_CHOICES = (
        ('K', 'King'),
        ('Q', 'Queen'),
        ('D', 'Double'),
        ('S', 'Single'),
        ('SF', 'Sofa Bed'),
        ('M', 'Mattress'),
        ('WM', "Water Mattress"),
        ('AM', "Air Mattress"),
        ('T', "Toddler Bed"),
    )
    bed_type = models.CharField(max_length=20, choices=BED_TYPE_CHOICES)
    num_of_beds = models.IntegerField()
    bedroom = models.ForeignKey(Bedroom, on_delete=models.CASCADE)


class Amenity(models.Model):
    kitchen = models.BooleanField()
    swimming_pool = models.BooleanField()
    internet = models.BooleanField()
    wireless = models.BooleanField()
    bbq = models.BooleanField()
    parking = models.BooleanField()
    house = models.OneToOneField(House, on_delete=models.CASCADE)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)


class Address(models.Model):
    STATE_CHOICES = (
        ('QLD', 'Queensland'),
        ('NT', 'Northern Territory'),
        ('NSW', 'New South Wales'),
        ('VIC', 'Victoria'),
        ('TAS', 'Tasmania'),
        ('SA', 'South Australia'),
        ('WA', 'Western Australia'),
        ('ACT', 'Australian Capital Territory'),
    )
    unit = models.IntegerField()
    street_no = models.IntegerField()
    street = models.CharField(max_length=200)
    street2 = models.CharField(max_length=200, blank=True, null=True)
    suburb = models.CharField(max_length=50)
    state = models.CharField(max_length=100, choices=STATE_CHOICES)
    postal_code = models.IntegerField()
    house = models.OneToOneField(House, on_delete=models.CASCADE, default=None, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return (self.unit.__str__() if self.unit > 0 else "") + " " + self.street_no.__str__() + " " + self.street + " " + self.suburb + ", " + self.state + ", " + self.postal_code.__str__()


class CreditCard(models.Model):
    CREDITCARD_TYPE_CHOICE = (
        ('VISA', 'VISA'),
        ('MasterCard', 'MasterCard'),
    )
    EXPIRE_MONTH_CHOICE = (
        ('JAN', '01'),
        ('FEB', '02'),
        ('MAR', '03'),
        ('APR', '04'),
        ('MAY', '05'),
        ('JUN', '06'),
        ('JUL', '07'),
        ('AUG', '08'),
        ('SEP', '09'),
        ('OCT', '10'),
        ('NOV', '11'),
        ('DEC', '12'),
    )
    EXPIRE_YEAR_CHOICE = (
        ('18', '2018'),
        ('19', '2019'),
        ('20', '2020'),
        ('21', '2021'),
        ('22', '2022'),
        ('23', '2023'),
    )
    type = models.CharField(max_length=10, choices=CREDITCARD_TYPE_CHOICE)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expire_month = models.CharField(max_length=3, choices=EXPIRE_MONTH_CHOICE)
    expire_year = models.CharField(max_length=4, choices=EXPIRE_YEAR_CHOICE)







