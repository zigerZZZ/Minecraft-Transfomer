import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
class Translator:
    def __init__(self, path="fine-tuned-model/last"):
        self.model = AutoModelForSeq2SeqLM.from_pretrained(path)
        self.tokenizer = AutoTokenizer.from_pretrained(path)

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
        self.model.eval()

    def translate(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        inputs = inputs.to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(**inputs)
        translated_text = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
        return translated_text


if __name__ == "__main__":
    translator = Translator()

    # 一些常见数据
    src = ["Minecraft","Botania","chest","cobblestone",
           "mob","mob spawner","Cupronickel Coil Block","vanilla Minecraft"]
    predict = translator.translate(src)
    for i in range(len(src)):
        print(f"原文: {src[i]}")
        print(f"机翻: {predict[i]}")
        print()

    print("-"*20)
    import pandas as pd
    data = pd.read_csv("datas/test.csv")
    # 随机选择10条数据
    data = data.sample(10)
    
    src = data["src"].tolist()
    target = data["target"].tolist()
    predict= translator.translate(src)
    
    for i in range(len(src)):
        print(f"原文: {src[i]}")
        print(f"译文: {predict[i]}")
        print(f"机翻: {target[i]}")
        print()