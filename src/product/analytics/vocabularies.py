#-*- coding: utf-8 -*-
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from product.analytics import _


TimeIntervalVocabulary = SimpleVocabulary([
    SimpleTerm(value = 30, title = _(u"30 dies")),
    SimpleTerm(value = 90, title = _(u"3 mesos")),
    SimpleTerm(value = 180, title = _(u"6 mesos")),
    SimpleTerm(value = 365, title = _(u"1 any")),
])
