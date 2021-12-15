from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from ebc.playcontrol import playcontrolMessageFactory as _



class IEstatica(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    marcacao = schema.Text(
        title=_(u"Marcacao"),
        required=True,
        description=_(u"Field description"),
    )
#
