import argparse

from models import Dataset

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--annotations', nargs='+', type=str, default='dataset/annotations',
                        help='Yolo txt annotations path')
    parser.add_argument('-i', '--images', nargs='+', type=str, default='dataset/images', help='images path')
    parser.add_argument('-c', '--classes', nargs='+', type=str, default='dataset/annotations/classes.txt', help='classes.txt path')
    parser.add_argument('-csv', '--csv-output', nargs='+', type=str, default='dataset.csv', help='csv output path')
    parser.add_argument('-o', '--output', nargs='+', type=str, default='output', help='labels output path')
    opt = parser.parse_args()
    dataset = Dataset(yolo_txt_path=opt.annotations,
                      images_path=opt.images,
                      classes_path=opt.classes)
    # dataset.to_csv(opt.csv_output)

    dataset.sprate_labels(output_path=opt.output)
