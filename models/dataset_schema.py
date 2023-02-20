class DatasetSchema:
    def __init__(self):
        self.index = ""
        self.image_path = ""
        self.txt_path = ""
        self.classes = {}

    def as_dict(self):
        return {
            "index": self.index,
            "image": self.image_path,
            "txt": self.txt_path,
            "classes": self.classes
        }