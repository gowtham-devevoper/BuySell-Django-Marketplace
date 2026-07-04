from django.db import models
from django.contrib.auth.models import User 
from datetime import timedelta
from django.utils import timezone


class Category(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class SubCategory(models.Model):
  category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name='subcategories'
  )
  name = models.CharField(max_length=100)
  def __str__(self):
    return self.name
  
#---LOCATION---

class State(models.Model):
  name = models.CharField(max_length=100,unique=True)
  def __str__(self):
    return self.name
  
class District(models.Model):
  state = models.ForeignKey(
    State,
    on_delete=models.CASCADE,
    related_name='districts'
  )

  name = models.CharField(max_length=100)
  def __str__(self):
    return self.name
  
# --- PRODUCTS ---

class Product(models.Model):

  seller = models.ForeignKey(User,on_delete=models.CASCADE)

  category = models.ForeignKey(Category,on_delete=models.CASCADE)

  subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)

  state = models.ForeignKey(State,on_delete=models.CASCADE)

  district =models.ForeignKey(District,on_delete=models.CASCADE)

  title = models.CharField(max_length=200)

  description = models.TextField()

  price = models.DecimalField(max_digits=12,decimal_places=2)

  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  
class ProductImage(models.Model):

  product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')

  image = models.ImageField(upload_to='products/')

  def __str__(self):
    return self.product.title
  
# ---- CAR DETAILS ----

class CarDetails(models.Model):

    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('CNG & Hybrids', 'CNG & Hybrids'),
        ('Electric', 'Electric'),
        ('LPG', 'LPG'),
    ]

    TRANSMISSION_CHOICES = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    ]

    OWNERS_CHOICES = [
    ('1', '1st Owner'),
    ('2', '2nd Owner'),
    ('3', '3rd Owner'),
    ('4', '4th Owner'),
    ('5', '5th Owners'),
]

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE
    )

    brand = models.CharField(
        max_length=100
    )

    model = models.CharField(
        max_length=100
    )

    year = models.PositiveIntegerField()

    fuel = models.CharField(
        max_length=50,
        choices=FUEL_CHOICES
    )

    transmission = models.CharField(
        max_length=50,
        choices=TRANSMISSION_CHOICES
    )

    km_driven = models.PositiveIntegerField()
    
    owners = models.CharField(
    max_length=10,
    choices=OWNERS_CHOICES,
    default='1'
    )


    def __str__(self):
        return self.product.title

# ---- BIKE DETAILS ---- (motorcycles)

class MotorcycleDetails(models.Model):

    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Electric', 'Electric'),
        ('Diesel', 'Diesel'),
    ]

    OWNER_CHOICES = [
        ('1', '1st Owner'),
        ('2', '2nd Owner'),
        ('3', '3rd Owner'),
        ('4', '4th Owner'),
        ('5', '4+ Owner'),
    ]

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE
    )

    brand = models.CharField(
        max_length=100
    )

    model = models.CharField(
        max_length=100
    )

    year = models.PositiveIntegerField()

    fuel = models.CharField(
        max_length=20,
        choices=FUEL_CHOICES
    )

    km_driven = models.PositiveIntegerField()

    owner = models.CharField(
        max_length=10,
        choices=OWNER_CHOICES
    )

    engine_cc = models.PositiveIntegerField()

    insurance_expiry = models.DateField(
        null=True,
        blank=True
    )
    INSURANCE_CHOICES = [
    ('Valid', 'Valid'),
    ('No Insurance', 'No Insurance'),
]

    insurance_type = models.CharField(
    max_length=50,
    choices=INSURANCE_CHOICES,
    default='No Insurance'
)

    def __str__(self):
        return self.product.title

# ---- BIKE DETAILS ---- (scooter)

class ScooterDetails(models.Model):

    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Electric', 'Electric'),
    ]

    OWNER_CHOICES = [
        ('1', '1st Owner'),
        ('2', '2nd Owner'),
        ('3', '3rd Owner'),
        ('4', '4th Owner'),
        ('5', '4+ Owner'),
    ]

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE
    )

    brand = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    year = models.PositiveIntegerField()

    fuel = models.CharField(
        max_length=20,
        choices=FUEL_CHOICES
    )

    km_driven = models.PositiveIntegerField()

    owner = models.CharField(
        max_length=10,
        choices=OWNER_CHOICES
    )

    insurance_type = models.CharField(
        max_length=50,
        blank=True
    )

    insurance_expiry = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.product.title
    

