import json
import os
# You can change input files path below
path = "xiaoxianruo_jsons"
files = os.listdir(path)
files.sort()

fileNum = 0

for file in files:
    with open(f"{path}/{file}") as input:
        os.makedirs(os.path.dirname(f"result/{file}"), exist_ok=True)
        
        # %05d means the number is a 5-digit integer.
        # You can change this number to %06d to get a 6-digit-numbered file name.
        output = open(f"result/%05d.txt" % fileNum, 'w')
        data = json.load(input)
        count = 0
        for item in data["people"][0]["pose_keypoints_2d"]:
            count += 1
            output.write(str(item)+' '),
            if (count % 3 == 0):
                output.write("\n")
    fileNum += 1

output.close()