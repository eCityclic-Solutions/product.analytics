# -*- coding: utf-8 -*-
from plone import api
from product.analytics.browser.utils import get_access_token
from product.analytics.browser.utils import get_property_id
from product.analytics.browser.utils import get_time_interval
from Products.Five import BrowserView


class DashBoardView(BrowserView):
    """ DashBoardView
    """

    @property
    def token(self):
        return get_access_token()

    @property
    def property_id(self):
        return get_property_id()

    @property
    def time_interval(self):
        return get_time_interval()

    def pagesTableTranslations(self):
        language = api.portal.get_current_language()
        if language == 'ca':
            translations = """*/
                path: "Ruta",
                page: "Pàgina",
                views: "Visites",
                uniqueViews: "Visites úniques",
                averageTime: "Temps promig",
                entrances: "Entrades"
                /*
            """
        elif language == 'es':
            translations = """*/
                path: "Ruta",
                page: "Página",
                views: "Visitas",
                uniqueViews: "Visitas únicas",
                averageTime: "Tiempo promedio",
                entrances: "Entradas"
                /*
            """
        else:
            translations = """*/
                path: "Path",
                page: "Page",
                views: "Views",
                uniqueViews: "Unique views",
                averageTime: "Average time",
                entrances: "Entrances"
                /*
            """
        return translations
