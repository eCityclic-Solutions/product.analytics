# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from plone import api
from product.analytics.browser.utils import get_time_interval
from product.analytics.browser.utils import get_access_token
from product.analytics.browser.utils import get_ga_id


class DashBoardView(BrowserView):
    """ DashBoardView 
    """

    @property
    def token(self):
        return get_access_token()

    @property
    def ga_id(self):
        return get_ga_id()

    @property
    def time_interval(self):
        return get_time_interval()

    def pagesTableTranslations(self):
        language = api.portal.get_current_language()
        if language == 'ca':
            return '''*/
                path: "Ruta", 
                page: "Pàgina",
                views: "Visites",
                uniqueViews: "Visites úniques",
                averageTime: "Temps promig",
                entrances: "Entrades"
                /*
            '''
        if language == 'es':
            return '''*/
                path: "Ruta", 
                page: "Página",
                views: "Visitas",
                uniqueViews: "Visitas únicas",
                averageTime: "Tiempo promedio",
                entrances: "Entradas"
                /*
            '''
        return '''*/
            path: "Path", 
            page: "Page",
            views: "Views",
            uniqueViews: "Unique views",
            averageTime: "Average time",
            entrances: "Entrances"
            /*
        '''
    
    
    