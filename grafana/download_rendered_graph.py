#!/usr/bin/env python3
import io

from requests import get


def download(url):
    '''
    Doc: http://docs.grafana.org/reference/sharing/#direct-link-rendered-image
    '''
    image = get(url, stream=True)
    return io.BytesIO(image.content)


if __name__ == '__main__':
    url = 'http://play.grafana.org/render/dashboard-solo/db/' \
          'grafana-play-home?orgId=1&panelId=4&from=14992721' \
          '91563&to=1499279391563&width=1000&height=500&tz=UTC' \
          '%2B02%3A00&timeout=5000'
    download(url)
