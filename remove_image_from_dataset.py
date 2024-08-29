import os
from modelscope.msdatasets import MsDataset
from datasets import Dataset

def remove_columns_and_save(dataset: MsDataset, columns_to_remove: list, output_path: str):
    # 将 MsDataset 转换为 Dataset
    dataset = Dataset.from_dict(dataset.to_dict())
    
    # 删除指定列
    dataset = dataset.remove_columns(columns_to_remove)
    
    # 创建输出目录（如果不存在）
    os.makedirs(output_path, exist_ok=True)
    
    # 保存数据集到输出目录
    dataset.save_to_disk(output_path)
    print(f"Dataset saved to {output_path}")

def load_saved_dataset(output_path: str) -> Dataset:
    # 从指定目录加载数据集
    dataset = Dataset.load_from_disk(output_path)
    return dataset

if __name__ == '__main__':
    # 获取当前文件的绝对路径
    current_file_path = os.path.abspath(__file__)
    
    # 获取当前文件所在的目录路径
    current_directory = os.path.dirname(current_file_path)

    # 设置缓存目录
    cache_dir = os.path.join(current_directory, 'Kolors_awesome_prompts')

    # 加载数据集
    ds = MsDataset.load('modelscope/Kolors_awesome_prompts', subset_name='default', split='train', cache_dir=cache_dir)

    # 假设你想删除名为 'IMAGE' 和 'PROMPT_EXAMPLE' 的列
    columns_to_remove = ['IMAGE', 'PROMPT_EXAMPLE']

    # 设置输出路径
    output_path = os.path.join(current_directory, 'Kolors_awesome_prompts_without_image')

    # 删除列并保存数据集
    remove_columns_and_save(ds, columns_to_remove, output_path)

    # 加载保存的数据集
    loaded_dataset = load_saved_dataset(output_path)
    print("Loaded dataset:", loaded_dataset)