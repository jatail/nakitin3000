# Nakitin3000
Nakittautumisjärjestelmä tapahtumajärjestejille. Live: <https://nakit.asteriski.fi>.

Author: [Janne Iltanen](https://github.com/jatail)

## Ohjeet kehitykseen
Mukana tulevat tarvittavat docker-tiedostot.
```
git clone https://github.com/asteriskiry/nakitin3000.git
cd nakitin3000
docker-compose up
```
Tämän jälkeen nakittimen pitäisi pyöriä osoitteessa <https://localhost:888>.

Uuden pääkäyttäjän pääset lisäämään näin:

Ensin ota "CONTAINER ID" talteen komennolla `docker ps`. Tämän jälkeen:
```
docker exec -it CONTAINER_ID /bin/sh
python manage.py createsuperuser
```
Korvaa CONTAINER_ID tietysti kontin id:llä jonka sait `docker ps`-komennolla. Adminhommia pääset tekemään osoitteessa <https://localhost:888/admin>.
