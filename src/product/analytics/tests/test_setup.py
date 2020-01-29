# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from product.analytics.testing import PRODUCT_ANALYTICS_INTEGRATION_TESTING  # noqa

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that product.analytics is properly installed."""

    layer = PRODUCT_ANALYTICS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if product.analytics is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'product.analytics'))

    def test_browserlayer(self):
        """Test that IProductAnalyticsLayer is registered."""
        from product.analytics.interfaces import (
            IProductAnalyticsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IProductAnalyticsLayer,
            utils.registered_layers(),
        )


class TestUninstall(unittest.TestCase):

    layer = PRODUCT_ANALYTICS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['product.analytics'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if product.analytics is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'product.analytics'))

    def test_browserlayer_removed(self):
        """Test that IProductAnalyticsLayer is removed."""
        from product.analytics.interfaces import \
            IProductAnalyticsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IProductAnalyticsLayer,
            utils.registered_layers(),
        )
