from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('shop/', views.shop, name='shop'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('usersignup/', views.usersignup, name='usersignup'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('adminuserlist/', views.adminuserlist, name='adminuserlist'),
    path('adminproductlist/', views.adminproductlist, name='adminproductlist'),
    path('adminaddproduct/', views.adminaddproduct, name='adminaddproduct'),
    path('updateproduct/', views.updateproduct, name='updateproduct'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('userblock/', views.userblock, name='userblock'),
    path('deleteproduct/', views.deleteproduct, name='deleteproduct'),
    path('adminaddcategory/', views.adminaddcategory, name='adminaddcategory'),
    path('shopsingle/', views.shopsingle, name='shopsingle'),
    path('updateproduct/<int:id>', views.updateproduct, name='updateproduct'),
    path('admincategorylist/', views.admincategorylist, name='admincategorylist'),
    path('deletecategory/', views.deletecategory, name='deletecategory'),
    path('updatecategory/', views.updatecategory, name='updatecategory'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('cart/', views.cart, name='cart'),
    path('otplogin/', views.otplogin, name='otplogin'),
    path('checkout/', views.checkout, name='checkout'),
    path('orderconfirm/', views.orderconfirm, name='orderconfirm'),
    path('delcartitems/', views.delcartitems, name='delcartitems'),
    path('updateaddress/<int:id>', views.updateaddress, name='updateaddress'),
    path('deleteaddress/', views.deleteaddress, name='deleteaddress'),
    path('address_select/', views.address_select, name='address_select'),
    path('order/', views.order, name='order'),
    path('plus_cart', views.plus_cart),
    path('minus_cart', views.minus_cart),
    path('cancelorder/<int:id>', views.cancelorder, name='cancelorder'),
    path('returnorder/<int:id>', views.returnorder, name='returnorder'),
    path('adminorderlist/', views.adminorderlist, name='adminorderlist'),
    path('updateorder/<int:id>', views.updateorder, name='updateorder'),
    path('paypal/', views.paypal, name='paypal'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('edituserprofile/', views.edituserprofile, name='edituserprofile'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('userotplogin/', views.userotplogin, name='userotplogin'),

]