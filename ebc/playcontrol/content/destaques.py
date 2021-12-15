# -*- coding: utf-8 -*-
"""Definition of the Destaques content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from ebc.playcontrol.interfaces import IDestaques
from ebc.playcontrol.config import PROJECTNAME


from Products.Archetypes.public import DisplayList
from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.SelectColumn import SelectColumn

import requests
import json

DestaquesSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    DataGridField(
        'noticias',
        columns=("id",),
        allow_reorder = True,
        widget=DataGridWidget(
            label="Selecione as notícias",
            columns={
                'id': SelectColumn("Programa", vocabulary="getProgramas"),
            },
        ),
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

DestaquesSchema['title'].storage = atapi.AnnotationStorage()
DestaquesSchema['description'].storage = atapi.AnnotationStorage()
DestaquesSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaquesSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaquesSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaquesSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaquesSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaquesSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaquesSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaquesSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaquesSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaquesSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaquesSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaquesSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}



schemata.finalizeATCTSchema(DestaquesSchema, moveDiscussion=False)


class Destaques(base.ATCTContent):
    """Description of the Example Type"""
    implements(IDestaques)

    meta_type = "Destaques"
    schema = DestaquesSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    def getProgramas(self):
        url = "https://play.ebc.com.br/v2/conteudos?limit=1000"
        req = requests.get(url, timeout=30)
        programas = req.json()
        saida = []

        for programa in programas:
            id = str(programa['id_conteudo'])
            titulo = programa['nm_conteudo']
            aux = (id, titulo)
            saida.append(aux)
        aux = sorted(saida ,key=lambda x: x[1])
        return DisplayList(aux)


    def getDados(self):
        selecionados = self.getNoticias()

        saida = []
        for selecionado in selecionados:
            id = selecionado['id']
            url = "https://play.ebc.com.br/v2/conteudos/%s" % id
            req = requests.get(url, timeout=30)
            programa = req.json()
            dict_programa = {
                "id_conteudo": programa['id_conteudo'],
                "nm_conteudo": programa['nm_conteudo'],
                "nm_conteudo_curto": programa['nm_conteudo_curto'],
                "nm_tipo_conteudo": programa['nm_tipo_conteudo'],
                "nm_genero": programa['nm_genero'],
                "ds_sinopse": programa['ds_sinopse'],
                "ds_sinopse_reduzida": programa['ds_sinopse_reduzida'],
                "nr_ano_lancamento": programa['nr_ano_lancamento'],
                "cd_classificacao_indicativa": programa['cd_classificacao_indicativa'],
                "ds_caminho_logo": programa['ds_caminho_logo'],
                "ds_caminho_capa_horizontal": programa['ds_caminho_capa_horizontal'],
                "ds_caminho_capa_vertical": programa['ds_caminho_capa_vertical'],
                "dt_priorizacao": "",
                "bl_licenciado_internacional": programa['bl_licenciado_internacional'],
                "participantes": programa['participantes']
            }

            saida.append(dict_programa)
        return json.dumps(saida)





atapi.registerType(Destaques, PROJECTNAME)
