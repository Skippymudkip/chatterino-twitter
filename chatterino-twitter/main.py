import time
from mentions import recentmention
from twitter import send_message

# PATH TO CHATTERINO LOGS WITH DOUBLE FORWARD SLASHES Ex. 'C:\\Users\\'
path = ''
user_id = ''

basemention = recentmention(path)

while True:
    newmention = recentmention(path)
    if newmention == basemention:
        time.sleep(0.01)
    else:
        send_message(user_id, message=newmention)
        basemention = newmention
        time.sleep(0.01)
