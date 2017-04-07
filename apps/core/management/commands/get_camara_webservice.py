from django.core.management.base import BaseCommand
from datetime import datetime
from dateutil.relativedelta import relativedelta
from apps.core.models import Room
import requests
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        initial_date = datetime.today()
        final_date = datetime.today() + relativedelta(months=3)
        params = {'dataInicial': initial_date.strftime('%d/%m/%Y'),
                  'dataFinal': final_date.strftime('%d/%m/%Y'),
                  'codComissao': '0',
                  'bolEdemocracia': '1'}
        response = requests.get(
            'https://infoleg.camara.leg.br/ws-pauta/evento/interativo',
            params=params, verify=False)
        data = json.loads(response.text)
        for item in data:
            if item['codReuniao'] == item['codReuniaoPrincipal']:
                room, created = Room.objects.get_or_create(
                    cod_reunion=item['codReuniao'])
                room.title_reunion = item['txtTituloReuniao']
                room.legislative_body_initials = item['txtSiglaOrgao']
                room.legislative_body_alias = item['txtApelido']
                room.legislative_body = item['txtNomeOrgao']
                room.subcommission = item['txtNomeSubcomissao']
                room.reunion_status = item['codEstadoReuniao']
                room.reunion_type = item['txtTipoReuniao']
                room.reunion_object = item['txtObjeto']
                room.location = item['txtLocal']
                room.legislative_body_type = item['codTipoOrgao']
                room.is_live = item['bolTransmissaoEmAndamento']
                room.youtube_id = item['idYoutube']
                room.is_visible = item['bolHabilitarEventoInterativo']
                room.youtube_status = item['codEstadoTransmissaoYoutube']
                date = datetime.strptime(item['datReuniaoString'],
                                         '%d/%m/%Y %H:%M:%S')
                room.date = date
                room.save()