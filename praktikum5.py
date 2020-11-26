data={}
while true:
    print("")
    x=input("(L)ihat, (T)ambah, (U)bah, (H)apus,(C)ari,(K)eluar: ")
    #untuk keluar dari program
    if x.lower() == "K":
        print("keluar dari program")
        break
    #untuk melihat list
    elif x.lower()== "|":
        if data.items():
            print("======================== Daftar Nilai====================")
            print("=========================================================")
            print("| No  |  Nim   |  Nama | tugas | uts | uas | akhir |")
            print("====================================================")
            i=0
            for x in data.items():
                i+=1
                print("|{6:4}|{0:13s}|{1:3}|{2:8d}|{3:6d}|{4:7d}|{5:12.2f}|"\
                    .format(x[0] ,x[1][0] ,x[1][1] ,x[1][2] ,x[1][3] ,x[1][4] , i))  
                print("============================================================================================================================")
                else:
                    print("================================== Daftar Nilai ========================================================================")
                    print("========================================================================================================================")
                    print("| No | Nama | Nim | tugas | uts | uas | nilai akhir |")
                    print("=====================================================")
                    print("|                      TIDAK ADA DAFTAR NILAI               |")
                    print("=============================================================")
                    #untuk menambahkan data
                    elif x.lower()=="t":
                        print("Tambah Data")
                        nim = int(input("nim\t\t: "))
                        nama = input("nama\t\t: ")
                        tugas = int(input("nilai tugas\t: "))
                        uts = int(input("nilai uts\t: "))
                        nilai akhir = ((tugas)*30/100+(uts)*35/100+ (uas)*35/100)
                        data[nama]=nim,tugas,uts,uas,nilaiakhir
                        #untuk mengubah data 
                        elif x.lower()=="u":
                            print("edit data nilai mahasiswa")
                            nama = input("masukan nama\t\t:")
                            if nama in data.keys():
                                nim = input("nim\t\t\t:")
                                tugas = int(input("nilai tugas baru\t: "))
                                uts = int(input("nilai uts baru\t\t: "))
                                uas = int(input("nilai uas baru\t\t: "))
                                nilaiakhir = ((tugas)*30/100+(uts)*35/100+(uas)*35/100)
                                else :
                                    print("data nilai{0}")tidak ada".format(nama))
                                    #untuk menghapus data
                                    elif x.lower()=="h":
                                    print("hapus data nilai mahasiswa")
                                    nama = input("masuakan nama\t:")
                                    if nama in data.keys():
                                        del data[nama]
                                        else:
                                            print("data{0}tidak ada".format(nama))
                                    #untuk mencari data
                                    elif x.lower()== "c":
                                        print("cari data nilai mahasiswa")
                                        nama = input("masukan nama\t: ")
                                        if nama in data.keys():
                                    print("===================dafatar nilai====================")
                                    print("====================================================")
                                    print("| nama | nim | tugas | uts | uas |nilaiakhir |")
                                    print("==============================================")
                                    print("|                      tidak ada dafartar nilai                  |")
                                    print("==================================================================")

                                    else :
                                       print("pilih menu yang tersedia")
                                
                    
 