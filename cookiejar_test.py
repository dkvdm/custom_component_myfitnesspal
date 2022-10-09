import myfitnesspal as ext_myfitnesspal
import pickle
import pathlib

# read cookie jar
current_path = pathlib.Path(__file__).parent.resolve()
file = open(f"{current_path}/myfitnesspal_cookiejar.pkl",'rb')
jar = pickle.load(file)
file.close()

client = ext_myfitnesspal.Client(cookiejar=jar)

print("logged in with cookiejar and reading latest weight...")
print(client.get_measurements("Weight"))