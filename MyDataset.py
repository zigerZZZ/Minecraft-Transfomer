import csv
from torch.utils.data import Dataset

class CustomTranslationDataset(Dataset):
    def __init__(self, csv_path, source_col="src", target_col="target"):
        self.samples = []
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.samples.append({
                    "input_ids": row[source_col],
                    "labels": row[target_col]
                })
    
    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, idx):
        return self.samples[idx]