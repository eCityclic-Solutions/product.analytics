# -*- coding: utf-8 -*-
from zope.interface import implementer
from zope.browsermenu.interfaces import IBrowserMenu
from zope.browsermenu.interfaces import IBrowserSubMenuItem # noqa
from plone.app.contentmenu.menu import BrowserMenu
from plone.app.contentmenu.menu import BrowserSubMenuItem # noqa
from plone import api
from plone.memoize.instance import memoize
from product.analytics.browser.utils import get_views
from product.analytics import _


@implementer(IBrowserMenu)
class AnalyticsMenu(BrowserMenu):
    """"""
    def getMenuItems(self, context, request):
        menu = [
            {
                'title': _(u'Dashboard'),
                'description': _(u'Dashboard'),
                'action': context.absolute_url() + '/@@dashboard-analytics-view',
                'selected': False,
                'icons': None,
                'extra': {
                    'id': 'dashboard-analytics-id',
                    'separator': None,
                    'class': 'dashboard-analytics'
                },
                'submenu': None
            },
            # {
            #     'title': _(u'See more visited pages'),
            #     'description': _(u'See more visited pages'),
            #     'action': context.absolute_url() + '/@@most-visited-analytics-view',
            #     'selected': False,
            #     'icons': None,
            #     'extra': {
            #         'id': 'most-visited-analytics-id',
            #         'separator': None,
            #         'class': 'most-visited-analytics'
            #     },
            #     'submenu': None
            # }
        ]

        return menu


@implementer(IBrowserSubMenuItem)
class AnalyticsSubMenuItem(BrowserSubMenuItem):

    submenuId = 'menu_analytics'
    order = 100

    views_msg = _(u'views')

    @property
    def extra(self):
        return {
            'id': 'menu-analytics',
        }

    def title(self):
        portal_path = '/'.join(api.portal.get().getPhysicalPath())
        context_path = '/'.join(self.context.getPhysicalPath())
        context_path = context_path.replace(portal_path, '')

        if not context_path:
            context_path = '/'

        views = get_views()
        if views:
            rows = views.get('rows', [])
            for row in rows:
                if row[1] == context_path:
                    return 'Analytics: ' + row[2] + ' ' + api.portal.translate(
                        self.views_msg, domain='products.analytics', 
                        lang=api.portal.get_current_language())
        return 'Analytics: No data'

    @property
    def description(self):
        return _(u"Number of visits for the current page in last 30 days.")

    @property
    def action(self):
        return '#'

    @memoize
    def available(self):
        return True

    def selected(self):
        return False