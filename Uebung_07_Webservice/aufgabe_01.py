import uvicorn
from fastapi import FastAPI
app = FastAPI()
d = {}
file = open("PLZO_CSV_LV95.csv", encoding="utf-8")
next(file)

for line in file:
    data = line.strip().split(";")
    plz = data[1]
    ortschaft = data[0]
    kanton = data[5]
    gemeindename = data[3]
    ekoordinate = data[6]
    nkoordinate = data[7]
    d[gemeindename] = {"gemeindename": gemeindename, "plz": plz,"ortschaft": ortschaft, "kanton": kanton, "ekoordinate":ekoordinate, "nkoordinate":nkoordinate}
file.close()

@app.get("/search")
async def search(gemeindename: str):
    if gemeindename in d:
        return d[gemeindename]
    else:
        return {"error": "not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)


#Eingabe im Browser: http://127.0.0.1:8080/search?gemeindename=Wolfwil