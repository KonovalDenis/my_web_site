from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
	user =  models.OneToOneField(User, on_delete = models.CASCADE)
	ballsBestResult = models.IntegerField(default = 0)
	ballsGamesPlayed = models.IntegerField(default = 0)
	gomokuWin = models.IntegerField(default = 0)
	gomokuLose = models.IntegerField(default = 0)
	gomokuGamesPlayed = models.IntegerField(default = 0)
	def __str__(self):
		return self.user.username
	# def get_absolute_url(self):
	# 	return reverse("Character:character", kwargs={"id": self.id})	
		# return reverse("KonoGame>urls.py>URLPATTERNS>namespace : Character>views.py> name of view")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()