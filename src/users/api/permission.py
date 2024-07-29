from rest_framework import permissions
from rest_framework.permissions import BasePermission





class IsServer(BasePermission):
    """
    Permission check for server.
    """

    def has_permission(self, request, view):
        # Inserisci qui la logica per verificare se la richiesta proviene dal server
        # Ad esempio, potresti controllare se la richiesta ha un certo header o un token specifico per il server.
        # Restituisci True se la richiesta proviene dal server, altrimenti False.
        # Esempio di controllo del token:
        # return request.META.get('HTTP_X_SERVER_TOKEN') == 'il_tuo_token_per_il_server'
        # Nota che questa logica deve essere personalizzata in base alle tue esigenze specifiche.

        # In questo esempio, per semplicità, si presume che il server possa essere identificato
        # attraverso un token personalizzato nell'header della richiesta.
        token = request.headers.get('Authorization')
        return token == 'SERVER'
