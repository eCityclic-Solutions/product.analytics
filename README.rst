=================
product.analytics
=================

Google Analytics integration. This product helps you integrate and view your Google Analytics data on v4

Features
--------

- View to display more visited pages
- Menu entry showing the number of visits of the current page


Translations
------------

This product has been translated into

- Catalan
- Spanish
- English


Installation
------------

Install product.analaytics by adding it to your buildout::

    [buildout]

    ...

    eggs =
        product.analytics


and then running ``bin/buildout``

Configuration
------------
Once you have installed the product in your Plone Site you will need to do the following steps

1. Create a Google service account: https://console.cloud.google.com/iam-admin/serviceaccounts/project. For more information check: https://cloud.google.com/iam/docs/service-account-overview
2. Once you have created your service account you need to create credentials as JSON type and download that file. Notice Google won't allow you to redownload the file
3. Place the file in your server in the following path: `/opt/analytics/google_analytics_key.json`
4. Create a Google Analytics property if you do not have one and give Reader permissions to your service account
5. Configure in ``/@@analytics-settings`` controlpanel the property id of your Analytics

TODO
-----------

- Move the expected json file path to enviroment variable so it can be configured
- Make a dashboard showing some nice graphics. Prior to Analytics v4 we were able to show graphics with Google API Client Library but that does not work yet for v4


Classifiers
-----------

Framework

- Plone 5.2
- Plone 6.0

Programming Language

- Python +3.7

License
-------

The project is licensed under the GPLv2.
