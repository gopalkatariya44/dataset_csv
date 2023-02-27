import argparse

from models import Dataset

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--annotations', type=str, default=None,
                        help='Yolo txt annotations path')
    parser.add_argument('-i', '--images', type=str, default=None, help='images path')
    parser.add_argument('-c', '--classes', type=str, default=None, help='classes.txt path')
    parser.add_argument('-csv', '--csv-output', type=str, default='dataset.csv', help='csv output path')
    parser.add_argument('-o', '--output', type=str, default='sprate_labels', help='labels output path')
    opt = parser.parse_args()
    dataset = Dataset(yolo_txt_path=opt.annotations,
                      images_path=opt.images,
                      classes_path=opt.classes)
    # dataset.to_csv(opt.csv_output)

    # dataset.sprate_labels(opt.output)

    dataset.change_label_to_index(opt.output)
