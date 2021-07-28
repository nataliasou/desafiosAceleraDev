from django.db import models
import uuid
from django.core import validators
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50,
                            help_text="Enter the name of the user")
    last_login = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254,
                              help_text="Enter your email adress")
    password = models.CharField('User Password',
                                max_length=50,
                                validators=[validators.MinLengthValidator(8)])

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=50, help_text="Enter the agent's name")
    status = models.NullBooleanField(help_text="escolha seu status")
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5, help_text="Enter the version")
    address = models.GenericIPAddressField('Agent IP Addess',
                                           protocol='IPV4', max_length=39)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this agent")
    LEVEL_STATUS = (
        ('C', 'Critical'),
        ('D', 'Debug'),
        ('E', 'Error'),
        ('W', 'Warning'),
        ('I', 'Info'),
    )
    level = models.CharField(max_length=1, choices=LEVEL_STATUS, blank=True,
                             default='E', help_text="Enter the events's level")
    data = models.TextField(max_length=1000, help_text="Describe the data")
    arquivado = models.NullBooleanField()
    date = models.DateField(null=True, blank=True)
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.level


class Group(models.Model):
    name = models.CharField(max_length=50, help_text="Enter a group")

    def __str__(self):
        return self.name


class GroupUser(models.Model):
    # Representing group user
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
