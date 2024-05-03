from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q

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

class ThreadManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs

class Thread(models.Model):
    first_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='thread_first_person')
    second_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='thread_second_person')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()

    class Meta:
        unique_together = ['first_person', 'second_person']

class Message(models.Model):
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.CASCADE, related_name='chatmessage_thread')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)