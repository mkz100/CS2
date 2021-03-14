import requests

# This function will pass your numbers to the machine learning model
# and return the top result with the highest confidence
def classify(numbers):
    key = "9efac6e0-842a-11eb-94af-bda5504cb1aa450db379-2daf-4eb0-8f52-ca02bfba0dfc"
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
data1 = 3   # ticket class
data2 = "male" # gender
data3 = 20  # age
data4 = 0   # siblings
data5 = 0   # parent
data6 = 0   # ticket fare
data7 = "Cherbourg" # boarding location

demo = classify([ data1, data2, data3, data4, data5, data6, data7 ])

label = demo["class_name"]
confidence = demo["confidence"]

# CHANGE THIS to do something different with the result
print (f"--- {name} '%s' with %d%% confidence" % (label, confidence))