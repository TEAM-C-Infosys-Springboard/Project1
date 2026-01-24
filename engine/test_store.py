from store import PyKVStore

kv = PyKVStore()

kv.put("name", "Divi")
print(kv.get("name"))

kv.delete("name")
print(kv.get("name"))
