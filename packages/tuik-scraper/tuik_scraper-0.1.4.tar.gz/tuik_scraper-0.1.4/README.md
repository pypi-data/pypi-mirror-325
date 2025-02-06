# TÜİK Scraper

Bu kütüphane, TÜİK verilerini kolayca çekip işlemenizi sağlar.

## Kurulum
```bash
pip install tuik_scraper

## Örnek Kullanım
from tuik_scraper import TuikScraper

tuik = TuikScraper()
print(tuik.kategoriler)  # Kategori isimlerini alır
tuik.indir("Enflasyon ve Fiyat")  # Veri indir
