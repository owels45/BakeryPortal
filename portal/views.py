import datetime

from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render

from portal.models import Order, Invoice, Recipe, RecipeList
from .forms import *
from django.urls import reverse
from django.contrib.auth.models import User


# Create your views here.
# für die Berechtigungsüberprüfung können diese Decorator verwendet werden:
# @login_required ODER @permission_required('portal.<permissionName>')


def index(request):
    """
    View function for home page of site.
    """
    # variables for context
    num_customers = UserProfile.objects.all().count()
    # Number of visits to this view, as counted in the session variable.
    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_customers': num_customers}
    )


def register(request):
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        user_info_form = UserInformationForm(request.POST, prefix='user_info')
        user_profile_form = UserProfileForm(request.POST, prefix='user_profile')
        if user_creation_form.is_valid() * user_info_form.is_valid() * user_profile_form.is_valid():
            # user = user_creation_form.save()
            new_user = User(
                username=user_creation_form.cleaned_data['username'],
                first_name=user_info_form.cleaned_data['first_name'],
                last_name=user_info_form.cleaned_data['last_name'],
                email=user_info_form.cleaned_data['email']
            )
            new_user.set_password(raw_password=user_creation_form.cleaned_data['password2'])
            new_user.save()
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = new_user
            user_profile.save()
            return HttpResponseRedirect(reverse('registration_complete'))
    else:
        user_creation_form = UserCreationForm()
        user_info_form = UserInformationForm(prefix='user_info')
        user_profile_form = UserProfileForm(prefix='user_profile')
    return render(request, 'registration/registration_form.html',
                  context={
                      'user_form': user_creation_form,
                      'user_info_form': user_info_form,
                      'user_profile_form': user_profile_form,
                  })


def registration_complete(request):
    return render(
        request,
        'registration/registration_complete.html'
    )


def order(request):
    OrderFormset = formset_factory(OrderForm, extra=10)
    if request.method == 'POST':
        formset = OrderFormset(request.POST)
        resultString = 'Bitte loggen Sie sich ein um eine bestellung aufzugeben.'
        if formset.is_valid() and request.user.is_authenticated:
            resultString = 'Bitte geben Sie mindestens eine Bestellung in die Bestellzeilen ein.'
            if formset.has_changed():
                new_order = Order(kunde=request.user, bestell_datum=datetime.datetime.now())
                new_order.save()
                new_invoice = Invoice(
                    order=new_order,
                    rechnungs_datum=datetime.datetime.now(),
                    bezahl_status='offen',
                    rechnungs_summe=0
                )
                resultString = 'Bestellung erfolgreich. Ihre Bestellungsnummer ist: ' + str(new_order.id) + "."
                for form in formset:
                    recipe_id = form.cleaned_data.get('rezept')
                    amount = form.cleaned_data.get('menge')
                    if recipe_id and amount:
                        recipe_ingredients = RecipeList.objects.filter(recipe=recipe_id)
                        for recipe_list in recipe_ingredients:
                            new_invoice.rechnungs_summe += \
                                float(amount) * recipe_list.amount * recipe_list.ingredient.price_per_unit
                        OrderPosition(
                            bestellung=new_order,
                            rezept=recipe_id,
                            menge=amount,
                            als_teig=form.cleaned_data.get('als_teig')
                        ).save()
                new_invoice.rechnungs_summe = round(new_invoice.rechnungs_summe, 2)
                new_invoice.save()
        return render(
            request,
            'portal/order_processing.html',
            context={'order_result': resultString,
                     }
        )
    else:
        return render(
            request,
            'portal/order_form.html',
            context={'order_form': OrderFormset()}
        )


def myorders(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(kunde=request.user)
        return render(
            request,
            'portal/myorders.html',
            context={'myorders': orders}
        )
    else:
        return render(
            request,
            'portal/myorders.html'
        )


def myinvoices(request):
    if request.user.is_authenticated:
        invocies = Invoice.objects.filter(order__kunde=request.user)
        return render(
            request,
            'portal/myinvoices.html',
            context={'myinvoices': invocies}
        )
    else:
        return render(
            request,
            'portal/myinvoices.html'
        )


def invoicedetail(request):
    if request.GET['id'].isdigit():
        invoice = Invoice.objects.get(id=int(request.GET['id']))
        if invoice.order.kunde == request.user:
            order_positions = OrderPosition.objects.filter(bestellung=invoice.order)
            return render(
                request,
                'portal/invoice_detail.html',
                context={'invoice': invoice,
                         'orderposition': order_positions,
                         'mwst': round(invoice.rechnungs_summe * 0.19, 2),
                         'total': round(invoice.rechnungs_summe * 1.19, 2)}
            )
    return render(
        request,
        'portal/invoice_detail.html',
    )