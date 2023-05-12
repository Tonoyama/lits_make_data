import os
import pandas as pd
import shutil

# CSVファイルのパスとデータセットフォルダのパスを指定
csv_path = "lits_df.csv"
dataset_folder = "./dataset_6"

# 出力先フォルダのパスを指定
output_folder_liver_mask = "liver_mask"
output_folder_liver_volume = "liver_volume"

# 出力先フォルダが存在しない場合は作成
if not os.path.exists(output_folder_liver_mask):
    os.makedirs(output_folder_liver_mask)

if not os.path.exists(output_folder_liver_volume):
    os.makedirs(output_folder_liver_volume)

# CSVファイルを読み込む
df = pd.read_csv(csv_path)

# liver_mask_emptyがTRUEの場合のみ処理を行う
for index, row in df.iterrows():
    if row['liver_mask_empty']:
        # liver_maskpathの画像をコピー
        liver_mask_source = os.path.join(dataset_folder, row['liver_maskpath'][28:])
        liver_mask_dest = os.path.join(output_folder_liver_mask, os.path.basename(row['liver_maskpath']))
        shutil.copyfile(liver_mask_source, liver_mask_dest)

        # filepathの画像をコピー
        liver_volume_source = os.path.join(dataset_folder, row['filepath'][28:])
        liver_volume_dest = os.path.join(output_folder_liver_volume, os.path.basename(row['filepath']))
        shutil.copyfile(liver_volume_source, liver_volume_dest)
