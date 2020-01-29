# -*- coding: utf-8 -*-
from plone import api
from product.analytics.browser.utils import get_views
from Products.Five import BrowserView


class MostVisitedView(BrowserView):
    """ MostVisitedView
    """

    def get_most_visited(self, number=10):
        portal_url = api.portal.get().absolute_url()
        views = get_views()

        if views:
            rows = views.get('rows', [])
            if rows:
                rows = sorted(rows, key=lambda row: int(row[2]))[::-1]
                rows = map(lambda row: {
                    'title': row[0],
                    'url': portal_url + row[1],
                    'views': row[2],
                }, rows[:number])

                return rows
        return None
