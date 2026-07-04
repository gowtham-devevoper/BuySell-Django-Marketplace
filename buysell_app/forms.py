from django import forms
from .models import *

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields =[
      'title',
      'description',
      'price',
      'state',
      'district'   
    ]

# ---------- CAR FORM ----------

CAR_BRANDS = [

    ('Hyundai', 'Hyundai'),
    ('Maruti Suzuki', 'Maruti Suzuki'),
    ('Tata', 'Tata'),
    ('Mahindra', 'Mahindra'),
    ('Honda', 'Honda'),
    ('Toyota', 'Toyota'),
    ('Kia', 'Kia'),
    ('Renault', 'Renault'),
    ('Skoda', 'Skoda'),
    ('Volkswagen', 'Volkswagen'),
    ('Nissan', 'Nissan'),
    ('MG', 'MG'),
    ('Jeep', 'Jeep'),
    ('Ford', 'Ford'),
    ('Chevrolet', 'Chevrolet'),
    ('Fiat', 'Fiat'),
    ('Datsun', 'Datsun'),
    ('Citroen', 'Citroen'),
    ('Isuzu', 'Isuzu'),
    ('Force Motors', 'Force Motors'),
    ('Mercedes-Benz', 'Mercedes-Benz'),
    ('BMW', 'BMW'),
    ('Audi', 'Audi'),
    ('Jaguar', 'Jaguar'),
    ('Land Rover', 'Land Rover'),
    ('Volvo', 'Volvo'),
    ('Lexus', 'Lexus'),
    ('Mini', 'Mini'),
    ('Porsche', 'Porsche'),
    ('Bentley', 'Bentley'),
    ('Rolls-Royce', 'Rolls-Royce'),
    ('Lamborghini', 'Lamborghini'),
    ('Ferrari', 'Ferrari'),
    ('Maserati', 'Maserati'),
    ('Aston Martin', 'Aston Martin'),
    ('BYD', 'BYD'),
    ('Tesla', 'Tesla'),

]

class CarDetailsForm(forms.ModelForm):
    
    brand = forms.ChoiceField(
        choices=CAR_BRANDS,
        required=True, 
    )

    class Meta:

        model = CarDetails

        fields = [
            'brand',
            'model',
            'year',
            'fuel',
            'transmission',
            'km_driven',
            'owners',
        ]

# --- bike - 01 ---

class MotorcycleDetailsForm(forms.ModelForm):

    class Meta:

        model = MotorcycleDetails

        fields = [
            'brand',
            'model',
            'year',
            'km_driven',
            'engine_cc'
        ]

        widgets = {

            'brand': forms.Select(
                choices=[
                    ('', 'Select Brand'),

                    ('Hero', 'Hero'),
                    ('Honda', 'Honda'),
                    ('Bajaj', 'Bajaj'),
                    ('TVS', 'TVS'),
                    ('Royal Enfield', 'Royal Enfield'),
                    ('Yamaha', 'Yamaha'),
                    ('KTM', 'KTM'),
                    ('Suzuki', 'Suzuki'),
                    ('Jawa', 'Jawa'),
                    ('Yezdi', 'Yezdi'),
                    ('BMW', 'BMW'),
                    ('Kawasaki', 'Kawasaki'),
                    ('Triumph', 'Triumph'),
                    ('Harley Davidson', 'Harley Davidson'),
                    ('Ducati', 'Ducati'),
                ]
            ),

            'year': forms.NumberInput(
                attrs={
                    'placeholder': 'Year'
                }
            ),

            'km_driven': forms.NumberInput(
                attrs={
                    'placeholder': 'KM Driven'
                }
            ),

            'engine_cc': forms.NumberInput(
                attrs={
                    'placeholder': 'Engine CC'
                }
            ),
        }

