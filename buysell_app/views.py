from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Max
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from users.models import UserProfile

def home(request):

    # Newest products first
    products = Product.objects.prefetch_related(
        "images"
    ).order_by(
        "-created_at",
        "-id"
    )

    q = request.GET.get(
        "q",
        ""
    ).strip()

    state = request.GET.get(
        "state"
    )

    district = request.GET.get(
        "district"
    )

    category = request.GET.get(
        "category"
    )

    # ---------------- Search ---------------- #

    if q:

        products = products.filter(

            Q(title__icontains=q) |

            Q(description__icontains=q) |

            # Cars
            Q(cardetails__brand__icontains=q) |
            Q(cardetails__model__icontains=q) |

            # Motorcycle
            Q(motorcycledetails__brand__icontains=q) |
            Q(motorcycledetails__model__icontains=q) |

            # Scooter
            Q(scooterdetails__brand__icontains=q) |
            Q(scooterdetails__model__icontains=q) |

            # Bicycle
            Q(bicycledetails__brand__icontains=q) |
            Q(bicycledetails__model__icontains=q) |

            # Property
            Q(houseapartmentdetails__property_type__icontains=q) |
            Q(houseapartmentdetails__purpose__icontains=q) |
            Q(houseapartmentdetails__bhk__icontains=q) |

            # Mobile
            Q(mobiledetails__brand__icontains=q) |
            Q(mobiledetails__model__icontains=q) |

            # Laptop
            Q(laptopdetails__brand__icontains=q) |
            Q(laptopdetails__model__icontains=q)

        ).distinct()

    # ---------------- Category Filter ---------------- #

    if category == "cars":

        products = products.filter(
            cardetails__isnull=False
        )

    elif category == "bikes":

        products = products.filter(

            Q(motorcycledetails__isnull=False) |

            Q(scooterdetails__isnull=False) |

            Q(bicycledetails__isnull=False)

        ).distinct()

    elif category == "houses":

        products = products.filter(
            houseapartmentdetails__isnull=False
        )

    elif category == "mobiles":

        products = products.filter(
            mobiledetails__isnull=False
        )

    elif category == "laptops":

        products = products.filter(
            laptopdetails__isnull=False
        )

    # ---------------- Location Filter ---------------- #

    if state:

        products = products.filter(
            state_id=state
        )

    if district:

        products = products.filter(
            district_id=district
        )

    # Always keep newest first
    products = products.order_by(
        "-created_at",
        "-id"
    )

    # ---------------- States ---------------- #

    states = State.objects.all()

    districts = District.objects.none()

    if state:

        districts = District.objects.filter(
            state_id=state
        )

    # ---------------- Wishlist ---------------- #

    wishlist_products = []

    if request.user.is_authenticated:

        wishlist_products = Wishlist.objects.filter(
            user=request.user
        ).values_list(
            "product_id",
            flat=True
        )

    context = {

        "products": products,

        "states": states,

        "districts": districts,

        "wishlist_products": wishlist_products,

        "search": q,

        "category": category,

    }

    return render(
        request,
        "home.html",
        context
    )

# -- --- Details Section --- --

def car_product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    unlocked = False
    if request.user.is_authenticated:
        unlocked = ContactUnlock.objects.filter(
            buyer=request.user,
            product=product
        ).exists()
        print("Buyer :", request.user)
        print("Product :", product.id)
        print("Unlocked :", unlocked)

    return render(
        request,
        "details/car_product_detail.html",
        {
            "product": product,
            "unlocked": unlocked,
        }
    )

def motorcycle_product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    unlocked = False
    if request.user.is_authenticated:
        unlocked = ContactUnlock.objects.filter(
            buyer=request.user,
            product=product
        ).exists()
    return render(
        request,
        "details/motorcycle_product_detail.html",
        {
            "product": product,
            "unlocked": unlocked,
        }
    )

def scooter_product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    unlocked = False
    if request.user.is_authenticated:
        unlocked = ContactUnlock.objects.filter(
            buyer=request.user,
            product=product
        ).exists()

    return render(
        request,
        "details/scooter_product_detail.html",
        {
            "product": product,
            "unlocked": unlocked,
        }
    )

def bicycle_product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    unlocked = False
    if request.user.is_authenticated:
        unlocked = ContactUnlock.objects.filter(
            buyer=request.user,
            product=product
        ).exists()

    return render(
        request,
        "details/bicycle_product_detail.html",
        {
            "product": product,
            "unlocked": unlocked,
        }
    )


