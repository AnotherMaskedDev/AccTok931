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

GetUpdateFiles()
print("Update completed successfully!")
os.system('pause')
