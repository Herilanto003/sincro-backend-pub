from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from club.models import Club


class GestionUtilisateur(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("EMAIL IS REQUIRED")

        if not password:
            raise ValueError("PASSWORD IS REQUIRED")

        user = self.model(
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class Compte(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=False
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = GestionUtilisateur()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perm(self, app_label):
        return True


class Membre(models.Model):
    code_membre = models.CharField(max_length=25)
    nom = models.CharField(max_length=25)
    prenoms = models.CharField(max_length=255, blank=True, null=True)
    cin = models.CharField(max_length=25)
    tel = models.CharField(max_length=30)
    sexe = models.CharField(max_length=12)
    photo_profil = models.ImageField(upload_to='images/')
    titre = models.CharField(max_length=25)
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE
    )
    compte = models.OneToOneField(
        Compte,
        on_delete=models.CASCADE,
        related_name='membre',
        db_index=True,
        db_constraint=False,
        null=True
    )