def house_product_detail(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id
    )

    wishlist_products = []
    unlocked = False

    if request.user.is_authenticated:

        wishlist_products = Wishlist.objects.filter(
            user=request.user
        ).values_list(
            'product_id',
            flat=True
        )

        unlocked = ContactUnlock.objects.filter(
            buyer=request.user,
            product=product
        ).exists()

    return render(
        request,
        'details/house_product_details.html',
        {
            'product': product,
            'wishlist_products': wishlist_products,
            'unlocked': unlocked,
        }
    )

def mobile_product_detail(request, pk):
    product = get_object_or_404(
        Product,
        id=pk
    )
    unlocked = False
    if request.user.is_authenticated:
        unlocked = ContactUnlock.objects.filter(
            buyer=request.user,
            product=product
        ).exists()

        print("Buyer :", request.user)
        print("Product :", product.id)
        print("Unlocked :", unlocked)

    return render(
        request,
        "details/mobile_product_detail.html",
        {
            "product": product,
            "unlocked": unlocked,
        }
    )

def laptop_product_detail(request, pk):
    product = get_object_or_404(
        Product,
        id=pk
    )
    unlocked = False
    
    if request.user.is_authenticated:
        unlocked = ContactUnlock.objects.filter(
            buyer=request.user,
            product=product
        ).exists()

    return render(
        request,
        "details/laptop_product_detail.html",
        {
            "product": product,
            "unlocked": unlocked,
        }
    )

# -- --- Sell Section --- --

def sell_page(request):
  categories = Category.objects.prefetch_related(
    'subcategories'
  )
  context = {
    'categories' : categories
  }
  return render(request,'sell/category_page.html',context)


@login_required
def create_product(request, sub_id):

  subcategory = SubCategory.objects.get(id=sub_id)
  if request.method == "POST":
    form = ProductForm(request.POST)
    if form.is_valid():
      product = form.save(commit=False)
      product.seller = request.user
      product.category = (
                subcategory.category
            )
      product.subcategory = (
                subcategory
            )
      product.save()
      return redirect('home')
  else:
    form = ProductForm()
  return render(request,'sell/create_product.html',{'form':form,
  'subcategory':subcategory})

# --- CAR FORM ---

@login_required
def car_create(request, sub_id):

    subcategory = SubCategory.objects.get(
        id=sub_id
    )

    if request.method == "POST":

        product_form = ProductForm(
            request.POST
        )

        car_form = CarDetailsForm(
            request.POST
        )

        if (
            product_form.is_valid()
            and
            car_form.is_valid()
        ):

            product = product_form.save(
                commit=False
            )

            product.seller = request.user

            product.category = (
                subcategory.category
            )

            product.subcategory = (
                subcategory
            )

            product.save()

            car = car_form.save(
                commit=False
            )

            car.product = product

            car.fuel = request.POST.get('fuel')

            car.transmission = request.POST.get('transmission')
            car.owners = request.POST.get('owners')

            car.save()

            images = request.FILES.getlist(
                'images'
                )
            
            for image in images:
               ProductImage.objects.create(
                  product=product,
                  image=image)
            return redirect('home')

    else:

        product_form = ProductForm()

        car_form = CarDetailsForm()

    return render( request,'sell/car_create.html',
        {
            'product_form': product_form,
            'car_form': car_form,
            'subcategory':subcategory
        }
    )
# --- Laptop ----
@login_required
def laptop_create(request, sub_id):

    subcategory = SubCategory.objects.get(
        id=sub_id
    )

    if request.method == "POST":

        product_form = ProductForm(
            request.POST
        )

        laptop_form = LaptopDetailsForm(
            request.POST
        )

        if (
            product_form.is_valid()
            and
            laptop_form.is_valid()
        ):

            product = product_form.save(
                commit=False
            )

            product.seller = request.user

            product.category = (
                subcategory.category
            )

            product.subcategory = (
                subcategory
            )

            product.save()

            laptop = laptop_form.save(
                commit=False
            )

            laptop.product = product

            laptop.save()

            images = request.FILES.getlist(
                "images"
            )

            for image in images:

                ProductImage.objects.create(

                    product=product,

                    image=image

                )

            return redirect(
                "home"
            )

    else:

        product_form = ProductForm()

        laptop_form = LaptopDetailsForm()

    return render(

        request,

        "sell/laptop_create.html",

        {

            "product_form": product_form,

            "laptop_form": laptop_form,

            "subcategory": subcategory,

        }

    )
