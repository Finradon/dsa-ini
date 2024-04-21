# dsa_ini

## Meister-Tool zur Hilfe während DSA4.1-Kämpfen

Dieses Tool hilft dabei, Initiative, Wunden, Schaden und mehr während DSA4.1-Kämpfen zu verwalten. Die App ist mit python und streamlit entwickelt worden.
Aktuell nur bedingt nutzbar.

### Starten

```console
pip install requirements.txt
streamlit run helden_ini.py
```

Es wird immer mit einem "Dummy" gestartet. Diesen kann man ersetzen indem man auf `Add Bandit` oder `Add Orc` klickt. Die Initiative wird dann ausgewürfelt und mit `Sort` kann man dann anhand Initiative sortieren. Mit `Next` kann man die Initiative weiterschalten, mit `Reset` wird alles zurückgesetzt.

Man kann mit dem `AT` oder `PA` Knopf eine Attacke/Parade auswürfeln und automatisch das Ergebnis einsehen. Schaden kann man ebenfalls bereits eingeben, mit automatischer Wunden-Berechnung (doch dieses Feature bedarf noch ein wenig Überarbeitung).