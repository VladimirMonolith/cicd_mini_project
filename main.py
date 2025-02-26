from fastapi import FastAPI
import uvicorn


app = FastAPI(title='cicd_mini_project')


@app.get('/')
def root():
    return {'message': 'Test cicd_mini_project'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
