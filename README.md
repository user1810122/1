*Envanter Yönetim Sistemi
Bu proje, Python'da nesne yönelimli programlama prensiplerini kullanarak geliştirilen basit bir envanter yönetim sistemidir. Sistem, kullanıcıların öğe eklemesine, güncellemesine ve kaldırmasına ve envanter seviyelerini takip etmesine olanak tanır.

*Özellikler
Öğeleri ekleme, güncelleme ve kaldırma
Envanter seviyelerini görüntüleme
Gereksinimler
Python 3.x
*Kurulum
Bu projeyi klonlayın:
git clone <repository-url>
Proje dizinine gidin:
cd <repository-directory>
*Kullanım
Ana Python betiğini çalıştırarak envanter yönetim sistemini başlatın:
python envanter.py
Komut satırı arayüzünde sunulan seçeneklerden birini seçerek sistemi kullanın:

1. Öğeyi Ekle: Yeni bir öğe ekler
2. Öğeyi Güncelle: Mevcut bir öğenin miktarını ve fiyatını günceller
3. Öğeyi Kaldır: Mevcut bir öğeyi envanterden kaldırır
4. Envanteri Görüntüle: Envanterdeki tüm öğeleri görüntüler
5. Çıkış: Sistemden çıkar
*Testler
Testleri çalıştırmak için aşağıdaki komutu kullanın:
python -m unittest test_envanter.py
Testler, unittest modülü kullanılarak yazılmıştır ve aşağıdaki fonksiyonları içerir:
test_urun_ekle: Bir öğenin envantere eklenmesini test eder
test_urun_sil: Bir öğenin envanterden kaldırılmasını test eder
test_miktar_guncelle: Bir öğenin miktarının güncellenmesini test eder
test_fiyat_guncelle: Bir öğenin fiyatının güncellenmesini test eder

