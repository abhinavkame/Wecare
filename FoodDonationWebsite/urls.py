"""NotesSharingWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',INDEX,name='home'),
    path('home',INDEX,name='home'),
    path('about',ABOUT,name='about'),
    path('contact',CONTACT,name='contact'),
    path('faqs',FAQs,name='faqs'),
    path('login',USERLOGIN,name='login'),
    path('LoginSup',USERLOGINSup,name='LoginSup'),
    path('admin-login',ADMINLOGIN,name='admin-login'),
    path('signup',SIGNUP,name="signup"),
    path('SignupSup',SIGNUPSup,name="SignupSup"),
    path('Static',static,name="Static"),
    path('admin_nav',ADMIN_NAV,name="admin_nav"),
    path('admin_home',ADMIN_HOME,name="admin_home"),
    path('admin_logout',ADMINLOGOUT,name="admin_logout"),
    path('view_users',VIEWUSERS,name="view_users"),
    path('view_users1',VIEWUSERS1,name="view_users1"),
    path('delete_users/<int:pid>',DELETEUSERS,name="delete_users"),
    path('user_nav',USERNAV,name="user_nav"),
    path('Sup_nav',SUPNAV,name="Sup_nav"),
    path('user_profile',USERPROFILE,name="user_profile"),
    path('edit_profile',EDITPROFILE,name="edit_profile"),
    path('user_logout',USERLOGOUT,name="user_logout"),
    path('change_pwd',CHANGEPASSWORD,name="change_pwd"),
    path('upload_notes',UPLOADNOTES,name="upload_notes"),
    path('view_notes',VIEWNOTES,name="view_notes"),
    path('view_funds',VIEWFUNDS,name="view_funds"),
    path('donatefund',donatefund,name="donatefund"),
    path('paypalpay',paypalpay,name="paypalpay"),
    path('delete_notes/<int:pid>',DELETENOTES,name="delete_notes"),
    path('delete_funds/<int:pid>',DELETEFUNDS,name="delete_funds"),
    path('pending_notes',PENDINGNOTES,name="pending_notes"),
    path('assign_notes/<int:pid>',ASSIGNNOTES,name="assign_notes"),
    path('accepted_notes',ACCEPTEDNOTES,name="accepted_notes"),
    path('donated',DONATED,name="donated"),
    path('rejected_notes',REJECTEDNOTES,name="rejected_notes"),
    path('all_notes',ALLNOTES,name="all_notes"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

