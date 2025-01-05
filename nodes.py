import time
import json

class DelayNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {
                        "myINT": ("INT",{"forceInput": False,"default":15}),
                        "anything" : ("IMAGE", {}),

                    }
                }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "waitand"
    CATEGORY = "test"

    def waitand(self, anything):
        time.sleep(10)
        return (anything,)
    

#promptList NAIv4preの仕様によりマックス6で設定
class NAIpromptList:
    @classmethod
    def INPUT_TYPES(s):
        return {"optional": {
            "prompt_1": ("STRING", {"multiline": True, "default": ""}),
            "prompt_2": ("STRING", {"multiline": True, "default": ""}),
            "prompt_3": ("STRING", {"multiline": True, "default": ""}),
            "prompt_4": ("STRING", {"multiline": True, "default": ""}),
            "prompt_5": ("STRING", {"multiline": True, "default": ""}),
            "prompt_6": ("STRING", {"multiline": True, "default": ""}),

        },
            # "optional": {
            #     "optional_prompt_list": ("LIST",)
            # }
        }

    RETURN_TYPES = ("LIST", "STRING")
    RETURN_NAMES = ("prompt_list", "prompt_strings")
    OUTPUT_IS_LIST = (False, True)
    FUNCTION = "run"
    CATEGORY = "jisaku"

    def run(self, **kwargs):
        prompts = []

        if "optional_prompt_list" in kwargs:
            for l in kwargs["optional_prompt_list"]:
                prompts.append(l)

        # Iterate over the received inputs in sorted order.
        for k in sorted(kwargs.keys()):
            v = kwargs[k]

            # Only process string input ports.
            # if isinstance(v, str) and v != '':
            #     prompts.append(v)
            prompts.append(v)

        return (prompts, prompts)
#promptList NAIv4preの仕様によりマックス6で設定
class NAIcharaPositions:
    @classmethod
    def INPUT_TYPES(s):
        return {"optional": {
            "Position":("BOOLEAN",{"default": False, "label_on": "ON", "label_off": "OFF"}, ),
            "Position_1_x": ("INT", {"default": 5,"min": 1, "max": 9, "step": 2,}),
            "Position_1_y": ("INT", {"default": 5,"min": 1, "max": 9, "step": 2,}),
            "Position_2_x": ("INT", {"default": 5,"min": 1, "max": 9, "step": 2,}),
            "Position_2_y": ("INT", {"default": 5,"min": 1, "max": 9, "step": 2,}),
            "Position_3_x": ("INT", {"default": 5,"min": 1, "max": 9, "step": 2,}),
            "Position_3_y": ("INT", {"default": 5,"min": 1, "max": 9, "step": 2,}),
            "Position_4_x": ("INT", {"default": 5,"min": 1, "max": 9, "step": 2,}),
            "Position_4_y": ("INT", {"default": 5,"min": 1, "max": 9, "step": 2,}),
            "Position_5_x": ("INT", {"default": 5,"min": 1, "max": 9, "step": 2,}),
            "Position_5_y": ("INT", {"default": 5,"min": 1, "max": 9, "step": 2,}),
            "Position_6_x": ("INT", {"default": 5,"min": 1, "max": 9, "step": 2,}),
            "Position_6_y": ("INT", {"default": 5,"min": 1, "max": 9, "step": 2,}),


        },
            # "optional": {
            #     "optional_prompt_list": ("LIST",)
            # }
        }

    RETURN_TYPES = ("BOOLEAN", "LIST")
    # RETURN_NAMES = ("prompt_list", "prompt_strings")
    # OUTPUT_IS_LIST = (False, True)
    FUNCTION = "run"
    CATEGORY = "jisaku"

    def run(self,Position,Position_1_x,Position_1_y,Position_2_x,Position_2_y,Position_3_x,Position_3_y,Position_4_x,Position_4_y,Position_5_x,Position_5_y,Position_6_x,Position_6_y):
        if Position:
                
            charp = [Position_1_x/10,Position_1_y/10],[Position_2_x/10,Position_2_y/10],[Position_3_x/10,Position_3_y/10],[Position_4_x/10,Position_4_y/10],[Position_5_x/10,Position_5_y/10],[Position_6_x/10,Position_6_y/10]

        else:
            charp = [[0.5,0.5],[0.5,0.5],[0.5,0.5],[0.5,0.5],[0.5,0.5],[0.5,0.5]]

        return (Position, charp)


