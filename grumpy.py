class GrupmyDict(dict):
    # nie musimy definiować __init__() bo mozemy uzyc istniejacego juz dict __init__()
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL IT AINT HERE!")

    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE DICTIONARY?")
        print("OK FINE..")
        return super().__setitem__(key, value)

    def __contains__(self, item):
        print("NO IT AINT IN HERE")
        return False


data = GrupmyDict({"first": "Tom", "animal": "cat"})
print(data)
data['city'] = "Tokio"
print(data)
