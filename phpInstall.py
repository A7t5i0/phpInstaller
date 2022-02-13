import os
commands = ["sudo apt update", "sudo apt install php php-cli php-fpm php-json php-common php-mysql php-zip php-gd php-mbstring php-curl php-xml php-pear php-bcmath"]
for command in commands:
    os.system(command)
loop=True
while loop==True:
    x=input("Do you want to see php version or modules? Type c to clear the terminal, v for version, m for modules and q to quit finnishing the installation...")
    if x=="c":
        os.system("clear")
    elif x=="v":
        os.system("php -v")
    elif x=="m":
        os.system("php -m")
    elif x=="q":
        loop=False
    else:
        print("Invalid option!")
print("PHP installation complete!")
