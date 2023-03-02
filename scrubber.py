from pprint import pprint

file = open(input("file path: "), "rt")

dirs = []

dir = ""

end = True

for line in file.readlines():
    if line != "\n" and line != "" and line != " " and line != "\t" and line != "\r":
        if end:
            start_index = line.find("C:/")
            if start_index != -1:
                end_index = line.find(".cpp")
                if end_index == -1:
                    end_index = line.find(".h")
                if end_index != -1:
                    dir = line[start_index:end_index + 4].replace(" ", "").replace("\"", "").replace("\n", "")
                    if dir not in dirs:
                        dirs.append(dir)
                else:
                    dir = line[start_index:].replace(" ", "").replace("\"", "").replace("\n", "")
                    end = False
        else:
            end_index = line.find(".cpp")
            if end_index == -1:
                end_index = line.find(".h")
            if end_index != -1:
                dir += line[:end_index + 4].replace(" ", "").replace("\"", "").replace("\n", "")
                end = True
                if dir not in dirs:
                    dirs.append(dir)
            else:
                dir += line.replace(" ", "").replace("\"", "").replace("\n", "")

pprint(dirs)
