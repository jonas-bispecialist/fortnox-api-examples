# 01 – Hämta data från Fortnox API med Python

Kod till guiden [Så hämtar du data från Fortnox API med Python](https://jonashertz.com/fortnox-api-python/).

Guiden förklarar varje steg. Här finns bara koden.

## Innehåll

`fortnox-api-python.ipynb` är en Jupyter-notebook med tre celler:

1. Spara Client ID, Client Secret och Tenant ID i Windows autentiseringshanterare (körs en gång)
2. Hämta en access token med servicekontot
3. Hämta kontoplanen och spara den som `konton.csv`

## Kräver

- Windows och Python 3.10 eller senare
- `pip install jupyterlab keyring requests pandas`
- En Fortnox-integration med servicekonto, godkänd av en systemadministratör (steg 1–3 i guiden)

## Obs

- Inga nycklar finns i koden, och lägg aldrig in dem där.
- Testad 2026-09-15. Hittar du fel, skapa gärna ett issue.
- Inte kopplad till eller godkänd av Fortnox AB.
