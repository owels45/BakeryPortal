from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import UserProfile
from .forms import *
from django.urls import reverse


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
        context={'num_customers': num_customers, },
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