# NAIのPostdadaを分解してEagleへ送信するデータにする
class NAIPostdataToString:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {
                        "PostJsondata": ("STRING",{"forceInput": False,}),
                    }

        }

    RETURN_TYPES = ("STRING","STRING","STRING",)
    RETURN_NAMES = ("Positive", "Negative","Setting")
    # OUTPUT_IS_LIST = (False, True)
    FUNCTION = "run"
    CATEGORY = "jisaku"

    def run(self,PostJsondata):

        data = json.loads(PostJsondata)
         # 必要な項目を取得
        base_positive = data.get("input", "N/A")
        model_value = data.get("model", "N/A")
        parameters = data.get("parameters", {})
        
        # parameters内の特定の値を取得
        width = parameters.get("width", "N/A")
        height = parameters.get("height", "N/A")
        steps = parameters.get("steps", "N/A")
        seed = parameters.get("seed", "N/A")
        scale = parameters.get("scale","N/A")
        base_negative = parameters.get("negative_prompt", "N/A")
        sampler = parameters.get("sampler","N/A")
        noise_schedule = parameters.get("noise_schedule","N/A")
        # CFG関係のオプションが設定されている場合取得
        optional_settings =''
        dynamic_thresholding = parameters.get("","N/A") #基本false
        cfg_rescale = parameters.get("cfg_rescale", 0) #基本0
        skip_cfg_above_sigma = parameters.get("skip_cfg_above_sigma",0) #基本0
        if dynamic_thresholding == True:
            optional_settings = optional_settings + "dynamic_thresholding:True "
        if cfg_rescale != 0:
            optional_settings = optional_settings + f"cfg_rescale: {cfg_rescale} "
        if skip_cfg_above_sigma != 0:
            optional_settings = optional_settings + f"skip_cfg_above_sigma: {skip_cfg_above_sigma} "

        # characterPromptsを取得
        character_prompts = parameters.get("characterPrompts", [])
        character_prompts_str = ''
        if parameters.get('use_coords','N/A') == True:
            for i, char_prompt in enumerate(character_prompts, 1):
                prompt = char_prompt.get("prompt", "N/A")
                uc = char_prompt.get("uc", "N/A")
                center = char_prompt.get("center", {})
                x = center.get("x", "N/A")
                y = center.get("y", "N/A")
                character_prompts_str = character_prompts_str + f'\nChara{i} Pos: {prompt} UC: {uc} Center: ({x},{y})'
        else:
            for i, char_prompt in enumerate(character_prompts, 1):
                prompt = char_prompt.get("prompt", "N/A")
                uc = char_prompt.get("uc", "N/A")
                character_prompts_str = character_prompts_str + f'\nChara{i} Pos: {prompt} UC: {uc} Center:None'

        settings =f'Model:{model_value} size:{width}x{height} Steps:{steps} CFG:{scale} Seed:{seed} sampler:{sampler} {noise_schedule}\n{optional_settings}\n{character_prompts_str}'


        return(base_positive,base_negative,settings,)


NODE_CLASS_MAPPINGS = {
    #aaaaaはclass名 "bbbbb": aaaaa,
    "DelayNode": DelayNode,
    "NAIpromptList":NAIpromptList,
    "NAIPositions":NAIcharaPositions,
    "NAIPostdata2string":NAIPostdataToString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # "bbbbb": "ccccc",
    "DelayNode":"DelayNode",
    "NAIpromptList":"NAIキャラプロンプトリスト",
    "NAIPositions":"NAIキャラポジション",
    "NAIPostdata2string":"NAIPostData分解",
}
