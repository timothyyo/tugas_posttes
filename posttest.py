#joshuatimothy
#2309116070

user ={'nama_mahasiswa' : 'joshua timothy',
         'nim_mahasiswa' : '2309116070'}
def login() :
    while True:
        nama_mahasiswa = input("masukkan nama_mahasiswa :")
        nim_mahasiswa = input("masukkan nim_mahasiswa:")
        if  nama_mahasiswa == user["nama_mahasiswa"] and nim_mahasiswa == user["nim_mahasiswa"]:
            print("Login Berhasil") 
            break
        else:
            print("data yang anda masukkan salah")

print("Login")
login()
print("Urutan Konversi :")
print("1.lbs")
print("2.ons")
print("3.gram")
satuan_kg =int (input("hitung satuan_kg :"))
operator = float(input("masukan operator(1,2,3):"))
if operator == 1:
   hasil = satuan_kg * 2.20462
   print(f"{satuan_kg} kg sama dengan {hasil} lb")
elif operator == 2:
   hasil = satuan_kg * 35.274
   print (f"{satuan_kg} kg sama dengan {hasil} ons")
elif operator == 3:
   hasil = satuan_kg * 1000
   print(f"{satuan_kg} kg sama dengan {hasil} g")
else:
   print("data tidak valid")
