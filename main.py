import socket as s
from colorama import Fore
import subprocess as sub

ll: list[str] = []
blue = Fore.BLUE

def writeToFile(Filename: str):
    try:

        with open(Filename, "w") as d:
            for s in ll:
                d.write(s)

    except FileExistsError as e:
        print(f"ERROR: {e}")

    except Exception as e:
        print(f"ERROR: {e}")

    return None

def nmap_scan(file: str):
    sub.run(f"nmap -iL {file}")

def Conc(file_name: str):
    with open(file_name, "r") as f:

        domains = f.readlines()
        for domain in domains:
            domain = domain.strip("\n")
            try:
               
               ip = s.gethostbyname(domain)
               print(Fore.GREEN + f"[*]DOMAIN: {domain}, IP: {ip}" + Fore.RESET)
               ll.append(f"{ip}\n")

            except s.gaierror as e:
                print(Fore.RED + f"[!]ERROR WHILE GETTING HOST NAME FROM DOMAIN: {domain}\nERROR TYPE: {e}" + Fore.RESET)
        
        f.close()

    return None

if __name__ == "__main__":
    try:
        print("PRESS CTRL+C to exit\n")

        inp = input(Fore.YELLOW + "[?]Enter file name for Gestting Domain IPs: " + Fore.RESET)
        Conc(inp)

        inp = input(Fore.YELLOW + "\n[?]Enter file name for To store IPs: " + Fore.RESET)
        writeToFile(inp)

        nmap_q = input("Would you like an automatic nmap scan on each ip(Y or N): ").lower()
        if nmap_q == "y" or nmap_q == "yes":
            nmap_scan(file=inp)

        elif nmap_q == "n" or nmap_q == "no":
            print(Fore.LIGHTCYAN_EX + "\nALR..}EXITING{..ALR" + Fore.RESET)

    except KeyboardInterrupt:
        print(blue + "\nPRESSED CTRL C..._EXITING_...C LRTC DESSERP" + Fore.RESET)
