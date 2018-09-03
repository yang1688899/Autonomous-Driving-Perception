import config
import utils

def get_box_infos(annotations,label_dict):
    box_infos = []
    for anno in annotations:
        box_info = ""
        img_path = config.TRAINDIR + anno["name"]
        box_info += img_path
        for box_anno in anno["labels"]:
            if box_anno["category"] in config.LABEL_NAME:
                clas = box_anno["category"]
                label_id = label_dict[clas]
                x1 = box_anno["box2d"]["x1"]
                y1 = box_anno["box2d"]["y1"]
                x2 = box_anno["box2d"]["x2"]
                y2 = box_anno["box2d"]["y2"]
                box_info += " %s,%s,%s,%s,%s" % (x1,y1,x2,y2,label_id)
        box_info += "\n"
        box_infos.append(box_info)
    return box_infos

def write_file(box_infos,filepath):
    with open(filepath,"w") as file:
        file.writelines(box_infos)


label_dict = {}
for i,label in enumerate(config.LABEL_NAME):
    label_dict[label] = i
annotations = utils.load_annotation(config.VALID_LABEL_FILE)

box_infos = get_box_infos(annotations,label_dict)

write_file(box_infos,"./val.txt")