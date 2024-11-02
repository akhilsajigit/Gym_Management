from django.shortcuts import render, redirect
from Webapp.models import *
from Backend.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Webapp.forms import TrainerRequestForm
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from Gym_Management import settings
import razorpay


# Main Template ---
def home_page(request):
    M_data = Membership_PlansDB.objects.all()
    return render(request, "Home.html", {'M_data': M_data})


def blog_page(request):
    return render(request, "Blog.html")


def gallery_page(request):
    return render(request, "Gallery.html")


def about_page(request):
    return render(request, "About.html")


def pricing_page(request):
    return render(request, "Pricing.html")


def contact_page(request):
    return render(request, "Contact.html")


def save_contact_data(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        obj = ContactDB(fd_Name=na, fd_Email=em, fd_Subject=sub, fd_Message=msg)
        obj.save()
    return redirect(contact_page)


# Equipment Page----------
def equip_index_page(request):
    c_data = CategoryDB.objects.all()
    p_data = ProductDB.objects.all()
    return render(request, "Equip_Index.html", {'c_data': c_data, 'p_data': p_data})


def equip_blog_page(request):
    c_data = CategoryDB.objects.all()
    return render(request, "Equipment_Blog.html", {'c_data': c_data})


def shop_page(request):
    c_data = CategoryDB.objects.all()
    sub_cat = Sub_CategoryDB.objects.all()
    return render(request, "Shop.html", {'sub_cat': sub_cat, 'c_data': c_data})


def sub_filtered_page(request, sub_cat_name):
    c_data = CategoryDB.objects.all()
    sub_cat = Sub_CategoryDB.objects.filter(Category_St=sub_cat_name)
    return render(request, "Sub_cat_Filtered.html", {'sub_cat': sub_cat, 'c_data': c_data})


def product_filtered_page(request, pro_name):
    c_data = CategoryDB.objects.all()
    p_data = ProductDB.objects.filter(Sub_Cat_Select=pro_name)
    return render(request, "Products_Filtered.html", {'p_data': p_data, 'c_data': c_data})


def single_product_page(request, p_id):
    c_data = CategoryDB.objects.all()
    p_data = ProductDB.objects.filter(id=p_id)
    return render(request, "Single_Product.html", {'c_data': c_data, 'p_data': p_data})


def product_search(request):
    product = ProductDB.objects.all()

    # Check if the form was submitted
    if request.method == "POST":
        searched_term = request.POST.get('searched_item')

        if not searched_term:
            messages.warning(request, "Please enter to search! ")
            return render(request, "Equip_Index.html")

        searched_product = ProductDB.objects.filter(Product_Name__icontains=searched_term)
        c_data = CategoryDB.objects.all()

        context = {
            'searched_product': searched_product,
            'c_data': c_data,
            'searched_term':searched_term
        }

        # if no results
        if not searched_product:
            messages.error(request, "Sorry..! Your search not exist")
            return render(request, "Search_Page.html")

        return render(request, "Search_Page.html", context)


def cart_page(request):
    c_data = CategoryDB.objects.all()
    cart_data = CartDB.objects.filter(Ct_User=request.session['Username'])
    sub_total = total = delivery_charge = 0
    for i in cart_data:
        sub_total = sub_total + i.Ct_Total_price
        if sub_total >= 10000:
            delivery_charge = 250
        else:
            delivery_charge = 500
        total = sub_total + delivery_charge
    return render(request, "Cart.html", {'c_data': c_data, 'cart_data': cart_data,
                                         'sub_total': sub_total, 'total': total, 'delivery_charge': delivery_charge})


def save_cart_data(request, p_id):
    if request.method == "POST":
        try:
            ct_img = request.FILES['cart_image']
            fs = FileSystemStorage()
            file = fs.save(ct_img.name, ct_img)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=p_id).Product_Image
        ct_ur = request.POST.get('cart_user')
        ct_pn = request.POST.get('product_name')
        ct_pp = request.POST.get('product_price')
        ct_qt = request.POST.get('quantity')
        ct_tt = request.POST.get('total')
        obj = CartDB(Ct_User=ct_ur, Ct_Product_Price=ct_pp, Ct_Product_Name=ct_pn,
                     Ct_Quantity=ct_qt, Ct_Total_price=ct_tt, Ct_Image=file)
        obj.save()
        return redirect(cart_page)


