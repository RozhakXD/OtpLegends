# OTP LEGENDS - MOBILE LEGENDS OTP SPAMMER
![OTP-LEGENDS](https://github.com/user-attachments/assets/d6bac68e-7fe6-4eb3-81f7-611a43ce2e34)

**OTPLegends** adalah alat sederhana yang digunakan untuk melakukan spamming kode OTP (One-Time Password) ke akun Mobile Legends Bang-Bang secara otomatis. Alat ini dapat digunakan untuk tujuan prank atau menguji kelemahan sistem keamanan OTP.

**Catatan Penting: Penggunaan alat ini hanya untuk tujuan edukasi atau prank dengan persetujuan. Penyalahgunaan alat ini dapat melanggar ketentuan layanan atau hukum yang berlaku. Gunakan dengan bijak!**

## Fitur
- Menggunakan threading untuk mempercepat proses pengiriman.
- Menampilkan hasil pengiriman secara real-time menggunakan pustaka `rich`.
- Mengirimkan spam OTP ke akun Mobile Legends.
- Mendukung pengaturan jumlah pengiriman.

## Cara Kerja
OTPLegends mengirimkan permintaan POST ke API Mobile Legends dengan parameter `roleId` dan `zoneId` dari akun target. Program ini menggunakan threading agar dapat mengirimkan beberapa permintaan sekaligus, serta menampilkan hasilnya menggunakan tampilan yang interaktif dengan **Rich**.

## Instalasi
1. Clone repositori ini ke komputer Anda:
    ```bash
    git clone https://github.com/RozhakXD/OtpLegends.git
    cd OtpLegends
    ```
2. Install dependensi yang diperlukan:
    ```bash
    pip install -r requirements.txt
    ```
3. Jalankan program:
    ```bash
    python Run.py
    ```

## Penggunaan
1. Setelah menjalankan program, Anda akan diminta memasukkan beberapa input seperti:
    - **Role ID**: ID akun target di Mobile Legends.
    - **Jumlah Spam**: Jumlah OTP yang ingin dikirimkan.
    - **Zone ID**: Zona ID akun target.
3. Alat ini kemudian akan mulai mengirimkan OTP secara otomatis berdasarkan input yang telah diberikan. Anda dapat menghentikan proses kapan saja dengan menekan `CTRL + C` atau `CTRL + Z`.

## Struktur Kode
- **requirements.txt**: Berisi daftar pustaka Python yang dibutuhkan oleh program (seperti `requests`, `rich`, dan `fake-useragent`).
- **Run.py**: File utama yang menjalankan seluruh proses spamming OTP.

## Teknologi yang Digunakan
- **Fake-UserAgent**: Digunakan untuk menghasilkan header User-Agent palsu secara dinamis.
- **Python**: Bahasa pemrograman utama yang digunakan untuk membangun alat ini.
- **Rich**: Digunakan untuk mempercantik output tampilan di terminal.
- **Requests**: Pustaka HTTP untuk mengirimkan permintaan POST ke server Mobile Legends.

## Tangkapan Layar
![Screenshot](https://github.com/user-attachments/assets/4d32ef26-27fd-4341-8068-4ce6daf88ed0)

## Dukungan
Jika Anda merasa proyek ini bermanfaat dan ingin mendukung pengembang, Anda bisa memberikan dukungan melalui:

- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)

Setiap dukungan akan sangat membantu untuk pengembangan lebih lanjut dari proyek ini.

## Catatan
- Anda mungkin perlu menyesuaikan roleId dan zoneId untuk target agar alat ini bekerja dengan benar.
- Jika API yang digunakan Mobile Legends berubah, alat ini mungkin tidak berfungsi lagi.

## Disclaimer
Kami tidak bertanggung jawab atas penggunaan alat ini yang melanggar hukum atau kebijakan platform. Penggunaan alat ini sepenuhnya adalah tanggung jawab pengguna.

## Lisensi
Proyek ini dilisensikan di bawah [MIT License]().
