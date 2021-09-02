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
        'service account to your analytics: '
        'semic-140@decisive-lambda-226112.iam.gserviceaccount.com'  # noqa: C812
    )


class AnalyticsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """ Analytics Settings ControlPanel
    """
    form = AnalyticsControlPanelEditForm
