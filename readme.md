# KNVB Api Python script

Met behulp van dit basic Python (2.7) script kun je alle data van de
wedstrijden van de huidige week downloaden bij de KNVB. Deze data wordt
vervolgens als JSON bestand opgeslagen met de naam `output_{%datetime%}.json`.

Vervolgens kun je met deze data zelf andere zaken ondernemen.

Je moet wel een **API Key** en een **API Path** opgeven. Deze gegevens
krijg je van de KNVB, zodat je een abonnement hebt afgesloten bij hun
KNVB Api Dataservice.

## Installeren

Haal de code lokaal, d.m.v. `git clone`
Nu kun je de afhankelijkheden installeren:

```
$ pip install -r requirements.txt
```

Het is ook mogelijk om met (virtualenv)[1] te werken.

## Draaien van het script

Als alle afhankelijkheden correct geinstalleerd zijn, kun je het script
draaien. Dit doe je via de commandline:

```
$ python knvb-api.py
```

Nu krijg je twee vragen waarop je antwoord dient te geven om verder te
kunnen gaan:

```
API Key: ...
API Path: ...
```

Hierna wordt de URL voor de KNVB Api opgebouwd en een zgn. `PHPSESSIONID`
opgevraagd. Als alles goed gegaan is, krijg je een eerder genoemd `output.json`
bestand.

## Help?

```
$ python knvb-api.py --help
```

[1]: https://virtualenv.pypa.io/en/stable/
