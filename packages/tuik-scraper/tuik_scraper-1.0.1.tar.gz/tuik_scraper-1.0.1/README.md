# TÜİK Scraper

Bu kütüphane, TÜİK verilerini kolayca çekip işlemenizi sağlar.

## Kurulum
```bash
pip install tuik_scraper

## Örnek Kullanım
from tuik_scraper import TuikScraper

tuik = TuikScraper()

tuik.kategoriler  # Kategori isimlerini yazdırır

tuik.tablolar("Enflasyon ve Fiyat") #Kategorideki tablo isimlerini getirir

#tuik.tablolar("kategori_adı")

tuik.indir_tablo("Enflasyon ve Fiyat", "İstatistiksel_Tablolar_Yeni_Mevsim_etkisinden_arındırılmış_TÜFE_göstergeleri") #Seçilen bir tabloyu indirir

#tuik.indir_tablo(kategori_adi, tablo_adi)

tuik.indir("Enflasyon ve Fiyat")  # Kategorideki tüm tabloları indirir
#tuik.indir(kategori_adı)
