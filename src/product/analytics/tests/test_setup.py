# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from product.analytics.testing import PRODUCT_ANALYTICS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that product.analytics is properly installed."""

    layer = PRODUCT_ANALYTICS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
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
        self.assertIn(IProductAnalyticsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PRODUCT_ANALYTICS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['product.analytics'])

    def test_product_uninstalled(self):
        """Test if product.analytics is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'product.analytics'))

    def test_browserlayer_removed(self):
        """Test that IProductAnalyticsLayer is removed."""
        from product.analytics.interfaces import \
            IProductAnalyticsLayer
        from plone.browserlayer import utils
        self.assertNotIn(IProductAnalyticsLayer, utils.registered_layers())
