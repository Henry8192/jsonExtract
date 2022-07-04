import json
import os
# You can change the path name here (which is your folder name)
path = "xiaoxianruo_jsons"
files = os.listdir(path)
files.sort()

fileNum = 0

for file in files:
    with open(f"{path}/{file}") as input:
        os.makedirs(os.path.dirname(f"result/{file}"), exist_ok=True)
        output = open(f"result/{fileNum}.txt", 'w')
        data = json.load(input)
        count = 0
        for item in data["people"][0]["pose_keypoints_2d"]:
            count += 1
            output.write(str(item)+' '),
            if (count % 3 == 0):
                output.write("\n")
    fileNum += 1

output.close()