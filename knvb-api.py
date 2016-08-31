import click
import datetime
import json
import md5
import requests
import codecs


def init(base_url, key, path):
  """
  Vraag de initialisatie URL op bij de KNVB Api; vervolgens krijg je
  een PHPSESSIONID terug in de ontvangen JSON-data. Deze ID dien je te
  gebruiken in vervolg aanvragen aan de API
  """
  url = '{0}/initialisatie/{1}'.format(base_url, path)
  headers = {
    'HTTP_X_APIKEY': key,
    'Content-Type': 'application/json'
  }

  r = requests.get(url, headers=headers)
  session_id = r.json()['List'][0]['PHPSESSID']
  click.echo('Session ID received: {0}'.format(session_id))

  return session_id


def do_request(base_url, api_path, key, session_id, extra_params=''):
  """
  Voer een aanvraag uit op de KNVB API, bijvoorbeeld /teams; hiermee
  vraag je alle team-data op
  """
  hashStr = md5.new('{0}#{1}#{2}'.format(key,
                                         api_path,
                                         session_id)).hexdigest()

  url = '{0}{1}?PHPSESSID={2}&hash={3}&{4}'.format(base_url,
                                                   api_path,
                                                   session_id,
                                                   hashStr,
                                                   extra_params)

  headers = {
    'HTTP_X_APIKEY': key,
    'Content-Type': 'application/json'
  }

  click.echo('URL: {0}'.format(url))
  r = requests.get(url, headers=headers)
  json_data = r.json()

  return json_data


def store_data(json_data):
  """
  Verkregen data opslaan als JSON bestand
  """
  if json_data['List']:
    dt = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
    with codecs.open('output_{0}.json'.format(dt), 'w', 'utf-8') as temp:
      temp.write(json.dumps(json_data, indent=2))


@click.command()
@click.option('--key', prompt='API Key', help='The API key')
@click.option('--path', prompt='API Path', help='The path used with the API')
def get_data(key, path):
  """
  Console aanroep
  """
  base_url = 'http://api.knvbdataservice.nl/api'
  session_id = init(base_url, key, path)
  weeknummer = datetime.datetime.now().isocalendar()[1]
  json_data = do_request(base_url,
                         '/wedstrijden',
                         key,
                         session_id,
                         'weeknummer={0}'.format(weeknummer))

  store_data(json_data)

if __name__ == '__main__':
    get_data()
