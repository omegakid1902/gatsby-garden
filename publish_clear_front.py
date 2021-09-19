import os
import frontmatter
from shutil import copy
import os

for root, dirs, files in os.walk("./content/"):
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), encoding="utf8", mode="r") as f:
                lines = f.readlines()

            idxs = []
            new_front = []
            with open(os.path.join(root, file), encoding="utf8", mode="w") as f:
                for line_id in range(len(lines)):
                    if lines[line_id].startswith("---"): 
                        idxs.append(line_id)

                    if lines[line_id].startswith("title:"):
                        new_front.append("---\n")
                        new_front.append(lines[line_id])
                        new_front.append("---\n")
                        
                start = 0
                if len(idxs) > 1 and idxs[0] == 0:
                    start = idxs[1] + 1
                
                for i in new_front:
                    f.write(i)

                for i in range(start, len(lines)):
                    f.write(lines[i])
