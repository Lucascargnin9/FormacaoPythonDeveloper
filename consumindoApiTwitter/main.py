
from fastapi import FastAPI
from src.services import *
import uvicorn
from src.responses import TrendItem


app = FastAPI()


@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
    return get_trends_from_mongo()


if __name__ == 'main':

    trends = get_trends_from_mongo()

    if not trends:
        save_trends()
    
    uvicorn.run(app, host='0.0.0.0', port=8000)



