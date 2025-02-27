# Proyek Penerapan Data Science: 
# Menyelesaikan Permasalahan Human Resources - Perusahaan Jaya Jaya Maju
# Adilah Widiasti - olaladilah 

import pandas as pd
import pickle

# Memuat model yang telah dilatih dari file
with open('model_terlatih.pkl', 'rb') as file_model:  # Menggunakan nama file yang lebih deskriptif
    model = pickle.load(file_model)  # Memuat model ke dalam variabel

# Menyiapkan data baru yang akan diprediksi
data_baru = pd.DataFrame({
    'Usia': [35], 
    'PerjalananBisnis': ['Travel_Rarely'], 
    'TarifHarian': [1100], 
    'Departemen': ['Sales'], 
    'JarakDariRumah': [5], 
    'Pendidikan': [3], 
    'BidangPendidikan': ['Life Sciences'], 
    'KepuasanLingkungan': [3], 
    'JenisKelamin': ['Male'], 
    'TarifPerJam': [70], 
    'KeterlibatanPekerjaan': [3], 
    'TingkatJabatan': [2], 
    'PeranPekerjaan': ['Sales Executive'], 
    'KepuasanKerja': [4], 
    'StatusPerkawinan': ['Married'], 
    'PendapatanBulanan': [5000], 
    'TarifBulanan': [20000], 
    'JumlahPerusahaanDikerjakan': [1], 
    'Lembur': ['No'], 
    'PersentaseKenaikanGaji': [12], 
    'PenilaianKinerja': [3], 
    'KepuasanHubungan': [4], 
    'TingkatOpsiSaham': [1], 
    'TotalTahunBekerja': [10], 
    'WaktuPelatihanTahunLalu': [3], 
    'KeseimbanganKerjaHidup': [3], 
    'TahunDiPerusahaan': [5], 
    'TahunDiPeranSaatIni': [2], 
    'TahunSejakPromosiTerakhir': [1], 
    'TahunBersamaManajerSaatIni': [3], 
    'StabilitasDiPeran': [0.6], 
    'LoyalitasTerhadapManajer': [0.6], 
    'RataRataPelatihanPerTahun': [1.5], 
    'UsiaSaatMulai': [25], 
    'RataRataTahunPerPerusahaan': [10], 
    'PendapatanPerKm': [200], 
    'LoyalitasPerusahaan': [0.7], 
    'FrekuensiPromosi': [2], 
    'RataRataPendapatanBulananPerTahun': [2000]
})

# Melakukan prediksi menggunakan model yang telah dilatih
hasil_prediksi = model.predict(data_baru)  # Menggunakan data baru untuk prediksi

# Menampilkan hasil prediksi
print("Hasil Prediksi:", hasil_prediksi)  