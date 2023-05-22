# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from product.analytics import _
from product.analytics.interfaces import IAnalyticsSettings


class AnalyticsControlPanelEditForm(controlpanel.RegistryEditForm):
    """ Analytics ControlPanel
    """

    schema = IAnalyticsSettings
    schema_prefix = 'product.analytics'

    label = _('Analytics Settings')
    description = _(
        'Settings of the analytics. You need to add the following '
        'service account: '
        'ecityclic-analytics@analytics-386813.iam.gserviceaccount.com '
        'to your property with Reader role' # noqa: C812
    )


class AnalyticsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """ Analytics Settings ControlPanel
    """
    form = AnalyticsControlPanelEditForm
