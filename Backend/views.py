from django.shortcuts import render, redirect
from Backend.models import *
from Webapp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def index_page(request):
    data = CategoryDB.objects.all()
    return render(request, "index.html", {'data': data})


# Category Section
# --------------------------------------------------------------------------------------------------------------------------
def add_categories(request):
    return render(request, "Add_Categories.html")


def save_categories(request):
    if request.method == "POST":
        cna = request.POST.get('category_name')
        cds = request.POST.get('category_description')
        c_img = request.FILES['category_image']
        obj = CategoryDB(Category_Name=cna, Category_Description=cds, Category_Image=c_img)
        obj.save()
    return redirect(add_categories)


def view_categories(request):
    data = CategoryDB.objects.all()
    return render(request, "View_Category.html", {'data': data})


def edit_categories_page(request, cat_id):
    data = CategoryDB.objects.get(id=cat_id)
    return render(request, "Edit_Categories.html", {'data': data})


def update_category_page(request, cat_id):
    if request.method == "POST":
        ecn = request.POST.get('edit_category_name')
        eds = request.POST.get('edit_category_description')
        try:
            e_img = request.FILES['edit_category_image']
            fs = FileSystemStorage()
            file = fs.save(e_img.name, e_img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=cat_id).Category_Image
        CategoryDB.objects.filter(id=cat_id).update(Category_Name=ecn, Category_Description=eds, Category_Image=file)
        messages.success(request, "Category Updated")
    return redirect(view_categories)


def delete_category_data(request, cat_id):
    x = CategoryDB.objects.filter(id=cat_id)
    x.delete()
    messages.error(request, "Category deleted")
    return redirect(view_categories)


# Sub-category Session
# --------------------------------------------------------------------------------------------------------------------------

def add_sub_categories(request):
    c_data = CategoryDB.objects.all()
    return render(request, "Add_Sub_Category.html", {'c_data': c_data})


def save_sub_categories(request):
    if request.method == "POST":
        scat = request.POST.get('select_cat')
        sna = request.POST.get('sub_cat_name')
        sds = request.POST.get('sub_cat_descript')
        s_img = request.FILES['sub_cat_img']
        obj = Sub_CategoryDB(Category_St=scat, Sub_Category_Name=sna, Sub_Category_Description=sds,
                             Sub_Category_Image=s_img)
        obj.save()
    return redirect(add_sub_categories)


def view_sub_categories(request):
    data = Sub_CategoryDB.objects.all()
    return render(request, "View_Sub_Category.html", {'data': data})


def edit_sub_categories(request, sub_id):
    c_data = CategoryDB.objects.all()
    s_data = Sub_CategoryDB.objects.get(id=sub_id)
    return render(request, "Edit_Sub_categories.html", {'s_data': s_data, 'c_data': c_data})


def update_sub_categories(request, sub_id):
    if request.method == "POST":
        scat = request.POST.get('edit_select_cat')
        sna = request.POST.get('edit_sub_cat_name')
        sds = request.POST.get('edit_sub_cat_descript')
        try:
            s_img = request.FILES['edit_sub_cat_img']
            fs = FileSystemStorage()
            file = fs.save(s_img.name, s_img)
        except MultiValueDictKeyError:
            file = Sub_CategoryDB.objects.get(id=sub_id).Sub_Category_Image
        Sub_CategoryDB.objects.filter(id=sub_id).update(Category_St=scat, Sub_Category_Name=sna,
                                                        Sub_Category_Description=sds, Sub_Category_Image=file)
    return redirect(view_sub_categories)


def delete_sub_category_data(request, sub_id):
    x = Sub_CategoryDB.objects.filter(id=sub_id)
    x.delete()
    messages.error(request, "Category deleted")
    return redirect(view_sub_categories)


# Product Session
# --------------------------------------------------------------------------------------------------------------------------

def add_products(request):
    cat_data = CategoryDB.objects.all()
    sub_data = Sub_CategoryDB.objects.all()
    return render(request, "Add_Products.html", {'cat_data': cat_data, 'sub_data': sub_data})


