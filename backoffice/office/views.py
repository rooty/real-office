# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

from .models import Message, MessageFolder, Project, Task, TaskState, OfficeContactInfo
from .forms import MessageForm, MessageReplyForm, TaskForm, ProjectForm, ContactInfoForm
from office.forms import ObjectPaymentForm, ObjectCostForm
from office.models import ObjectPayment, ObjectCost
from utils import is_staff_required
from utils.views import ProtectedListView
from advert.models import ContactInfo, ContactType, Advert


class MessagesList(ProtectedListView):
    model = Message
    context_object_name = 'messages'
    paginate_by = 10
    template_name = 'office/messages.html'
    partial_template_name = 'quotes/includes/quotes.html'


@is_staff_required
def view_home(request):
    return redirect('view_projects')


@is_staff_required
def viewmessages(request, folder_id=1):
    """
    view messages
    """
    qset = Q()
    folder_id = int(folder_id)
    if folder_id == 1:
        qset = Q(user_to=request.user)
    elif folder_id == 2:
        qset = Q(user_from=request.user, delivery=False)
    elif folder_id == 3:
        qset = Q(user_from=request.user, delivery=True)

    messages = Message.objects.filter(qset)

    paginator = Paginator(messages, 10)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        messages = paginator.page(page)
    except (InvalidPage, EmptyPage):
        messages = paginator.page(paginator.num_pages)

    return render(
        request,
        "office/messages.html",
        {
            'messages':messages,
            'messages_list':messages.object_list,
        }
    )

@is_staff_required
def new_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            newmessage = form.save(commit=False)
            newmessage.user_from = request.user
            newmessage.save()
            return redirect(reverse('view_messages', kwargs={'folder_id':1,},))
    else:
        form = MessageForm()
    userlist = User.objects.filter(is_staff=True)
    return render(
        request,
        "office/new_messages.html",
            {
            'form':form,
            'userlist':userlist,
            }
    )


