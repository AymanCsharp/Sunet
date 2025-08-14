#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
import time
from colorama import init, Fore, Back, Style

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.RED}    
{Fore.RED}    
{Fore.RED}                                              
{Fore.CYAN}                     ███████╗██╗   ██╗               ███╗   ██╗███████╗████████╗
{Fore.MAGENTA}                  ██╔════╝██║   ██║               ████╗  ██║██╔════╝╚══██╔══╝
{Fore.WHITE}                    ███████╗██║   ██║               ██╔██╗ ██║█████╗     ██║   
{Fore.RED}                      ╚════██║██║   ██║               ██║╚██╗██║██╔══╝     ██║   
{Fore.YELLOW}                   ███████║╚██████╔╝               ██║ ╚████║███████╗   ██║   
{Fore.GREEN}                    ╚══════╝ ╚═════╝                ╚═╝  ╚═══╝╚══════╝   ╚═╝                                                                                                                                                      
{Fore.GREEN}    
{Fore.CYAN}     
{Fore.MAGENTA}    
{Fore.WHITE}     
{Fore.RED}                                        
{Fore.YELLOW}     ╔══════════════════════════════════════╗
{Fore.GREEN}      ║           Sunet tool                 ║     
{Fore.CYAN}       ║           " Port/Host Checker "      ║
{Fore.MAGENTA}    ╚══════════════════════════════════════╝
{Style.RESET_ALL}
"""
    print(banner)

def check_server(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False
    except Exception:
        return False

def main():
    while True:
        print("\033[H\033[J")
        print_banner()
        print(f"{Fore.CYAN}Welcome To Sunet Tool{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Host/Port Checker Tool{Style.RESET_ALL}")
        print()
        print(f"{Fore.GREEN}Enter Host:Port - Example: 1.2.7:25255{Style.RESET_ALL}")
        print(f"{Fore.WHITE}to quit type 'exit'{Style.RESET_ALL}")
        print()
        
        try:
            user_input = input(f"{Fore.CYAN}Sunet> {Style.RESET_ALL}").strip()
            
            if user_input.lower() == 'exit':
                print(f"\n{Fore.YELLOW}Thank you for using Sunet!{Style.RESET_ALL}")
                break
            
            if ':' not in user_input:
                print(f"\n{Fore.RED}Error! Please use Host:Port format{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Example: 192.168.1.1:80{Style.RESET_ALL}")
                input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
                continue
            
            host, port_str = user_input.split(':', 1)
            host = host.strip()
            
            try:
                port = int(port_str.strip())
                if port < 1 or port > 65535:
                    raise ValueError("Port out of range")
            except ValueError:
                print(f"\n{Fore.RED}Error: Invalid port number (1-65535){Style.RESET_ALL}")
                input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
                continue
            
            print(f"\n{Fore.CYAN}Checking {host}:{port}...{Style.RESET_ALL}")
            
            for i in range(3):
                print(f"{Fore.YELLOW}.{Style.RESET_ALL}", end="", flush=True)
                time.sleep(0.5)
            print()
            
            if check_server(host, port):
                print(f"\n{Fore.GREEN}ONLINE - Server is reachable{Style.RESET_ALL}")
                print(f"{Fore.CYAN}{host}:{port} is available{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.RED}OFFLINE - Server is not reachable{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}{host}:{port} is not available{Style.RESET_ALL}")
            
            print()
            input(f"{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
            
        except KeyboardInterrupt:
            print(f"\n\n{Fore.YELLOW}Program interrupted by user{Style.RESET_ALL}")
            break
        except EOFError:
            print(f"\n\n{Fore.YELLOW}Thank you for using Sunet!{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n{Fore.RED}Unexpected Error: {e}{Style.RESET_ALL}")
        input("Press Enter to exit...")