class BicycleDetails(models.Model):

    OWNER_CHOICES = [
        ('1', '1st Owner'),
        ('2', '2nd Owner'),
        ('3', '3rd Owner'),
        ('4', '4th Owner'),
        ('5', '4+ Owner'),
    ]

    GEAR_CHOICES = [
        ('Gear', 'Gear Cycle'),
        ('Non Gear', 'Non Gear Cycle'),
    ]

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE
    )

    brand = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    year = models.PositiveIntegerField()

    gear_type = models.CharField(
        max_length=20,
        choices=GEAR_CHOICES
    )

    owner = models.CharField(
        max_length=10,
        choices=OWNER_CHOICES
    )

    def __str__(self):
        return self.product.title
    

# ---- Property ----
class HouseApartmentDetails(models.Model):

    TYPE_CHOICES = [
        ('Flats / Apartments', 'Flats / Apartments'),
        ('Independent / Builder Floors', 'Independent / Builder Floors'),
        ('Farm House', 'Farm House'),
        ('House & Villa', 'House & Villa'),
        ('Duplex', 'Duplex'),
    ]

    PURPOSE_CHOICES = [
        ('Sale', 'Sale'),
        ('Rent', 'Rent'),
    ]

    BHK_CHOICES = [
        ('1', '1 BHK'),
        ('2', '2 BHK'),
        ('3', '3 BHK'),
        ('4', '4 BHK'),
        ('5', '4+ BHK'),
    ]

    BATHROOM_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '4+'),
    ]

    FURNISHING_CHOICES = [
        ('Furnished', 'Furnished'),
        ('Semi-Furnished', 'Semi-Furnished'),
        ('Unfurnished', 'Unfurnished'),
    ]

    LISTED_BY_CHOICES = [
        ('Builder', 'Builder'),
        ('Dealer', 'Dealer'),
        ('Owner', 'Owner'),
    ]

    PARKING_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '3+'),
    ]

    FACING_CHOICES = [
        ('North', 'North'),
        ('South', 'South'),
        ('East', 'East'),
        ('West', 'West'),
        ('North-East', 'North-East'),
        ('North-West', 'North-West'),
        ('South-East', 'South-East'),
        ('South-West', 'South-West'),
    ]

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE
    )

    purpose = models.CharField(
        max_length=20,
        choices=PURPOSE_CHOICES
    )

    property_type = models.CharField(
        max_length=100,
        choices=TYPE_CHOICES
    )

    bhk = models.CharField(
        max_length=10,
        choices=BHK_CHOICES
    )

    bathrooms = models.CharField(
        max_length=10,
        choices=BATHROOM_CHOICES
    )

    furnishing = models.CharField(
        max_length=30,
        choices=FURNISHING_CHOICES
    )

    listed_by = models.CharField(
        max_length=20,
        choices=LISTED_BY_CHOICES
    )

    super_builtup_area = models.PositiveIntegerField(
        help_text="Includes walls and common areas."
    )

    carpet_area = models.PositiveIntegerField(
        help_text="Actual usable area inside the property."
    )

    maintenance = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    total_floors = models.PositiveIntegerField()

    floor_no = models.PositiveIntegerField()

    car_parking = models.CharField(
        max_length=10,
        choices=PARKING_CHOICES
    )

    facing = models.CharField(
        max_length=20,
        choices=FACING_CHOICES
    )

    def __str__(self):
        return self.product.title
    

