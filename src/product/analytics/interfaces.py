# -*- coding: utf-8 -*-
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface
from zope import schema
from product.analytics.vocabularies import TimeIntervalVocabulary
from product.analytics import _


class IProductAnalyticsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IAnalyticsSettings(Interface):

    ga_id = schema.TextLine(
        title=_(u'View ID'),
        description=_(u'View ID'),
        required=False,
    )

    time_interval = schema.Choice(
        title=_(u'Time interval'),
        description=_(u'Time interval of data showed in analytics views'),
        required=False,
        vocabulary=TimeIntervalVocabulary,
        default=30,
    )