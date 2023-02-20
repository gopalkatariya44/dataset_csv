from models import Dataset

if __name__ == '__main__':
    dataset = Dataset(yolo_txt_path="dataset/annotations",
                      images_path="dataset/images",
                      classes_path="dataset/annotations/classes.txt")

    dataset.to_csv(csv_path="dataset/dataset.csv", image_ex=".jpg")
