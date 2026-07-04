from django.urls import path 
from .import views

urlpatterns = [
  
  path('',views.home,name='home'),

  path('sell/',views.sell_page,name='sell'),

  path('create-product/<int:sub_id>/',views.create_product,name='create_product'),

  path('load-districts/',views.load_districts,name='load_districts'),


  # --- Creat_product_Post ---

  path('car-create/<int:sub_id>/',views.car_create,name='car_create'),

  path('motorcycle-create/<int:sub_id>/',views.motorcycle_create,name='motorcycle_create'),

  path('scooter/create/<int:subcategory_id>/',views.scooter_create,name='scooter_create'),

  path('bicycle/create/<int:subcategory_id>/',views.bicycle_create,name='bicycle_create'),

  path('house-apartment/create/<int:subcategory_id>/',views.house_apartment_create,name='house_apartment_create'),

  path("sell/mobile/<int:sub_id>/",views.mobile_create,name="mobile_create"),

 path("sell/laptop/<int:sub_id>/",views.laptop_create,name="laptop_create"),
  

  # --- Product_detail ---

  path('car/<int:pk>/',views.car_product_detail,name='car_product_detail'),

  path('motorcycle-detail/<int:pk>/',views.motorcycle_product_detail,name='motorcycle_product_detail'),

  path('scooter/product/<int:id>/',views.scooter_product_detail,name='scooter_product_detail'),
  
  path('bicycle/<int:product_id>/',views.bicycle_product_detail,name='bicycle_product_detail'),

  path('house/<int:product_id>/',views.house_product_detail,name='house_product_detail'),

  path("mobile/<int:pk>/",views.mobile_product_detail,name="mobile_product_detail"),
  
  path("laptop/<int:pk>/",views.laptop_product_detail,name="laptop_product_detail"),

# --- WISHLIST ---

  path('wishlist/toggle/<int:product_id>/',views.toggle_wishlist,name='toggle_wishlist'),

  path('wishlist/',views.my_wishlist,name='my_wishlist'),



  path('seller/<int:user_id>/',views.seller_profile,name='seller_profile'),

  path('my-products/',views.my_products,name='my_products'),

  path('edit-product/<int:pk>/',views.edit_product,name='edit_product'),

  path('delete-product/<int:pk>/',views.delete_product,name='delete_product'),

  path('delete-image/<int:image_id>/',views.delete_image,name='delete_image'),


  # --- Chat system ---

  path("chat/",views.chat_list,name="chat_list"),
  
  path("chat/start/<int:product_id>/",views.start_chat,name="start_chat"),
  
  path("chat/<int:room_id>/",views.chat_room,name="chat_room"),

  path("chat/send/<int:room_id>/",views.send_message,name="send_message"),
  
  path("chat/messages/<int:room_id>/",views.get_messages,name="get_messages"),


# -- Subscription --

path("subscription/",views.subscription_plans,name="subscription_plans"),

path("subscription/<int:plan_id>/",views.subscribe_plan,name="subscribe_plan"),

path("subscription/success/<int:plan_id>/",views.payment_success,name="payment_success"),


path("unlock-contact/<int:product_id>/",views.unlock_contact,name="unlock_contact"),

path("notifications/",views.notification_list,name="notification_list"),

path("help-support/",views.help_support,name="help_support"),

]