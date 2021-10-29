from fastapi import FastAPI

app = FastAPI()

# Minimal app - get request
@app.get("/", tags=['ROOT'])
async def root() -> dict:
	return {"ping" : "Pong"}



# Get --> Read ToDo
@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
	return {"data":todos}

# Post --> Create ToDo
# Put --> Update ToDo
# Delete --> Delete ToDO
todos = [
	{
		'id':1,
		'Activity': 'Learning how to create API using Fast API'
	},
	{
		'id':2,
		'Activity': 'Learning how integrate Fast API with React Js Framework'
	},
	{
		'id':3,
		'Activity': 'Learning how connect any database with Fast API'
	},
	{
		'id':4,
		'Activity': 'Create an ecommerce using Fast API, React Js, and MongoDB or SQL'
	}
]