class MobileDetails(models.Model):

    BRAND_CHOICES = [

        ("Apple", "Apple"),
        ("Samsung", "Samsung"),
        ("Xiaomi", "Xiaomi"),
        ("Redmi", "Redmi"),
        ("POCO", "POCO"),
        ("Realme", "Realme"),
        ("OnePlus", "OnePlus"),
        ("Vivo", "Vivo"),
        ("OPPO", "OPPO"),
        ("iQOO", "iQOO"),
        ("Nothing", "Nothing"),
        ("Motorola", "Motorola"),
        ("Google Pixel", "Google Pixel"),
        ("Nokia", "Nokia"),
        ("Honor", "Honor"),
        ("Huawei", "Huawei"),
        ("Infinix", "Infinix"),
        ("Tecno", "Tecno"),
        ("Lava", "Lava"),
        ("Micromax", "Micromax"),
        ("Lenovo", "Lenovo"),
        ("Asus", "Asus"),
        ("Sony", "Sony"),
        ("LG", "LG"),
        ("HTC", "HTC"),
        ("BlackBerry", "BlackBerry"),
        ("JioPhone", "JioPhone"),
        ("Other", "Other"),

    ]

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE
    )

    brand = models.CharField(
        max_length=50,
        choices=BRAND_CHOICES
    )

    model = models.CharField(
        max_length=100
    )

    def __str__(self):
        return f"{self.brand} {self.model}"
    
class LaptopDetails(models.Model):

    BRAND_CHOICES = [

        ("Apple", "Apple"),
        ("Dell", "Dell"),
        ("HP", "HP"),
        ("Lenovo", "Lenovo"),
        ("Asus", "Asus"),
        ("Acer", "Acer"),
        ("MSI", "MSI"),
        ("Samsung", "Samsung"),
        ("LG", "LG"),
        ("Microsoft", "Microsoft"),
        ("Huawei", "Huawei"),
        ("Honor", "Honor"),
        ("Razer", "Razer"),
        ("Alienware", "Alienware"),
        ("Gigabyte", "Gigabyte"),
        ("Avita", "Avita"),
        ("Infinix", "Infinix"),
        ("Realme", "Realme"),
        ("Chuwi", "Chuwi"),
        ("Others", "Others"),

    ]

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE
    )

    brand = models.CharField(
        max_length=50,
        choices=BRAND_CHOICES
    )

    model = models.CharField(
        max_length=100
    )

    def __str__(self):

        return f"{self.brand} {self.model}"

    # ---------
  
    
class Wishlist(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            'user',
            'product'
        )

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"
    

# ---------------- CHAT ----------------

class ChatRoom(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="chat_rooms"
    )

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="buyer_rooms"
    )

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="seller_rooms"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        unique_together = (
            "product",
            "buyer",
            "seller"
        )

    def __str__(self):

        return f"{self.product.title}"


class Message(models.Model):

    room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name="messages"
    )

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ["created_at"]

    def __str__(self):

        return self.message[:40]




# -------------------------
# Subscription Plans
# -------------------------

class SubscriptionPlan(models.Model):

    name = models.CharField(
        max_length=50
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    duration_days = models.PositiveIntegerField()

    description = models.CharField(
        max_length=200
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):

        return self.name


# -------------------------
# User Subscription
# -------------------------

class UserSubscription(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.CASCADE
    )

    start_date = models.DateTimeField(
        auto_now_add=True
    )

    end_date = models.DateTimeField()

    is_active = models.BooleanField(
        default=True
    )

    def save(self, *args, **kwargs):

        if not self.end_date:

            self.end_date = timezone.now() + timedelta(
                days=self.plan.duration_days
            )

        super().save(
            *args,
            **kwargs
        )

    def is_valid(self):

        return (

            self.is_active

            and

            self.end_date >= timezone.now()

        )

    def __str__(self):

        return f"{self.user.username} - {self.plan.name}"



# Contact Unlock
# -------------------------

class ContactUnlock(models.Model):

    buyer = models.ForeignKey(

        User,

        on_delete=models.CASCADE,

        related_name="contact_unlocks"

    )

    seller = models.ForeignKey(

        User,

        on_delete=models.CASCADE,

        related_name="contact_buyers"

    )

    product = models.ForeignKey(

        Product,

        on_delete=models.CASCADE

    )

    subscription = models.ForeignKey(

        UserSubscription,

        on_delete=models.CASCADE

    )

    unlocked_at = models.DateTimeField(

        auto_now_add=True

    )

    class Meta:

        unique_together = (

            "buyer",

            "product"

        )

    def __str__(self):

        return f"{self.buyer.username} unlocked {self.product.title}"
    
class Notification(models.Model):

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="buyer_notifications"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = [
            "-created_at"
        ]

    def __str__(self):

        return self.title