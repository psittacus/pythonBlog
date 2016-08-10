from ftplib import FTP
import io
import requests
import string

titel = str(input("Titel: "))

new_content = str(input("Content: "))

old_content = requests.get(url).content.decode() # Gets the html-code of the generated link. You have to replace "url" with the url of your blog

tmpcontent = old_content.split("<!-- split the shit here -->") # splits the html-code at the sign

final_content = tmpcontent[0] + "<!-- split the shit here --><div class=\"styleMe\"><h2 id=\"titel\">" + titel + "</h2><br><p id=\"content\">" + new_content + "</p><br></div>" + tmpcontent[1] # generates the new html-code

final_content_in_bytes = final_content.encode("utf-8") # encodes all to a byte-like object so you can upload it to the server

ftp = FTP('') # your ftp-server url
print(ftp.login("", "")) # username and password
bio = io.BytesIO(final_content_in_bytes)
ftp.storbinary('STOR index.html', bio) # uploads the code
ftp.quit() # quits the connection
