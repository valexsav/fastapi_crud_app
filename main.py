from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def main_page():
    return {"message": "yo hows life?"}

@app.get("/health")
def health_check():
    return {"health": "good"}