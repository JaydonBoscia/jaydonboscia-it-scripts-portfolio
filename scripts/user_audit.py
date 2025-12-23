import os
import platform
import getpass
from datetime import datetime

def collect_system_info():
    return {
        "OS": platform.system(),
        "OS_Version": platform.version(),
        "Machine": platform.machine(),
        "Hostname": platform.node(),
        "Current_User": getpass.getuser(),
        "Timestamp": datetime.now().isoformat()
    }

def get_local_users():
    if os.name == "nt":
        return os.popen("net user").read()
    else:
        return os.popen("cut -d: -f1 /etc/passwd").read()

def write_report(data):
    with open("user_audit_report.txt", "w") as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")

if __name__ == "__main__":
    info = collect_system_info()
    users = get_local_users()
    info["Local_Users"] = users
    write_report(info)
    print("User audit completed. Report generated.")
