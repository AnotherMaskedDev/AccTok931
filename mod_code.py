def GetUpdateFiles():
    global filename, download_link
    filename = get_filename_from_url(download_link)

    if os.path.exists(filename) != True:
        response = requests.get(download_link, stream=True)

        if response.status_code == 200:
            print("Update Found!\n")
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
