import os
import requests
from bs4 import BeautifulSoup
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TuikScraper:
    def __init__(self):
        self.base_url = "https://data.tuik.gov.tr/"
        self.download_folder = os.path.join(os.environ["USERPROFILE"], "Downloads") if os.name == "nt" else os.path.join(os.environ["HOME"], "Downloads")
        print(f"📂 Dosyalar şu klasöre indirilecek: {self.download_folder}")
        self.kategoriler = self._get_kategoriler()

    def _get_kategoriler(self):
        """ TÜİK'teki tüm veri kategorilerini döndürür."""
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, "html.parser")
        themes = soup.find_all("div", class_="text-center")
        theme_names = [a.text.strip() for t in themes for a in t.find_all("a")]
        theme_ids = [a["href"].split("=")[-1] for t in themes for a in t.find_all("a")]
        return list(zip(theme_names, theme_ids))

    def _get_driver(self):
        """ Selenium WebDriver başlatır. """
        options = Options()
        options.add_argument("--headless")  # Arka planda çalıştır
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def _get_tablo_links(self, kategori_id):
        """ Bir kategorideki tüm tablo başlıklarını ve bağlantıları döndürür. """
        driver = self._get_driver()
        url = f"https://data.tuik.gov.tr/Kategori/GetKategori?p={kategori_id}#nav-db"
        driver.get(url)
        time.sleep(3)

        try:
            # "İstatistiksel Tablolar" sekmesine tıkla
            istatistiksel_tablolar = driver.find_element(By.ID, "nav-profile-tab")
            istatistiksel_tablolar.click()
            time.sleep(3)
        except:
            print("❌ İstatistiksel Tablolar sekmesi bulunamadı!")
            driver.quit()
            return {}

        tablo_linkleri = {}

        while True:
            rows = driver.find_elements(By.XPATH, "//tr")
            for row in rows:
                excel_links = row.find_elements(By.XPATH, ".//a[contains(@href, 'DownloadIstatistikselTablo')]")

                if excel_links:
                    title_cells = row.find_elements(By.XPATH, ".//td")
                    title_text = title_cells[0].text.strip() if title_cells and title_cells[0].text.strip() else "Bilinmeyen_Tablo"

                    # Temiz başlık
                    safe_title = re.sub(r'[<>:"/\\|?*]', "", title_text).replace(" ", "_")

                    # Başlık ve link eşleştir
                    tablo_linkleri[safe_title] = excel_links[0].get_attribute("href")

            # Sayfada "Sonraki" butonu varsa tıkla
            try:
                next_button = driver.find_element(By.ID, "istatistikselTable_next")
                if "disabled" in next_button.get_attribute("class"):
                    break  # Son sayfa
                else:
                    next_button.click()
                    time.sleep(3)
            except:
                break  # Sonraki sayfa yok

        driver.quit()
        return tablo_linkleri

    def tablolar(self, kategori_adi):
        """ Bir kategorideki tüm tablo isimlerini liste olarak döndürür. """
        kategori = [k[1] for k in self.kategoriler if k[0] == kategori_adi]
        if not kategori:
            print("❌ Kategori bulunamadı!")
            return []

        for theme in kategori:
            return list(self._get_tablo_links(theme).keys())  # Sadece tablo isimlerini döndür

    def indir_tablo(self, kategori_adi, tablo_adi):
        """ Kullanıcının belirttiği tabloyu indirir. """
        kategori = [k[1] for k in self.kategoriler if k[0] == kategori_adi]
        if not kategori:
            print("❌ Kategori bulunamadı!")
            return

        for theme in kategori:
            tablo_linkleri = self._get_tablo_links(theme)

            if tablo_adi in tablo_linkleri:
                file_url = tablo_linkleri[tablo_adi]
                file_path = os.path.join(self.download_folder, f"{tablo_adi}.xls")

                print(f"📥 {tablo_adi} indiriliyor...")
                response = requests.get(file_url, stream=True)
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)

                print(f"✅ {tablo_adi} indirildi: {file_path}")
                return

        print(f"❌ '{tablo_adi}' adlı tablo bulunamadı!")

    def indir(self, kategori_adi):
        """ Bir kategorideki tüm tabloları direkt indirir. """
        kategori = [k[1] for k in self.kategoriler if k[0] == kategori_adi]
        if not kategori:
            print(f"❌ '{kategori_adi}' kategorisinde indirilecek tablo bulunamadı!")
            return

        for theme in kategori:
            tablo_linkleri = self._get_tablo_links(theme)

            for tablo_adi, file_url in tablo_linkleri.items():
                file_path = os.path.join(self.download_folder, f"{tablo_adi}.xls")

                print(f"📥 {tablo_adi} indiriliyor...")
                response = requests.get(file_url, stream=True)
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)

                print(f"✅ {tablo_adi} indirildi: {file_path}")

if __name__ == "__main__":
    tuik = TuikScraper()

    
    tuik.indir("Enflasyon ve Fiyat")
       