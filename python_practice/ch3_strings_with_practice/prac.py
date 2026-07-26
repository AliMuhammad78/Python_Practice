letter = """Dear <|NAME|>,
You are selected!
Date: <|DATE|>""" 

rep = letter.replace("<|NAME|>", "Harry")
rep = rep.replace("<|DATE|>", "6th June 2023")
print(rep)