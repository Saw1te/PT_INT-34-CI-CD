from fastapi import FastAPI, status

app = FastAPI()

@app.get("/")
def get_main():
    return {'message': 'Hello World!'}

@app.get("/healthz")
def get_healthz():
    return "200 OK"
