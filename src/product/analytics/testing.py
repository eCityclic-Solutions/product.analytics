# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import product.analytics


class ProductAnalyticsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=product.analytics)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'product.analytics:default')


PRODUCT_ANALYTICS_FIXTURE = ProductAnalyticsLayer()


PRODUCT_ANALYTICS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PRODUCT_ANALYTICS_FIXTURE,),
    name='ProductAnalyticsLayer:IntegrationTesting',
)


PRODUCT_ANALYTICS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PRODUCT_ANALYTICS_FIXTURE,),
    name='ProductAnalyticsLayer:FunctionalTesting',
)


PRODUCT_ANALYTICS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PRODUCT_ANALYTICS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ProductAnalyticsLayer:AcceptanceTesting',
)
