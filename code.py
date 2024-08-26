def GetUpdateFiles():
    global filename
    url = 'https://www.dropbox.com/scl/fi/vwxvwd3vd23e288o8z29n/ModernGUI.zip?rlkey=lkx9w4j1rxttemi5q78053mrl&st=tl2t9994&dl=1'
    filename = get_filename_from_url(url)

    if os.path.exists(filename) != True:
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            total_size = int(response.headers.get('content-length', 0))
            block_size = 8192  # 8 KB
            downloaded_size = 0
            
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=block_size):
                    file.write(chunk)
                    downloaded_size += len(chunk)
                    percent_complete = (downloaded_size / total_size) * 100
                    print(f"\rDownload progress: {percent_complete:.2f}% complete", end="")
            print("\nFile downloaded successfully and saved as", filename)
            ExtractUpdateFiles()
        else:
            print("Failed to download file")
    else:
        ExtractUpdateFiles()

def ExtractUpdateFiles():
    extractor_path = resource_path('External\\Extractors\\7z\\7z.exe')
    if os.path.exists("UpdateFiles"):
        pass
    else:
        os.system("mkdir UpdateFiles")
    file_path = resource_path(filename)
    output_dir = resource_path('UpdateFiles')
    command = '"{}" x "{}" -o"{}" -r -y'.format(extractor_path, file_path, output_dir)
    subprocess.run(command, shell=True)
    command = 'del /f /s /q "{}" '.format(file_path)
    os.system(command)
    source_dir = resource_path('UpdateFiles')
    out_dir = resource_path("")
    CompleteUpdate(source_dir, out_dir)

def CompleteUpdate(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            dest_path = os.path.join(dest_dir, item)
            shutil.move(src_path, dest_path)
    except:
        pass
    command = 'del /f /s /q "{}\*" '.format(src_dir)
    os.system(command)
    command = 'for /d %x in ("{}\*") do rmdir /s /q "%x"'.format(src_dir)
    os.system(command)

GetUpdateFiles()
print("Update completed successfully!")
os.system('pause')
