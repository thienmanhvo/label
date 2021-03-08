import os


def rename_all_file_with_prefix(source_dir: str, prefix: str):
    for filename in os.listdir(f"{source_dir}"):
        os.rename(f'{source_dir}/{filename}', f"{source_dir}/{prefix}_{filename}")


rename_all_file_with_prefix('handwriting/Linh/data', "Linh");
