# -*- coding: utf-8 -*-
from product.analytics import _
from product.analytics.vocabularies import TimeIntervalVocabulary
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IProductAnalyticsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IAnalyticsSettings(Interface):
    """ Analytics Settings
    """

    property_id = schema.TextLine(
        title=_('Property ID'),
        description=_('Property ID'),
        required=False,
    )

    time_interval = schema.Choice(
        title=_('Time interval'),
        description=_('Time interval of data showed in analytics views'),
        required=False,
        vocabulary=TimeIntervalVocabulary,
        default=30,
    )
