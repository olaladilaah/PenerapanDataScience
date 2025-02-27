# Proyek Penerapan Data Science : 
Menyelesaikan Permasalahan Human Resources - Perusahaan Jaya Jaya Maju
- Nama: Adilah Widiasti
- Email: adilahwidiasti86@gmail.com
- Id Dicoding: olaladilah

## Business Understanding
Perusahaan Jaya Jaya Maju saat ini tengah menghadapi tantangan besar terkait dengan tingginya angka perputaran karyawan (attrition). Meskipun telah berkembang pesat menjadi perusahaan besar, manajemen sumber daya manusia di Jaya Jaya Maju masih menemui berbagai kesulitan. Sebagai dampaknya, tingkat attrition perusahaan ini mencapai lebih dari 10% dari total karyawan. Oleh karena itu, diperlukan sebuah kajian mendalam untuk mengidentifikasi faktor-faktor yang mempengaruhi perputaran karyawan ini guna membantu tim HR dalam menurunkan angka attrition yang tinggi.

### Permasalahan Bisnis
Tingginya tingkat perputaran karyawan di Jaya Jaya Maju telah memunculkan berbagai tantangan serius yang dapat berdampak besar pada kelangsungan bisnis perusahaan. Beberapa masalah utama yang timbul akibat hal ini meliputi:
1. **Penurunan Produktivitas**  
   Kehilangan karyawan, terutama yang berpengalaman, langsung memengaruhi produktivitas baik di level tim maupun organisasi secara keseluruhan. Penggantian karyawan senior yang memiliki pengetahuan dan keterampilan spesifik membutuhkan waktu yang tidak sebentar, yang dapat menghambat performa perusahaan.
2. **Gangguan pada Proses Operasional**  
   Perputaran karyawan yang tinggi dapat mengganggu kelancaran operasional sehari-hari, memperlambat penyelesaian proyek atau tugas-tugas yang tengah berjalan. Akibatnya, kualitas dan ketepatan waktu dalam pelayanan kepada klien bisa terganggu.
3. **Penurunan Kepuasan Karyawan yang Tersisa**  
   Angka perputaran karyawan yang tinggi sering kali berimbas pada menurunnya moral dan kepuasan kerja karyawan yang masih bertahan. Mereka mungkin merasa lingkungan kerja semakin tidak stabil dan kurang mendukung, yang dapat memperburuk tingkat keterikatan mereka dengan perusahaan.
4. **Risiko pada Reputasi Perusahaan**  
   Jika masalah attrition terus berlanjut, reputasi perusahaan sebagai tempat kerja yang nyaman dan stabil dapat terancam. Hal ini berisiko mengurangi daya tarik perusahaan di mata calon karyawan potensial, serta menyulitkan perusahaan dalam menarik dan mempertahankan talenta terbaik di masa mendatang.

### Cakupan Proyek
1. Mengumpulkan dan mengelola informasi terkait dengan profil serta aktivitas karyawan.  
2. Menganalisis data tersebut untuk menemukan pola dan faktor-faktor yang memengaruhi tingkat perputaran karyawan.  
3. Membangun model prediksi dengan menggunakan metode algoritma Logistic Regression untuk memperkirakan kemungkinan perputaran.  
4. Mendesain dasbor interaktif yang menyajikan hasil analisis dan proyeksi secara visual untuk mempermudah pengambilan keputusan.  
5. Menyusun rekomendasi tindakan lanjutan yang berdasarkan pada hasil temuan dari analisis yang telah dilakukan.  

### Persiapan
Berikut adalah langkah-langkah untuk mempersiapkannya:

