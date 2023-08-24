# Ses Kaydetme ve E-posta İle Gönderme Aracı

Bu araç, ses kaydı yapmanıza ve kaydedilen sesi belirtilen bir e-posta adresine göndermenize olanak tanır.

## Kullanım Talimatları

1. Öncelikle, gerekli kütüphaneleri indirin. Aşağıdaki adımları takip edebilirsiniz:

   ```bash
   pip install -r requirements.txt
   ```
2. voice.py adlı bu Python betiğini çalıştırarak, özel bir .exe dosyası oluşturabilirsiniz. Betiği aşağıdaki gibi çalıştırın:
   ```bash
   python create_exe.py -s <Gönderen E-posta> -p <Gönderen Şifre> -r <Alıcı E-posta> -d <Kaydedilecek Süre)  -n <Exe İsmi> -c <İcon>
    ```

3. Betik çalıştırıldığında, exe dosyasına dönüşecek ve o exe dosyası açıldığında ses kaydedilecek ve belirtilen alıcı e-posta adresine gönderilecektir.


## Argümanlar
- -s veya --sender-email: Gönderenin e-posta adresi (Zorunlu).
- -p veya --sender-password: Gönderenin e-posta şifresi (Zorunlu).
- -r veya --receiver-email: Alıcının e-posta adresi (Zorunlu).
- -d veya --duration: Kaydedilecek sesin süresi (Varsayılan: 5 saniye).
- -n veya --exe-name: Oluşturulacak .exe dosyasının adı (Zorunlu).
- -c veya --icon-path: İkon dosyasının yolu (isteğe bağlı).


## Örnek Kullanım
Aşağıda, aracı nasıl kullanacağınıza dair örnek bir komut verilmiştir:

```bash
python create_exe.py -s myemail@gmail.com -p mypassword -r recipient@example.com -d 10 -n audio_sender -c icon.ico
```
Bu komut, 10 saniye süreyle ses kaydedecek ve audio_sender.exe adında bir dosya oluşturacaktır. Ayrıca, icon.ico adlı bir ikon dosyasını da ekleyecektir.

## Sorumluluk Reddi

Bu araç, kullanıcıların eğitim amaçları için bir örnek sunumu olarak tasarlanmıştır. Aracın kullanımı tamamen kullanıcının kendi sorumluluğundadır. Geliştirici, aracın hatalı kullanımından veya verilerin yetkisiz erişim sonucu açığa çıkmasından sorumlu tutulamaz.

Bu aracı kullanırken, kişisel veya hassas bilgileri paylaşmamaya dikkat edin ve veri güvenliği önlemlerini almayı unutmayın. Aracın olası güvenlik açıkları veya veri ihlalleri sonucunda ortaya çıkabilecek zarar veya kayıplardan geliştirici muaf tutulur.

**Not:** Lütfen bu aracı etik ve yasal sınırlar içinde kullanın. Kötü niyetli veya yasa dışı kullanım, yasal sonuçlara neden olabilir.


## Lisans

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

Bu projeyi [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) altında lisansladık. Lisansın tam açıklamasını [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) sayfasında bulabilirsiniz.




   
