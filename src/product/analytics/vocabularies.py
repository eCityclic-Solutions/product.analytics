# -*- coding: utf-8 -*-
from product.analytics import _
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


TimeIntervalVocabulary = SimpleVocabulary([
    SimpleTerm(value=30, title=_('30 dies')),
    SimpleTerm(value=90, title=_('3 mesos')),
    SimpleTerm(value=180, title=_('6 mesos')),
    SimpleTerm(value=365, title=_('1 any')),
])
