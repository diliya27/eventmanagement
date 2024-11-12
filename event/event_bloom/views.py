import razorpay
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import BookingForm
from .models import Story, Service, Inform, Wedding, Weddingdetail, Event, Payment, Book_event
from django.contrib.auth import authenticate,login



# Create your views here.
def home(request):
    return render(request,'base.html')


def story(request):
    item=Story.objects.all()
    return render(request,'story.html',{'item':item})

def storydetail(request,id):
    s=Story.objects.get(id=id)
    return render(request,'storydetail.html',{'s':s})

def gallery(request):
    return render(request,'gallery.html')
def service(request):
    item = Service.objects.all()

    return render(request,'service.html',{'item':item})

def servicedetail(request,id):
    v=Service.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        info = Inform.objects.create(name=name,number=number,email=email,message=message)
        info.save()
    return render(request,'servicedetail.html',{'v':v})

def inform(request):
    item = Inform.objects.all()
    return render(request,'inform.html',{'item': item})

def dest(request):
    return  render(request,'destination.html')
def beach(request):
    return render(request,'beach.html')
def wedding(request):
    item= Wedding.objects.all()
    return render(request,'wedding.html',{'item':item})

def weddingdetail(request,id):
    w = Story.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        wed = Weddingdetail.objects.create(name=name,number=number,email=email,message=message)
        wed.save()
    return render(request,'weddingdetail.html',{'w':w})
# def booking(request):
#     if request.method=='POST':
#         form=BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     form=BookingForm()
#
#     return render(request,'booking.html',{'form':form})
def register(request):
    if (request.method == 'POST'):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if (cp == p):
            s = User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
            s.save()
            return redirect('home')
    return render(request,'register.html')

def user_login(request):
    if (request.method == 'POST'):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, "invalid credentials")

    return render(request,'login.html')
def user_logout(request):

    logout(request)
    return redirect('/login/')

def add_to_event(request,ev):
    s=Service.objects.get(id=ev)
    u=request.user
    a = s.advance_amt
    event = Event.objects.create(service=s, user=u,advance_amt=a)
    event.save()
    # return  HttpResponse("event  added")
    return redirect('event_bloom:event_view')

def event_view(request):
    u=request.user
    event=Event.objects.filter(user=u)
    total=0
    for i in event:
        total=total+i.service.advance_amt
    return render(request, 'event.html',{'event':event,'total':total})

@login_required()
def book_event(request):

    if(request.method=='POST'):
        phone=request.POST.get('phone')
        u=request.user
        e=Event.objects.filter(user=u)
        total = 0
        for i in e:
            total = total + i.service.advance_amt  # Total amount
        total = int(total * 100)

        # create Razorpay client using our API credentials
        client = razorpay.Client(auth=('rzp_test_WwAeIbYfM7kzyI', 'FPK6OKnPtRRvAm0lRNyu6qVt'))

        # create order in Razorpay
        response_payment = client.order.create(dict(amount=total, currency='INR'))
        #
        #

        print(response_payment)

        book_id = response_payment['id']
        book_status = response_payment['status']
        if book_status == "created":
            p = Payment.objects.create(name=u.username, amount=total, book_id=book_id)
            p.save()
            noe = len(e)
            for i in e:
                o = Book_event.objects.create(user=u, event=i.service, no_of_events=noe, order_id=book_id,phone=phone)
                o.save()
        response_payment['name']=u.username
        return render(request, 'payment.html', {'payment': response_payment})

    return render(request, 'book_event.html')


@csrf_exempt
def payment_status(request,u):
    print(request.user.is_authenticated)  # false
    if not request.user.is_authenticated:
        user = User.objects.get(username=u)
        login(request, user)
        print(user.is_authenticated)  # true

    if(request.method=='POST'):
        response=request.POST
        print(response)
        # to check the authenticity of razorpay signature
        param_dict = {
            'razorpay_order_id': response['razorpay_order_id'],
            'razorpay_payment_id': response['razorpay_payment_id'],
            'razorpay_signature': response['razorpay_signature']
        }
        client = razorpay.Client(auth=('rzp_test_WwAeIbYfM7kzyI', 'FPK6OKnPtRRvAm0lRNyu6qVt'))
        try:
            status = client.utility.verify_payment_signature(param_dict)  # to check the authenticity of razorpay signature
            print(status)

            ord = Payment.objects.get(book_id=response['razorpay_order_id'])
            ord.razorpay_payment_id = response['razorpay_payment_id']  # edit payment id response['razorpay_payment_id']
            ord.paid = True  # edit paid to true
            ord.save()
            print('saved')
            o = Book_event.objects.filter(user=user, order_id=response['razorpay_order_id'])
            print(o)
            event = Event.objects.filter(user=user)
            for i in o:
                i.payment_status = "paid"  # edit payment_status="paid
                i.save()

            print(status)
            event.delete()
            return render(request, 'payment_status.html', {'status': True})
        except:
            return render(request, 'payment_status.html', {'status': False})
    return render(request, 'payment_status.html')



















