# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from product.analytics.interfaces import IAnalyticsSettings
from product.analytics import _


class AnalyticsControlPanelEditForm(controlpanel.RegistryEditForm):
    
    schema = IAnalyticsSettings
    schema_prefix = 'product.analytics'

    label = _(u"Analytics Settings")
    description = _(
        u"Settings of the analytics. You need to add the following service account to your analytics: " +
        u"semic-140@decisive-lambda-226112.iam.gserviceaccount.com"
    )


class AnalyticsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = AnalyticsControlPanelEditForm