import json
import csv


def export_csv(file_name, list_data):
    myFile = open("export_file/{}".format(file_name), 'w', newline="")
    with myFile:
        write = csv.writer(myFile)
        write.writerows(list_data)


# export_csv("grom.csv", mylist)
def import_csv(file_name):
    results = []
    with open(file_name, newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            results.append(row)
    return results


#data = import_csv("export_file/grom.csv")


def export_json(file_name, list_data):

    data = {}
    data['call_book'] = []
    for i in list_data:
        data['call_book'].append({
            'family': i[0],
            'name': i[1],
            'tel': i[2],
            'comment': i[3]
        })

    with open("export_file/{}".format(file_name), 'w') as outfile:
        json.dump(data, outfile)


# export_json("data.json", data)


def import_json(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        results = []
        for p in data['call_book']:
            results.append([p["family"], p["name"], p["tel"], p["comment"]])
    return results


#data_json = import_json("data.txt")

###########################


def search_contact(list_data, search_data):
    result = []
    result_all = []
    o = 0
    for i in list_data:
        for y in i:
            if y.lower() == search_data.lower():
                if not result:
                    result = list_data[o]
                else:
                    result_all.append(result)
                    result_all.append(list_data[o])
                    result = result_all
        o += 1
    return result


#search = search_contact(data, "mobile")
# print(search)
