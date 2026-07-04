from django.contrib import admin
from . models import *

admin.site.register(Category)
admin.site.register(SubCategory)

admin.site.register(State)
admin.site.register(District)

admin.site.register(Product)
admin.site.register(ProductImage)

admin.site.register(CarDetails)

admin.site.register(MotorcycleDetails)
admin.site.register(ScooterDetails)
admin.site.register(BicycleDetails)

admin.site.register(HouseApartmentDetails)

admin.site.register(MobileDetails)

admin.site.register(Wishlist)

admin.site.register(ChatRoom)
admin.site.register(Message)

admin.site.register(SubscriptionPlan)
admin.site.register(UserSubscription)
admin.site.register(ContactUnlock)

admin.site.register(Notification)