def save_products(request):
    if request.method == "POST":
        sc = request.POST.get('cat_select')
        ss = request.POST.get('sub_cat_select')
        pn = request.POST.get('product_name')
        pa = request.POST.get('about_product')
        pp = request.POST.get('product_price')
        pd = request.POST.get('product_description')
        p_img = request.FILES['product_image']
        obj = ProductDB(Cat_Select=sc, Sub_Cat_Select=ss, Product_Name=pn, Product_About=pa,
                        Product_Price=pp, Product_Description=pd, Product_Image=p_img)
        obj.save()
        return redirect(add_products)


def view_products(request):
    data = ProductDB.objects.all()
    return render(request, "View_Products.html", {'data': data})


def edit_products_page(request, p_id):
    p_data = ProductDB.objects.get(id=p_id)
    cat_data = CategoryDB.objects.all()
    sub_data = Sub_CategoryDB.objects.all()
    return render(request, "Edit_Products.html", {'p_data': p_data, 'cat_data': cat_data, 'sub_data': sub_data})


def update_products_page(request, p_id):
    if request.method == "POST":
        sc = request.POST.get('edit_cat_select')
        ss = request.POST.get('edit_sub_cat_select')
        pn = request.POST.get('edit_product_name')
        pa = request.POST.get('edit_about_product')
        pp = request.POST.get('edit_product_price')
        pd = request.POST.get('edit_product_description')
        try:
            p_img = request.FILES['edit_product_image']
            fs = FileSystemStorage()
            file = fs.save(p_img.name, p_img)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=p_id).Product_Image
        ProductDB.objects.filter(id=p_id).update(Cat_Select=sc, Sub_Cat_Select=ss, Product_Name=pn, Product_About=pa,
                                                 Product_Price=pp, Product_Description=pd, Product_Image=file)
    return redirect(view_products)


def delete_product_data(request, p_id):
    x = ProductDB.objects.filter(id=p_id)
    x.delete()
    return redirect(view_products)


# Admin or Superuser login Session
# --------------------------------------------------------------------------------------------------------------------------

def admin_login_page(request):
    return render(request, "Admin_Login.html")


def admin_session_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        ps = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=ps)
            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = ps
                return redirect(index_page)
            else:
                return redirect(admin_login_page)
        else:
            return redirect(admin_login_page)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)


# Trainer Request-Approval Session
# --------------------------------------------------------------------------------------------------------------------------
def view_trainer_request(request):
    T_data = TrainerRequest.objects.all()
    return render(request, "View_Trainer_Request.html", {'T_data': T_data})


def admin_trainer_request_view(request, t_id):
    requests = TrainerRequest.objects.get(id=t_id)

    return render(request, "Admin_trainer_requests.html", {'requests': requests})


def approve_trainer_request(request, request_id):
    request = TrainerRequest.objects.get(id=request_id)
    request.approved = True
    request.save()
    return redirect(view_trainer_request)


def delete_trainer_request(request, request_id):
    request = TrainerRequest.objects.get(id=request_id)
    request.delete()
    return redirect(view_trainer_request)


# Single-Workout session
# --------------------------------------------------------------------------------------------------------------------------

# Daily_Workout_Cat_DB
def single_workout_page(request):
    return render(request, "Single_wkt_Page.html")


def add_swkt_category(request):
    return render(request, "Add_Single_Wkt_Category.html")


def save_swkt_category(request):
    if request.method == "POST":
        cwn = request.POST.get('category_workout')
        cds = request.POST.get('workout_cat_description')
        cimg = request.FILES['workout_cat_image']
        obj = Workout_Cat_DB(Workout_Cat=cwn, Workout_desc=cds, Workout_Cat_Image=cimg)
        obj.save()
        return redirect(add_swkt_category)


def view_swkt_cat(request):
    wk_out = Workout_Cat_DB.objects.all()
    return render(request, "View_Single_wkt_Category.html", {'wk_out': wk_out})


