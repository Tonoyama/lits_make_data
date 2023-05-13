import csv

def process_csv(csv_file, txt_file):
    with open(csv_file, 'r') as csvfile, open(txt_file, 'w') as txtfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['liver_mask_empty'] == 'True':
                filepath = row['liver_maskpath']
                new_filepath = filepath.replace('../input/lits-png/dataset_6/', '')
                txtfile.write(new_filepath + '\n')

# Train用ファイルの作成
process_csv('lits_train.csv', 'liver_train.txt')

# Val用ファイルの作成
process_csv('lits_probe.csv', 'liver_val.txt')
