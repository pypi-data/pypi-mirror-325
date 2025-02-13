import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
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
        df = pd.DataFrame({"Kategori Adı": theme_names, "Kategori ID": theme_ids})
        return df

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
            return []

        tablo_listesi = []

        while True:
            rows = driver.find_elements(By.XPATH, "//tr")
            for row in rows:
                excel_links = row.find_elements(By.XPATH, ".//a[contains(@href, 'DownloadIstatistikselTablo')]")
                if excel_links:
                    title_text = "Bilinmeyen_Tablo"
                    for prev_row in reversed(rows[: rows.index(row)]):
                        title_cells = prev_row.find_elements(By.XPATH, ".//td")
                        if title_cells and title_cells[0].text.strip():
                            title_text = title_cells[0].text.strip()
                            break
                    
                    safe_title = re.sub(r'[<>:"/\\|?*]', "", title_text).replace(" ", "_")
                    file_url = excel_links[0].get_attribute("href")
                    tablo_listesi.append((safe_title, file_url))

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
        return tablo_listesi

    def tablolar(self, kategori_adi):
        """ Bir kategorideki tüm tablo isimlerini döndürür. """
        kategori = self.kategoriler[self.kategoriler["Kategori Adı"] == kategori_adi]["Kategori ID"].unique()
        if len(kategori) == 0:
            print("❌ Kategori bulunamadı!")
            return []

        for theme in kategori:
            tablo_listesi = self._get_tablo_links(theme)
            return [tablo[0] for tablo in tablo_listesi]  # Sadece tablo isimlerini döndür

    def indir_tablo(self, kategori_adi, tablo_adi):
        """ Kullanıcının belirttiği tabloyu indirir. """
        kategori = self.kategoriler[self.kategoriler["Kategori Adı"] == kategori_adi]["Kategori ID"].unique()
        if len(kategori) == 0:
            print("❌ Kategori bulunamadı!")
            return

        for theme in kategori:
            tablo_listesi = self._get_tablo_links(theme)

            for safe_title, file_url in tablo_listesi:
                if tablo_adi in safe_title:
                    file_path = os.path.join(self.download_folder, f"{safe_title}.xls")
                    
                    print(f"📥 {safe_title} indiriliyor...")
                    response = requests.get(file_url, stream=True)
                    with open(file_path, "wb") as file:
                        for chunk in response.iter_content(chunk_size=8192):
                            file.write(chunk)

                    print(f"✅ {safe_title} indirildi: {file_path}")
                    return

        print(f"❌ '{tablo_adi}' adlı tablo bulunamadı!")


