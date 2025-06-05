import socket as s
from colorama import Fore
import subprocess as sub
import argparse as a

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
    parser = a.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")

    functions = subparser.add_argument("run", description="Run program")
    functions.add_argument("--input_file")
    functions.add_argument("--output_file")
    functions.add_argument("--nmap_scan", type=bool)
    args = parser.parse_args()
    try:
        print("PRESS CTRL+C to exit\n")

        # arg for file with domain IP's and output file
        if args.command == "run":
            Conc(args.input_file)
            writeToFile(args.output_file)
            if args.nmap_scan == True:
                nmap_scan(file=inp)
                print(Fore.LIGHTCYAN_EX + "\nALR..}EXITING{..ALR" + Fore.RESET)
                
    except KeyboardInterrupt:
        print(blue + "\nPRESSED CTRL C..._EXITING_...C LRTC DESSERP" + Fore.RESET)
