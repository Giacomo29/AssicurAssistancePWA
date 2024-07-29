from django.urls import path
from assicurassistapp.api.views import (ClientiListCreateAPIView, ClientiDetailAPIView, CercaClientePerCognome, CercaClientePerTarga,
                                        VeicoliListCreateAPIView, VeicoliDetailAPIView, VeicoliClienteAPIView, VeicoliNonAssicuratiAPIView,
                                        PolizzeListCreateAPIView, PolizzeDetailAPIView, PolizzeInScadenzaNelMese,
                                        CompagniaListCreateAPIView, CompagniaDetailAPIView, PolizzeCompagniaListAPIView,
                                        BrokerListCreateAPIView, BrokerDetailAPIView,
                                        CercaPolizzaPerCognomeCliente, CercaPolizzaPerTarga, CercaPolizzaPerCodiceFiscaleCliente,
                                        DownloadDocumentiView, EliminaDocumentoPolizza, AggiungiDocumentoPolizza, ModificaDocumentoPolizza, returnPortafoglio)

urlpatterns = [
    # APIs for clients
    path('clienti/', ClientiListCreateAPIView.as_view(), name='clienti-list'),
    path('clienti/<str:pk>/', ClientiDetailAPIView.as_view(), name='clienti-detail'),
    path('clienti/cerca-per-cognome/<str:cognome>/', CercaClientePerCognome.as_view(), name='cerca-cliente-per-cognome'),
    path('clienti/cerca-per-targa/<str:targa>/', CercaClientePerTarga.as_view(), name='cerca-cliente-per-targa'),
    
    path('polizze/portafoglio/', returnPortafoglio.as_view(), name='portafoglio'),

    # APIs for vehicles
    path('veicoli/', VeicoliListCreateAPIView.as_view(), name='veicoli-list'),
    path('veicoli/<str:pk>/', VeicoliDetailAPIView.as_view(), name='veicoli-detail'),
    path('veicoli/cliente/<str:cliente>/', VeicoliClienteAPIView.as_view(), name='veicoli-cliente'),
    path('veicoli-non-assicurati/', VeicoliNonAssicuratiAPIView.as_view(), name='veicoli-non-assicurati'),
    
    # APIs for insurance policies
    path('polizze/', PolizzeListCreateAPIView.as_view(), name='polizze-list'),
    path('polizze/<str:pk>/', PolizzeDetailAPIView.as_view(), name='polizze-detail'),
    path('polizze/scadenza-nel-mese/<int:month>/', PolizzeInScadenzaNelMese.as_view(), name='polizze-scadenza-nel-mese'),
    path('polizze/cerca-per-cognome/<str:cognome>/', CercaPolizzaPerCognomeCliente.as_view(), name='cerca-polizza-per-cognome'),
    path('polizze/cerca-per-targa/<str:targa>/', CercaPolizzaPerTarga.as_view(), name='cerca-polizza-per-targa'),
    path('polizze/cerca-per-codice-fiscale/<str:codice_fiscale>/', CercaPolizzaPerCodiceFiscaleCliente.as_view(), name='cerca-polizza-per-codice-fiscale'),

    # Download documents
    path('polizze/download_documenti/<str:id_polizza>/', DownloadDocumentiView.as_view(), name='download_documenti'),
    path('polizze/<str:id_polizza>/modifica_documento/<int:id_documento>/', ModificaDocumentoPolizza.as_view(), name='modifica_documento_polizza'),
    path('polizze/<str:id_polizza>/elimina_documento/<int:id_documento>/', EliminaDocumentoPolizza.as_view(), name='elimina_documento_polizza'),
    path('polizze/aggiungi_documento/<str:id_polizza>/', AggiungiDocumentoPolizza.as_view(), name='aggiungi_documento_polizza'),
    

    # APIs for insurance companies
    path('compagnie/', CompagniaListCreateAPIView.as_view(), name='compagnie-list'),
    path('compagnie/<str:pk>/', CompagniaDetailAPIView.as_view(), name='compagnia-detail'),
    path('compagnie-polizze/<str:compagnia>/', PolizzeCompagniaListAPIView.as_view(), name='compagnia-clienti'),

    # APIs for brokers
    path('broker/', BrokerListCreateAPIView.as_view(), name='broker-list'),
    path('broker/<str:pk>/', BrokerDetailAPIView.as_view(), name='broker-detail'),

]