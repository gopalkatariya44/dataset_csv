# dataset_csv

if you have both images and txt in different folder
``` 
python main.py -a dataset/annotations -i dataset/images -c dataset/annotations/classes.txt
```
                -csv "dataset.csv" 
                -o "sprate_labels_output"

if you have both images and txt in one folder
``` 
python main.py -i "dataset" -c "classes.txt" -o "output"
```