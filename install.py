#=====Import Module=====#
import os, time, datetime
#=====Color=====#
red = '\033[1;91m'
green = '\033[1;92m'
yellow = '\033[1;93m'
blue = '\033[1;94m'
purple = '\033[1;95m'
cyan = '\033[1;96m'
white = '\033[1;97m'
#=====Date Time=====#
date_time = datetime.datetime.now()
day_now = date_time.strftime("%d/%m/%Y")
time_now = date_time.strftime("%H:%M:%S")
k = f"""{white}┌─[{yellow}{day_now}{white}]──[{yellow}{time_now}{white}]\n├─[{red}root{green}@{blue}VaNaKa{white}]\n└─>{cyan}"""
banner = """
\033[1;97m===============================================================================
\033[1;96m  _   _       _   _       _   __      _   _  __  
\033[1;97m | | | |     | \ | |     | | / /     | | | |/  |   \033[1;92mAuthor:\033[1;97m @VuNhatAnh
\033[1;96m | | | | __ _|  \| | __ _| |/ /  __ _| | | |`| |   \033[1;92mGithub:\033[1;97m https://www.facebook.com/VuNhatAnh.X.ThaoHienXinhGai
\033[1;97m | | | |/ _` | . ` |/ _` |    \ / _` | | | | | |   \033[1;97mCopyright (c) 2022 Vu Nhat Anh
\033[1;96m \ \_/ / (_| | |\  | (_| | |\  \ (_| \ \_/ /_| |_  
\033[1;97m  \___/ \__,_\_| \_/\__,_\_| \_/\__,_|\___/ \___/
\033[1;97m===============================================================================
\033[1;92m                                INSTALL VaNaKa
\033[1;97m===============================================================================
"""
#=====Banner=====#
print(banner)
#=====Install=====#
print('[01] Install pip & run VaNaKa-V1 by python') 
print('[02] Install pip3 & run VaNaKa-V1 by python3')
print('[03] Exit')

option = input(k)
if option == "1" or option == "01":
    os.system("pip install cloudscraper")
    os.system("pip install socks")
    os.system("pip install pysocks")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install undetected_chromedriver")
    os.system("pip install httpx")
    print("[OK] Done !")
    time.sleep(1)
    print("[*] Preparing...")
    time.sleep(2)
    os.system('python VaNaKa-V1.py')

elif option == "2" or option == "02":
    os.system("pip3 install cloudscraper")
    os.system("pip3 install socks")
    os.system("pip3 install pysocks")
    os.system("pip3 install requests")
    os.system("pip3 install colorama")
    os.system("pip3 install undetected_chromedriver")
    os.system("pip3 install httpx")
    print("[OK] Done !")
    time.sleep(1)
    print("[*] Preparing...")
    time.sleep(2)
    os.system('python3 VaNaKa-V1.py')
elif option == "3" or option == "03":
    os.sys.exit()
if os.name == "nt":
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")
    print("[OK] Done !")
    time.sleep(1)
    print("[*] Preparing...")
    time.sleep(2)
    os.system('python VaNaKa-V1.py')
else:
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")
    print("[OK] Done !")
    time.sleep(1)
    print("[*] Preparing...")
    time.sleep(2)
    os.system('python VaNaKa-V1.py')



