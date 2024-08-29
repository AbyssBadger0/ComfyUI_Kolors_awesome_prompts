import os
from datasets import Dataset

class KolorsAwesomePrompts:
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    data_path = os.path.join(current_directory, 'Kolors_awesome_prompts_without_image')
    dataset = Dataset.load_from_disk(data_path)
    styles = dataset['NAME_ZH']
    def __init__(self):
        pass


    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True,"default": ""}),
                "neg_prompt":("STRING", {"multiline": True, "default": ""}),
                "style": (s.styles,)
                }
            }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("prompt", "neg_prompt")
    FUNCTION = "kolors_awesome_prompts"
    CATEGORY = "prompts"

    def kolors_awesome_prompts(self, prompt, neg_prompt, style):
        for row in self.dataset:
            if row['NAME_ZH'] == style:
                prompt = row['PROMPT'].replace("{prompt}", prompt)
                
                # 检查 neg_prompt 是否以标点符号结尾
                if neg_prompt and neg_prompt[-1] in "。，！;？.,!":
                    neg_prompt = neg_prompt[:-1] + "、"
                elif len(neg_prompt) > 0:
                    neg_prompt += "、"
        return (prompt,neg_prompt)

NODE_CLASS_MAPPINGS = {
    "KolorsAwesomePrompts": KolorsAwesomePrompts
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KolorsAwesomePrompts": "KolorsAwesomePrompts"
}