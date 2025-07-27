# una colección de key:value pares   ordenadas y cambiables. No duplicados

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}


#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("USA"))

#if capitals.get("Russia"):
#    print(f"That capital exists")
#else:
#    print("That capital doesn't exist")

#capitals.update({"Germany": "Berlin"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()

#keys = capitals.keys()

#for key in capitals.keys():
#    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)