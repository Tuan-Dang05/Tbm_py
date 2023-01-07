from time import sleep
from colorama import Fore, Back, Style
import sys
def monhoc():
    print(Fore.GREEN,Style.BRIGHT + "Chọn môn học ".upper().center(50))
    print(Fore.YELLOW,Style.BRIGHT+'0.'+Fore.CYAN,Style.BRIGHT+'Xem điểm tb tất cả các môn')
    sleep(0)
    print(Fore.YELLOW,Style.BRIGHT+'1.'+Fore.CYAN,Style.BRIGHT+'Toán'.center(5))
    sleep(0.1)
    print(Fore.YELLOW,Style.BRIGHT+'2.'+Fore.CYAN,Style.BRIGHT+'Văn'.center(5))
    sleep(0.2)
    print(Fore.YELLOW,Style.BRIGHT+'3.'+Fore.CYAN,Style.BRIGHT+'Anh'.center(5))
    sleep(0.3)
    chon = int(input(Fore.WHITE+'📱 --> '))
    print()
    if chon == 0:
        print("dang trong qua trinh nang cap")
    elif chon == 1:
        sleep(0.4)
        # open("TOAN.txt",'w')
        def toan():
            press = True
            toan = open("TOAN.txt",'r+')
            print(Fore.CYAN,Style.BRIGHT+'1.XEM ĐIỂM'.center(50))
            sleep(0)
            print(Fore.CYAN,Style.BRIGHT+'2.NHẬP ĐIỂM'.center(50))
            sleep(0.1)
            print(Fore.CYAN,Style.BRIGHT+'3.ĐIỂM TB MÔN TOÁN'.center(50))
            sleep(0.2)
            print(Fore.CYAN,Style.BRIGHT+'4.quay lại'.center(50))
            sleep(0.3)
            mode_1 = int(input(Fore.WHITE+'📱 --> '))
            # toan2 = open("TOAN.txt",'w+')
            if mode_1 == 1:
                he_so_1 = toan.readline()
                he_so_2 = toan.readline()
                he_so_3 = toan.readline()
                print(Fore.WHITE+"Điểm hệ số 1: " + Fore.MAGENTA,Style.BRIGHT ,he_so_1)
                sleep(0.1)
                print(Fore.WHITE+"Điểm hệ số 2: "+ Fore.CYAN,Style.BRIGHT,he_so_2)
                sleep(0.2)
                print(Fore.WHITE+"Điểm hệ số 3: "+ Fore.RED,Style.BRIGHT ,he_so_3)
                sleep(0.4)
                while press == True: 
                    press_toan = int(input(Fore.WHITE+"Press 1 to back menu: "))
                    print()
                    if press_toan == 1:
                        monhoc()
                        sleep(1)
                    else:
                        print(Fore.RED+"errol")
                        continue
            elif mode_1 == 2:
            
                    print("Nhập hệ số 1: ")
                    hs1 = input('-> ').split()
                    print("Nhập hệ số 2: ")
                    hs2 = input('-> ')
                    print("Nhập hệ số 3: ")
                    hs3 = input('-> ')
                    sleep(0.2)
                    for i_toan in hs1:
                        toan.write(str(i_toan+' '))
                    toan.write('\n')
                    toan.write(str(hs2))
                    toan.write('\n')
                    toan.write(str(hs3))
                
            elif mode_1 == 3:
                tb_toan_hs1 = toan.readline().split()
                tb_toan_hs2 = toan.readline().split()
                tb_toan_hs3 = toan.readline().split()
                tong_hs1 = list(map(float,tb_toan_hs1))
                tong_hs2 = list(map(float,tb_toan_hs2))
                tong_hs3 = list(map(float,tb_toan_hs3))
                if tb_toan_hs1 == tb_toan_hs2:
                    print(Fore.RED + "Điểm còn chưa nhập tính cc j?")
                    sleep(1)
                    print()
                    monhoc()
                else:
                    print(Fore.RED+"TRUNG BÌNH MÔN:"+Back.MAGENTA,Fore.WHITE,round(sum(tong_hs1+(tong_hs2*2) +(tong_hs3*3))/len(tb_toan_hs1+(tb_toan_hs2*2)+(tb_toan_hs3*3)),1),Style.RESET_ALL)
                    sleep(2)
                    monhoc()
                    
            elif mode_1 == 4:
                print()
                sleep(0.5)
                print()
                sleep(1)
                print()
                monhoc()
            
        toan()
    elif chon == 2:
        sleep(0.4)
        # open("TOAN.txt",'w')
        def van():
            press = True
            van = open("VAN.txt",'r+')
            print(Fore.CYAN,Style.BRIGHT+'1.XEM ĐIỂM'.center(50))
            sleep(0)
            print(Fore.CYAN,Style.BRIGHT+'2.NHẬP ĐIỂM'.center(50))
            sleep(0.1)
            print(Fore.CYAN,Style.BRIGHT+'3.ĐIỂM TB MÔN VĂN'.center(50))
            sleep(0.2)
            print(Fore.CYAN,Style.BRIGHT+'4.quay lại'.center(50))
            sleep(0.3)
            mode_1 = int(input(Fore.WHITE+'📱 --> '))

            if mode_1 == 1:
                he_so_1 = van.readline()
                he_so_2 = van.readline()
                he_so_3 = van.readline()
                print(Fore.WHITE+"Điểm hệ số 1: " + Fore.MAGENTA,Style.BRIGHT ,he_so_1)
                sleep(0.1)
                print(Fore.WHITE+"Điểm hệ số 2: "+ Fore.CYAN,Style.BRIGHT,he_so_2)
                sleep(0.2)
                print(Fore.WHITE+"Điểm hệ số 3: "+ Fore.RED,Style.BRIGHT ,he_so_3)
                sleep(0.4)
                while press == True: 
                    press_van = int(input(Fore.WHITE+"Press 1 to back menu: "))
                    if press_van == 1:
                        monhoc()
                        sleep(1)
                    else:
                        print(Fore.RED+"errol")
                        continue
            elif mode_1 == 2:
                print("Nhập hệ số 1: ")
                hs1 = input('-> ').split()
                print("Nhập hệ số 2: ")
                hs2 = input('-> ')
                print("Nhập hệ số 3: ")
                hs3 = input('-> ')
                sleep(0.2)
                for i_van in hs1:
                    van.write(str(i_van+' '))
                van.write('\n')
                van.write(str(hs2))
                van.write('\n')
                van.write(str(hs3))
            elif mode_1 == 3:
                tb_van_hs1 = van.readline().split()
                tb_van_hs2 = van.readline().split()
                tb_van_hs3 = van.readline().split()
                tong_hs1 = list(map(float,tb_van_hs1))
                tong_hs2 = list(map(float,tb_van_hs2*2))
                tong_hs3 = list(map(float,tb_van_hs3*3))
                if tb_van_hs1 == tb_van_hs2:
                    print(Fore.RED + "Điểm còn chưa nhập tính cc j?")
                    sleep(1)
                    print()
                    monhoc()
                else:
                    print(Fore.RED+"TRUNG BÌNH MÔN:"+Back.MAGENTA,Fore.WHITE,round(sum(tong_hs1+(tong_hs2*2) +(tong_hs3*3))/len(tb_van_hs1+(tb_van_hs2*2)+(tb_van_hs3*3)),1),Style.RESET_ALL)
                    sleep(2)
                    monhoc()


            elif mode_1 == 4:
                print()
                sleep(0.5)
                print()
                sleep(1)
                print()
                monhoc()
        van()
    elif chon == 3:
        sleep(0.4)
        # open("TOAN.txt",'w')
        def anh():
            press = True
            anh = open("ANH.txt",'r+')
            print(Fore.CYAN,Style.BRIGHT+'1.XEM ĐIỂM'.center(50))
            sleep(0)
            print(Fore.CYAN,Style.BRIGHT+'2.NHẬP ĐIỂM'.center(50))
            sleep(0.1)
            print(Fore.CYAN,Style.BRIGHT+'3.ĐIỂM TB MÔN ANH'.center(50))
            sleep(0.2)
            print(Fore.CYAN,Style.BRIGHT+'4.quay lại'.center(50))
            sleep(0.3)
            mode_1 = int(input(Fore.WHITE+'📱 --> '))
            # toan2 = open("TOAN.txt",'w+')
            if mode_1 == 1:
                he_so_1 = anh.readline()
                he_so_2 = anh.readline()
                he_so_3 = anh.readline()
                print(Fore.WHITE+"Điểm hệ số 1: " + Fore.MAGENTA,Style.BRIGHT ,he_so_1)
                sleep(0.1)
                print(Fore.WHITE+"Điểm hệ số 2: "+ Fore.CYAN,Style.BRIGHT,he_so_2)
                sleep(0.2)
                print(Fore.WHITE+"Điểm hệ số 3: "+ Fore.RED,Style.BRIGHT ,he_so_3)
                sleep(0.4)
                while press == True: 
                    press_anh = int(input(Fore.WHITE+"Press 1 to back menu: "))
                    if press_anh == 1:
                        monhoc()
                        sleep(1)
                    else:
                        print(Fore.RED+"errol")
                        continue
            elif mode_1 == 2:
                print("Nhập hệ số 1: ")
                hs1 = input('-> ').split()
                print("Nhập hệ số 2: ")
                hs2 = input('-> ')
                print("Nhập hệ số 3: ")
                hs3 = input('-> ')
                sleep(0.2)
                for i_anh in hs1:
                    anh.write(str(i_anh+' '))
                anh.write('\n')
                anh.write(str(hs2))
                anh.write('\n')
                anh.write(str(hs3))
            elif mode_1 == 3:
                tb_anh_hs1 = anh.readline().split()
                tb_anh_hs2 = anh.readline().split()
                tb_anh_hs3 = anh.readline().split()
                tong_hs1 = list(map(float,tb_anh_hs1))
                tong_hs2 = list(map(float,tb_anh_hs2*2))
                tong_hs3 = list(map(float,tb_anh_hs3*3))
                if tb_anh_hs1 == tb_anh_hs2:
                    print(Fore.RED + "Điểm còn chưa nhập tính cc j?")
                    sleep(1)
                    print()
                    monhoc()
                else:
                    print(Fore.RED+"TRUNG BÌNH MÔN:"+Back.MAGENTA,Fore.WHITE,round(sum(tong_hs1+(tong_hs2*2) +(tong_hs3*3))/len(tb_anh_hs1+(tb_anh_hs2*2)+(tb_anh_hs3*3)),1),Style.RESET_ALL)
                    sleep(2)
                    monhoc()

            elif mode_1 == 4:
                print()
                sleep(0.5)
                print()
                sleep(1)
                print()
                monhoc()
    else:
        print(Fore.RED+"ĐANG TRONG QUÁ TRÌNH UPDATE")
        anh()
monhoc()


