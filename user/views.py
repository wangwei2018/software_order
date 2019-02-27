import os
import json
from .models import User, Soft_Category, Order, Order_New
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, HttpResponse


# Create your views here.
def login(request):
    if request.method == "GET":
        status = request.GET.get("status")
        context = {"status": status}
        return render(request, 'login.html', context)
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if not user:
            context = {"status": "failed"}
            return render(request, 'login.html', context)
        else:
            auth.login(request, user)
            return HttpResponseRedirect("/index")


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")
        flag = 0
        for user in User.objects.all():
            if username == user.username:
                flag = 1
                break
        if flag == 0:
            new_user = User()
            new_user.username = username
            new_user.set_password(password)
            new_user.role = role
            new_user.save()
            return HttpResponseRedirect("/login?status=success")
        else:
            return render(request, 'register.html', {"status": "failed"})


@login_required
def index(request):
    role = request.user.role
    if role == "customer":
        return render(request, "customer.html")
    else:
        return render(request, "programmer.html")


@login_required
def upload_file(request):
    if request.method == "POST":
        soft_name = request.POST.get("soft_name")
        category_id = request.POST.get("select_category")
        desc = request.POST.get("remark")
        for key, file in request.FILES.items():
            dir_path = os.path.join(settings.ENROLLED_DATA, request.user.username)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            file_path = os.path.join(dir_path, file.name)
            if not os.path.exists(file_path):
                with open(file_path, "wb") as f:  # 打开文件
                    for chunk in file.chunks():
                        f.write(chunk)  # chunk方式写入文件
        order = Order()
        order.user_id = request.user
        order.category_id = Soft_Category.objects.get(id=category_id)
        order.soft_name = soft_name
        order.desc = desc
        order.package_url = file_path
        order.save()
        try:
            new_order = Order_New.objects.get(user_id=request.user)
        except:
            new_order = Order_New()
            new_order.user_id = request.user
            new_order.count = 0
        new_order.count += 1
        new_order.save()

    return HttpResponse("成功")


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index")


@login_required
def get_categories(request):
    if request.is_ajax():
        categories = Soft_Category.objects.all()
        info_list = []
        for category in categories:
            info = {}
            info["id"] = category.id
            info["name"] = category.name
            info_list.append(info)
        return HttpResponse(json.dumps(info_list))
    return None


@login_required
def get_new_orders(request):
    if request.is_ajax():
        try:
            new_order = Order_New.objects.get(user_id=request.user)
            return HttpResponse(json.dumps({"count": new_order.count}))
        except:
            pass
        return HttpResponse(json.dumps({"count": 0}))


@login_required
def my_order(request):
    orders = request.user.orders.all()
    new_order = request.user.new_order
    if new_order.count > 0:
        new_order.count = 0
        new_order.save()
    if not request.is_ajax():
        return render(request, "my_order.html", context={"orders": orders})
    else:
        order_list = []
        for order in orders:
            info = {}
            info["id"] = order.id
            info["soft_name"] = order.soft_name
            info["status"] = order.status
            info["desc"] = order.desc
            info["category"] = str(order.category_id)
            order_list.append(info)

        return HttpResponse(json.dumps(order_list))


@login_required
def delete_order(request):
    if request.is_ajax():
        order_id = request.POST.get("order_id")
        order = Order.objects.get(id=order_id)
        order.delete()
        return HttpResponse("success")


@login_required
def edit_order_info(request):
    if request.is_ajax():
        order_id = request.POST.get("order_id")
        order = Order.objects.get(id=order_id)
        info = {}
        info["id"] = order.id
        info["status"] = order.status
        info["soft_name"] = order.soft_name
        info["desc"] = order.desc
        info["category"] = order.category_id.name
        return HttpResponse(json.dumps(info))


@login_required
def edit_order(request):
    if request.is_ajax():
        order_id = request.POST.get("order_id")
        soft_name = request.POST.get("soft_name")
        soft_desc = request.POST.get("soft_desc")
        order = Order.objects.get(id=order_id)
        order.soft_name = soft_name
        order.desc = soft_desc
        order.save()
        return HttpResponse("成功")


@login_required
def get_orders(request):
    if request.is_ajax():
        orders = Order.objects.filter(status=0)
        order_list = []
        for order in orders:
            info = {}
            info["id"] = order.id
            info["soft_name"] = order.soft_name
            info["status"] = order.status
            info["desc"] = order.desc
            info["category"] = str(order.category_id)
            order_list.append(info)

        return HttpResponse(json.dumps(order_list))


@login_required
def receive_order(request):
    if request.is_ajax():
        order_id = request.POST.get("order_id")
        order = Order.objects.get(id=order_id)
        order.programer_id = request.user
        order.status = 1
        order.save()
        return HttpResponse("成功")


@login_required
def programer_order(request):
    orders = request.user.has_orders.all()
    if not request.is_ajax():
        return render(request, "programer_order.html")
    else:
        order_list = []
        for order in orders:
            info = {}
            info["id"] = order.id
            info["soft_name"] = order.soft_name
            info["status"] = order.status
            info["desc"] = order.desc
            info["category"] = str(order.category_id)
            order_list.append(info)

        return HttpResponse(json.dumps(order_list))

@login_required
def achive_order(request):
    order_id = request.POST.get("order_id")
    order = Order.objects.get(id=order_id)
    order.status=2
    order.save()
    return HttpResponse("成功")
