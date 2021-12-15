# -*- coding: utf-8 -*-
"""Definition of the Estatica content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from ebc.playcontrol import playcontrolMessageFactory as _

from ebc.playcontrol.interfaces import IEstatica
from ebc.playcontrol.config import PROJECTNAME

import json

EstaticaSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'marcacao',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Marcação"),
        ),
        required=True,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

EstaticaSchema['title'].storage = atapi.AnnotationStorage()
EstaticaSchema['description'].storage = atapi.AnnotationStorage()
EstaticaSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
EstaticaSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
EstaticaSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
EstaticaSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
EstaticaSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
EstaticaSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
EstaticaSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
EstaticaSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
EstaticaSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
EstaticaSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
EstaticaSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
EstaticaSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(EstaticaSchema, moveDiscussion=False)


class Estatica(base.ATCTContent):
    """Description of the Example Type"""
    implements(IEstatica)

    meta_type = "Estatica"
    schema = EstaticaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    marcacao = atapi.ATFieldProperty('marcacao')


    def getDados(self):
        titulo = self.Title()
        marcacao = self.getMarcacao()
        print(marcacao)
        marcacao = marcacao.replace('\r\n','\\n')
        aux = {
            "nm_titulo": titulo,
            "ds_texto": marcacao,
        }
        print(aux)
        return json.dumps(aux, indent=4)



atapi.registerType(Estatica, PROJECTNAME)
