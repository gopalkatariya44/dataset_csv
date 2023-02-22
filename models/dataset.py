import os
import re
import config
import pandas as pd
from .dataset_schema import DatasetSchema
import shutil


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
        """
        txt format:\n
        bus\n
        car\n
        bike\n
        :return: List Classes ["bus", "car", "bike"]
        """
        with open(self.classes_path, 'r') as f:
            return [i.split('\n')[0] for i in f.readlines()]

    def to_csv(self, csv_path=None):
        df = pd.DataFrame(self.dataset_to_list())
        df.to_csv(csv_path, index=False)
        print(f"csv file generated here '{csv_path}'")

    def similar_image_text_dict(self):
        compiled_image_regex = re.compile(config.image_regex)
        images_list = [i for i in os.listdir(self.images_path) if re.search(compiled_image_regex, i)]
        yolo_txt_list = [i for i in os.listdir(self.yolo_txt_path) if i.endswith('.txt') and i != "classes.txt"]
        # create dict for same txt and images
        file_dict = {}
        for i, txt in enumerate(yolo_txt_list):
            for j, image in enumerate(images_list):
                prefix = txt[:-4:]
                if prefix in image:
                    if prefix in file_dict:
                        file_dict[prefix].append(image, txt)
                    else:
                        file_dict[prefix] = [image, txt]
        return file_dict

    def dataset_to_list(self):
        """
        return all iamges path and txt path with there labels\n
        {
        \t'index': 0,\n
        \t'image_path': 'dataset/images/20230207145026.jpg',\n
        \t'txt_path': 'dataset/annotations/20230207145026.txt',\n
        \t'classes': {'0': 'car'}\n
        }
        :return: list of dict
        """
        dataset_list = []
        # now start create a dataset list for csv
        final_dict = self.similar_image_text_dict()
        for index, i in enumerate(final_dict):
            with open(f"{self.yolo_txt_path}/{final_dict[i][-1]}", 'r') as f:
                lines = f.readlines()
            dataset_schema = DatasetSchema(index=index,
                                           image_path=f"{self.images_path}/{final_dict[i][0]}",
                                           txt_path=f"{self.yolo_txt_path}/{final_dict[i][1]}",
                                           classes={},
                                           )
            for line in lines:
                label_index = int(line.split()[0])
                classes_list = self.read_classes()
                dataset_schema.classes.update({
                    f"{label_index}": classes_list[label_index]
                })
            dataset_list.append(dataset_schema.as_dict())
        return dataset_list

    def sprate_labels(self, output_path: str):
        classes = self.read_classes()
        final_dict = self.similar_image_text_dict()

        for index, i in enumerate(final_dict):
            with open(f"{self.yolo_txt_path}/{final_dict[i][-1]}", 'r') as f:
                lines = f.readlines()

            for line in lines:
                label_index = int(line.split()[0])
                os.makedirs(f"{output_path}/{classes[label_index]}", exist_ok=True)
                with open(f"{output_path}/{classes[label_index]}/{final_dict[i][1]}", 'a') as f:
                    f.write(line)
                if not os.path.exists(output_path + '/' + classes[label_index] + '/' + final_dict[i][0]):
                    shutil.copy(self.images_path + '/' + final_dict[i][0],
                                output_path + '/' + classes[label_index] + '/' + final_dict[i][0])
        print(f"sprate labels folder generated here : {output_path}/")
