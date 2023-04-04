import pandas as pd
import openai
import time

def gptclassifier(df, messages, completions, timer_frequency):

    i=0    
    for txt in df.loc[:,["caption","username"]].iterrows():
        
        # timer
        i+=1
        if i%timer_frequency==1:
            print(f"Counter at {i}")

        messages.append(
                {"role": "user", "content": f"Post: '{txt[1]['caption']}'. User: @{txt[1]['username']}"})
        
        # try except to prevent openAIs limits
        try:
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                messages=messages)
            completions.append(response["choices"][0]["message"]["content"])
        except Exception as err:
            print("Waiting for 65s", err.__class__.__name__)
            time.sleep(65)
            try:
                response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                    messages=messages)
                completions.append(response["choices"][0]["message"]["content"])
            except Exception as err:
                print("Waiting for 65s again", err.__class__.__name__)
                time.sleep(65)
                response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                    messages=messages)
                completions.append(response["choices"][0]["message"]["content"])
        
        messages.pop()
                

    four_labels = ["Likely sponsored." if ((response.endswith("ly sponsored."))
                                   or (response.endswith("ly sponsored")))
                          else "Self advertisement." if ((response.endswith("lf advertisement.")) or (response.endswith("lf advertisement")))
                          else "Ambiguous." if ((response.endswith("Ambiguous."))
                                         or (response.endswith("Ambiguous")))
                          else "Likely not sponsored." if ((response.endswith("not sponsored.")) or (response.endswith("not sponsored")))
                          else response for response in completions]
    return completions, four_labels