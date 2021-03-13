import requests

# This function will pass your numbers to the machine learning model
# and return the top result with the highest confidence
def classify(numbers):
    key = "380ac9a0-839c-11eb-be59-6fb58e7091697c871dd4-e92c-4985-8d97-bd71a8c30878"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.post(url, json={ "data" : numbers })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
name = "Jack"   # your name
data1 = 1   # ticket class
data2 = "male" # gender
data3 = 20  # age
data4 = 1   # siblings
data5 = 2   # parent
data6 = 4   # ticket fare
data7 = "Cherbourg" # boarding location

demo = classify([ data1, data2, data3, data4, data5, data6, data7 ])

label = demo["class_name"]
confidence = demo["confidence"]

# CHANGE THIS to do something different with the result
print (f"--- {name} '%s' with %d%% confidence" % (label, confidence))