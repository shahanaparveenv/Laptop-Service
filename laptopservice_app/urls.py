from django.urls import path

from laptopservice_app import views

urlpatterns = [
    path('hello',views.hello,name='hello'),
    path('', views.home, name='index'),
    path('login_view', views.login_view, name='login_view'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('Registration_User', views.Registration_User,name='Registration_User'),
    path('customerbase', views.customerbase, name = 'customerbase'),
    path('customer_add', views.customer_add, name = 'customer_add'),
    path('sellerbase', views.sellerbase, name = 'sellerbase'),
    path('seller_add', views.seller_add, name = 'seller_add'),
    path('adminbase', views.adminbase, name = 'adminbase'),
    path('customer_view', views.customer_view, name = 'customer_view'),
    path('seller_view', views.seller_view, name = 'seller_view'),
    path('delete/<int:id>/', views.customer_delete,name='delete'),
    path('seller_delete/<int:id>/', views.seller_delete,name='seller_delete'),
    path('feedback_form',views.save_feedback,name='feedback_form'),
    path('view_customer_feedback',views.view_customer_feedback,name='view_customer_feedback'),
    path('view_seller_feedback',views.view_seller_feedback,name='view_seller_feedback'),
    # path('feedback_delete/<int:id>/', views.feedback_delete,name='feedback_delete'),
    path('customer_feedback',views.customer_feedback,name='customer_feedback'),
    path('seller_feedback_form',views.save_seller_feedback,name='seller_feedback_form'),
    path('seller_feedback',views.seller_feedback,name='seller_feedback'),
    path('update/<int:id>/',views.admin_reply_feedback,name='update'),
    path('sellerupdate/<int:id>/',views.admin_seller_reply_feedback,name='sellerupdate'),
    path('addProduct',views.product_seller,name='addProduct'),
    path('viewProduct',views.product_display,name='viewProduct'),
    path('productdelete/<int:id>/', views.product_delete,name='productdelete'),
    path('product_view',views.product_view,name='product_view'),
    path('customer_product_view',views.customer_product_view,name='customer_product_view'),
    path('add_to_cart/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('viewCart',views.viewCart, name='viewCart'),
    path('deleteItems/<int:id>/', views.deleteItems,name='deleteItems'),
    path('buynow/<int:id>/', views.buynow, name='buynow'),
    path('payment/<int:id>/', views.paynow, name='payment'),


]