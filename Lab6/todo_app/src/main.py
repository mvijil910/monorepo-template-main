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

@app.get("books/{book_id}/checkout_book")
def first_apiV2(path_param: str, ): 
    return {"msg": path_param}