def edit_swkt_category(request, w_id):
    data = Workout_Cat_DB.objects.get(id=w_id)
    return render(request, "Edit_Single_Wkt_Category.html", {'data': data})


def update_swkt_category(request, w_id):
    if request.method == "POST":
        wn = request.POST.get('edit_cat_wkt')
        ds = request.POST.get('edit_wkt_cat_desc')
        try:
            e_img = request.FILES['edit_wkt_cat_image']
            fs = FileSystemStorage()
            file = fs.save(e_img.name, e_img)
        except MultiValueDictKeyError:
            file = Workout_Cat_DB.objects.get(id=w_id).Workout_Cat_Image
        Workout_Cat_DB.objects.filter(id=w_id).update(Workout_Cat=wn, Workout_desc=ds, Workout_Cat_Image=file)

    return redirect(view_swkt_cat)


def delete_swkt_category(request, w_id):
    x = Workout_Cat_DB.objects.filter(id=w_id)
    x.delete()
    return redirect(view_swkt_cat)


# Daily Workout session
# -----------------------------------------------------------------------------------------------------------------------

def daily_workout_page(request):
    return render(request, "Daily_wkt_Page.html")


def add_daily_workout_cat(request):
    return render(request, "Add_Daily_Wkt_Cat.html")


def save_daily_category(request):
    if request.method == "POST":
        cwn = request.POST.get('category_workout')
        cds = request.POST.get('workout_cat_description')
        cimg = request.FILES['workout_cat_image']
        obj = Daily_Workout_Cat_DB(Daily_Workout_Cat=cwn, Daily_Workout_desc=cds, Daily_Workout_Cat_Image=cimg)
        obj.save()
        return redirect(daily_workout_page)


def view_daily_cat(request):
    wk_out = Daily_Workout_Cat_DB.objects.all()
    return render(request, "View_Daily_wkt_Category.html", {'wk_out': wk_out})


def edit_daily_category(request, w_id):
    data = Daily_Workout_Cat_DB.objects.get(id=w_id)
    return render(request, "Edit_Daily_Wkt_Cat.html", {'data': data})


def update_daily_category(request, w_id):
    if request.method == "POST":
        wn = request.POST.get('edit_cat_wkt')
        ds = request.POST.get('edit_wkt_cat_desc')
        try:
            e_img = request.FILES['edit_wkt_cat_image']
            fs = FileSystemStorage()
            file = fs.save(e_img.name, e_img)
        except MultiValueDictKeyError:
            file = Daily_Workout_Cat_DB.objects.get(id=w_id).Daily_Workout_Cat_Image
        Daily_Workout_Cat_DB.objects.filter(id=w_id).update(Daily_Workout_Cat=wn, Daily_Workout_desc=ds,
                                                            Daily_Workout_Cat_Image=file)
    return redirect(view_daily_cat)


def delete_daily_category(request, w_id):
    x = Daily_Workout_Cat_DB.objects.filter(id=w_id)
    x.delete()
    return redirect(view_daily_cat)


# Saving Video to DayDB
# -------------------------------------------------
def add_daily_workouts(request):
    D_data = DayDB.objects.all()
    return render(request, "Add_Daily_Workouts.html", {'D_data': D_data})


def save_daily_workouts(request):
    if request.method == "POST":
        wc = request.POST.get('select_cat')
        wn = request.POST.get('workout_name')
        ws = request.POST.get('workout_sets')
        wd = request.POST.get('workout_description')
        wi = request.FILES['workout_image']
        wv = request.FILES['workout_video']
        obj = Daily_WorkoutsDB(Day_Cat=wc, Workout_Name=wn, Sets=ws,
                               Description=wd, Workout_Image=wi, Video=wv)
        obj.save()

        return redirect(daily_workout_page)


def view_daily_workouts(request):
    wk_out = Daily_WorkoutsDB.objects.all()
    return render(request, "View_Daily_Workouts.html", {'wk_out': wk_out})


# Single workout-video session
# -------------------------------------------------------

def add_single_workouts(request):
    data = Workout_Cat_DB.objects.all()
    return render(request, "Add_Single_Workouts.html", {'data': data})


