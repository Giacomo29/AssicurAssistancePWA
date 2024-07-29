from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.views import View
from assicurassistapp.api.permissions import (ClienteIsOwner, PolizzaIsOwner,
                                            VeicoloIsOwner,
                                            CompagniaIsOwner, BrokerIsOwner,)
from assicurassistapp.models import (Cliente, Veicolo,
                                    Compagnia, Polizza,
                                    Broker, Documento)
from assicurassistapp.api.serializers import (ClienteSerializer, VeicoloSerializer,
                                            CompagniaSerializer, PolizzaSerializer,
                                            BrokerSerializer, DocumentoSerializer)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView
from zipfile import ZipFile
import io
import zipfile
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta,datetime

class ClientiListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating clients.
    """
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns the list of clients belonging to the authenticated user.
        """
        owner_queryset = Cliente.objects.filter(user=self.request.user).order_by('cognome')
        return owner_queryset

    def perform_create(self, serializer):
        """
        Sets the authenticated user as the owner of the created client.
        """
        serializer.save(user=self.request.user)


class ClientiDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for details, updating, and deleting a client.
    """
    queryset = Cliente.objects.all().order_by('cognome')
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated, ClienteIsOwner]


class CercaClientePerCognome(generics.ListAPIView):
    """
    API endpoint for searching clients by last name.
    """
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns clients whose last name contains the provided keyword.
        """
        cognome = self.kwargs['cognome']
        owner_queryset = Cliente.objects.filter(user=self.request.user, cognome__icontains=cognome)
        return owner_queryset


class CercaClientePerTarga(generics.ListAPIView):
    """
    API endpoint for searching clients by vehicle plate number.
    """
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns clients who own a vehicle with the provided plate number.
        """
        targa = self.kwargs['targa']
        owner_queryset = Cliente.objects.filter(user=self.request.user, veicoli__targa__icontains=targa)
        return owner_queryset


class VeicoliListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating vehicles.
    """
    serializer_class = VeicoloSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns the list of vehicles belonging to the authenticated user.
        """
        owner_queryset = Veicolo.objects.filter(user=self.request.user)
        return owner_queryset

    def perform_create(self, serializer):
        """
        Sets the authenticated user as the owner of the created vehicle.
        """
        serializer.save(user=self.request.user)


class VeicoliClienteAPIView(generics.ListAPIView):
    """
    API endpoint for listing vehicles owned by a specific client.
    """
    serializer_class = VeicoloSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns vehicles owned by the specified client.
        """
        owner_queryset = Veicolo.objects.filter(user=self.request.user, proprietario_id=self.kwargs['cliente'])
        return owner_queryset


class VeicoliNonAssicuratiAPIView(generics.ListAPIView):
    """
    API endpoint for listing uninsured vehicles.
    """
    serializer_class = VeicoloSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns vehicles that are not covered by any insurance policy.
        """
        veicoli_assicurati = Polizza.objects.filter(user=self.request.user).values('veicolo')
        veicoli = Veicolo.objects.filter(user=self.request.user).exclude(targa__in=veicoli_assicurati)
        return veicoli


#TODOS
'''
sia che metta la funzione:
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, targa=self.kwargs['pk'])
        return obj
sia che io non la metta (come la funzione sotto) il risultato non cambia, quindi la funzione get_or404 in polizse detail server?
    

'''

class VeicoliDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for details, updating, and deleting a vehicle.
    """
    queryset = Veicolo.objects.all().order_by('targa')
    serializer_class = VeicoloSerializer
    permission_classes = [IsAuthenticated, VeicoloIsOwner]


class PolizzeListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating insurance policies.
    """
    serializer_class = PolizzaSerializer
    permission_classes = [IsAuthenticated,]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        """
        Returns the list of insurance policies belonging to the authenticated user.
        """
        owner_queryset = Polizza.objects.filter(user=self.request.user).order_by('data_fine')
        return owner_queryset

    def perform_create(self, serializer):
        """
        Sets the authenticated user as the owner of the created insurance policy.
        """
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to create a new insurance policy.
        """
        if 'documenti' in request.data:
            documenti = request.data.get('documenti')
        else:
            documenti = None
        return self.create(request, *args, **kwargs)

class PolizzeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for details, updating, and deleting an insurance policy.
    """
    queryset = Polizza.objects.all().order_by('data_fine')
    serializer_class = PolizzaSerializer
    permission_classes = [IsAuthenticated, PolizzaIsOwner]


class PolizzeInScadenzaNelMese(generics.ListAPIView):
    """
    API endpoint for listing insurance policies expiring in a specific month.
    """
    serializer_class = PolizzaSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns insurance policies expiring in the specified month.
        """
        anno = None
        try:
            anno = self.request.query_params.get('anno')
            if anno != None:
                return Polizza.objects.filter(user=self.request.user).filter(data_fine__year=anno, data_fine__month=self.kwargs['month']) | Polizza.objects.filter(user=self.request.user).filter(semestrale=True).filter(data_fine_due__year=anno, data_fine_due__month=self.kwargs['month']).order_by('data_fine' and 'data_fine_due')
        except:
            pass

        return Polizza.objects.filter(user=self.request.user).filter(data_fine__month=self.kwargs['month']) | Polizza.objects.filter(user=self.request.user).filter(semestrale=True).filter(data_fine_due__year=anno, data_fine_due__month=self.kwargs['month']).order_by('data_fine' and 'data_fine_due')


class CompagniaListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating insurance companies.
    """
    serializer_class = CompagniaSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns the list of insurance companies belonging to the authenticated user.
        """
        owner_queryset = Compagnia.objects.filter(user=self.request.user).order_by('nome')
        return owner_queryset

    def perform_create(self, serializer):
        """
        Sets the authenticated user as the owner of the created insurance company.
        """
        serializer.save(user=self.request.user)


class CompagniaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for details, updating, and deleting an insurance company.
    """
    queryset = Compagnia.objects.all().order_by('nome')
    serializer_class = CompagniaSerializer
    permission_classes = [IsAuthenticated, CompagniaIsOwner]


class PolizzeCompagniaListAPIView(generics.ListAPIView):
    """
    API endpoint for listing insurance policies belonging to a specific insurance company.
    """
    serializer_class = PolizzaSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns insurance policies associated with the specified insurance company.
        """
        get_object_or_404(Compagnia, pk=self.kwargs['compagnia'])
        owner_queryset = Polizza.objects.filter(user=self.request.user).filter(compagnia=self.kwargs['compagnia'])
        return owner_queryset




class BrokerListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating insurance brokers.
    """
    serializer_class = BrokerSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns the list of insurance brokers belonging to the authenticated user.
        """
        owner_queryset = Broker.objects.filter(user=self.request.user).order_by('nome')
        return owner_queryset

    def perform_create(self, serializer):
        """
        Sets the authenticated user as the owner of the created insurance broker.
        """
        serializer.save(user=self.request.user)


class BrokerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for details, updating, and deleting an insurance broker.
    """
    queryset = Broker.objects.all().order_by('nome')
    serializer_class = BrokerSerializer
    permission_classes = [IsAuthenticated, BrokerIsOwner]


class CercaPolizzaPerCognomeCliente(generics.ListAPIView):
    """
    API endpoint for searching insurance policies by client's last name.
    """
    serializer_class = PolizzaSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns insurance policies associated with clients whose last name contains the provided keyword.
        """
        nome = None
        try:
            
            nome = self.request.query_params.get('nome')
            if nome != None:
                #return Polizza.objects.filter(user=self.request.user).filter(veicolo__proprietario__cognome__icontains=self.kwargs['cognome'], veicolo__proprietario__nome__icontains=nome) and Polizza.objects.filter(user=self.request.user).filter(cliente__cognome__icontains=self.kwargs['cognome'], cliente__nome__icontains=nome)
                return Polizza.objects.filter(user=self.request.user).filter(user=self.request.user).filter(cliente__cognome__icontains=self.kwargs['cognome'], cliente__nome__icontains=nome)
        except:
            pass

        #return Polizza.objects.filter(user=self.request.user).filter(veicolo__proprietario__cognome__icontains=self.kwargs['cognome']) and Polizza.objects.filter(user=self.request.user).filter(cliente__cognome__icontains=self.kwargs['cognome'])
        return Polizza.objects.filter(user=self.request.user).filter(cliente__cognome__icontains=self.kwargs['cognome'])


