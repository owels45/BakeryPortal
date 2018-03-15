from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import UserProfile
from .forms import UserForm, UserProfileForm
from django.shortcuts import render_to_response
from django.template import RequestContext


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
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.POST, prefix='user_profile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            user_profile = upf.save(commit=False)
            user_profile.user = user
            user_profile.save()
            return HttpResponseRedirect('/')
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='user_profile')
    return render(request, 'registration/register.html',context={'user_form': uf, 'user_profile_form': upf})
