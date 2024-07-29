from apscheduler.schedulers.blocking import BlockingScheduler
from assicurassistapp.models import Polizza, Cliente
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
import sys
import vonage

from django.http import HttpResponse
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

def send_notification(data_utente):
    print('Invio notifica...')
    channel_layer = get_channel_layer()
    
    user_data = {
        'id': data_utente['user'].id,
        'username': data_utente['user'].username,
        'email': data_utente['user'].email,
    }
    
    data = {
        'current_notification': 'Scadenza polizza',
        'account': user_data,
        'polizza': data_utente['polizza'],
        'cliente': f"{data_utente['nome']} {data_utente['cognome']}",
    }

    async_to_sync(channel_layer.group_send)(
        'notifications_group',
        {
            'type': 'send_notification',
            'value': json.dumps(data)
        }
    )

    return HttpResponse("Notifica inviata con successo!")

def send_email(email, polizza):
    # Implementa la logica per l'invio dell'email qui
    print(f"Invia email a {email} per la polizza {polizza}")

def send_sms(number):
    pass

def get_clienti_in_scadenza():
    oggi = timezone.now().date()
    data_scadenza = oggi + timedelta(days=30)

    polizze_in_scadenza = Polizza.objects.filter(
        Q(data_fine__range=[oggi, data_scadenza]) | Q(data_fine_due__range=[oggi, data_scadenza]),
        Q(cliente__ultima_notifica__lt=oggi) | Q(cliente__ultima_notifica__isnull=True), 
        cliente__comunicazioni=True
    )

    print(f'[SISTEMA] Trovate {polizze_in_scadenza.count()} polizze in scadenza tra oggi e un mese')
    for polizza in polizze_in_scadenza:
        cliente = polizza.cliente
        print(f'[SISTEMA] Cliente: {cliente.nome} {cliente.cognome}, Polizza: {polizza.id_polizza}')

        if cliente.ultima_notifica is None or (oggi - cliente.ultima_notifica).days > 30:
            data_utente = {
                'nome': cliente.nome,
                'cognome': cliente.cognome,
                'polizza': polizza.id_polizza,
                'user': cliente.user
            }

            if cliente.email:
                data_utente['email'] = cliente.email
                send_email(cliente.email, polizza.id_polizza)
            
            if cliente.telefono:
                data_utente['telefono'] = cliente.telefono
                send_sms(cliente.telefono)

            send_notification(data_utente)
            cliente.ultima_notifica = oggi
            cliente.save()

def delete_expired_polizze():
    data_limite = timezone.now().date() - timedelta(days=3 * 30)
    polizze_da_elim = Polizza.objects.filter(data_fine__lte=data_limite)
    count = polizze_da_elim.count()
    polizze_da_elim.delete()
    
    print(f'[SISTEMA] Eliminate {count} polizze scadute da più di 3 mesi')

def run():
    print('[SISTEMA] Avvio invio notifiche ai clienti...')
    print('[SISTEMA] Avvio scheduler per invio email e sms ai clienti in scadenza...')
    print('[SISTEMA] Premi CTRL+C per terminare il processo')

    try:
        scheduler = BlockingScheduler()
        scheduler.add_job(get_clienti_in_scadenza, 'interval', seconds=10)
        scheduler.start()
    
    except KeyboardInterrupt:
        print('[SISTEMA] Interruzione da tastiera rilevata. Terminazione del processo...')
        sys.exit(0)

if __name__ == "__main__":
    run()
