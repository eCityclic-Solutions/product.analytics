# -*- coding: utf-8 -*-
from plone import api
from plone.app.contentmenu.menu import BrowserMenu
from plone.app.contentmenu.menu import BrowserSubMenuItem
from plone.memoize.instance import memoize
from product.analytics import _
from product.analytics.browser.utils import get_views
from zope.browsermenu.interfaces import IBrowserMenu
from zope.browsermenu.interfaces import IBrowserSubMenuItem
from zope.interface import implementer


@implementer(IBrowserMenu)
class AnalyticsMenu(BrowserMenu):
    """ Analytics Menu
    """

    def getMenuItems(self, context, request):
        menu = [
            # {
            #     'title': _('Dashboard'),
            #     'description': _('Dashboard'),
            #     'action': context.absolute_url() + '/@@dashboard-analytics-view',
            #     'selected': False,
            #     'icons': None,
            #     'extra': {
            #         'id': 'dashboard-analytics-id',
            #         'separator': None,
            #         'class': 'dashboard-analytics',
            #     },
            #     'submenu': None,
            # },
            {
                'title': _('Most visited'),
                'description': _('Most visited'),
                'action': context.absolute_url() + '/@@most-visited-analytics-view',
                'selected': False,
                'icons': None,
                'extra': {
                    'id': 'most-visited-analytics-id',
                    'separator': None,
                    'class': 'most-visited-analytics',
                },
                'submenu': None,
            },
        ]

        return menu


@implementer(IBrowserSubMenuItem)
class AnalyticsSubMenuItem(BrowserSubMenuItem):
    """ Analytics Submenu
    """

    submenuId = 'menu_analytics'
    order = 100

    views_msg = _('views')

    @property
    def extra(self):
        return {
            'id': 'menu-analytics',
        }

    def title(self):
        portal_path = '/'.join(api.portal.get().getPhysicalPath())
        context_path = '/'.join(self.context.getPhysicalPath())

        parent = self.context.aq_parent
        try:
            default_page = parent.default_page
            if default_page == self.context.id:
                context_path = '/'.join(parent.getPhysicalPath())
        except AttributeError:
            pass

        context_path = context_path.replace(portal_path, '')

        if not context_path:
            context_path = '/'

        views = get_views()
        if not views:
            return None
        
        reports = views.get('reports', [])
        if not reports:
            return 'Analytics: No data'

        rows = reports[0].get('rows', [])
        if not rows:
            return 'Analytics: No data'

        for row in rows:
            if row['dimensionValues'][1]['value'] == context_path:
                views_msg = api.portal.translate(self.views_msg, domain='products.analytics', lang=api.portal.get_current_language())
                return 'Analytics: ' + row['metricValues'][0]['value'] + ' ' + views_msg
        return 'Analytics: No data'

    @property
    def description(self):
        return _('Number of visits for the current page in last 30 days.')

    @property
    def action(self):
        return '#'

    @memoize
    def available(self):
        return True

    def selected(self):
        return False
