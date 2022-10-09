import myfitnesspal as ext_myfitnesspal
from http.cookiejar import CookieJar
import pickle
import webbrowser


print("You'll be asked to log into myfitnesspal in order to generate a cookiejar for the extension to use")
input("Press Enter to log in...")

webbrowser.open('https://www.myfitnesspal.com/account/my-goals')

print("\nNow that you've (hopefully!) logged in, press enter in order to locate the logged in session and save it to myfitnesspal_cookiejar.pkl")
input("Press Enter to generate cookie jar...")

client = ext_myfitnesspal.Client()

# attempt to read something
client.get_measurements("Weight")

# save cookie jar
filehandler = open("myfitnesspal_cookiejar.pkl","wb")
pickle.dump(client.session.cookies,filehandler)
filehandler.close()

print('successfully saved cookiejar to "myfitnesspal_cookiejar.pkl"')
print("locate myfitnesspal_cookiejar.pkl and save it to custom_components/my_fitnesspal/myfitnesspal_cookiejar.pkl for HASS to be able to use it")