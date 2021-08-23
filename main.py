import os
import colorama
import pyfiglet
from colorama import Fore
from colorama import Style


print(pyfiglet.figlet_format('Menu Program'))

while True:
  print("\n\n")
  print(Fore.CYAN+ f'Press 1 To run a linux command{Style.RESET_ALL}')
  print(Fore.CYAN+ f'Press 2 To create Volume Group{Style.RESET_ALL}')
  print(Fore.CYAN+ f'Press 3 To create LVM{Style.RESET_ALL}')
  print(Fore.CYAN+ f'Press 4 To make your partition permanent{Style.RESET_ALL}')
  print(Fore.CYAN+ f'Press 5 To create a User{Style.RESET_ALL}')
  print(Fore.CYAN+ f'Press 6 To create a Crontab{Style.RESET_ALL}') 
  print(Fore.CYAN+ f'Press 7 To format a disk{Style.RESET_ALL}')
  print(Fore.CYAN+ f'Press 8 To configure the httpd server{Style.RESET_ALL}')
  print(Fore.CYAN+ f'Press 9 To configure Docker server{Style.RESET_ALL}')
  print(Fore.CYAN+ f'Press 10 To Exit the program{Style.RESET_ALL}')

  x= input("Enter your choice ")

  if x== '1':
      command= str(input('Enter your command: '))
      os.system(f'{command}')

  elif x== '2':
      os.system('fdisk -l')
      vgname= str(input("Enter the vg name: "))
      disk1= str(input("Disk1(without /dev/): "))
      disk2= str(input("Disk2(without /dev/): "))
      os.system(f'vgcreate {vgname} /dev/{disk1} /dev/{disk2}')
      os.system(f'vgdisplay {vgname}')

  elif x=='3':
      lvname= str(input('Enter the lv name '))
      vgname= str(input('Enter the vg name '))
      lvsize= str(input('Enter the lv size '))
      os.system(f'lvcreate --size {lvsize} --name {lvname} {vgname}')
      os.system(f'lvdisplay /dev/{vgname}/{lvname}')

  elif x=='4':
      devicename= input('Enter the disk name: ')
      mountpoint= input('Enter the mount point: ')
      os.system(f"echo '{devicename} {mountpoint} ext4 defaults 0 0' >> /root/rhcsa-py/fstab")

  elif x=='5':
      user= str(input("Enter the user name: "))
      os.system(f'useradd -G testgroup {user}')

  elif x=='6':
      delay= str(input("Enter the time in the actual format: "))
      cmd= str(input("Enter the command: "))
      os.system(f'echo "{delay} {cmd}" >> /var/spool/cron/root')
      print(os.system('crontab -l'))

  elif x=='7':
      os.system('fdisk -l')
      disk= str(input("Enter the disk name: "))
      os.system(f'mkfs.ext4 {disk}')

  elif x=='8':
      os.system('yum install httpd -y')
      os.system('systemctl start httpd')
    
  elif x=='9':
      os.system('yum install docker-ce -y')
      os.system('systemctl start docker')

  elif x=='10':
      break

  else:
      print("Enter correct option")