def save_single_workouts(request):
    if request.method == "POST":
        wc = request.POST.get('select_cat')
        wn = request.POST.get('workout_name')
        ws = request.POST.get('workout_sets')
        wd = request.POST.get('workout_description')
        wi = request.FILES['workout_image']
        wv = request.FILES['workout_video']
        obj = Single_WorkoutsDB(Cat_Name=wc, Workout_Name=wn, Sets=ws,
                                Description=wd, Workout_Image=wi, Video=wv)
        obj.save()

        return redirect(add_single_workouts)


def view_single_workouts(request):
    wk_out = Single_WorkoutsDB.objects.all()
    return render(request, "View_Single_Workouts.html", {'wk_out': wk_out})


def edit_single_workouts(request, s_id):
    cat = Workout_Cat_DB.objects.all()
    data = Single_WorkoutsDB.objects.get(id=s_id)
    return render(request, "Edit_Single_Workouts.html", {'data': data, 'cat': cat})


def update_single_workouts(request, s_id):
    if request.method == "POST":
        wc = request.POST.get('edit_select_cat')
        wn = request.POST.get('edit_workout_name')
        ws = request.POST.get('edit_workout_sets')
        wd = request.POST.get('edit_workout_description')
        wi = request.FILES['edit_workout_image']
        try:
            wv = request.FILES['edit_workout_video']

            fs = FileSystemStorage()
            file_video = fs.save(wv.name, wv)
            # file_img = fs.save(wv.name, wi)
        except MultiValueDictKeyError:
            file_video = Single_WorkoutsDB.objects.get(id=s_id).Video
            # file_img = Single_WorkoutsDB.objects.get(id=s_id).Workout_Image
        Single_WorkoutsDB.objects.filter(id=s_id).update(Cat_Name=wc, Workout_Name=wn, Sets=ws,
                                                         Description=wd, Workout_Image=wi, Video=file_video)
        return redirect(view_single_workouts)


def delete_single_workouts(request, s_id):
    x = Single_WorkoutsDB.objects.get(id=s_id)
    x.delete()
    return redirect(view_single_workouts)


# Day Cat Session
# -----------------------------------------------------------
def add_day_category(request):
    cat = Daily_Workout_Cat_DB.objects.all()
    return render(request, "Add_Day_Category.html", {'cat': cat})


def save_day_category(request):
    if request.method == "POST":
        cn = request.POST.get('select_cat')
        cd = request.POST.get('day_name')
        obj = DayDB(Day_Cat=cn, Day=cd)
        obj.save()
        return redirect(daily_workout_page)


def view_day_category(request):
    data = DayDB.objects.all()
    return render(request, "View_Day_Category.html", {'data': data})


# Register MemberShip Session
# ______________________________________________________________

def membership_plan_page(request):
    return render(request, "Membership_Plan.html")


def add_membership_plan_page(request):
    return render(request, "Add_Membership_Plan.html")


def save_membership_plan(request):
    if request.method == "POST":
        mn = request.POST.get('plan_name')
        mp = request.POST.get('plan_price')
        md = request.POST.get('plan_description')
        obj = Membership_PlansDB(Plan_Name=mn, Plan_Price=mp, Plan_Description=md)
        obj.save()
        return redirect(membership_plan_page)


def view_membership_plan_page(request):
    data = Membership_PlansDB.objects.all()
    return render(request, "View_Membership_Plan.html", {'data': data})

def edit_membership_plan(request, m_id):
    return redirect(view_membership_plan_page)



def delete_membership_plan(request, m_id):
    
    x = Membership_PlansDB.objects.get(id=m_id)
    x.delete()
    return redirect(view_membership_plan_page)

# Feedback Session
# ---------------------------------

def view_feedback_page(request):
    data = ContactDB.objects.all()
    return render(request, "View_Feedbacks.html", {'data': data})


def delete_feedback(request, f_id):
    x = ContactDB.objects.get(id=f_id)
    x.delete()
    return redirect(view_feedback_page)