# ---- mobile -----
@login_required
def mobile_create(request, sub_id):

    subcategory = SubCategory.objects.get(
        id=sub_id
    )

    if request.method == "POST":
        product_form = ProductForm(
            request.POST
        )
        mobile_form = MobileDetailsForm(
            request.POST
        )

        if (
            product_form.is_valid()
            and
            mobile_form.is_valid()
        ):
            product = product_form.save(
                commit=False
            )
            product.seller = request.user
            product.category = (
                subcategory.category
            )
            product.subcategory = (
                subcategory
            )
            product.save()
            mobile = mobile_form.save(
                commit=False
            )

            mobile.product = product
            mobile.save()
            images = request.FILES.getlist(
                "images"
            )

            for image in images:
                ProductImage.objects.create(
                    product=product,
                    image=image
                )
            return redirect(
                "home"
            )

    else:
        product_form = ProductForm()
        mobile_form = MobileDetailsForm()

    return render(
        request,
        "sell/mobile_create.html",
        {
            "product_form": product_form,
            "mobile_form": mobile_form,
            "subcategory": subcategory,
        }
    )

# --- bike --- 
# --- motorcycles ---

@login_required
def motorcycle_create(request, sub_id):

    subcategory = SubCategory.objects.get(
        id=sub_id
    )

    if request.method == "POST":

        product_form = ProductForm(
            request.POST
        )

        motorcycle_form = MotorcycleDetailsForm(
            request.POST
        )

        if (
            product_form.is_valid()
            and
            motorcycle_form.is_valid()
        ):

            product = product_form.save(
                commit=False
            )

            product.seller = request.user

            product.category = (
                subcategory.category
            )

            product.subcategory = (
                subcategory
            )

            product.save()

            motorcycle = motorcycle_form.save(
                commit=False
            )

            motorcycle.product = product

            motorcycle.fuel = request.POST.get(
                'fuel'
            )

            motorcycle.owner = request.POST.get(
                'owner'
            )

            insurance_type = request.POST.get(
                'insurance_type'
            )

            if insurance_type == "No Insurance":

                motorcycle.insurance_expiry = None

            else:

                motorcycle.insurance_expiry = request.POST.get(
                    'insurance_expiry'
                )

            motorcycle.save()

            images = request.FILES.getlist(
                'images'
            )

            for image in images:

                ProductImage.objects.create(
                    product=product,
                    image=image
                )

            return redirect(
                'home'
            )

    else:

        product_form = ProductForm()

        motorcycle_form = MotorcycleDetailsForm()

    return render(
        request,
        'sell/motorcycle_create.html',
        {
            'product_form': product_form,
            'motorcycle_form': motorcycle_form,
            'subcategory': subcategory
        }
    )

@login_required
def scooter_create(request, subcategory_id):

    subcategory = get_object_or_404(
        SubCategory,
        id=subcategory_id
    )

    if request.method == 'POST':

        product_form = ProductForm(request.POST)

        scooter_form = ScooterDetailsForm(request.POST)

        if product_form.is_valid() and scooter_form.is_valid():

            product = product_form.save(commit=False)

            product.seller = request.user

            product.category = subcategory.category

            product.subcategory = subcategory

            product.save()

            scooter = scooter_form.save(commit=False)

            scooter.product = product

            scooter.save()

            images = request.FILES.getlist('images')

            for image in images:

                ProductImage.objects.create(
                    product=product,
                    image=image
                )

            return redirect('home')

    else:

        product_form = ProductForm()

        scooter_form = ScooterDetailsForm()

    return render(
        request,
        'sell/scooter_create.html',
        {
            'product_form': product_form,
            'scooter_form': scooter_form,
            'subcategory': subcategory
        }
    )

def bicycle_create(request, subcategory_id):

    subcategory = get_object_or_404(
        SubCategory,
        id=subcategory_id
    )

    if request.method == 'POST':

        product_form = ProductForm(request.POST)

        bicycle_form = BicycleDetailsForm(request.POST)

        if product_form.is_valid() and bicycle_form.is_valid():

            product = product_form.save(commit=False)

            product.seller = request.user

            product.category = subcategory.category

            product.subcategory = subcategory

            product.save()

            bicycle = bicycle_form.save(commit=False)

            bicycle.product = product

            bicycle.save()
            
            images = request.FILES.getlist('images')
            
            for image in images:
                ProductImage.objects.create(
                    product=product,
                    image=image
                    )

            return redirect('home')

    else:

        product_form = ProductForm()

        bicycle_form = BicycleDetailsForm()

    return render(
        request,
        'sell/bicycle_create.html',
        {
            'product_form': product_form,
            'bicycle_form': bicycle_form,
            'subcategory': subcategory
        }
    )


