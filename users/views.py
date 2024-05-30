from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Profile
from .forms import NewUserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/myapp/products')

    form = NewUserForm()
    return render(request, 'users/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def create_profile(request):
    if request.method == 'POST':
        contact_number = request.POST.get('contact_number')
        image = request.FILES['upload']
        user = request.user
        profile = Profile(user=user, image=image, contact_number=contact_number)
        profile.save()
    return render(request, 'users/createprofile.html')

def seller_profile(request, id):
    return render(request, 'users/sellerprofile.html', {'seller': User.objects.get(id=id)})