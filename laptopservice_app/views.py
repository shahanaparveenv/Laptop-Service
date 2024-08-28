from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from laptopservice_app.forms import LoginRegister, CustomerRegister, SellerRegister, FeedbackForm, ReplyFeedbackForm, \
    SellerFeedbackForm, ReplySellerFeedbackForm, ProductSellerForm
from laptopservice_app.models import Customer, Seller, Feedback, SellerFeedback, Product, AddToCart, BuyNow, Payment


# Create your views here.
def hello(request):
    return render(request,'hello.html')
def home(request):
    return render(request, 'index.html')
# def userlogin(request):
#     return render(request, 'indexlogin.html')
def dashboard(request):
    return render(request,'dashboard.html')
def adminbase(request):
    return render(request,'admin/adminbase.html')
def customerbase(request):
    return render(request,'customer/customerbase.html')
def sellerbase(request):
    return render(request,'seller/sellerbase.html')

def customer_add(request):
    return render(request,'customer/customer_add.html')
def customer_view(request):
    return render(request,'customer/customer_view.html')
def Registration_User(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        if form1.is_valid():
            form1.save()
    return render(request,'reg.html',{'form':form})


def customer_add(request):
    form1=LoginRegister()
    form2=CustomerRegister()
    if request.method == 'POST':
        form1 = LoginRegister(request.POST)
        form2 = CustomerRegister(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_customer = True
            a.save()
            user1=form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect('customerbase')
    return render(request, 'customer/customer_add.html', {'form1':form1, 'form2':form2})

def customer_view(request):
    data=Customer.objects.all()
    return render(request,'customer/customer_view.html',{'data':data})



#delete
def customer_delete(request,id):
    data=Customer.objects.get(id=id)
    data.delete()
    return redirect('customer_view')

def seller_add(request):
    form1=LoginRegister()
    form2=SellerRegister()
    if request.method == 'POST':
        form1=LoginRegister(request.POST)
        form2=SellerRegister(request.POST)

        if form1.is_valid() and form2.is_valid():
            a=form1.save(commit=False)
            a.is_seller = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect('sellerbase')
    return render(request,'seller/seller_add.html',{'form1':form1, 'form2':form2})

def seller_view(request):
    data=Seller.objects.all()
    return render(request,'seller/seller_view.html',{'data':data})



#delete
def seller_delete(request,id):
    data=Seller.objects.get(id=id)
    data.delete()
    return redirect('seller_view')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminbase')
            elif user.is_customer:
                return redirect('customer_product_view')
            elif user.is_seller:
                return redirect('sellerbase')
        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'indexlogin.html')

#saving customer feedback
def save_feedback(request):
    user=request.user
    customer=Customer.objects.get(user=user)
    data=FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            a=form.save(commit=False)
            a.user=customer
            a.save()
            return redirect('customerbase')
    return render(request,'customer/feedback_form.html',{'form': data})


#customer feedback viewing
def customer_feedback(request):
    user=request.user
    customer=Customer.objects.get(user=user)
    data = Feedback.objects.filter(user=customer)
    return render(request, 'customer/customer_feedback.html', {'data': data})



#seller feedback viewing
def seller_feedback(request):
    data = SellerFeedback.objects.all()
    return render(request, 'seller/seller_feedback.html', {'data': data})

#save seller feedback
def save_seller_feedback(request):
    user=request.user
    seller=Seller.objects.get(user=user)
    data=SellerFeedbackForm()
    if request.method == 'POST':
        form = SellerFeedbackForm(request.POST)
        if form.is_valid():
            a=form.save(commit=False)
            a.user=seller
            a.save()
            return redirect('sellerbase')
    return render(request,'seller/seller_feedback_form.html',{'data': data})


def view_customer_feedback(request):
    data = Feedback.objects.all()
    return render(request, 'admin/feedback_view.html', {'data': data})


def view_seller_feedback(request):
    data = SellerFeedback.objects.all()
    return render(request, 'admin/feedback_seller_view_admin.html', {'data': data})

def admin_reply_feedback(request,id):

    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST' :
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request,'Reply send for complaint')
        return redirect('view_customer_feedback')
    return render(request,'admin/feedback_reply.html',{'feedback':feedback})

