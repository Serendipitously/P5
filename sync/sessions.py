from urlparse import urljoin

import requests
from django.conf import settings


def _validate_setting_set(name):
    if not getattr(settings, name):
        raise Exception('Django setting not set: %s' % name)


class BaseSession(requests.Session):
  host_root = None

  def request(self, method, url, **kwargs):
    if 'timeout' not in kwargs:
      kwargs['timeout'] = settings.EXTERNAL_REQUEST_TIMEOUT

    url = urljoin(self.host_root, url)
    return super(BaseSession, self).request(method, url, **kwargs)