import os
import re
import config


class Dataset:
    def __init__(self, yolo_txt_path=None, images_path=None, classes_path=None):
        if yolo_txt_path is None or images_path is None or classes_path is None:
            print("please give dataset paths....")
        self.yolo_txt_path = yolo_txt_path
        self.images_path = images_path
        self.classes_path = classes_path

    @staticmethod
    def verfy_dataset():
        print("Verfy Dataset.........")

    def read_classes(self):
        with open(self.classes_path, 'r') as f:
            return [i.split('\n')[0] for i in f.readlines()]

    def to_csv(self, csv_path=None):
        dataset_list = []
        p = re.compile(config.image_regex)
        images_list = [i for i in os.listdir(self.images_path) if re.search(p, i)]
        yolo_txt_list = [i for i in os.listdir(self.yolo_txt_path) if i.endswith('.txt') and i != "classes.txt"]

        for index, img, txt in enumerate(zip(images_list, yolo_txt_list)):
            with open(f"{self.yolo_txt_path}/{txt}", 'r') as f:
                lines = f.readlines()
            dataset_list.append({
                "image": f"{self.images_path}/{img}",
                "txt": f"{self.yolo_txt_path}/{txt}",
                "classes": {}
            })
            for line in lines:
                label_index = line.split()[0]
                classes_list = self.read_classes()
                print(classes_list[int(label_index)])
                dataset_list[index]['classes'].update({

                })


if __name__ == '__main__':
    dataset = Dataset(yolo_txt_path="static/dataset/annotations",
                      images_path="static/dataset/images",
                      classes_path="static/dataset/annotations/classes.txt")

    dataset.to_csv(csv_path="dataset.csv")
    print(dataset.read_classes())
