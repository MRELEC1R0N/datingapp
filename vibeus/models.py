from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.models import User

User = get_user_model()

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    HOBBIES_CHOICES = (
        ('anime', 'Anime'),
        ('games', 'Games'),
        ('photography', 'Photography'),
        ('cooking', 'Cooking'),
        ('drawing', 'Drawing'),
        ('dance', 'Dance'),
        ('writing', 'Writing'),
        ('movies', 'Movies'),
        ('video', 'Video'),
        ('painting', 'Painting'),
        ('learning', 'Learning'),
    )

    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    bio = models.TextField()
    hobbies = models.CharField(max_length=200, choices=HOBBIES_CHOICES)



def get_default_user():
    return User.objects.get_or_create(username='default')[0].id

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE, default=get_default_user)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE, default=get_default_user)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)