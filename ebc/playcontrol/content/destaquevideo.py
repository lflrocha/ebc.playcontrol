# -*- coding: utf-8 -*-
"""Definition of the Destaque Video content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from ebc.playcontrol import playcontrolMessageFactory as _

from ebc.playcontrol.interfaces import IDestaqueVideo
from ebc.playcontrol.config import PROJECTNAME

from Products.ATVocabularyManager import NamedVocabulary
from Products.Archetypes.public import DisplayList
from Products.CMFCore.utils import getToolByName

import json

DestaqueVideoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.TextField(
        'descricao',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Descrição"),
            maxlength=256,
        ),
        required=True,


    ),

    atapi.StringField(
        'servico',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"ID Serviço"),
        ),
        required=True,
        vocabulary=NamedVocabulary("""servicos_vocab"""),
    ),

    atapi.StringField(
        'link',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Link do vídeo"),
        ),
        required=True,
    ),

    atapi.ImageField(
        'thumbnail',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Thumbnail"),
            description=_(u"No tamanho 1024x576 pixels."),
        ),
        required=True,
        validators=('isNonEmptyFile'),
        sizes = {'destaque' : (1024, 576)},
        pil_quality=100,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

# DestaqueVideoSchema['title'].widget.label = _(u"Linha 1")
DestaqueVideoSchema['title'].widget.maxlength = 64
DestaqueVideoSchema['title'].storage = atapi.AnnotationStorage()
DestaqueVideoSchema['description'].storage = atapi.AnnotationStorage()
DestaqueVideoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueVideoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueVideoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueVideoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueVideoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueVideoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueVideoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueVideoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueVideoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueVideoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueVideoSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
DestaqueVideoSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}



schemata.finalizeATCTSchema(DestaqueVideoSchema, moveDiscussion=False)


class DestaqueVideo(base.ATCTContent):
    """Description of the Example Type"""
    implements(IDestaqueVideo)

    meta_type = "DestaqueVideo"
    schema = DestaqueVideoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    servico = atapi.ATFieldProperty('servico')
    thumbnail = atapi.ATFieldProperty('thumbnail')
    link = atapi.ATFieldProperty('link')
    descricao = atapi.ATFieldProperty('descricao')


    def getDados(self):
        titulo = self.Title().replace('"', '\\"')
        sinopse = self.getDescricao().replace('"', '\\"')
        sinopse = sinopse.replace('\r\n','\\n')
        servico = self.getServico()
        link = self.getLink()
        filename = self.getFilename('thumbnail')
        aux = {
            "nm_titulo": titulo,
            "ds_sinopse": sinopse,
            "ds_caminho_capa_horizontal": "https://play.ebc.com.br/imagens/%s" % filename,
            "cd_servico": servico,
            "url_streaming": link
        }
        return json.dumps([aux])



atapi.registerType(DestaqueVideo, PROJECTNAME)