def delete_cart_data(request, cat_id):
    x = CartDB.objects.filter(id=cat_id)
    x.delete()
    return redirect(cart_page)


def checkout_page(request):
    c_data = CategoryDB.objects.all()
    cart_data = CartDB.objects.filter(Ct_User=request.session['Username'])
    sub_total = total = delivery_charge = 0
    for i in cart_data:
        sub_total = sub_total + i.Ct_Total_price
        if sub_total >= 10000:
            delivery_charge = 250
        else:
            delivery_charge = 500
        total = sub_total + delivery_charge
    return render(request, "CheckOut.html", {'c_data': c_data, 'cart_data': cart_data,
                                             'sub_total': sub_total, 'total': total,
                                             'delivery_charge': delivery_charge})


def save_customer_data(request):
    if request.method == "POST":
        cn = request.POST.get('customer_name')
        cc = request.POST.get('customer_country')
        ca = request.POST.get('customer_address')
        cy = request.POST.get('customer_city')
        cm = request.POST.get('customer_mobile')
        ce = request.POST.get('customer_email')
        pr = request.POST.get('price')
        obj = OrderDB(Customer_Name=cn, Customer_State=cc, Customer_Address=ca,
                      Customer_City=cy, Customer_Mobile=cm, Customer_Email=ce, Order_Price=pr)
        obj.save()
        return redirect(shop_payment_page)


def shop_payment_page(request):
    customer = OrderDB.objects.order_by('-id').first()
    pay = customer.Order_Price
    amount = int(pay * 100)
    pay_str = str(amount)
    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_PMmGnroCxOlaJ0', 'rD9yidEziI0RjKCkl2HUPe7u'))
        payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1'})
    return render(request, "Shop_Payment.html", {'customer': customer, 'pay_str': pay_str})


# User Authentication -----
def user_login_page(request):
    return render(request, "UserLogin.html")


def user_register(request):
    return render(request, "User_Register.html")


