class Editor:
    def __init__(self, license_key: str):
        self.license_key = license_key
    def view_document(self):
        print("Перегдяд дозволений.")
    def edit_document(self):
        print("Редагування дозволено.")

class ProEditor(Editor):
    def edit_document(self):
        print("Редагування не дозволено.")

license_key = "1111"
while True:
    key = input("Введіть ключ, або 'stop' для виходу: ")
    if key == "stop":
        break
    elif key == license_key:
        key_found = Editor(license_key)
    else:
        key_found = ProEditor(license_key)
        
    key_found.view_document()
    key_found.edit_document()
