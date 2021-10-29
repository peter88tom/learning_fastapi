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
@app.post("/todo", tags=["todos"])
async def add_todo(todo:dict) -> dict:
	todos.append(todo)
	return {"data" : "ToDo has been added"}

# Put --> Update ToDo
@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id:int, body:dict) -> dict:
	for todo in todos:
		try:
			if int(todo['id']) == id:
				todo['Activity'] = body['Activity']

				return {
					"data":f"Todo number {id} is updated"
				}
		except Exception as e:
			print(e)
			return {
					"data":f"ToDo with Id number  {id} was not updated"
				}


# Delete --> Delete ToDO
@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int)->dict:
	for todo in todos:
		try:
			if int(todo['id']) == id:
				todos.remove(todo)
				return {
					"data": f"ToDo with ID number {id} was removed from the list"
				}
		except Exception as e:
			return {
				"data":f"ToDo with ID number {id} does not exist"
			}

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