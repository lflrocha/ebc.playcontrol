from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from ebc.playcontrol import playcontrolMessageFactory as _



class IDestaqueVideo(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    servico = schema.TextLine(
        title=_(u"ID Servico"),
        required=True,
        description=_(u"Field description"),
    )
#
    thumbnail = schema.Bytes(
        title=_(u"Thumbnail"),
        required=False,
        description=_(u"Field description"),
    )
#
    link = schema.TextLine(
        title=_(u"Link do video"),
        required=True,
        description=_(u"Field description"),
    )
#
    descricao = schema.Text(
        title=_(u"Descricao"),
        required=True,
        description=_(u"Field description"),
    )
#
