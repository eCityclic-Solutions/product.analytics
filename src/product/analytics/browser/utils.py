# -*- coding: utf-8 -*-
from apiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
from plone import api
from plone.memoize import ram

import httplib2
import os
import time


# The scope for the OAuth2 request.
SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'

# The location of the key file with the key data.
KEY_FILEPATH = '/opt/analytics/google_analytics_key.json'


def _cached_views(method, ga_id, time_interval):
    return (ga_id, time_interval, time.time() // (60 * 60))


def get_service():
    scopes = [SCOPE]
    file_path = os.path.abspath(KEY_FILEPATH)
    if not os.path.exists(file_path):
        return None

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        file_path, scopes=scopes)

    http = httplib2.Http()
    http = credentials.authorize(http)
    service = build('analytics', 'v3', http=http, cache_discovery=False)
    return service


def get_analytics_query(service, ga_id, time_interval):
    try:
        data_query = service.data().ga().get(**{
            'ids': 'ga:' + ga_id,
            'dimensions': 'ga:pageTitle, ga:pagePath',
            'metrics': 'ga:pageviews',
            'start_date': str(time_interval) + 'daysAgo',
            'end_date': 'today',
            'sort': '-ga:pageviews',
            'max_results': 10000,
        })
        return data_query.execute()
    except HttpError:
        return None


def get_views():
    ga_id = get_ga_id()
    time_interval = get_time_interval()
    if not ga_id:
        return None
    return _get_views(ga_id, time_interval)


@ram.cache(_cached_views)
def _get_views(ga_id, time_interval):
    service = get_service()
    if not service:
        return None
    json_structure = get_analytics_query(service, ga_id, time_interval)
    return json_structure


def get_access_token():
    file_path = os.path.abspath(KEY_FILEPATH)
    return ServiceAccountCredentials.from_json_keyfile_name(
        file_path, SCOPE).get_access_token().access_token


def get_ga_id():
    return api.portal.get_registry_record('product.analytics.ga_id')


def get_time_interval():
    return api.portal.get_registry_record('product.analytics.time_interval')
