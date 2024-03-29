Pomodoro Zamanlayıcı Uygulaması
==============================

Bu uygulama, çalışma oturumlarınızı ve molalarınızı yönetmenize yardımcı olan basit bir Pomodoro Zamanlayıcısıdır. Python dili kullanılarak yazılmıştır ve grafiksel kullanıcı arayüzü için Tkinter kütüphanesini kullanır.

Özellikler
----------
- Özelleştirilebilir çalışma süresi ve tekrar sayısı
- Seçilebilir arka plan sesleri ile sesli bildirimler
- Zaman azaldıkça zamanlayıcı halkasının renginin beyazdan kahverengine geçişi
- Zamanlayıcıyı başlatma, durdurma ve sıfırlama kontrolleri

Gereksinimler
-------------
- Python 3.x
- Tkinter kütüphanesi (genellikle Python ile birlikte gelir)
- Pygame kütüphanesi (ses oynatma için)

Kullanım
--------
Uygulamayı çalıştırmak için, main.py dosyasını Python ile yürütün:

    python main.py

Arayüz kontrollerini kullanarak arka plan sesini seçebilir ve çalışma süresi ile tekrar sayısını ayarlayabilirsiniz.

Ses Dosyaları
-------------
Lütfen ses dosyalarının main.py dosyası ile aynı dizinde bulunduğundan emin olun. Varsayılan ses dosyaları şunlardır:
- fire_sound.mp3
- rain_sound.mp3
- waves_sound.mp3
- birds_sound.mp3
- storm_sound.mp3

Bu dosyaları, adlandırma kurallarına uygun olarak herhangi başka MP3 dosyaları ile değiştirebilirsiniz.

Özelleştirme
-------------
Çalışma süresini ve tekrar sayısını `TimerLogic` sınıfının `__init__` metodunun parametrelerini değiştirerek özelleştirebilirsiniz.

Destek
------
Herhangi bir sorunla karşılaşırsanız veya önerileriniz varsa, lütfen projenin GitHub sayfasında bir sorun açın.


