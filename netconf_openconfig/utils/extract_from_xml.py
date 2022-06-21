# pylint: disable=C0415
import xml.etree.ElementTree as etree


def get_all_components_from_xml(xml_str):
    root = etree.fromstring(xml_str)
    # components
    #    print(root[0][0])
    #    print(root[0][0].tag)
    #    print(root[0][0].text)
    #    print(root[0][0].attrib)
    #    print(root[0][0][0][1].tag)
    print("--------------------")

    for item_i in range(len(root[0][0])):  # parsing de tous les component
        print("component ")
        for item_j in range(len(root[0][0][item_i])):  # parsing d'un component
            print(". ", root[0][0][item_i][item_j].tag, " ", root[0][0][item_i][item_j].text)
            for item_k in range(len(root[0][0][item_i][item_j])):
                print(".. ", root[0][0][item_i][item_j][item_k].tag, " ", root[0][0][item_i][item_j][item_k].text)
                for item_l in range(len(root[0][0][item_i][item_j][item_k])):
                    print("... ", root[0][0][item_i][item_j][item_k][item_l].tag, " ",
                          root[0][0][item_i][item_j][item_k][item_l].text)
                    for item_m in range(len(root[0][0][item_i][item_j][item_k][item_l])):
                        print(".... ", root[0][0][item_i][item_j][item_k][item_l][item_m].tag, " ",
                              root[0][0][item_i][item_j][item_k][item_l][item_m].text)

#        for j in range(len(root[0][0][i])):
#            print("--- component name : ", root[0][0][i][j].text)
#            label = root[0][0][i][j].tag
#            if label == 'name':
#                component[i].append(root[0][0][i][j].text)
#            else:
#                if label == 'subcomponents':
#                    for k in range(len(root[0][0][i][j])):
#                        label2 = root[0][0][i][j][k].tag
#                        if label2 == 'name':
#                            component[i].append(root[0][0][i][j][k].text)

#    print("component", component)

#    print(root[0][0][0].tag)
#    print(root[0][0][0].text)
#    print(root[0][0][0].attrib)
# name
#    print(root[0][0][0][0].tag)
#    print(root[0][0][0][0].text)
#    print(root[0][0][0][0].attrib)
# config
#    print(root[0][0][0][1].tag)
#    print(root[0][0][0][1].text)
#    print(root[0][0][0][1].attrib)
# subcomponents
#    print(root[0][0][1][2].tag)
#    print(root[0][0][1][2].text)
#    print(root[0][0][1][2].attrib)
