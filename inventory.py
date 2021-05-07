file=open("db-inventory.txt","a")
while True :
    Answer = input ('Input data inventory baru ? [y/n] : ')
    print('='*35)
    if Answer == 'y' :
        NamaPerangkat = input ('Nama Perangkat : ')
        Lokasi = input ('Lokasi : ')
        print('-'*35)
        file.write('Nama Perangkat : '+NamaPerangkat+', '
        'Lokasi : '+Lokasi+'\n')
    else :
        file = open ('db-inventory.txt','r')
        for item in file :
            item=item.strip()
            print (item)
        file.close()
        break
file.close()