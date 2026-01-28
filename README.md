Projekti i Scraping-ut të Kriptomonedhave

Ky projekt është krijuar si pjesë e detyrës për mbledhjen dhe integrimin e të dhënave nga interneti. Ai kombinon teknikën e **Web Scraping** me përdorimin e një **API** publike.

Çfarë bën ky program?
1. **Web Scraping**: Merr 5 titujt e fundit të lajmeve nga faqa [CoinDesk](https://www.coindesk.com/) duke përdorur `BeautifulSoup`.
2. **Integrimi i API**: Merr çmimin aktual të Bitcoin në USD nga API publike e [CoinGecko](https://www.coingecko.com/).
3. **Ruajtja e të dhënave**: Bashkon lajmet me çmimin aktual dhe i ruan ato në një skedar `lajmet_kripto.csv`.

Libraritë e nevojshme
Për të ekzekutuar këtë kod, duhet të keni të instaluara libraritë e mëposhtme:
* `requests` - për kërkesat HTTP.
* `beautifulsoup4` - për analizimin e kodit HTML.

Mund t'i instaloni me komandën:
```bash
pip install requests beautifulsoup4
