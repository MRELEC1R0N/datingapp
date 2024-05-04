from django.shortcuts import render,redirect ,HttpResponse
from .forms import UserSignUpForm , UserProfileForm,MessageForm
from django.contrib.auth import authenticate, login 
from .models import UserProfile , Message
from django.contrib.auth.models import User



# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def user_signup(request):
    if request.method == 'POST':
        user_form = UserSignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user_profile = profile_form.save(commit=False)
            user_profile.user = user
            user_profile.name = user.username  # Set the profile name to the username
            user_profile.save()
            return redirect('dashboard', username=user.username)
    else:
        user_form = UserSignUpForm()
        profile_form = UserProfileForm()
    return render(request, 'login_signup/signup.html', {'user_form': user_form, 'profile_form': profile_form})




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard', username=user.username)
        else:
            print("Invalid login attempt")  # Debugging message
            # Handle invalid login
            # For example, you can render the login page again with an error message
            return render(request, 'login_signup/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login_signup/login.html')



def dashboard(request, username):
    if request.user.is_authenticated and request.user.username == username:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'dashboard/dashboard.html', {'profile': user_profile})
    else:
        return redirect('login')
    



def map(request):
    return HttpResponse("This is map")


def chat_view(request):
    if request.user.is_authenticated:
        users = User.objects.all().exclude(id=request.user.id)  # get all users except the current user
        return render(request, 'chat/chat.html', {'users': users})
    else:
        return redirect('login')


def private_chat_view(request, user_id):
    if request.user.is_authenticated:
        other_user = User.objects.get(id=user_id)
        messages = Message.objects.filter(sender__in=[request.user, other_user], receiver__in=[request.user, other_user])
        room_name = f'{request.user.id}_{other_user.id}'  # Create room name
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.sender = request.user
                message.receiver = other_user
                message.save()
                return redirect('private_chat', user_id=user_id)
        else:
            form = MessageForm()
        return render(request, 'chat/private_chat.html', {'messages': messages, 'form': form, 'other_user': other_user, 'room_name': room_name})
    else:
        return redirect('login')