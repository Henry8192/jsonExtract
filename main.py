import json
import os
path = "xiaoxianruo_jsons"
files = os.listdir(path)
for file in files:
    with open(f"{path}/{file}") as input:
        data = json.load(input)
        count = 0
        for item in data["people"][0]["pose_keypoints_2d"]:
            count += 1
            print(item, ' ', end=""),
            if (count % 3 == 0):
                print()

