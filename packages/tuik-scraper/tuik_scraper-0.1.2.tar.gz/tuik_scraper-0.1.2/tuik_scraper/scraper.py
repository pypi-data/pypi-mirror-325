import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
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
    
    def indir(self, kategori_adi):
        """ Belirtilen kategoriye ait verileri indirir."""
        kategori = self.kategoriler[self.kategoriler["Kategori Adı"] == kategori_adi]["Kategori ID"].unique()
        if len(kategori) == 0:
            print("❌ Kategori bulunamadı!")
            return
        
        for theme in kategori:
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            url = f"https://data.tuik.gov.tr/Kategori/GetKategori?p={theme}#nav-db"
            driver.get(url)
            time.sleep(3)

            try:
                istatistiksel_tablolar = driver.find_element(By.ID, "nav-profile-tab")
                istatistiksel_tablolar.click()
                time.sleep(3)
            except:
                print("❌ İstatistiksel Tablolar sekmesi bulunamadı!")
                driver.quit()
                return
            
            downloaded_files = set()
            while True:
                try:
                    rows = driver.find_elements(By.XPATH, "//tr")
                    excel_rows = [row for row in rows if row.find_elements(By.XPATH, ".//a[contains(@href, 'DownloadIstatistikselTablo')]")]
                    
                    if not excel_rows:
                        print("❌ Bu sayfada Excel bağlantısı bulunamadı!")
                        break
                    
                    for idx, row in enumerate(excel_rows):
                        excel_button = row.find_element(By.XPATH, ".//a[contains(@href, 'DownloadIstatistikselTablo')]")
                        file_url = excel_button.get_attribute("href")
                        
                        # Dosya adını belirleme
                        title_text = "Bilinmeyen_Tablo"
                        for prev_row in reversed(rows[: rows.index(row)]):
                            title_cells = prev_row.find_elements(By.XPATH, ".//td")
                            if title_cells and title_cells[0].text.strip():
                                title_text = title_cells[0].text.strip()
                                break
                        
                        safe_title = re.sub(r'[<>:"/\\|?*]', "", title_text).replace(" ", "_")
                        file_path = os.path.join(self.download_folder, f"{safe_title}.xls")
                        
                        if file_path in downloaded_files:
                            print(f"🔄 {safe_title}.xls zaten indirildi, atlanıyor.")
                            continue
                        
                        response = requests.get(file_url, stream=True)
                        with open(file_path, "wb") as file:
                            for chunk in response.iter_content(chunk_size=8192):
                                file.write(chunk)
                        
                        print(f"✅ {idx+1}. dosya indirildi: {file_path}")
                        downloaded_files.add(file_path)
                
                except Exception as e:
                    print("❌ Excel dosyaları indirilemedi!", e)
                    break
                
                try:
                    next_button = driver.find_element(By.ID, "istatistikselTable_next")
                    if "disabled" in next_button.get_attribute("class"):
                        print("📌 Son sayfaya ulaşıldı.")
                        break
                    else:
                        print("➡ Sonraki sayfaya geçiliyor...")
                        next_button.click()
                        time.sleep(3)
                except:
                    print("📌 Sonraki butonu bulunamadı veya artık sayfa değiştirilemiyor.")
                    break
            
            driver.quit()