def admin_seller_reply_feedback(request,id):

    reply = SellerFeedback.objects.get(id=id)
    data = ReplySellerFeedbackForm(instance=reply)
    if request.method == 'POST' :
        form = ReplySellerFeedbackForm(request.POST, instance=reply)
        if form.is_valid():
            form.save()
            return redirect('view_seller_feedback')
    return render(request,'admin/feedback_seller_reply.html',{'data':data})

#products
def product_seller(request):
    user = request.user
    sellerProduct = Seller.objects.get(user=user)
    form = ProductSellerForm()
    if request.method == 'POST':
        form1=ProductSellerForm(request.POST, request.FILES)
        if form1.is_valid():
            a=form1.save(commit=False)
            a.seller=sellerProduct
            a.save()
            messages.info(request,'product added')
            return redirect('viewProduct')
    return render(request,'seller/add_product.html',{'form':form})


def product_display(request):
    user=request.user
    sellerProduct = Seller.objects.get(user=user)
    data=Product.objects.filter(seller=sellerProduct)
    return render(request,'seller/product_display.html',{'data':data })

def product_delete(request,id):
    data=Product.objects.get(id=id)
    data.delete()
    return redirect('viewProduct')

#general product view
def product_view(request):
    data=Product.objects.all()
    return render(request,'product_view.html',{'data':data})

#product view by customer
def customer_product_view(request):
    data=Product.objects.all()
    return render(request,'customer/customer_product_view.html',{'data':data})

#add product to cart -- method 1
# def add_to_cart(request, id):
#     user=request.user
#     customer=Customer.objects.get(user=user)
#     product = Product.objects.get(id=id)
#     AddToCart.objects.create(customer=customer, product=product)
#     return redirect('customer_product_view')

#add product to cart -- method 2
# def add_to_cart(request, id):
#     user=request.user
#     customer=Customer.objects.get(user=user)
#     product = Product.objects.get(id=id)
#     obj= AddToCart()
#     obj.customer=customer
#     obj.product=product
#     obj.save()
#     return redirect('customer_product_view')

#add product to cart -- method 3
def add_to_cart(request, id):
    user=request.user
    customer=Customer.objects.get(user=user)
    product = Product.objects.get(id=id)
    cart_item=AddToCart.objects.filter(customer=customer,product=product)
    if cart_item.exists():
        messages.info(request,"Item already exists")
        return redirect('customer_product_view')
    else:
        obj = AddToCart(customer=customer, product=product)
        obj.save()
        return redirect('customer_product_view')


def viewCart(request):
    user=request.user
    customer = Customer.objects.get(user=user)
    data=AddToCart.objects.filter(customer=customer)
    total=sum(int(i.product.price) for i in data)
    return render(request,'view_cart.html',{'data':data, 'total':total})

def deleteItems(request,id):
    product=AddToCart.objects.get(id=id)
    product.delete()
    return redirect('viewCart')

# buy now function
def buynow(request,id):
    user=request.user
    userid = Customer.objects.get(user=user)
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        count = int(request.POST.get('count'))
        address = request.POST.get('address')
        phonenumber = request.POST.get('phone')
        postcode = request.POST.get('post')
        if product.count < count :
            messages.info(request,'not available')
        else:
            a=product.price
            total=int(a)*count

            obj = BuyNow()
            obj.user = userid
            obj.product = product
            obj.quantity=count
            obj.totalprice=total
            obj.address=address
            obj.phone=phonenumber
            obj.post=postcode
            obj.save()
            return redirect('payment',id=obj.id)
    return render(request,'buy_now.html',{'user':user, 'userid':userid, 'product':product})

def paynow(request,id):
    buynow_id = BuyNow.objects.get(id=id)
    user = Customer.objects.get(user=request.user)
    data = buynow_id
    c = data.product

    if request.method == 'POST':
        cardnumber = request.POST.get('cardnumber')
        cvv = request.POST.get('cvv')
        date = request.POST.get('date')
        Payment.objects.create(cardnumber=cardnumber, cvv=cvv, expiry_date=date, buynowProduct=buynow_id)
        data.buynow_status = 1
        data.save()
        a= int(buynow_id.product.count - buynow_id.quantity)
        c.count = a
        c.save()
        return redirect('customer_product_view')
    return render(request, 'payment.html', {'buynow_id': buynow_id, 'user':user})




