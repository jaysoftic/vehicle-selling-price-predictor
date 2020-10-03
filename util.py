import numpy as np
import pickle
import json

model = None
columns = None
vehicles = None

def load_artifacts():
    global model
    global columns
    # here we are going to load our artifacts

    with open("./artifacts/model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("./artifacts/columns.json", "r") as f:
        columns = json.load(f)["data_columns"]


def get_vehicles():
    load_artifacts()
    global vehicles
    vehicles = columns[8:]
    return vehicles

def predict_price(year, present_price, kms, owner, diesel, petrol, individual, manual, vehicle):
    try:
        vehicle_index = -1
        if vehicle != "800":
            vehicle_index = columns.index(vehicle)

        X_pred = np.zeros(len(columns))

        count = 0
        features = [year, present_price, kms, owner, diesel, petrol, individual, manual] # it's just for looping purpose

        for f in features:
            X_pred[count] = f
            count += 1

        if vehicle_index > 0:
            X_pred[vehicle_index] = 1

        result = model.predict([X_pred])[0]

        return result
    except:
        return 1

if __name__ == "__main__":
    load_artifacts()
    # print(predict_price(6, 9.54, 43000, 0, 1, 0, 0, 1, "sx4"))
    # print(get_vehicles())