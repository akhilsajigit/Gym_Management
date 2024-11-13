from django.urls import path
from Backend import views

urlpatterns = [
    path("index_page/", views.index_page, name="index_page"),

    # Category Section_____
    path("add_categories/", views.add_categories, name="add_categories"),
    path("view_categories/", views.view_categories, name="view_categories"),
    path("save_categories/", views.save_categories, name="save_categories"),
    path("edit_categories_page/<int:cat_id>", views.edit_categories_page, name="edit_categories_page"),
    path("update_category_page/<int:cat_id>", views.update_category_page, name="update_category_page"),
    path("delete_category_data/<int:cat_id>", views.delete_category_data, name="delete_category_data"),

    # Sub-category Section_____
    path("add_sub_categories/", views.add_sub_categories, name="add_sub_categories"),
    path("view_sub_categories/", views.view_sub_categories, name="view_sub_categories"),
    path("save_sub_categories/", views.save_sub_categories, name="save_sub_categories"),
    path("edit_sub_categories/<int:sub_id>", views.edit_sub_categories, name="edit_sub_categories"),
    path("update_sub_categories/<int:sub_id>", views.update_sub_categories, name="update_sub_categories"),
    path("delete_sub_category_data/<int:sub_id>", views.delete_sub_category_data, name="delete_sub_category_data"),

    # Product Section_______
    path("add_products/", views.add_products, name="add_products"),
    path("save_products/", views.save_products, name="save_products"),
    path("view_products/", views.view_products, name="view_products"),
    path("edit_products_page/<int:p_id>", views.edit_products_page, name="edit_products_page"),
    path("update_products_page/<int:p_id>", views.update_products_page, name="update_products_page"),
    path("delete_product_data/<int:p_id>", views.delete_product_data, name="delete_product_data"),

    # Admin Login_Logout Section
    path("", views.admin_login_page, name="admin_login_page"),
    path("admin_session_login/", views.admin_session_login, name="admin_session_login"),
    path("admin_logout/", views.admin_logout, name="admin_logout"),

    # Admin Trainer Approval and delete pages
    path("view_trainer_request/", views.view_trainer_request, name="view_trainer_request"),
    path("admin_trainer_request_view/<int:t_id>", views.admin_trainer_request_view, name="admin_trainer_request_view"),
    path("approve_trainer_request/<int:request_id>", views.approve_trainer_request, name="approve_trainer_request"),
    path("delete_trainer_request/<int:request_id>", views.delete_trainer_request, name="delete_trainer_request"),

    # Workout pages
    path("single_workout_page/", views.single_workout_page, name="single_workout_page"),
    path("daily_workout_page/", views.daily_workout_page, name="daily_workout_page"),

    # Single workout Category
    path("add_swkt_category/", views.add_swkt_category, name="add_swkt_category"),
    path("save_swkt_category/", views.save_swkt_category, name="save_swkt_category"),
    path("view_swkt_cat/", views.view_swkt_cat, name="view_swkt_cat"),
    path("edit_swkt_category/<int:w_id>", views.edit_swkt_category, name="edit_swkt_category"),
    path("update_swkt_category/<int:w_id>", views.update_swkt_category, name="update_swkt_category"),
    path("delete_swkt_category/<int:w_id>", views.delete_swkt_category, name="delete_swkt_category"),

    # Daily workout Category
    path("add_daily_workout_cat/", views.add_daily_workout_cat, name="add_daily_workout_cat"),
    path("save_daily_category/", views.save_daily_category, name="save_daily_category"),
    path("view_daily_cat/", views.view_daily_cat, name="view_daily_cat"),
    path("edit_daily_category/<int:w_id>", views.edit_daily_category, name="edit_daily_category"),
    path("update_daily_category/<int:w_id>", views.update_daily_category, name="update_daily_category"),
    path("delete_daily_category/<int:w_id>", views.delete_daily_category, name="delete_daily_category"),

    # Add Single Workout Videos
    path("add_single_workouts/", views.add_single_workouts, name="add_single_workouts"),
    path("save_single_workouts/", views.save_single_workouts, name="save_single_workouts"),
    path("view_single_workouts/", views.view_single_workouts, name="view_single_workouts"),
    path("edit_single_workouts/<int:s_id>", views.edit_single_workouts, name="edit_single_workouts"),
    path("update_single_workouts/<int:s_id>", views.update_single_workouts, name="update_single_workouts"),
    path("delete_single_workouts/<int:s_id>", views.delete_single_workouts, name="delete_single_workouts"),

    # Day Category
    path("add_day_category/", views.add_day_category, name="add_day_category"),
    path("save_day_category/", views.save_day_category, name="save_day_category"),
    path("view_day_category/", views.view_day_category, name="view_day_category"),
    path("add_daily_workouts/", views.add_daily_workouts, name="add_daily_workouts"),
    path("save_daily_workouts/", views.save_daily_workouts, name="save_daily_workouts"),
    path("view_daily_workouts/", views.view_daily_workouts, name="view_daily_workouts"),

    # Membership Plans
    path("membership_plan_page/", views.membership_plan_page, name="membership_plan_page"),
    path("add_membership_plan_page/", views.add_membership_plan_page, name="add_membership_plan_page"),
    path("save_membership_plan/", views.save_membership_plan, name="save_membership_plan"),
    path("view_membership_plan_page/", views.view_membership_plan_page, name="view_membership_plan_page"),
    path("delete_membership_plan/<int:m_id>", views.delete_membership_plan, name="delete_membership_plan"),

    # Feedbacks
    path("view_feedback_page/", views.view_feedback_page, name="view_feedback_page"),
    path("delete_feedback/<int:f_id>", views.delete_feedback, name="delete_feedback"),
]
