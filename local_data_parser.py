import local_data  # Import the module you are interested in
import inspect
import pandas as pd
import json

# List to hold names of variables
variable_names = []
answers=[]
questions=[]
topic=[]
s=local_data
for name in dir(s):
    if not name.startswith('__'):
        attribute = getattr(s, name)
        if not inspect.ismodule(attribute):
            variable_names.append(name)
            if name.startswith("answer"):
                answers.append(name)
            elif name.startswith("question"):
                questions.append(name)
            else:
                topic.append(name)


# print(answers,questions,topic)
# print(getattr)
# a=getattr(local_data,answers[0])
# print(a)
                
data={
        "Topic":[getattr(local_data,i) for i in topic],
        "Question":[getattr(local_data,i) for i in questions],
        "Answer":[getattr(local_data,i) for i in answers]
      }

def formating_prompt(data):
    fmrt="<s>[INST] {} {} [/INST] {} </s>".format(data[0],data[1],data[2]).replace("\"","'")
    return {"text":fmrt}
l=""
for i in range(len(topic)):
    a=formating_prompt([data["Topic"][i],data["Question"][i],data["Answer"][i]])
    dt=json.dumps(a)+"\n"
    l+=dt
# print(l)
f=open("HDiagPro.jsonl","w")
f.write(l)




    


