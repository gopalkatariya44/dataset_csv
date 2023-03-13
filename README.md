# dataset_csv

if you have both images and txt in different folder
``` 
python main.py --annotations dataset/annotations --images dataset/images --classes dataset/annotations/classes.txt
```
                -csv "dataset.csv" 
                -o "sprate_labels_output"

if you have both images and txt in one folder
``` 
python main.py --images "dataset" --classes "classes.txt" --csv-output "dataset.csv" --output "sp_labels"
```

``` 
python main.py --annotations "VOC2012/yolotxt" --images "VOC2012/JPEGImages" --classes "VOC2012/classes.txt" --output "sp_labels" --csv-output "VOC2012/dataset.csv"
```