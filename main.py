import json
with open('xiaoxianruo_jsons/xiaoxianruo_0_00000_keypoints.json') as input:
    data = json.load(input)
    count = 0
    for item in data["people"][0]["pose_keypoints_2d"]:
        count += 1
        print(item, ' ',end = ""),
        if (count % 3 == 0):
            print()