@is_staff_required
def viewmessage(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    message.delivery = True
    message.readed = True
    message.save()

    return render(
        request,
        "office/message.html",
            {
                'message': message,
            }
    )

@is_staff_required
def reply_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.method == 'POST':
        form = MessageReplyForm(request.POST, request.FILES)
        if form.is_valid():
            newmessage = form.save(commit=False)
            newmessage.user_to = message.user_from
            newmessage.user_from = request.user
            newmessage.save()
            return redirect(reverse('view_messages', kwargs={'folder_id':1,},))
    else:
        form = MessageReplyForm()
    userlist = User.objects.filter(is_staff=True)
    return render(
        request,
        "office/new_messages.html",
            {
            'form':form,
            'userlist':userlist,
            }
    )



@is_staff_required
def del_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    message.delete()
    return redirect(reverse('view_messages', kwargs={'folder_id':1,},))

@is_staff_required
def view_projects(request):
    projects = Project.objects.all()

    paginator = Paginator(projects, 10)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        projects = paginator.page(page)
    except (InvalidPage, EmptyPage):
        projects = paginator.page(paginator.num_pages)

    return render(
        request,
        "office/projects_list.html",
            {
            'projects':projects,
            'projects_list':projects.object_list,
            }
    )


@is_staff_required
def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            newproject = form.save(commit=False)
            newproject.owner = request.user
            newproject.save()
            return redirect(reverse('view_project', kwargs={'project_id':newproject.id,},))
    else:
        form = ProjectForm()

    return render(
        request,
        "office/new_project.html",
            {
            'form': form,
            }
    )


@is_staff_required
def view_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = Task.objects.filter(project=project)

    return render(
        request,
        "office/project.html",
            {
            'project': project,
            'tasks':tasks,
            }
    )

@is_staff_required
def project_add_task(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            newtask = form.save(commit=False)
            newtask.project = project
            newtask.save()
            newmesage = Message.objects.create(
                user_from=request.user,
                user_to = newtask.worker,
                subject = u'Вам поставленна новая задача',
                body = u'Проект: <a href="/office/project/view/%s/">%s</a>. Вам поставлена задача: <a href="/office/project/view/%s/#task_%s">%s</a>' %
                       (project.id, project.title, project.id, newtask.id, newtask.title),
            )
            return redirect(reverse('view_project', kwargs={'project_id':project_id,},))
    else:
        form = TaskForm()

    return render(
        request,
        "office/new_task.html",
            {
            'form': form,
            'project':project,
            }
    )

@is_staff_required
def task_edit(request, task_id):
    task = Task.objects.get(pk=task_id)
    project = Project.objects.get(pk=task.project.id)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            newtask = form.save()
            return redirect(reverse('view_project', kwargs={'project_id':task.project.id,},))
    else:
        form = TaskForm(instance=task)

    return render(
        request,
        "office/new_task.html",
            {
            'form': form,
            'project':project,
            'task':task,
            }
    )


@is_staff_required
def edit_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            newproject = form.save()
            return redirect(reverse('view_project', kwargs={'project_id':newproject.id,},))
    else:
        form = ProjectForm(instance=project)

    return render(
        request,
        "office/new_project.html",
            {
            'form': form,
            }
    )

@is_staff_required
def view_contacts(request, type_id=0):
    contacttypes= ContactType.objects.all()
    if int(type_id) == 900:
        if request.user.is_superuser:
            contacts = OfficeContactInfo.objects.all()
        else:
            contacts = OfficeContactInfo.objects.filter(owner=request.user)
    elif type_id:
        contacts = ContactInfo.objects.filter(accounttype__id=type_id)
    else:
        contacts = ContactInfo.objects.all()

    paginator = Paginator(contacts, 10)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        contacts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        contacts = paginator.page(paginator.num_pages)

    return render(
        request,
        "office/contacts_list.html",
            {
            'contacts':contacts,
            'contacts_list':contacts.object_list,
            'contacttypes':contacttypes,
            'contacttype':type_id,
            }
    )


@is_staff_required
def view_contact(request, contact_id, type_id):
    # @todo: надо сделать проверку на owner
    if int(type_id) == 900:
        contact = get_object_or_404(OfficeContactInfo, pk=contact_id)
    else:
        contact = get_object_or_404(ContactInfo, pk=contact_id)

    return render(
        request,
        "office/contact.html",
            {
                'contact': contact,
                'contacttype':type_id,
            }
    )

@is_staff_required
def new_contact(request):
    if request.method == 'POST':
        form = ContactInfoForm(request.POST, request.FILES)
        if form.is_valid():
            newcontact = form.save(commit=False)
            newcontact.owner = request.user
            newcontact.save()
            return redirect(reverse('view_contact', kwargs={'contact_id':newcontact.id,'type_id':900},))
    else:
        form = ContactInfoForm()

    return render(
        request,
        "office/edit_contact.html",
            {
            'form': form,
            'contacttype':900,
            }
    )



@is_staff_required
def edit_contact(request, contact_id, type_id):
    if type_id == 900:
        contact = get_object_or_404(OfficeContactInfo, pk=contact_id)
    else:
        contact = get_object_or_404(ContactInfo, pk=contact_id)
    if request.method == 'POST':
        form = ContactInfoForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            newproject = form.save(commit=False)
            #newproject.owner = request.user
            newproject.save()
            return redirect(reverse('view_contact', kwargs={'contact_id':newproject.id,},))
    else:
        form = ContactInfoForm(instance=contact)

    return render(
        request,
        "office/edit_contact.html",
            {
            'form': form,
            'contact':contact,
            'contacttype':type_id,
            }
    )


@is_staff_required
def del_contact(request, contact_id):
    contact = get_object_or_404(OfficeContactInfo, pk=contact_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            newproject = form.save(commit=False)
            newproject.owner = request.user
            newproject.save()
            return redirect(reverse('view_contact', kwargs={'contact_id':newproject.id,},))
    else:
        form = ProjectForm()

    return render(
        request,
        "office/new_project.html",
            {
            'form': form,
            }
    )

@is_staff_required
def view_adverts(request, type_id=0):
    if int(type_id):
        if int(type_id) == 900:
            type_def_name = 'Сотрудник'
            adverts = Advert.objects.all()
        else:
            type_def_name = ContactType.objects.get(pk=type_id).name
            adverts = Advert.objects.filter(contact__accounttype__id=type_id)
    else:
        type_def_name = ''
        adverts = Advert.objects.all()

    contacttypes= ContactType.objects.all()

    paginator = Paginator(adverts, 10)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        adverts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        adverts = paginator.page(paginator.num_pages)

    return render(
        request,
        "office/adverts_list.html",
            {
            'adverts':adverts,
            'adverts_list':adverts.object_list,
            'contacttypes':contacttypes,
            'type_def_name':type_def_name,
            }
    )

@is_staff_required
def view_advert(request, advert_id):
    advert = get_object_or_404(Advert, pk=advert_id)

    payments = ObjectPayment.objects.filter(advert=advert)
    costs = ObjectCost.objects.filter(advert=advert)
    if request.method == 'POST':
        payform = ObjectPaymentForm(request.POST)
        costform = ObjectCostForm(request.POST)
        ex = False
        if payform.is_valid():
            newpay = payform.save(commit=False)
            newpay.advert = advert
            newpay.save()
            ex = True

        if costform.is_valid():
            newcost = costform.save(commit=False)
            newcost.advert = advert
            newcost.save()
            ex = True

        if ex:
            return redirect(reverse('view_advert', kwargs={'advert_id':advert_id,},))
    else:
        payform = ObjectPaymentForm()
        costform = ObjectCostForm()

    return render(
        request,
        "office/advert.html",
            {
                'advert':advert,
                'payments':payments,
                'costs':costs,
                'payform':payform,
                'costform':costform,
            }
    )

@is_staff_required
def edit_advert(request, advert_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = Task.objects.filter(project=project)

    return render(
        request,
        "office/project.html",
            {
            'project': project,
            'tasks':tasks,
            }
    )
