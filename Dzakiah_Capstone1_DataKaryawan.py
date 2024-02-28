from tabulate import tabulate
import time

A=9500
B=7000
C=3000


head = ['ID Karyawan', 'Nama', 'NIK', 'Usia', 'Jenis Kelamin', 'Jabatan', 'Divisi', 'Gaji']
isiData = [
    ['1', 'Dzakiah Putri Farikha', '6789101512010002', '30', 'Perempuan', 'Chief Executive Officer', 'CEO', A],
    ['2', 'Arsyil Malik', '3279101512014567', '37', 'Laki-Laki', 'Marketing Manager', 'Marketing', B],
    ['3', 'Usamah Ibadurrahman', '8567101512010333', '35', 'Laki-Laki', 'Human Resource Development', 'Officer', B],
    ['4', 'Subhan Azhar', '8795101512010202', '28', 'Laki-Laki', 'Chief Operation Officer', 'Operation', B],
    ['5', 'Azzarya Chrisayudha', '3459101512010002', '29', 'Laki-Laki', 'Staff', 'Operation', C],
    ['6', 'Imam Hidayat', '3909101566677702', '32', 'Laki-Laki', 'Staff', 'Marketing', C]
]

while True: 
     menuAdminOrKaryawan=('''
          ==========================================================
                              Menu PT. IKA
          ==========================================================
                    1. Menu Admin
                    2. Menu Karyawan
                    3. Exit
          ''')
     print(menuAdminOrKaryawan)
     pilihMenu=input('Silahkan masukkan nomor menu [1-3]: ')
     if pilihMenu == '1': # Menu admin
        menuAdminAwal=('''
          ==========================================================
                         Menu Admin PT. IKA
          ==========================================================
                    !!! Silahkan Masukkan Password !!!
        ''')
        passAdmin = input('Masukkan Password Admin: ')
        while True:
          if passAdmin == 'ikaika':
               menu=('''
          ==========================================================
                         Menu Admin PT. IKA
          ==========================================================
          1. Report Data Karyawan
          2. Menambahkan Data Karyawan
          3. Mengubah Data Karyawan
          4. Menghapus Data Karyawan
          5. Hitung Gaji Karyawan Untuk Akhir Bulan
          6. Exit
          ==========================================================
                    ''')
               print(menu)
               pilihan=input('Masukkan pilihan [1-6]: ')
               if pilihan =='1': # MENU READ DATA
                    while True: 
                         print('''
          ==========================================================
                    Report Data Karyawan PT. IKA
          ==========================================================
               1. Report Seluruh Data
               2. Report Data Tertentu
               3. Kembali ke Menu Utama
          ==========================================================
                              ''')
                         pilihanRead=input('Silahkan Pilih Sub Menu Read Data [1-3]: ')
                         if pilihanRead == '1': #tampilan seluruh data
                              print('\n \t \t ---- Seluruh Data Karyawan PT. IKA ----')
                              print(tabulate(isiData, headers=head, tablefmt='fancy_grid')) # back ke sub menu
                         elif pilihanRead == '2': # untuk cari salah satu ID Karyawan
                              id_panggil = input('Silahkan masukkan ID Karyawan yang ingin ditampilkan: ')
                              filtered_data = []
                              for i in isiData:
                                   if id_panggil == i[0]:
                                        filtered_data.append(i)
                                        if filtered_data:
                                             print(tabulate(filtered_data, headers=head, tablefmt='fancy_grid'))
                                             break
                              else:
                                   print('\n \t\t *************** Data tidak ditemukan ***************')
                         elif pilihanRead == '3': #kembali ke menu utama
                              break
                         else:
                              print('\n \t****** Inputan yang anda masukkan salah, silahkan input yang benar ******')
               elif pilihan =='2': # MENU CREATE DATA
                    while True: 
                         print(''' 
          ==========================================================
                    Menambahkan Data Karyawan PT. IKA
          ==========================================================
                    1. Tambah Data Karyawan Baru
                    2. Kembali ke Menu Utama
          ==========================================================
                         ''')
                         pilihanCreate=input('Silahkan Pilih Sub Menu Create Data [1-2]: ')
                         if pilihanCreate =='1': #tambah data karyawan
                              tambahNama=input('Masukkan Nama:')
                              tambahNik=input('Masukkan NIK:')
                              if not tambahNik.isdigit():
                                   print('NIK harus berupa Angka')
                                   continue
                              tambahUsia=input('Masukkan Usia:')
                              if not tambahUsia.isdigit():
                                   print('Usia harus berupa Angka')
                                   continue
                              tambahJenisKelamin=input('Masukkan Jenis Kelamin:')
                              tambahJabatan=input('Masukkan Jabatan:')
                              tambahDivisi=input('Masukkan Divisi: ') 
                              tambahGaji=input('Masukkan Golongan Gaji [A/B/C]: ')
                              if tambahGaji.upper() == 'A':
                                   tambahGaji = A
                              elif tambahGaji.upper() == 'B':
                                   tambahGaji = B
                              elif  tambahGaji.upper() == 'C':
                                   tambahGaji = C
                              else:
                                   print('\n \t***** Golongan Gaji Tidak Valid *****')
                                   True
                              konfirmasi = input('Apakah anda yakin untuk menambahkan data? [y/n]:')
                              if konfirmasi.lower() == 'y':
                                   new_data = [str(len(isiData) + 1), tambahNama, tambahNik, tambahUsia, tambahJenisKelamin,tambahJabatan, tambahDivisi, tambahGaji]
                                   isiData.append(new_data)
                                   print('Data berhasil ditambahkan')
                                   print(tabulate(isiData, headers=head, tablefmt='fancy_grid'))
                              else:
                                   print('\n Data tidak berhasil ditambahkan')
                                   True
                         elif pilihanCreate=='2':
                              break
                         else: 
                              print('\n \t****** Inputan yang anda masukkan salah, silahkan input yang benar ******')
                              True 
               elif pilihan =='3': # MENU UPDATE DATA
                    while True:
                         print('''
          ==========================================================
                    Mengubah Data Karyawan PT. IKA
          ==========================================================
               1. Ubah Seluruh Data Karyawan
               2. Ubah Salah Satu
               3. Kembali ke Menu Utama
          ==========================================================
                              ''')
                         pilihanUpdate = input('Pilih Submenu Update [1-3]: ')
                         if pilihanUpdate == '1': #Ubah seluruh data karyawan
                              print(tabulate(isiData, headers=head, tablefmt='fancy_grid'))
                              index_to_update = (input('Masukkan ID Karyawan yang akan diupdate: '))
                              if not index_to_update.isdigit():
                                   print('Anda hanya bisa memasukan angka bulat')
                                   continue
                              index_to_update=int(index_to_update)
                              if 1 <= index_to_update <= len(isiData):
                                   updatedNama = input('Masukkan Nama Baru:')
                                   updatedNik = input('Masukkan NIK Baru:')
                                   if not updatedNik.isdigit():
                                        print('NIK harus berupa Angka')
                                        continue
                                   updatedUsia = input('Masukkan Usia Baru:')
                                   if not updatedUsia.isdigit():
                                        print('Usia harus berupa Angka')
                                        continue
                                   updatedJenisKelamin = input('Masukkan Jenis Kelamin Baru:')
                                   updatedJabatan = input('Masukkan Jabatan Baru:')
                                   updatedDivisi = input('Masukkan Divisi Baru: ')
                                   updatedGaji = input('Masukkan Golongan Gaji Baru [A/B/C]: ')
                                   while True: 
                                        if updatedGaji == 'A':
                                             updatedGaji = A
                                             break
                                        elif updatedGaji == 'B':
                                             updatedGaji = B
                                             break
                                        elif  updatedGaji == 'C':
                                             updatedGaji = C
                                             break
                                        else:
                                             print('\n \t***** Golongan Gaji Tidak Valid *****')
                                             continue
                                   konfirmasiUpdate = input('Apakah anda yakin untuk mengupdate data? [y/n]: ')
                                   if konfirmasiUpdate.lower() == 'y':
                                        isiData[index_to_update - 1] = [str(index_to_update), updatedNama, updatedNik, updatedUsia, updatedJenisKelamin, updatedJabatan, updatedDivisi, updatedGaji]
                                        print('\n**** Data berhasil diupdate ****')
                                        print(tabulate(isiData, headers=head, tablefmt='fancy_grid'))
                                   else:
                                        True
                              else:
                                   print('\n \t****** Inputan yang anda masukkan salah, silahkan input yang benar ******')
                              True
                                 
                         elif pilihanUpdate == '2': # Update Salah Satu data karyawan
                              print(tabulate(isiData, headers=head, tablefmt='fancy_grid'))
                              index_to_update = input('Masukkan ID Karyawan yang akan diupdate: ')
                              if not index_to_update.isdigit():
                                   print('Anda hanya bisa memasukkan angka bulat')
                              elif  int(index_to_update) <  1 or int(index_to_update) > len(isiData):
                                   print('ID Karyawan tidak valid')
                              else:
                                   index_to_update = int(index_to_update)
                              
                                   if 1 <= index_to_update <= len(isiData):
                                        print('''
                                        Ketik salah satu pilihan yang ingin diganti 
                                        [1] Nama
                                        [2] NIK
                                        [3] Usia
                                        [4] Jenis Kelamin
                                        [5] Jabatan
                                        [6] Divisi
                                        [7] Golongan Gaji [A/B/C]                 
                                        ''')
                                        pilihanUpdateRinci = input('Masukkan angka: ')
                                   
                                   while True:
                                        if '1' <= pilihanUpdateRinci <= '6':
                                             updatedValue = input(f'Masukkan {head[int(pilihanUpdateRinci)]} Baru: ')
                                             konfirmasiSatu = input('Apakah anda yakin untuk mengubah data? [y/n]: ')
                                             
                                             if konfirmasiSatu.lower() == 'y':
                                                  isiData[index_to_update - 1][int(pilihanUpdateRinci)] = updatedValue
                                                  print("\nData berhasil diupdate.")
                                                  print(tabulate(isiData, headers=head, tablefmt='fancy_grid'))
                                                  break
                                             else:
                                                  break
                                        elif pilihanUpdateRinci == '7':
                                             updatedValue = input('Masukkan Gaji Baru [A/B/C]: ')
                                             
                                             if updatedValue in ['A', 'B', 'C']:
                                                  konfirmasiSatu = input(f'Apakah anda yakin untuk mengubah gaji menjadi {updatedValue}? [y/n]: ')
                                                  if konfirmasiSatu.lower() == 'y':
                                                       if updatedValue == 'A':
                                                            updatedValue = A
                                                       elif updatedValue == 'B':
                                                            updatedValue = B
                                                       elif updatedValue == 'C':
                                                            updatedValue = C
                                                  
                                                       isiData[index_to_update - 1][int(pilihanUpdateRinci)] = updatedValue
                                                       print("\nData berhasil diupdate.")
                                                       print(tabulate(isiData, headers=head, tablefmt='fancy_grid'))
                                                       break
                                                  else:
                                                       break
                                             else:
                                                  print('\n \t***** Golongan Gaji Tidak Valid *****')
                                                  continue
                                        else:
                                             print('\n \t****** Inputan yang anda masukkan salah, silahkan input yang benar. Silakan pilih angka 1-7.')
                                             continue
                              # else:
                              #      print('\n \t**** Masukkan data yang benar!!! ****')
                         elif pilihanUpdate == '3':
                              break
                         else:
                              print('\n \t****** Inputan yang anda masukkan salah, silahkan input yang benar ******')
               elif pilihan =='4': # MENU DELETE DATA
                    while True:
                         print('''
          ==========================================================
                    Menghapus Data Karyawan PT. IKA
          ==========================================================
               1. Hapus Data Karyawan
               2. Kembali ke Menu Utama
          ==========================================================
                              ''')
                         pilihanDelete = input('Pilihan Submenu Delete: ') 
                         if pilihanDelete== '1':
                              print(tabulate(isiData, headers=head, tablefmt='fancy_grid'))
                              index_to_delete = input('Masukkan ID Karyawan yang akan dihapus: ')
                              if not index_to_delete.isdigit():
                                        print('Anda hanya bisa memasukan angka bulat')
                                        continue
                              index_to_delete=int(index_to_delete)
                              
                              if 1 <= index_to_delete <= len(isiData):
                                   konfirmasiDelete = input('Apakah Anda yakin untuk menghapus data? [y/n]: ')
                                   if konfirmasiDelete.lower() == 'y':
                                        deleted_data = isiData.pop(index_to_delete - 1)
                                        print(f"\nData karyawan dengan ID {index_to_delete} ({deleted_data[1]}) berhasil dihapus.")
                                        print("\n\tData setelah penghapusan:")
                                        print(tabulate(isiData, headers=head, tablefmt='fancy_grid'))
                                   else:
                                        print('\nData Tidak Berhasil Diubah')
                                        True
                              else:
                                   print('\nID Karyawan tidak ditemukan')
                                   True
                         elif pilihanDelete == '2':
                              break
                         else:
                              print('\n \t****** Inputan yang anda masukkan salah, silahkan input yang benar ******')           
               elif pilihan =='5': # MENU UPDATE GAJI KARYAWAN UNTUK AKHIR BULAN
                    while True: 
                         print('''
                              ==========================================================
                                        Menu Gaji Karyawan PT. IKA
                              ==========================================================
                                   1. Update Gaji Karyawan
                                   2. Kembali ke Menu Utama
                              ==========================================================   
                         ''')
                         pilihanGaji = input('Masukkan menu: ')
                         if pilihanGaji == '1':
                                   print(tabulate(isiData, headers=head, tablefmt='fancy_grid'))
                                   index_to_update_gaji = input('Masukkan ID Karyawan yang akan diupdate: ')
                                   if not index_to_update_gaji.isdigit():
                                        print('Anda hanya bisa memasukan angka bulat')
                                        continue
                                   index_to_update_gaji=int(index_to_update_gaji)
                                   if 1 <= index_to_update_gaji <= len(isiData):
                                        jumlah_hari_kerja = 22
                                        absensi_bulanan = input('Masukkan jumlah hari kerja karyawan dalam sebulan: ')
                                        if not absensi_bulanan.isdigit():
                                             print('Anda hanya bisa memasukan angka bulat')
                                             continue
                                        absensi_bulanan=int(absensi_bulanan)
                                        golGaji = input('''
                                        Daftar Golongan Gaji: 
                                        [A] 9500
                                        [B] 7000
                                        [C] 3000
                                        Masukkan golongan gaji karyawan: 
                                        ''')
                                        if absensi_bulanan <= jumlah_hari_kerja:
                                             if golGaji == 'A':
                                                  tarif_per_hari= A / 22
                                             elif golGaji == 'B':
                                                  tarif_per_hari= B / 22
                                             elif golGaji == 'C':
                                                  tarif_per_hari= C / 22
                                             else:
                                                  print('Data Tidak Valid')
                                                  True
                                             updatedGaji = tarif_per_hari * absensi_bulanan
                                             isiData[index_to_update_gaji - 1][-1] = updatedGaji 
                                             print("\nData berhasil diupdate.")
                                             print(tabulate(isiData, headers=head, tablefmt='fancy_grid'))
                                        else:
                                             print('\n \t**** Jumlah Hari Kerja atau Golongan Gaji Tidak Valid ***')
                                             True
                                   else: 
                                        print('\n \t**** Masukkan data yang benar!!! ****')
                                        continue
                         elif pilihanGaji == '2':
                              break
                         else:
                              print('\n \t****** Inputan yang anda masukkan salah, silahkan input yang benar ******') 
               elif pilihan =='6':
                    break
               else:
                    print('\n\t ******** Program yang anda masukkan salah ********')
                    True
          else:
               print('Masukkan Password yang benar!!!')
               time.sleep (1)
               break 
     elif pilihMenu == '2': # MENU KARYAWAN
          print('''
          ==========================================================
                         Menu Karyawan PT. IKA
          ==========================================================
               !!! Silahkan Masukkan Password!!!
               ''')
          passKaryawan = input('Masukkan Password Karyawan: ')
          while True:
               if passKaryawan == 'ika':
                    print('''
          ==========================================================
                         Menu Karyawan PT. IKA
          ==========================================================
                    1. Report Data Karyawan
                    2. Check Gaji 
                    3. Exit
                    ''')
                    menuKaryawan = input('Masukkan menu pilihan sub menu: ')
                    if menuKaryawan == '1': # Report Data Karyawan
                         selected_columns = [0, 1, 4, 5, 6]
                         selected_data = [[row[i] for i in selected_columns] for row in isiData]
                         print(tabulate(selected_data, headers=['ID Karyawan', 'Nama', 'Jenis Kelamin', 'Jabatan', 'Divisi'], tablefmt='fancy_grid'))
                         True
                    elif menuKaryawan== '2': # Check gaji hanya satu karyawan
                         gajiID = input('Masukkan ID Karyawan: ')
                         found = False
                         for row in isiData:
                              if row[0] == gajiID:
                                   gaji_data = [row]
                                   print(tabulate(gaji_data, headers=head, tablefmt='fancy_grid'))
                                   found = True
                                   True
                         if not found:
                              print(f'Tidak ada Karyawan dengan ID {gajiID}')
                    elif menuKaryawan == '3':
                         break
               else:
                    print('Masukkan Password yang benar!!!')
                    break
     elif pilihMenu =='3':
          print('Thank you and Goodbye!')
          exit()   
     else:
          print('Masukkan Inputan yang benar!!!')
          True       