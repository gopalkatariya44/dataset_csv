import os
import re
import config
import pandas as pd


class Dataset:
    def __init__(self, yolo_txt_path: str = None, images_path: str = None, classes_path: str = None):
        """
        yolo_txt_path: add yolo txt folder path here.\n
        images_path: add yolo images folder path here.\n
        classes_path: add single file classes.txt here.
        """
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

    def to_csv(self, csv_path=None, image_ex=".jpg"):
        df = pd.DataFrame(self.dataset_to_list(image_ex))
        df.to_csv(csv_path, index=False)

    def dataset_to_list(self, image_ex):
        dataset_list = []
        p = re.compile(config.image_regex)
        images_list = [i for i in os.listdir(self.images_path) if re.search(p, i)]
        yolo_txt_list = [i for i in os.listdir(self.yolo_txt_path) if i.endswith('.txt') and i != "classes.txt"]
        index = 0

        for txt in yolo_txt_list:
            with open(f"{self.yolo_txt_path}/{txt}", 'r') as f:
                lines = f.readlines()
            if f"{txt.split('.')[0]}{image_ex}" in images_list:
                dataset_list.append({
                    "index": index,
                    "image": f"{self.images_path}/{txt.split('.')[0]}{image_ex}",
                    "txt": f"{self.yolo_txt_path}/{txt}",
                    "classes": {}
                })
                for line in lines:
                    label_index = int(line.split()[0])
                    classes_list = self.read_classes()
                    dataset_list[index]['classes'].update({
                        f"{label_index}": classes_list[label_index]
                    })
                    # if classes_list[int(label_index)] not in dataset_list[index]['classes']:
                    #     dataset_list[index]['classes'].append(classes_list[int(label_index)])
                index += 1
        return dataset_list
