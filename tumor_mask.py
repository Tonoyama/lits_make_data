import os
import pandas as pd
import shutil

# CSVファイルのパスとデータセットフォルダのパスを指定
csv_path = "lits_df.csv"
dataset_folder = "./dataset_6"

# 出力先フォルダのパスを指定
output_folder_tumor_mask = "tumor_mask"
output_folder_tumor_volume = "tumor_volume"

# 出力先フォルダが存在しない場合は作成
if not os.path.exists(output_folder_tumor_mask):
    os.makedirs(output_folder_tumor_mask)

if not os.path.exists(output_folder_tumor_volume):
    os.makedirs(output_folder_tumor_volume)

# CSVファイルを読み込む
df = pd.read_csv(csv_path)

# tumor_mask_emptyがTRUEの場合のみ処理を行う
for index, row in df.iterrows():
    if row['tumor_mask_empty']:
        # tumor_maskpathの画像をコピー
        tumor_mask_source = os.path.join(dataset_folder, row['tumor_maskpath'][28:])
        tumor_mask_dest = os.path.join(output_folder_tumor_mask, os.path.basename(row['tumor_maskpath']))
        shutil.copyfile(tumor_mask_source, tumor_mask_dest)

        # filepathの画像をコピー
        tumor_volume_source = os.path.join(dataset_folder, row['filepath'][28:])
        tumor_volume_dest = os.path.join(output_folder_tumor_volume, os.path.basename(row['filepath']))
        shutil.copyfile(tumor_volume_source, tumor_volume_dest)
