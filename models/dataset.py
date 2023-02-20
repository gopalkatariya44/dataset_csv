import os
import re
import config
import pandas as pd
from .dataset_schema import DatasetSchema


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

    def to_csv(self, csv_path=None):
        df = pd.DataFrame(self.dataset_to_list())
        df.to_csv(csv_path, index=False)
        print(f"csv file generated here '{csv_path}'")

    def dataset_to_list(self):
        dataset_list = []
        p = re.compile(config.image_regex)
        images_list = [i for i in os.listdir(self.images_path) if re.search(p, i)]
        yolo_txt_list = [i for i in os.listdir(self.yolo_txt_path) if i.endswith('.txt') and i != "classes.txt"]

        # create dict for same txt and images
        file_dict = {}
        for i, filename1 in enumerate(yolo_txt_list):
            for j, filename2 in enumerate(images_list):
                prefix = filename1[:-4:]
                if prefix in filename2:
                    if prefix in file_dict:
                        file_dict[prefix].append(filename2, filename1)
                    else:
                        file_dict[prefix] = [filename2, filename1]

        # now start create a dataset list for csv
        index = 0
        for i in file_dict:
            with open(f"{self.yolo_txt_path}/{file_dict[i][-1]}", 'r') as f:
                lines = f.readlines()

            dataset_schema = DatasetSchema()
            dataset_schema.index = index
            dataset_schema.image_path = f"{self.images_path}/{file_dict[i][0]}"
            dataset_schema.txt_path = f"{self.yolo_txt_path}/{file_dict[i][-1]}"

            for line in lines:
                label_index = int(line.split()[0])
                classes_list = self.read_classes()
                dataset_schema.classes.update({
                    f"{label_index}": classes_list[label_index]
                })

            dataset_list.append(dataset_schema.as_dict())
            index += 1
        return dataset_list
