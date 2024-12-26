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
            if isinstance(v, str) and v != '':
                prompts.append(v)

        return (prompts, prompts)

NODE_CLASS_MAPPINGS = {
    # "bbbbb": aaaaa,
    "DelayNode": DelayNode,
    "NAIpromptList":NAIpromptList,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    # "bbbbb": "ccccc",
    "DelayNode":"DelayNode",
    "NAIpromptList":"NAIキャラプロンプトリスト",
}

