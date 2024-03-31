import subprocess

print("[+] ifconfig en0 before changing MAC address")
subprocess.call(["ifconfig", "en0", "down"])
subprocess.call(["sudo", "ifconfig", "en0", "hw", "ether", "00:11:22:33:44:55"])
subprocess.call(["ifconfig", "en0", "up"])
print("[+] ifconfig en0 after changing MAC address")