def save_user_register(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        ue = request.POST.get('user_email')
        up = request.POST.get('user_pass')
        up2 = request.POST.get('user_pass2')
        pass_size = len(up)
        obj = RegisterDB(User_Name=un, User_Email=ue, User_Password=up)
        if RegisterDB.objects.filter(User_Name=un):
            messages.warning(request, "Username already Exists")
            return redirect(user_register)
        elif RegisterDB.objects.filter(User_Email=ue):
            messages.warning(request, "Email already Exists")
            return redirect(user_register)
        elif up != up2:
            messages.warning(request, "Passwords are not equal")
            return redirect(user_register)
        elif pass_size < 8:
            messages.warning(request, "Passwords not strong")
            return redirect(user_register)
        else:
            obj.save()
            messages.success(request, "User Registered Successfully")
        return redirect(user_login_page)


def user_login_session(request):
    if request.method == "POST":
        usr = request.POST.get('username')
        pwd = request.POST.get('password')
        if RegisterDB.objects.filter(User_Name=usr).exists():
            if RegisterDB.objects.filter(User_Name=usr, User_Password=pwd).exists():
                request.session['Username'] = usr
                request.session['Password'] = pwd
                sec = RegisterDB.objects.get(User_Name=request.session['Username'])
                messages.success(request, f"Welcome {sec.User_Name}")
                return redirect(home_page)
            else:
                messages.warning(request, "Incorrect Password")
                return redirect(user_login_page)
        else:
            messages.warning(request, "User not exists")
            return redirect(user_login_page)
    else:
        return redirect(user_login_page)


def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Logout Successfully")
    return redirect(home_page)


# _______________________________________________________________________________________________________________________
def career_page(request):
    return render(request, "Career.html")


def trainer_request_view(request):
    if request.method == 'POST':
        form = TrainerRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(career_page)
        else:
            data = {
                'name': request.GET.get('name'),
                'email': request.GET.get('email'),
                'phone': request.GET.get('phone'),
                'course': request.GET.get('course'),
                'experience': request.GET.get('experience'),
                'certification': request.GET.get('certification')
            }
            form = TrainerRequestForm(initial=data)
    else:
        form = TrainerRequestForm()
    return render(request, 'Trainer_Request.html', {'form': form})


# ___________________________________________________


def courses_page(request):
    data = Workout_Cat_DB.objects.all()
    data2 = Daily_Workout_Cat_DB.objects.all()
    return render(request, "Courses.html", {'data': data, 'data2': data2})


def video_filtered_page(request, sub_cat):
    data = Single_WorkoutsDB.objects.filter(Cat_Name=sub_cat)
    return render(request, "Video_Filtered.html", {'data': data})


def single_video(request, w_id):
    w_data = Single_WorkoutsDB.objects.get(id=w_id)
    return render(request, "Video_Display.html", {'w_data': w_data})


def day_filtered_page(request, sub_cat2):
    data2 = DayDB.objects.filter(Day_Cat=sub_cat2)
    return render(request, "Day_Filtered.html", {'data2': data2})


def daily_video_filtered(request, day):
    d_data = Daily_WorkoutsDB.objects.filter(Day_Cat=day)
    return render(request, "Daily_video_filtered.html", {'d_data': d_data})


def daily_video_display(request, D_id):
    w_data = Daily_WorkoutsDB.objects.get(id=D_id)
    return render(request, "Daily_Video_Display.html", {'w_data': w_data})


# ___________________________________________________

def user_gym_register_page(request, m_id):
    cat_data = Workout_Cat_DB.objects.all()
    cat2 = Daily_Workout_Cat_DB.objects.all()
    trainer = TrainerRequest.objects.filter(approved=True)
    plan = Membership_PlansDB.objects.get(id=m_id)
    return render(request, "User_Gym_Register.html",
                  {'cat_data': cat_data, 'trainer': trainer, 'plan': plan, 'cat2': cat2})


def save_user_gym_register(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        ad = request.POST.get('address')
        ph = request.POST.get('phone')
        dt = request.POST.get('joining_date')
        st = request.POST.get('select_trainer')
        sc = request.POST.get('select_course')
        sp = request.POST.get('selected_plan')
        pp = request.POST.get('payment_plan')
        gen = request.POST.get('gender')
        ht = request.POST.get('height')
        wt = request.POST.get('weight')
        md = request.POST.get('medical')
        en = request.POST.get('em_name')
        ep = request.POST.get('em_phone')
        us = request.POST.get('user_session')
        p_img = request.FILES['profile_image']
        if Gym_MemberDB.objects.filter(User_Session=us).exists():
            messages.warning(request, "You already registered")
            return redirect(home_page)
        else:
            obj = Gym_MemberDB(Name=na, Email=em, Address=ad, Phone=ph, Joining_Date=dt,
                               Select_Trainer=st, Select_Course=sc, Select_Plan=sp,
                               Amount=pp, Gender=gen, Height=ht, Weight=wt, Medical=md,
                               Emergency_Name=en, Emergency_Phone=ep, User_Session=us,
                               Profile_Image=p_img)
            obj.save()
            subject = 'Zacson Gym'
            message = 'This is from Zacson Gym, Welcome to our team and your registration completed with payments'
            send_mail(subject,
                      message, settings.EMAIL_HOST_USER, [em], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect(gym_payment_page)


def gym_payment_page(request):
    payer = Gym_MemberDB.objects.order_by('-id').first()
    # approve user to profile after payment
    payer.Payment_approved = True
    payer.save()
    pay = payer.Amount
    amount = int(pay * 100)  # Assigning the payment amount in rupees
    pay_str = str(amount)
    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_PMmGnroCxOlaJ0', 'rD9yidEziI0RjKCkl2HUPe7u'))
        payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1'})
    return render(request, "Gym_Payment.html", {'payer': payer, 'pay_str': pay_str})


def member_profile_page(request):
    try:
        m_data = Gym_MemberDB.objects.get(User_Session=request.session['Username'])
        r_data = RegisterDB.objects.get(User_Name=request.session['Username'])
        return render(request, "Member_Profile.html", {'m_data': m_data, 'r_data': r_data})
    except:
        r_data = RegisterDB.objects.get(User_Name=request.session['Username'])
        return render(request, "Member_Profile.html", {'r_data': r_data})
