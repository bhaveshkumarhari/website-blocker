import time
from datetime import datetime as dt

#hosts_temp = "hosts"
hosts_path = "/etc/hosts" # hosts file path
redirect = "127.0.0.1" # localhost ip.
# websites which want to block.
website_list = ["www.facebook.com","facebook.com"]

while True:
    # between two times as working hours. add website lists.
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,15):
        print("Working hours...")
        # open a hosts file for read and write.
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                # check if website is listed in content of a hosts file.
                if website in content:
                    pass # do nothing if listed website in hosts file.
                else:
                    # write website and redirect to a hosts file.
                    file.write(redirect + " " + website + "\n")
    # outside of the working hours. delete website lists.
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines() # read every line of file and stores in content variable.
            file.seek(0) # take pointer to start of the file
            for line in content: # each line iteration in content
                # checks website of website_list if it contains in any line
                if not any(website in line for website in website_list):
                    file.write(line) # if does't contain then append lines.
            file.truncate() # delete everything after appending the contents.
        print("Fun hours...")
    time.sleep(5)
