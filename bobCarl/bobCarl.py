
with open("actions.txt","r") as f:
    sentences =f.read()
dict_sentences={}
size = 42
fail = ""

for sentence in sentences.splitlines():
    actor,x,y,object=sentence.split()
    if actor == "Bob":
        if object in dict_sentences:
            dict_sentences[object]+=1
        else:
            if len(dict_sentences) == size:
                fail = "Bob"
                break
            else: 
                dict_sentences[object] = 1
    else:
        if object in dict_sentences:
            dict_sentences[object]-=1
            if dict_sentences[object] == 0:
                dict_sentences.pop(object)
        else:
            fail = "Carl"
            break


if fail == "":
    print("Saglikli bisekilde doldurduk")
else: 
    print(f"{fail} fail")