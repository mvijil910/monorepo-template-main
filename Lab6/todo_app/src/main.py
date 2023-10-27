from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/api")
def first_api(): 
    return {"msg": "hello_world"}

@app.get("/books/{path_param}")
def first_apiV2(path_param: str): 
    return {"msg": path_param}


@app.get("/books/")
def first_apiV3(title: str): 
    return {"msg": title}

@app.post("/books/create_book")
def first_apiV4(new_book=Body()): 
    print(new_book)
    return {"msg": new_book}

# query and path param
@app.get("/books/{title}/")
def first_apiV5(title: str, book_id: str ): 
    return {"msg": title, "msg2": book_id}

# Create a PUT ReST API

# Create a DELETE ReST API