Sumber data: [Link GitHub](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

**Menyiapkan lingkungan:**
Jika Anda menginstal Python melalui Anaconda atau Miniconda, Anda bisa memanfaatkan conda sebagai alat untuk mengelola paket dan lingkungan virtual. Berikut ini adalah langkah-langkah yang perlu diikuti untuk membuat lingkungan virtual menggunakan conda dalam rangka melakukan prediksi:
1. Buka terminal atau PowerShell pada sistem Anda.
2. Gunakan perintah berikut untuk membuat lingkungan virtual baru:
    ```
    conda create --name prediksi_attrition python=3.9
    ```
3. Aktifkan lingkungan yang baru dibuat dengan perintah ini:
    ```
    conda activate prediksi_attrition
    ```
4. Instal pustaka yang diperlukan dengan menjalankan perintah berikut:
    ```
    pip install numpy==1.24.4 pandas==2.1.4 matplotlib==3.7.5 seaborn==0.13.2 scikit-learn==1.4.0 SQLAlchemy==2.0.30
    ```
5. Untuk menjalankan Jupyter Notebook, ketik perintah berikut:
    ```
    jupyter-notebook
    ```
6. Buka file `prediction.py` di Jupyter Notebook.
7. Masukkan data yang ingin diprediksi ke dalam variabel `X_new`.
8. Klik tombol "run code" untuk menjalankan prediksi.
9. Hasil prediksi akan ditampilkan setelah proses selesai.

## Business Dashboard
Dasbor bisnis ini dirancang untuk memberikan gambaran menyeluruh tentang data karyawan, tingkat perputaran, dan faktor-faktor yang mempengaruhi tingginya angka attrition. Dalam dasbor ini, akan ditampilkan berbagai variabel penting, termasuk informasi demografis, tingkat penghasilan, kondisi pekerjaan, kepuasan karyawan, keseimbangan antara pekerjaan dan kehidupan, serta faktor-faktor lain yang berperan dalam peningkatan angka perputaran karyawan.

## Conclusion
Karyawan yang lebih cenderung untuk meninggalkan perusahaan biasanya memiliki usia yang relatif muda dan belum menikah, dengan gaji yang lebih rendah, meskipun mereka sering memiliki sumber pendapatan tambahan yang lebih besar. Mereka juga menghadapi kesulitan dalam menjaga keseimbangan antara pekerjaan dan kehidupan pribadi. Selain itu, banyak dari mereka merasa tidak puas dengan lingkungan kerja, khususnya dalam hal hubungan dengan atasan. Karyawan yang jarang mendapatkan kesempatan untuk naik jabatan juga lebih sering memutuskan untuk keluar. Sebagian besar dari mereka berasal dari bidang teknisi laboratorium, sumber daya manusia, dan ilmuwan riset. Namun, tidak sedikit juga yang meninggalkan perusahaan dengan latar belakang pendidikan di bidang teknik dan pemasaran.

### Rekomendasi Action Items
Berikut ini adalah beberapa rekomendasi yang dapat diterapkan oleh perusahaan Jaya Jaya Maju untuk mengurangi tingkat perputaran karyawan:
1. **Perjalanan Dinas (Business Travel):**  
   Lakukan evaluasi rutin mengenai kebutuhan perjalanan dinas dan pertimbangkan opsi alternatif seperti pekerjaan jarak jauh (remote work) untuk mengurangi tekanan yang dapat memengaruhi kesejahteraan dan kepuasan karyawan.
2. **Departemen:**  
   Lakukan kajian lebih mendalam terhadap faktor-faktor yang menyebabkan tingginya attrition di departemen R&D dan Sales. Perusahaan mungkin perlu meninjau kembali budaya kerja atau mengembangkan program peningkatan karir di kedua departemen tersebut.
3. **Tingkat Pendidikan dan Bidang:**  
   Evaluasi kembali program pelatihan dan kesempatan pengembangan karir untuk karyawan, terutama di bidang seperti Life Sciences dan Medical. Fokuskan perhatian pada area ini untuk memperbaiki tingkat retensi karyawan yang memiliki latar belakang pendidikan tersebut.
4. **Kepuasan Lingkungan Kerja:**  
   Perhatikan karyawan yang menunjukkan tingkat kepuasan rendah terhadap lingkungan kerja mereka. Identifikasi faktor-faktor penyebab ketidakpuasan dan tawarkan solusi yang dapat mencakup program kesejahteraan, peningkatan komunikasi, atau perbaikan fasilitas kerja.
5. **Jenis Kelamin:**  
   Tinjau kembali tantangan atau isu-isu yang dihadapi oleh karyawan pria. Pastikan bahwa kebijakan serta program yang ada mendukung kebutuhan dan harapan semua karyawan, tanpa memandang jenis kelamin.
6. **Peran dan Tingkatan Pekerjaan:**  
   Lakukan analisis mendalam terhadap peran-peran seperti Teknisi Laboratorium, Eksekutif Penjualan, dan Ilmuwan Riset. Tinjau beban kerja, peluang pengembangan profesional, serta kesejahteraan yang diberikan kepada mereka.
7. **Keseimbangan Kerja dan Kehidupan serta Lembur:**  
   Evaluasi dampak jam kerja tambahan (lembur) terhadap tingkat perputaran karyawan. Pertimbangkan untuk memperkenalkan kebijakan yang lebih baik dalam mengelola jam kerja dan mendorong keseimbangan antara pekerjaan dan kehidupan pribadi.
8. **Penilaian Kinerja dan Kepuasan Kerja:**  
   Berikan umpan balik yang jelas serta kesempatan pengembangan kepada karyawan yang merasa tidak puas atau kurang dihargai dalam pekerjaan mereka.
9. **Status Pernikahan:**  
   Perhatikan tingkat perputaran yang tinggi di kalangan karyawan yang masih lajang. Evaluasi apakah ada program dukungan sosial atau kesejahteraan yang dapat disesuaikan untuk memenuhi kebutuhan karyawan dengan status pernikahan tersebut.
10. **Stabilitas Peran dan Hubungan dengan Manajer:**  
   Tinjau pengalaman karyawan dalam menjalankan peran mereka serta hubungan yang mereka miliki dengan manajer. Berikan pelatihan kepemimpinan yang relevan untuk memperbaiki kualitas hubungan tersebut dan meningkatkan stabilitas dalam pekerjaan.
11. **Kompensasi dan Tunjangan:**  
   Pastikan kompensasi dan tunjangan yang diberikan perusahaan cukup untuk menjaga kepuasan dan loyalitas karyawan. Evaluasi struktur kompensasi agar lebih adil dan kompetitif dengan standar industri.
12. **Pelatihan dan Pengembangan Karir:**  
   Tingkatkan investasi dalam program pelatihan serta pengembangan karir karyawan. Pastikan semua karyawan memiliki kesempatan yang setara untuk berkembang dalam karir mereka, yang akan meningkatkan keterikatan dan memperkuat upaya retensi.

## Email dan password Metabase
Email: root@mail.com
Password: root123
