from django.urls import path
from Webapp import views

urlpatterns = [
    # Main Template
    path("", views.home_page, name="Home"),
    path("About/", views.about_page, name="About"),
    path("Blog/", views.blog_page, name="Blog"),
    path("Courses/", views.courses_page, name="Courses"),
    path("Pricing/", views.pricing_page, name="Pricing"),
    path("Gallery/", views.gallery_page, name="Gallery"),
    path("Contact/", views.contact_page, name="Contact"),
    path("save_contact_data/", views.save_contact_data, name="save_contact_data"),
    path("Career/", views.career_page, name="Career"),

    # Equipment Page
    path("Equipment_Page/", views.equip_index_page, name="Equipment_Page"),
    path("Shop/", views.shop_page, name="Shop"),
    path("Equipment_Blog/", views.equip_blog_page, name="Equipment_Blog"),
    path("single_product_page/<int:p_id>", views.single_product_page, name="single_product_page"),
    path("Each_Sub_Category/<sub_cat_name>", views.sub_filtered_page, name="Each_Sub_Category"),
    path("product_filtered/<pro_name>", views.product_filtered_page, name="product_filtered"),
    path("Cart/", views.cart_page, name="Cart"),
    path("save_cart_data/<int:p_id>", views.save_cart_data, name="save_cart_data"),
    path("delete_cart_data/<int:cat_id>", views.delete_cart_data, name="delete_cart_data"),
    path("checkout_page/", views.checkout_page, name="checkout_page"),
    path("save_customer_data/", views.save_customer_data, name="save_customer_data"),
    path("shop_payment_page/", views.shop_payment_page, name="shop_payment_page"),

    # User Authentication Session
    path("User_Login", views.user_login_page, name="User_Login"),
    path("User_Register", views.user_register, name="User_Register"),
    path("save_user_register/", views.save_user_register, name="save_user_register"),
    path("user_login_session/", views.user_login_session, name="user_login_session"),
    path("user_logout/", views.user_logout, name="user_logout"),

    # Trainer request to backend
    path("trainer_request_view", views.trainer_request_view, name="trainer_request_view"),

    # Workout Video Session
    path("video_filtered_page/<sub_cat>", views.video_filtered_page, name="video_filtered_page"),
    path("day_filtered_page/<sub_cat2>", views.day_filtered_page, name="day_filtered_page"),
    path("daily_video_display/<int:D_id>", views.daily_video_display, name="daily_video_display"),
    path("daily_video_filtered/<day>", views.daily_video_filtered, name="daily_video_filtered"),
    path("single_video/<int:w_id>", views.single_video, name="single_video"),

    # Gym Register and Profile
    path("user_gym_register_page/<int:m_id>", views.user_gym_register_page, name="user_gym_register_page"),
    path("save_user_gym_register/", views.save_user_gym_register, name="save_user_gym_register"),
    path("gym_payment_page/", views.gym_payment_page, name="gym_payment_page"),
    path("Member_Profile/", views.member_profile_page, name="Member_Profile"),
]
