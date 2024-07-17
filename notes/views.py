from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login
from datetime import date
# Create your views here.
def paypalpay(request):
    if not request.user.is_authenticated:
        return redirect('login')
    donate = DonateFund.objects.all()
    d = { 'donate': donate }
    return render(request, 'donate_fund.html',d)

def donatefund(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method == "POST":
        f = request.POST['donatefund']
        u1 = User.objects.filter(username = request.user.username).first()
        try:
            DonateFund.objects.create(user=u1,donatefund=f)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request, 'store.html',d)

def NAV(request):
    return render(request,'navigation.html')

def INDEX(request):
    return render(request,'index.html')

def ABOUT(request):
    return render(request,'about.html')

def CONTACT(request):
    return render(request,'contact.html')

def FAQs(request):
    return render(request,'faqs.html')

def USERLOGIN(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user:
                login(request,user)
                error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'login.html',d)

def USERLOGINSup(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user:
                login(request,user)
                error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'LoginSup.html',d)

def USERLOGOUT(request):
    logout(request)
    return redirect('home')

def USERNAV(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id = request.user.id)
    data = Signup.objects.get(user = user)
    d = {'user':user,'data':data}
    return render(request,'user_nav.html',d)

def SUPNAV(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id = request.user.id)
    data = Signup.objects.get(user = user)
    d = {'user':user,'data':data}
    return render(request,'Sup_nav.html',d)
def USERPROFILE(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id = request.user.id)
    data = Signup.objects.get(user = user)
    d = {'user':user,'data':data}
    return render(request,'profile.html',d)

def EDITPROFILE(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id = request.user.id)
    data = Signup.objects.get(user = user)
    
    error = "true"
    if request.method == "POST":
        f = request.POST['firstname']
        l = request.POST['lastname']
        c = request.POST['contact']
         
        
        e = request.POST['eid'] 
        user.first_name = f
        user.last_name = l
        data.contact = c
      
        user.username = e

        user.save()
        data.save()
        error="false"

    d = {'user':user,'data':data,'error':error}
    return render(request,'edit_profile.html',d)

def CHANGEPASSWORD(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method == 'POST':
        o = request.POST['pwd']
        n = request.POST['new_pwd']
        c = request.POST['cnfrm_pwd']
        if n == c:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "no"
        else:
            error = "yes"
    d = {'error':error}
    return render(request,'change_pwd.html',d)

def UPLOADNOTES(request):
    if not request.user.is_authenticated:
       return redirect('login')
    error = ""
    if request.method == "POST":
        b1 = request.POST['branch1']
        s1 = request.POST['subject1']
        n1 = request.FILES['notesfile1']
        f1 = request.POST['filetype1']  
        st1= request.POST['state'] 
        ci1= request.POST['city'] 
        d1 = request.POST['description1']
        u1 = User.objects.filter(username = request.user.username).first()
        try:
            Notes.objects.create(user=u1,uploadingdate=date.today(),branch=b1,subject=s1,notesfile=n1,filetyoe=f1,state=st1,city=ci1,description=d1,status='pending')
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'upload_notes.html',d)   

def VIEWNOTES(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id = request.user.id)
    notes = Notes.objects.filter(user = user)

    d = {'notes':notes}
    return render(request,'view_notes.html',d) 

def VIEWFUNDS(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id = request.user.id)
    donate = DonateFund.objects.filter(user = user)

    d = {'donate':donate}
    return render(request,'view_funds.html',d) 

def DELETENOTES(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('view_notes') 

def DELETEFUNDS(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    donate = DonateFund.objects.get(id=pid)
    donate.delete()
    return redirect('view_funds') 

def ADMIN_HOME(request):
    if not request.user.is_staff:
        return redirect('ADMINLOGIN')
    pn = Notes.objects.filter(status = "pending").count()
    ac = Notes.objects.filter(status = "accepted").count()
    re = Notes.objects.filter(status = "rejected").count()
    do = Notes.objects.filter(status = "donated").count()
    al = Notes.objects.all().count()
    d = {'pn':pn,'ac':ac,'re':re,'al':al,'do':do}
    return render(request,'admin_home.html',d)

def ADMIN_NAV(request):
    if not request.user.is_staff:
        return redirect('ADMINLOGIN')
    return render(request,'admin_nav.html')

def VIEWUSERS(request):
    if not request.user.is_authenticated:
        return redirect('admin-login')
    user = Signup.objects.all()
    d = {'user':user}
    return render(request,'view_users.html',d) 

def VIEWUSERS1(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = Signup.objects.all()
    d = {'user':user}
    return render(request,'view_users1.html',d) 

def DELETEUSERS(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin-login')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('view_users') 

def ADMINLOGIN(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'admin-login.html',d)   

def PENDINGNOTES(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status = "pending")

    d = {'notes':notes}
    return render(request,'pending_notes.html',d)

def ASSIGNNOTES(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.get(id=pid)
    error = ""
    if request.method == 'POST':
        s = request.POST['status']
        try:
            notes.status = s
            notes.save()
            error = "no"
        except:
            error = "yes"
    d ={'error':error,'notes':notes}
    return render(request,'assign_status.html',d) 

def ACCEPTEDNOTES(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status = "accepted"
        )

    d = {'notes':notes}
    return render(request,'accepted_notes.html',d)

def DONATED(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status = "donated")

    d = {'notes':notes}
    return render(request,'donated.html',d)

def REJECTEDNOTES(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status = "rejected")

    d = {'notes':notes}
    return render(request,'rejected_notes.html',d)

def ALLNOTES(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.all()

    d = {'notes':notes}
    return render(request,'all_notes.html',d)    

def ADMINLOGOUT(request):
    logout(request)
    return redirect('home')

def SIGNUP(request):
    error = ""
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        e = request.POST['emailid'] 
        ps = request.POST['pwd']
        
        try:
            user = User.objects.create_user(username=e,password=ps,first_name=f,last_name=l)
            Signup.objects.create(user=user,contact=c)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'signup.html',d)   


def SIGNUPSup(request):
    error = ""
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        e = request.POST['emailid'] 
        ps = request.POST['pwd']
        
        try:
            user = User.objects.create_user(username=e,password=ps,first_name=f,last_name=l)
            Signup.objects.create(user=user,contact=c)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'SignupSup.html',d)   