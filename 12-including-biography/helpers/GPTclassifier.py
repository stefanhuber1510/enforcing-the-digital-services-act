import pandas as pd
import openai
import time

def gptclassifier(df,base_messages,completions,timer_frequency=5):

    i=0    
    for txt in df.loc[:,["caption","username"]].iterrows():
        
        # timer
        i+=1
        if i%timer_frequency==2:
            print(f"Counter at {i}")

        messages = base_messages.copy()
        messages.append({"role": "user", "content": f"Post: '{txt[1]['caption']}'. User: @{txt[1]['username']}"})
        # try except to prevent openAIs limits
        try:
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                messages=messages)
            completions.append(response["choices"][0]["message"]["content"])
        except Exception as err:
            print("Waiting for 65s", err.__class__.__name__)
            print("-----------------")
            print(err)
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
    four_labels = [True if ((response.endswith("otentially sponsored"))
                                   or (response.endswith("otentially sponsored."))
                                   or (response.endswith("otentially Sponsored.")))
                          else False if ((response.endswith("ly not sponsored"))
                                         or (response.endswith("ly not sponsored."))
                                         or (response.endswith("leave blank as well")))
                          else 'Self adv' if ((response.endswith("lf advertisement"))
                                         or (response.endswith("lf advertisement."))
                                         or (response.endswith("leave blank as well")))
                          else 'Ambiguous' if ((response.endswith("biguous"))
                                         or (response.endswith("biguous."))
                                         or (response.endswith("leave blank as well")))
                          else response for response in results[0]]
    
    return completions, four_labels