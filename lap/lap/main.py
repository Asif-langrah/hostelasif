from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def asif():
    return {"asif langrah"}
@app.get("/chatgpt")
def asif():
    chatgpt ={"im duffer"}
    return {"chatgpt"}
@app.post("/")
def asif(management,university,iba):
    return {"key1":management, "key2":university, "key3":iba},  
