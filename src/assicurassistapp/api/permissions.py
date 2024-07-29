from rest_framework import permissions
from assicurassistapp.models import Cliente, Veicolo, Polizza, Compagnia, Broker
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import BasePermission
from rest_framework.authentication import get_authorization_header
from rest_framework.authentication import TokenAuthentication
from users.models import CustomUser

class ClienteIsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a Cliente object to edit it.
    """

    def has_permission(self, request, view):
        """Check if the request user is the owner of the Cliente object."""
        db = Cliente.objects.filter(codice_fiscale=view.kwargs['pk'], user=request.user)
        return db.exists()

class PolizzaIsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a Polizza object to edit it.
    """

    def has_permission(self, request, view):
        """Check if the request user is the owner of the Polizza object."""
        db = Polizza.objects.filter(id_polizza=view.kwargs['pk'], user=request.user)
        return db.exists()

class VeicoloIsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a Veicolo object to edit it.
    """

    def has_permission(self, request, view):
        """Check if the request user is the owner of the Veicolo object."""
        db = Veicolo.objects.filter(targa=view.kwargs['pk'], user=request.user)
        return db.exists()

class CompagniaIsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a Compagnia object to edit it.
    """

    def has_permission(self, request, view):
        """Check if the request user is the owner of the Compagnia object."""
        db = Compagnia.objects.filter(nome=view.kwargs['pk'], user=request.user)
        return db.exists()

class BrokerIsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a Broker object to edit it.
    """

    def has_permission(self, request, view):
        """Check if the request user is the owner of the Broker object."""
        db = Broker.objects.filter(nome=view.kwargs['pk'], user=request.user)
        return db.exists()

class IsVerified(permissions.BasePermission):
    """
    Custom permission to only allow verified users to edit objects.
    """

    def has_permission(self, request, view):
        """Check if the request user is verified."""
        return request.user.is_verified
