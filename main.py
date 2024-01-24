import pickle
var = input("Please enter the news text you want to verify: ")
load_model = pickle.load(open('final_model.sav', 'rb'))
prediction = load_model.predict([var])
print("The given statement is ", prediction[0])