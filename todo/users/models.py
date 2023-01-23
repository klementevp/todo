from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        # Создает и регестрирует пользователя с email, password, date_of_birth, username 

        if not email:
            raise ValueError('Пользователь должен иметь почту')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):

        #Создает и регистрирует суперпользователя с email, username, password

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True, verbose_name='Почта')
    username = models.CharField(max_length=60, unique=True, null=True, blank=True, verbose_name='Никнейм')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Регистрация')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin




