from anonfile import AnonFile

catch = 2

token = input("What is your anonfiles API key? ")
anon = AnonFile(token)

uptodown1 = input("choose one of the following to continue, 1 - upload 2 - download : ")
uptodown = int(uptodown1)
up = input("What file should be uploaded? EX - C:\Downloads\text.txt Enter directory here : ")
down = input("What is the URL for the file to download : ")

if uptodown < catch:
	# upload a file and enable progressbar terminal feedback
	upload = anon.upload(up, progressbar=True)
	print(upload.url.geturl())
else:
	# download a file and set the download directory
	from pathlib import Path
	target_dir = Path.home().joinpath('Downloads')
	filename = anon.download(down, path=target_dir)
	print(filename)