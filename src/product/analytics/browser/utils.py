# -*- coding: utf-8 -*-
from apiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
from plone import api
from plone.memoize import ram

import os
import time


# The scope for the OAuth2 request.
SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'

# The location of the key file with the key data.
KEY_FILEPATH = '/opt/analytics/google_analytics_key.json'


def _cached_views(method, property_id, time_interval):
    return (property_id, time_interval, time.time() // (60 * 60))


def get_analytics():
    scopes = [SCOPE]
    file_path = os.path.abspath(KEY_FILEPATH)
    if not os.path.exists(file_path):
        return None

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        file_path,
        scopes=scopes,
    )

    try:
        analytics = build('analyticsdata', 'v1beta', credentials=credentials, cache_discovery=False)
    except Exception:
        analytics = None
    return analytics


def get_analytics_query(analytics, property_id, time_interval):
    try:
        property_id = f'properties/{property_id}'
        request = {
            'requests': [{
                'dateRanges': [{
                    'startDate': f'{str(time_interval)}daysAgo',
                    'endDate': 'today',
                }],
                'dimensions': [{'name': 'pageTitle'}, {'name': 'pagePath'}],
                'metrics': [{'name': 'screenPageViews'}],
                'limit': 10000,
            }],
        }

        data_query = analytics.properties().batchRunReports(
            property=property_id,
            body=request,
        )

        return data_query.execute()
    except HttpError:
        return None


def get_views():
    property_id = get_property_id()
    time_interval = get_time_interval()
    if not property_id:
        return None
    return _get_views(property_id, time_interval)


@ram.cache(_cached_views)
def _get_views(property_id, time_interval):
    analytics = get_analytics()
    if not analytics:
        return None

    json_structure = get_analytics_query(analytics, property_id, time_interval)
    return json_structure


def get_access_token():
    try:
        file_path = os.path.abspath(KEY_FILEPATH)
        file = ServiceAccountCredentials.from_json_keyfile_name(file_path, SCOPE)
        token = file.get_access_token().access_token
        return token
    except FileNotFoundError:
        return None


def get_property_id():
    try:
        return api.portal.get_registry_record('product.analytics.property_id')
    except api.exc.InvalidParameterError:
        return None


def get_time_interval():
    try:
        return api.portal.get_registry_record('product.analytics.time_interval')
    except api.exc.InvalidParameterError:
        return None
