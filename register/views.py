from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
from django.http import HttpResponse

from register.Schemas.Checking import *
from register.Schemas.Register import *
from register.Schemas.Person import *

from django.contrib.auth.models import User #Здесь все юзеры, тa модель нах не нужна
from django.contrib import auth
from django.contrib.auth import logout as django_logout
from django.template import Context, loader


def home(request):
    return redirect("/register")


def address(request):
    return render(request, 'address.html')


def contact(request):
    return render(request, 'contact.html')


def banished(request):
    return render(request, 'banished.html')


def checking(request):
    checking1 = get_all_checking()

    search = "none"
    is_search = False
    is_empty = True
    counter_1 = 1
    counter_2 = 1

    if request.method == "POST":
        _search = request.POST['search']

        checking1 = find_checking_by_person_name(_search)
        if checking1:
            is_empty = False
        is_search = True
        search = _search

    return render(request, 'checking.html', locals())


def court_proceedings(request):
    return render(request, 'court_proceedings.html')


def documents(request):
    return render(request, 'documents.html')


def question(request):
    return render(request, 'question.html')


def work_material(request):
    return render(request, 'work_material.html')


def work_material_1(request):
    return render(request, 'work_material_1.html')


def work_material_2(request):
    return render(request, 'work_material_2.html')


def work_material_3(request):
    return render(request, 'work_material_3.html')


def work_material_6(request):
    return render(request, 'work_material_6.html')


def data_about_checking(request):
    return render(request, 'data_about_checking.html')


def public_council(request):
    return render(request, 'public_council.html')


def public_council_2(request):
    return render(request, 'public_council_2.html')


def public_council_3(request):
    return render(request, 'public_council_3.html')


def public_council_4(request):
    return render(request, 'public_council_4.html')


def public_council_5(request):
    return render(request, 'public_council_5.html')


def register(request):

    register1 = get_all_register()
    search = "none"
    is_search = False
    is_empty = True

    if request.method == "POST":
        _search = request.POST['search']

        register1 = find_register_by_person_name(_search)
        if register1:
            is_empty = False
        is_search = True
        search = _search

    return render(request, 'register.html', locals())


def login(request):
    error_message = 0

    if request.user.is_authenticated:
        if request.user.is_active:
            return redirect("/admin_register")
        else:
            logout(request)
            error_message = 2
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                print("Login successful")
                return redirect("/admin_register")

            else:
                print("login error")
                error_message = 1

    return render(request, 'login.html', locals())


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("/")


def admin_checking(request):
    if request.user.is_authenticated:
        checking1 = get_all_checking()

        search = "none"
        is_search = False
        is_empty = True

        if request.method == "POST":
            _search = request.POST['search']

            checking1 = find_checking_by_person_name(_search)
            if checking1:
                is_empty = False
            is_search = True
            search = _search

        return render(request, 'admin_checking.html', locals())
    else:
        return render(request, '401.html')


def admin_checking_add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST['name']
            category = request.POST['category']
            job = request.POST['job']
            position = request.POST['position']
            region = request.POST['region']
            isPretender = request.POST['isPretender']
            solution = request.POST['solution']
            date_accept_ban = request.POST['date_accept_ban']
            date_refuse_ban = request.POST['date_refuse_ban']
            resolution = request.POST['resolution']

            if add_new_checking(add_new_person(name, category, job, position, region, isPretender), solution, resolution,
                             date_accept_ban, date_refuse_ban) == -1:
                return render(request, '500.html')
    return redirect("/admin_checking")


def admin_checking_delete(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
           if delete_checking(id) == -1:
               return render(request, '500.html')
    return redirect("/admin_checking")


def admin_checking_update(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST['name']
            category = request.POST['category']
            job = request.POST['job']
            position = request.POST['position']
            region = request.POST['region']
            isPretender = request.POST['isPretender']
            solution = request.POST['solution']
            date_accept_ban = request.POST['date_accept_ban']
            date_refuse_ban = request.POST['date_refuse_ban']
            resolution = request.POST['resolution']
            if update_checking_with_person(id, name, category, job, position, region, solution, resolution,
                                        date_refuse_ban,
                                        date_accept_ban, isPretender) == -1:
                return render(request, '500.html')
    else:
        return render(request, '401.html')
    return redirect("/admin_checking")


def admin_checking_move(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            result = request.POST['result']
            ban_time = request.POST['ban_time']
            if move_checking(id, result, ban_time) == -1:
                return render(request, "500.html")
    return redirect("/admin_checking")


def admin_register(request):
    if request.user.is_authenticated:
        register1 = get_all_register()

        search = "none"
        is_search = False
        is_empty = True

        if request.method == "POST":
            _search = request.POST['search']

            register1 = find_register_by_person_name(_search)
            if register1:
                is_empty = False
            is_search = True
            search = _search

        return render(request, 'admin_register.html', locals())
    else:
        return render(request, '401.html')


def admin_register_add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST['name']
            category = request.POST['category']
            job = request.POST['job']
            position = request.POST['position']
            region = request.POST['region']
            isPretender = request.POST['isPretender']
            result = request.POST['result']
            ban_time = request.POST['ban_time']
            if add_new_register(add_new_person(name, category, job, position, region, isPretender), result, ban_time) == -1:
                return render(request, '500.html')
    else:
        return render(request, '401.html')
    return redirect("/admin_register")


def admin_register_delete(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            if delete_register(id) == -1:
                return render(request, '500.html')
    else:
        return render(request, '401.html')
    return redirect("/admin_register")


def admin_register_update(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST['name']
            category = request.POST['category']
            job = request.POST['job']
            position = request.POST['position']
            region = request.POST['region']
            isPretender = request.POST['isPretender']
            result = request.POST['result']
            ban_time = request.POST['ban_time']
            if update_register_with_person(id, name, category, job, position, region, result, ban_time, isPretender) == -1:
                return render(request, '500.html')
    else:
        return render(request, '401.html')
    return redirect("/admin_register")


def admin_users(request):
    if request.user.is_authenticated and request.user.is_superuser:
        error_message = 0
        users = User.objects.all()

        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']
            email = request.POST['email']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']

            if User.objects.filter(username=username).exists():
                error_message = 2
            else:
                if password == password2:
                    user = User.objects.create_user(username=username,
                                                    password=password,
                                                    email=email,
                                                    first_name=firstname,
                                                    last_name=lastname)
                    user.is_staff = True
                    user.save()
                else:
                    error_message = 1

        return render(request, 'admin_users.html', locals())
    else:
        return render(request, '401.html')


def admin_users_admin_deadmin(request, username):
    user = request.user
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            try:
                u = User.objects.get(username=username)
                if u.is_superuser:
                    u.is_superuser = False
                else:
                    u.is_superuser = True
                u.save()
                auth.logout(request)
                auth.login(request, user)

            except User.DoesNotExist:
                print("User does not exist")
                return render(request, '404.html')
    else:
        return render(request, '401.html')
    return redirect("/admin_users")


def admin_users_ban_deban(request, username):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            try:
                u = User.objects.get(username=username)
                if u.is_active:
                    u.is_active = False
                else:
                    u.is_active = True
                u.save()

            except User.DoesNotExist:
                print("User does not exist")
                return render(request, '404.html')
    else:
        return render(request, '401.html')
    return redirect("/admin_users")


def admin_users_delete(request, username):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            try:
                u = User.objects.get(username=username)
                u.delete()
                print("The user is deleted")
            except User.DoesNotExist:
                print("User does not exist")
                return render(request, '404.html')
    else:
        return render(request, '401.html')

    return redirect("/admin_users")






