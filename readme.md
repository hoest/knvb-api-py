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

Het is ook mogelijk om met [virtualenv](https://virtualenv.pypa.io) te werken.

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

## Output

Voorbeeld van de output:

```json
{
  "errorcode": 1000,
  "message": "Ok, matches data follows",
  "List": [
    {
      "PuntenTeam2Strafsch": null,
      "ClassId": "25",
      "District": "W1",
      "Kleedkamer_official": "",
      "ThuisClub": "Spakenburg JO11-6 ZA",
      "ThuisLogo": "http://bin617.website-voetbal.nl/sites/voetbal.nl/files/knvblogos/BBBZ43E.png",
      "Facility_Id": "FGDZ12N",
      "UitClubNummer": "BBCC89Q",
      "Aantal_Fotos": 0,
      "Competitie": "W1-B4200*-25-468830!",
      "PuntenTeam1Verl": null,
      "Tijd": "0830",
      "UitTeamId": "275723",
      "PouleId": "468830",
      "Hulpscheidsrechter2": "",
      "Hulpscheidsrechter1": "",
      "PuntenTeam2Verl": null,
      "PuntenTeam1": null,
      "PuntenTeam2": null,
      "Overzicht_Reacties": "",
      "VeldClub": "",
      "WedstrijdDag": 2,
      "CompType": "B",
      "Kleedkamer_thuis": "",
      "CompId": "B4200",
      "MatchID": "10735335",
      "VeldKNVB": "veld 4 Spakenburg",
      "ThuisClubNummer": "BBBZ43E",
      "Aantal_Reacties": "",
      "ThuisTeamId": "256736",
      "Facility_Adres": "Westdijk 12",
      "Scheidsrechter": "",
      "Aantal_Videos": 0,
      "Verzameltijd": "",
      "PuntenTeam1Strafsch": null,
      "Datum": "2016-09-03",
      "UitClub": "VVZ '49 JO11-5 ZA",
      "Facility_naam": "Sportpark De Westmaat",
      "Zaalveld": "Veld",
      "UitLogo": "http://knvbclubapp.nl/sites/all/themes/knvbdataservice/images/clublogo/1420815713.png",
      "Bijzonderheden": "",
      "Facility_Stad": "BUNSCHOTEN-SPAKENBURG",
      "WedstrijdNummer": "31036",
      "Kleedkamer_uit": "",
      "Facility_Postcode": "3752AE"
    },
    { ... }
  ]
}
```