# ----- Propertys ------

def house_apartment_create(request, subcategory_id):

    subcategory = get_object_or_404(
        SubCategory,
        id=subcategory_id
    )

    if request.method == "POST":

        product_form = ProductForm(request.POST)

        house_form = HouseApartmentDetailsForm(request.POST)

        if product_form.is_valid() and house_form.is_valid():

            product = product_form.save(commit=False)

            product.seller = request.user

            product.category = subcategory.category

            product.subcategory = subcategory

            product.save()

            house = house_form.save(commit=False)

            house.product = product

            house.save()

            images = request.FILES.getlist('images')

            for image in images:

                ProductImage.objects.create(
                    product=product,
                    image=image
                )

            return redirect('home')

    else:

        product_form = ProductForm()

        house_form = HouseApartmentDetailsForm()

    return render(
        request,
        'sell/house_apartment_create.html',
        {
            'product_form': product_form,
            'house_form': house_form,
            'subcategory': subcategory,
        }
    )


def load_districts(request):

    state_id = request.GET.get("state")

    districts = District.objects.filter(
        state_id=state_id
    )

    data = []

    for district in districts:

        data.append({

            "id":district.id,

            "name":district.name

        })

    return JsonResponse(
        data,
        safe=False
    )

# ---- WISHLIST CODE ----

@login_required
def toggle_wishlist(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    wishlist = Wishlist.objects.filter(
        user=request.user,
        product=product
    )

    if wishlist.exists():

        wishlist.delete()

    else:

        Wishlist.objects.create(
            user=request.user,
            product=product
        )

    return redirect(
        request.META.get(
            'HTTP_REFERER',
            'home'
        )
    )


@login_required
def my_wishlist(request):

    wishlist_items = Wishlist.objects.filter(
        user=request.user
    ).select_related(
        'product'
    ).prefetch_related(
        'product__images'
    )

    return render(
        request,
        'wishlist.html',
        {
            'wishlist_items': wishlist_items
        }
    )

# --- seller_profile  ---

def seller_profile(request, user_id):

    seller = get_object_or_404(
        User,
        id=user_id
    )

    products = Product.objects.filter(
        seller=seller
    ).prefetch_related(
        'images'
    )

    total_ads = products.count()

    wishlist_count = Wishlist.objects.filter(
        product__seller=seller
    ).count()

    context = {

        'seller': seller,

        'products': products,

        'total_ads': total_ads,

        'wishlist_count': wishlist_count

    }

    return render(
        request,
        'seller_profile.html',
        context
    )

# --- my product ---

@login_required
def my_products(request):

    products = Product.objects.filter(
        seller=request.user
    ).prefetch_related(
        'images'
    ).order_by(
        '-created_at'
    )

    return render(request,'my_products.html',{'products': products})

@login_required
def edit_product(request, pk):

    product = get_object_or_404(
        Product,
        id=pk,
        seller=request.user
    )

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            instance=product
        )

        if form.is_valid():
            form.save()
            images = request.FILES.getlist(
                'images'
            )

            for image in images:

                ProductImage.objects.create(
                    product=product,
                    image=image
                )

            return redirect(
                'my_products'
            )

    else:

        form = ProductForm(
            instance=product
        )

    return render(
        request,
        'edit_product.html',
        {
            'form': form,
            'product': product
        }
    )


@login_required
def delete_product(request, pk):

    product = get_object_or_404(
        Product,
        id=pk,
        seller=request.user
    )

    if request.method == "POST":
        product.delete()
        return redirect(
            'my_products'
        )

    return render(
        request,
        'delete_product.html',
        {
            'product': product
        }
    )


@login_required
def delete_image(request, image_id):

    image = get_object_or_404(
        ProductImage,
        id=image_id
    )

    if image.product.seller != request.user:

        return redirect(
            'my_products'
        )

    product_id = image.product.id
    image.delete()
    return redirect(
        'edit_product',
        pk=product_id
    )

