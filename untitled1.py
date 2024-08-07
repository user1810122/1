# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/129vEdBKv9HgeuUxkRqL2UhexvFC_MQeg
"""

class Urun:
  #bu kod bloğunda stoktaki ürünlerin özelliklerini bir class içinde tanımlıyoruz
    def __init__(self, urun_id, isim, miktar, fiyat):
        self.urun_id = urun_id
        self.isim = isim
        self.miktar = miktar
        self.fiyat = fiyat

    def miktar_guncelle(self, yeni_miktar):
        self.miktar = yeni_miktar

    def fiyat_guncelle(self, yeni_fiyat):
        self.fiyat = yeni_fiyat

class Envanter:
  #bu kod bloğunda kodumuzda kullanacağımız fonksiyonları class a tanımlıyoruz
    def __init__(self):
        self.urunler = {}

    def urun_ekle(self, urun):
        self.urunler[urun.urun_id] = urun

    def urun_sil(self, urun_id):
        if urun_id in self.urunler:
            del self.urunler[urun_id]

    def urun_getir(self, urun_id):
        return self.urunler.get(urun_id)

    def miktar_guncelle(self, urun_id, yeni_miktar):
        urun = self.urun_getir(urun_id)
        if urun:
            urun.miktar_guncelle(yeni_miktar)

    def fiyat_guncelle(self, urun_id, yeni_fiyat):
        urun = self.urun_getir(urun_id)
        if urun:
            urun.fiyat_guncelle(yeni_fiyat)

def calistir():
    envanter = Envanter()
   #burada kullanıcının seçim yapması içn ekrana seçenekleri yazdırıyoruz
    while True:
        print("\nEnvanter Yönetimi")
        print("1. Ürün Ekle")
        print("2. Ürün Güncelle")
        print("3. Ürün Sil")
        print("4. Envanteri Görüntüle")
        print("5. Çıkış")

        secim = input("Seçiminizi yapın: ")
        #kullanıcnın seçimine göre gerekli fonksiyonları çağırıyoruz
        if secim == "1":
            urun_id = input("Ürün ID: ")
            isim = input("Ürün İsmi: ")
            miktar = int(input("Miktar: "))
            fiyat = float(input("Fiyat: "))
            urun = Urun(urun_id, isim, miktar, fiyat)
            envanter.urun_ekle(urun)
            print("Ürün eklendi.")

        elif secim == "2":
            urun_id = input("Güncellenecek Ürün ID: ")
            yeni_miktar = int(input("Yeni Miktar: "))
            yeni_fiyat = float(input("Yeni Fiyat: "))
            envanter.miktar_guncelle(urun_id, yeni_miktar)
            envanter.fiyat_guncelle(urun_id, yeni_fiyat)
            print("Ürün güncellendi.")

        elif secim == "3":
            urun_id = input("Silinecek Ürün ID: ")
            envanter.urun_sil(urun_id)
            print("Ürün silindi.")

        elif secim == "4":
            for urun_id, urun in envanter.urunler.items():
                print(f"ID: {urun_id}, İsim: {urun.isim}, Miktar: {urun.miktar}, Fiyat: {urun.fiyat}")

        elif secim == "5":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    calistir()

import unittest
#yazdığımız kodun test aşaması

class EnvanterTest(unittest.TestCase):
    def setUp(self):
        self.envanter = Envanter()
        self.urun = Urun("1", "Defter", 50, 2.5)
        self.envanter.urun_ekle(self.urun)

    def test_urun_ekle(self):
        self.assertEqual(len(self.envanter.urunler), 1)

    def test_urun_sil(self):
        self.envanter.urun_sil("1")
        self.assertEqual(len(self.envanter.urunler), 0)

    def test_miktar_guncelle(self):
        self.envanter.miktar_guncelle("1", 75)
        self.assertEqual(self.envanter.urun_getir("1").miktar, 75)

    def test_fiyat_guncelle(self):
        self.envanter.fiyat_guncelle("1", 3.0)
        self.assertEqual(self.envanter.urun_getir("1").fiyat, 3.0)

if __name__ == "__main__":
    unittest.main(exit=False)