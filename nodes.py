import time

# class aaaaa:
#     @classmethod
#     def INPUT_TYPES(s):
#         return {"required":
#                     {
#                         "myINT": ("INT",{"forceInput": False,"default":10}),
#                         "anything" : ("*", {}),

#                     }
#                 }

#     RETURN_TYPES = ("INT",)
#     FUNCTION = "go"
#     CATEGORY = "test"

#     def go(self, myINT):
#         time.sleep(10)
#         return myINT

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
            "Position_1_x": ("FLOAT", {"default": 0.5,"min": 0.1, "max": 0.9, "step": 0.2,}),
            "Position_1_y": ("FLOAT", {"default": 0.5,"min": 0.1, "max": 0.9, "step": 0.2,}),
            "Position_2_x": ("FLOAT", {"default": 0.5,"min": 0.1, "max": 0.9, "step": 0.2,}),
            "Position_2_y": ("FLOAT", {"default": 0.5,"min": 0.1, "max": 0.9, "step": 0.2,}),
            "Position_3_x": ("FLOAT", {"default": 0.5,"min": 0.1, "max": 0.9, "step": 0.2,}),
            "Position_3_y": ("FLOAT", {"default": 0.5,"min": 0.1, "max": 0.9, "step": 0.2,}),
            "Position_4_x": ("FLOAT", {"default": 0.5,"min": 0.1, "max": 0.9, "step": 0.2,}),
            "Position_4_y": ("FLOAT", {"default": 0.5,"min": 0.1, "max": 0.9, "step": 0.2,}),
            "Position_5_x": ("FLOAT", {"default": 0.5,"min": 0.1, "max": 0.9, "step": 0.2,}),
            "Position_5_y": ("FLOAT", {"default": 0.5,"min": 0.1, "max": 0.9, "step": 0.2,}),
            "Position_6_x": ("FLOAT", {"default": 0.5,"min": 0.1, "max": 0.9, "step": 0.2,}),
            "Position_6_y": ("FLOAT", {"default": 0.5,"min": 0.1, "max": 0.9, "step": 0.2,}),


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
                
            charp = [Position_1_x,Position_1_y],[Position_2_x,Position_2_y],[Position_3_x,Position_3_y],[Position_4_x,Position_4_y],[Position_5_x,Position_5_y],[Position_6_x,Position_6_y]

        else:
            charp = [[0.5,0.5],[0.5,0.5],[0.5,0.5],[0.5,0.5],[0.5,0.5],[0.5,0.5]]

        return (Position, charp)
NODE_CLASS_MAPPINGS = {
    # "bbbbb": aaaaa,
    "DelayNode": DelayNode,
    "NAIpromptList":NAIpromptList,
    "NAIPositions":NAIcharaPositions,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    # "bbbbb": "ccccc",
    "DelayNode":"DelayNode",
    "NAIpromptList":"NAIキャラプロンプトリスト",
    "NAIPositions":"NAIキャラポジション"
}

