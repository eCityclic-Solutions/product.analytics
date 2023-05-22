# -*- coding: utf-8 -*-
from plone import api
from product.analytics.browser.utils import get_views
from Products.Five import BrowserView


class MostVisitedView(BrowserView):
    """ MostVisitedView
    """

    def __call__(self):
        self.portal = api.portal.get()
        self.portal_url = self.portal.absolute_url()
        self.portal_path = '/'.join(self.portal.getPhysicalPath())
        self.section_path = '/'.join(self.context.getPhysicalPath()).replace(self.portal_path, '')

        self.most_visited = self.get_most_visited()
        return super().__call__()

    def get_most_visited(self, number=50):
        portal_url = api.portal.get().absolute_url()
        views = get_views()

        if not views:
            return None
        
        reports = views.get('reports', [])
        if not reports:
            return None

        rows = reports[0].get('rows', [])
        if not rows:
            return None

        rows = list(filter(lambda row: self.section_path in row['dimensionValues'][1]['value'], rows))
        rows = map(lambda row: {
            'title': row['dimensionValues'][0]['value'],
            'url': portal_url + row['dimensionValues'][1]['value'],
            'views': row['metricValues'][0]['value'],
        }, rows[:number])

        return rows
