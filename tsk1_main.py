class Editor:
    def __init__(self, license_key: str):
        self.license_key = license_key
    def view_document(self):
        print("Перегдяд дозволений.")
    def edit_document(self):
        print(f"Редагування дозволено. Ключ {self.license_key} вірний.")

class ProEditor(Editor):
    def edit_document(self):
        print(f"Редагування не дозволено. Ключ {self.license_key} не вірний.")

license_key = "1111"
while True:
    key = input("Введіть ключ, або 'stop' для виходу: ")
    if key == "stop":
        break
    elif key == license_key:
        key_found = Editor(key)
    else:
        key_found = ProEditor(key)

    key_found.edit_document()    
    key_found.view_document()
    
