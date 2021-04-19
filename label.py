import os
from shutil import copyfile

HAMEXGray_data = "internet_handwriting/HAMEXGray"
HAMEXGray_label = "internet_handwriting/HamexLabel"

MathBrush_data = "internet_handwriting/MathBrush"
MathBrush_label = "internet_handwriting/MathBrushLabel"

MfrDBGray_data = "internet_handwriting/MfrDBGray"
MfrDBGray_label = "internet_handwriting/MfrDBLabel"


def rename_all_file_with_prefix(source_dir: str, prefix: str):
    for filename in os.listdir(f"{source_dir}"):
        os.rename(f'{source_dir}/{filename}', f"{source_dir}/{prefix}_{filename}")


# rename_all_file_with_prefix('team_handwriting/Duy/data/451-500', "Duy");

def copy_team():
    path = "team_handwriting"
    dirs = next(os.walk(f"{path}"))[1]
    for dir in dirs:
        data_path = f"{path}/{dir}/data"
        label_path = f"{path}/{dir}/fixed_label"
        dir_datas = next(os.walk(f"{data_path}"))[1]
        for dir_data in dir_datas:
            for filename in os.listdir(f"{data_path}/{dir_data}"):
                if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(
                        ".png") or filename.endswith(".PNG") or filename.endswith(".JPG") or filename.endswith(".JPEG"):
                    filename_without_extension = os.path.splitext(filename)[0]
                    if os.path.exists(f"{label_path}/{dir_data}/{filename_without_extension}.txt"):
                        print(filename_without_extension)
                        copyfile(f"{data_path}/{dir_data}/{filename}", f"data/{filename}")
                        copyfile(f"{label_path}/{dir_data}/{filename_without_extension}.txt",
                                 f"data/{filename_without_extension}.txt")


def copy_intenet():
    path = "internet_handwriting"
    data_path = f"{path}/data"
    dirs = next(os.walk(f"{data_path}"))[1]
    label_path = f"{path}/fixed_label"
    for dir in dirs:
        for filename in os.listdir(f"{data_path}/{dir}"):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(
                    ".png") or filename.endswith(".PNG") or filename.endswith(".JPG") or filename.endswith(".JPEG"):
                filename_without_extension = os.path.splitext(filename)[0]
                if os.path.exists(os.path.join(os.path.join(label_path, dir), f"{filename_without_extension}.txt")):
                    print(filename_without_extension)
                    copyfile(f"{data_path}/{dir}/{filename}", f"data/{filename}")
                    copyfile(f"{label_path}/{dir}/{filename_without_extension}.txt",
                             f"data/{filename_without_extension}.txt")


def copy():
    path = "admin"
    dirs = next(os.walk(f"{path}"))[1]
    for dir in dirs:
        data_path = f"{path}/{dir}/data"
        label_path = f"{path}/{dir}/label"
        dir_datas = next(os.walk(f"{data_path}"))[1]
        for dir_data in dir_datas:
            for filename in os.listdir(f"{data_path}/{dir_data}"):
                if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(
                        ".png") or filename.endswith(".PNG") or filename.endswith(".JPG") or filename.endswith(".JPEG"):
                    filename_without_extension = os.path.splitext(filename)[0]
                    if os.path.exists(f"{label_path}/{dir_data}/{filename_without_extension}.txt"):
                        print(filename_without_extension)
                        copyfile(f"{data_path}/{dir_data}/{filename}", f"data/{filename}")
                        copyfile(f"{label_path}/{dir_data}/{filename_without_extension}.txt",
                                 f"data/{filename_without_extension}.txt")


copy()
copy_team()
copy_intenet()
