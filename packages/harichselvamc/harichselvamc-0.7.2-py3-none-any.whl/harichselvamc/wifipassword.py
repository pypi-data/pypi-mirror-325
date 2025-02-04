import subprocess
import platform

def get_wifi_password(network_name: str) -> str:
    """
    Retrieves the Wi-Fi password for the given network name.
    Works on Windows, macOS, and Linux.
    
    :param network_name: The SSID (Wi-Fi network name) to retrieve the password for.
    :return: The Wi-Fi password or an error message if not found.
    """
    os_name = platform.system()

    try:
        if os_name == "Windows":
            result = subprocess.run(
                ["netsh", "wlan", "show", "profile", network_name, "key=clear"],
                capture_output=True,
                text=True,
                check=True
            )
            for line in result.stdout.split("\n"):
                if "Key Content" in line:
                    return line.split(":")[1].strip()
            return "Password not found or network does not exist."

        elif os_name == "Darwin":  # macOS
            result = subprocess.run(
                ["security", "find-generic-password", "-ga", network_name],
                capture_output=True,
                text=True
            )
            return result.stderr.split('"')[1] if "password" in result.stderr else "Password not found."

        elif os_name == "Linux":
            result = subprocess.run(
                ["nmcli", "-s", "-g", "802-11-wireless-security.psk", "connection", "show", network_name],
                capture_output=True,
                text=True
            )
            return result.stdout.strip() if result.stdout else "Password not found."

        else:
            return "Unsupported OS."

    except subprocess.CalledProcessError:
        return "Error retrieving password. Make sure the network exists."

