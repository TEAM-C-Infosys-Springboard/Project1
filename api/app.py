from fastapi import FastAPI
from engine.store import PyKVStore

app = FastAPI(title="PyKV - In-Memory Key Value Store")

# Create one global store instance
kv_store = PyKVStore()


@app.post("/put")
def put_value(key: str, value: str):
    kv_store.put(key, value)
    return {"message": "Key stored successfully"}


@app.get("/get/{key}")
def get_value(key: str):
    value = kv_store.get(key)
    if value is None:
        return {"error": "Key not found"}
    return {"key": key, "value": value}


@app.delete("/delete/{key}")
def delete_value(key: str):
    success = kv_store.delete(key)
    if not success:
        return {"error": "Key not found"}
    return {"message": "Key deleted successfully"}
