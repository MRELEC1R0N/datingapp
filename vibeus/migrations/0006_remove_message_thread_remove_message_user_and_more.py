# Generated by Django 5.0.4 on 2024-05-04 06:11

import django.db.models.deletion
import vibeus.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibeus', '0005_remove_message_receiver_remove_message_sender_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='thread',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(default=vibeus.models.get_default_user, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(default=vibeus.models.get_default_user, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
