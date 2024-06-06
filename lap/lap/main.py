from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def asif():
    return {"asif langrah"}
@app.get("/chatgpt")
def asif():
    chatgpt ={"im duffer"}
    return {"chatgpt"}