class CercaPolizzaPerCodiceFiscaleCliente(generics.ListAPIView):
    """
    API endpoint for searching insurance policies by client's fiscal code.
    """
    serializer_class = PolizzaSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns insurance policies associated with the specified client's fiscal code.
        """
        owner_queryset = Polizza.objects.filter(user=self.request.user).filter(cliente_id=self.kwargs['codice_fiscale'])
        return owner_queryset


class CercaPolizzaPerTarga(generics.ListAPIView):
    """
    API endpoint for searching insurance policies by vehicle plate number.
    """
    serializer_class = PolizzaSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns insurance policies associated with the specified vehicle plate number.
        """
        owner_queryset = Polizza.objects.filter(user=self.request.user).filter(veicolo_id=self.kwargs['targa'])
        return owner_queryset


class DownloadDocumentiView(View):
    """
    View for downloading documents related to an insurance policy.
    """
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to download documents related to an insurance policy.
        """
        id_polizza = kwargs.get('id_polizza')
        polizza = get_object_or_404(Polizza, id_polizza=id_polizza)
        documents = polizza.documenti.all()

        if documents:
            zip_data = self.create_zip(documents)
            response = HttpResponse(zip_data, content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename={id_polizza}_documenti.zip'
            return response
        else:
            return HttpResponse(status=404)

    def create_zip(self, documents):
        """
        Creates a zip file containing the provided documents.
        """
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as zipf:
            for document in documents:
                with open(document.file.path, 'rb') as file:
                    zipf.writestr(document.file.name, file.read())
        return buffer.getvalue()


class EliminaDocumentoPolizza(APIView):
    """
    API endpoint for deleting a document related to an insurance policy.
    """
    def delete(self, request, id_polizza, id_documento):
        """
        Handles DELETE requests to delete a document related to an insurance policy.
        """
        try:
            polizza = Polizza.objects.get(id_polizza=id_polizza)
            documento = Documento.objects.get(id=id_documento, polizza=polizza)
        except (Polizza.DoesNotExist, Documento.DoesNotExist):
            return Response({"message": "Polizza o documento non trovato"}, status=status.HTTP_404_NOT_FOUND)

        documento.delete()
        return Response({"message": "Documento eliminato con successo"})


class ModificaDocumentoPolizza(APIView):
    """
    API endpoint for modifying a document related to an insurance policy.
    """
    def put(self, request, id_polizza, id_documento):
        """
        Handles PUT requests to modify a document related to an insurance policy.
        """
        try:
            polizza = Polizza.objects.get(id_polizza=id_polizza)
            documento = Documento.objects.get(id=id_documento, polizza=polizza)
        except (Polizza.DoesNotExist, Documento.DoesNotExist):
            return Response({"message": "Polizza o documento non trovato"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DocumentoSerializer(documento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Documento modificato con successo"})
        return Response({"message": "Errore nella validazione dei dati", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AggiungiDocumentoPolizza(APIView):
    """
    API endpoint for adding a document related to an insurance policy.
    """
    def post(self, request, id_polizza):
        """
        Handles POST requests to add a document related to an insurance policy.
        """
        try:
            polizza = Polizza.objects.get(id_polizza=id_polizza)
        except Polizza.DoesNotExist:
            return Response({"message": "Polizza non trovata"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DocumentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(polizza=polizza)
            return Response({"message": "Documento aggiunto con successo"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Errore nella validazione dei dati", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class returnPortafoglio(APIView):
    """
    API endpoint for returning the sum of the premiums of the all policies.
    """
    
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        """
        Handles GET requests to return the sum of the premiums of the all policies.
        """
        #le polizze scadute per piu di 3 mesi non vengono considerate
        
        polizze = Polizza.objects.filter(user=request.user).filter(data_fine__gte=datetime.now()-timedelta(days=90))
        
        #polizze = Polizza.objects.filter(user=request.user)
        portafoglio = 0
        for polizza in polizze:
            if polizza.premio is not None:
                portafoglio += polizza.premio
        return Response({"portafoglio": portafoglio})

    
    
    