# ---- scooter bike brand
SCOOTER_BRANDS = [

    # Honda
    ('Honda Activa', 'Honda Activa'),
    ('Honda Dio', 'Honda Dio'),
    ('Honda Aviator', 'Honda Aviator'),

    # TVS
    ('TVS Jupiter', 'TVS Jupiter'),
    ('TVS Ntorq', 'TVS Ntorq'),
    ('TVS Zest', 'TVS Zest'),
    ('TVS iQube', 'TVS iQube'),

    # Suzuki
    ('Suzuki Access 125', 'Suzuki Access 125'),
    ('Suzuki Burgman Street', 'Suzuki Burgman Street'),
    ('Suzuki Avenis', 'Suzuki Avenis'),

    # Hero
    ('Hero Pleasure+', 'Hero Pleasure+'),
    ('Hero Destini 125', 'Hero Destini 125'),
    ('Hero Xoom', 'Hero Xoom'),

    # Yamaha
    ('Yamaha RayZR 125', 'Yamaha RayZR 125'),
    ('Yamaha Fascino 125', 'Yamaha Fascino 125'),

    # Bajaj
    ('Bajaj Chetak', 'Bajaj Chetak'),

    # Ola Electric
    ('Ola S1 Air', 'Ola S1 Air'),
    ('Ola S1 Pro', 'Ola S1 Pro'),

    # Ather
    ('Ather 450S', 'Ather 450S'),
    ('Ather 450X', 'Ather 450X'),

    # Simple Energy
    ('Simple One', 'Simple One'),

    # Vida
    ('Vida V1', 'Vida V1'),

    # Ampere
    ('Ampere Magnus', 'Ampere Magnus'),
    ('Ampere Primus', 'Ampere Primus'),

    # Bounce
    ('Bounce Infinity', 'Bounce Infinity'),

]



class ScooterDetailsForm(forms.ModelForm):

    brand = forms.ChoiceField(
        choices=SCOOTER_BRANDS,
        required=True,
    )

    class Meta:

        model = ScooterDetails

        fields = [
            'brand',
            'model',
            'year',
            'fuel',
            'km_driven',
            'owner',
            'insurance_type',
            'insurance_expiry'
        ]

        widgets = {

            'year': forms.NumberInput(
                attrs={
                    'placeholder': 'Year'
                }
            ),

            'km_driven': forms.NumberInput(
                attrs={
                    'placeholder': 'KM Driven'
                }
            ),

            'insurance_expiry': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

        }

BICYCLE_BRANDS = [

    ('Hero', 'Hero'),
    ('Hercules', 'Hercules'),
    ('Atlas', 'Atlas'),
    ('Firefox', 'Firefox'),
    ('Montra', 'Montra'),
    ('Btwin', 'Btwin'),
    ('Trek', 'Trek'),
    ('Giant', 'Giant'),
    ('Scott', 'Scott'),
    ('Cannondale', 'Cannondale'),
    ('Polygon', 'Polygon'),

]

class BicycleDetailsForm(forms.ModelForm):

    brand = forms.ChoiceField(
        choices=BICYCLE_BRANDS,
        required=True
    )

    class Meta:

        model = BicycleDetails

        fields = [
            'brand',
            'model',
            'year',
            'gear_type',
            'owner'
        ]

# ---- Property ----

class HouseApartmentDetailsForm(forms.ModelForm):

    class Meta:

        model = HouseApartmentDetails

        fields = [
            'purpose',
            'property_type',
            'bhk',
            'bathrooms',
            'furnishing',
            'listed_by',
            'super_builtup_area',
            'carpet_area',
            'maintenance',
            'total_floors',
            'floor_no',
            'car_parking',
            'facing',
        ]

        widgets = {

            'super_builtup_area': forms.NumberInput(
                attrs={
                    'placeholder':
                    'Super Built-up Area (sqft)'
                }
            ),

            'carpet_area': forms.NumberInput(
                attrs={
                    'placeholder':
                    'Carpet Area (sqft)'
                }
            ),

            'maintenance': forms.NumberInput(
                attrs={
                    'placeholder':
                    'Monthly Maintenance'
                }
            ),

            'total_floors': forms.NumberInput(),

            'floor_no': forms.NumberInput(),
        }


class MobileDetailsForm(forms.ModelForm):

    class Meta:

        model = MobileDetails

        fields = [

            "brand",
            "model"

        ]

class LaptopDetailsForm(forms.ModelForm):

    class Meta:

        model = LaptopDetails
        fields = [
            "brand",
            "model",
        ]

        widgets = {
            "brand": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
            "model": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Laptop Model"
                }
            ),
        }