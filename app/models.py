from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.utils import timezone

from django.contrib.auth.base_user import BaseUserManager


class Base(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, Base):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email


class Group(Base):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    description = models.CharField(max_length=20)

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return self.name


class GroupMembers(Base):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    class Meta:
        db_table = 'group_members'
        unique_together = [['group_id', 'user_id']]

    def __str__(self):
        return f"{self.group.name}_{self.user.name}"


class Bill(Base):
    class SplitType(models.TextChoices):
        PERCENTAGE = 'P', _('PERCENTAGE')
        ABSOLUTE = 'A', _('ABSOLUTE')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="bill_group")
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bill_user")
    total_amount = models.FloatField()
    split_type = models.CharField(
        max_length=10,
        choices=SplitType.choices,
        default=SplitType.ABSOLUTE
    )
    expense_splits = models.JSONField()

    class Meta:
        db_table = 'bills'


class GroupBalances(Base):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="gb_group")
    user_to_receive = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    user_to_pay = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payer")
    amount = models.FloatField()

    class Meta:
        db_table = 'group_balances'