# --- CHAT SYSTEM CODE ---

@login_required
def start_chat(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    if request.user == product.seller:
        return redirect(
            "home"
        )

    room, created = ChatRoom.objects.get_or_create(

        product=product,
        buyer=request.user,
        seller=product.seller

    )

    return redirect(
        "chat_room",
        room.id
    )

@login_required
def chat_room(request, room_id):

    room = get_object_or_404(
        ChatRoom,
        id=room_id
    )

    if request.user not in [
        room.buyer,
        room.seller

    ]:

        return redirect(
            "home"
        )

    if request.method == "POST":

        text = request.POST.get(
            "message"
        )

        if text:

            Message.objects.create(
                room=room,
                sender=request.user,
                message=text
            )

            return redirect(
                "chat_room",
                room.id
            )

    messages = room.messages.all()

    messages.exclude(
        sender=request.user
    ).update(
        is_read=True
    )

    return render(
        request,
        "chat/chat_room.html",

        {

            "room": room,

            "messages": messages

        }

    )


@login_required
def chat_list(request):

    rooms = ChatRoom.objects.filter(

        Q(
            buyer=request.user
        )

        |

        Q(
            seller=request.user
        )

    ).annotate(

        last_time=Max(
            "messages__created_at"
        )

    ).order_by(

        "-last_time"
    )

    return render(

        request,

        "chat/chat_list.html",

        {

            "rooms": rooms

        }

    )

@login_required
def send_message(request, room_id):

    room = get_object_or_404(
        ChatRoom,
        id=room_id
    )

    if request.method == "POST":

        text = request.POST.get("message")

        if text:

            msg = Message.objects.create(
                room=room,
                sender=request.user,
                message=text
            )

            return JsonResponse({

                "success": True,
                "message": msg.message,
                "time": msg.created_at.strftime("%I:%M %p"),
                "sender": request.user.id
            })
    return JsonResponse({
        "success": False
    })


@login_required
def get_messages(request, room_id):

    room=get_object_or_404(
        ChatRoom,
        id=room_id
    )
    messages=[]

    for m in room.messages.all():
        messages.append({
            "sender":m.sender.id,
            "text":m.message,
            "time":m.created_at.strftime("%I:%M %p")
        })

    return JsonResponse({
        "messages":messages
    })


# Subscription Plans
# -----------------------------

@login_required
def subscription_plans(request):

    plans = SubscriptionPlan.objects.filter(
        is_active=True
    ).order_by(
        "price"
    )

    return render(
        request,
        "subscription/plans.html",
        {
            "plans": plans
        }
    )

@login_required
def subscribe_plan(request, plan_id):

    plan = get_object_or_404(
        SubscriptionPlan,
        id=plan_id
    )

    return render(
        request,
        "subscription/payment.html",
        {
            "plan": plan
        }
    )

@login_required
def payment_success(request, plan_id):

    plan = get_object_or_404(
        SubscriptionPlan,
        id=plan_id
    )

    UserSubscription.objects.filter(
        user=request.user,
        is_active=True
    ).update(
        is_active=False
    )

    subscription = UserSubscription.objects.create(
        user=request.user,
        plan=plan,
        end_date=timezone.now() + timedelta(
            days=plan.duration_days
        )
    )

    return render(
        request,
        "subscription/payment_success.html",
        {
            "subscription": subscription
        }
    )

@login_required
def unlock_contact(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    subscription = UserSubscription.objects.filter(
        user=request.user,
        is_active=True,
        end_date__gte=timezone.now()
    ).first()

    if not subscription:

        return redirect(
            "subscription_plans"
        )

    ContactUnlock.objects.get_or_create(
    buyer=request.user,
    seller=product.seller,
    product=product,
    subscription=subscription
)
    
    Notification.objects.create(
    seller=product.seller,
    buyer=request.user,
    product=product,
    title="🔓 Contact Unlocked",
    message=f"{request.user.first_name} unlocked your contact for '{product.title}'."
)
    return redirect(
    request.META.get(
        "HTTP_REFERER",
        "home"
    )
)



@login_required
def notification_list(request):

    notifications = Notification.objects.filter(
        seller=request.user
    ).order_by(
        "-created_at"
    )
    notifications.filter(
        is_read=False
    ).update(
        is_read=True
    )

    return render(
        request,
        "noti/notification_list.html",
        {
            "notifications": notifications
        }
    )


def help_support(request):
    return render(request, "help_support.html")