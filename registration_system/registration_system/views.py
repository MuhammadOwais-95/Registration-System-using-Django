
from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from registration_system import settings
from django.core.mail import send_mail,EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token


@login_required(login_url="Login_page")
def home(request):
    # print(custom_messages)
    return render(request,'index.html')

def SignUpPage(request):
    return render(request,'sign_up.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        f_name = request.POST.get('firstname')
        l_name = request.POST.get('lastname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! please try some other Username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request,"Password Did'nt matched")
            return redirect(request,'home')
        
        my_user = User.objects.create_user(username,email,pass1)
        my_user.first_name = f_name
        my_user.last_name = l_name
        my_user.is_active = False
        my_user.save()

        messages.success(request,"Account Successfully Created!! Please check your email to confirm your email address in order to activate your account.")
        
        # welcome emial

        subject = "Welcome to Powerfull Solutions || Django Login!!"
        message = (
            "Hello " + my_user.email + "!! \n"
            "Welcome to Powerfull Solutions!! \n"
            "Thank you for visiting our website\n."
            "We have also sent you a confirmation email, "
            "please confirm your email address. \n\n"
            "Thanking You\n Muhammad Owais"
        )
        email_from = settings.EMAIL_HOST_USER  
        recipient_list = [my_user.email]
        send_mail(subject, message, email_from, recipient_list)


        #confirmation email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ PS - Django Login!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': my_user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token': generate_token.make_token(my_user)
        })
        
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [my_user.email],
        )
        email.fail_silently = True
        email.send()
    
        return redirect('Login_page')
    else:
        return render(request,"sign_up.html")
    

def activate(request,uidb64,token):
    try:
        uid =force_str(urlsafe_base64_decode(uidb64))
        my_user = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        my_user = None

    if my_user is not None and generate_token.check_token(my_user,token):
        my_user.is_active = True
        # user.profile.signup_confirmation = True
        my_user.save()
        login(request,my_user)
        messages.success(request, "Your Account has been activated!!")
        return redirect('Login_page')
    else:
        return render(request,'activation_failed.html')





# user login
def Login_page (request):
    return render(request,'login.html')

def user_login (request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("password1")
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request,f"Hello! {username} ")
            messages.success(request,"Successfully Loged In!")
            messages.success(request,"Now You can Sign up, Sign in, or Log out.")
            return redirect("home")
        else:
            messages.error(request,"Wrong! username OR password")
            return render(request,'login.html')


# user logout 
def user_logout(request):
    logout(request)
    messages.success(request,"Successfully Loged out!")
    return redirect('Login_page')  # Redirect to a named URL pattern or a URL string.

        