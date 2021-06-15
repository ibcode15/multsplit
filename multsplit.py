from uuid import uuid4

def Multsplit(string: str, items_of_split: list, Return: type = list, Mapping: dict = {}):
    if len(items_of_split) == 1:
        return "need more than one item for splitting"
    elif len(items_of_split) == 0:
        return "items_of_split is empty"
    else:
        replace = str(uuid4()) + str(uuid4()) + str(uuid4()) + str(uuid4())
        for x in range(len(items_of_split)):
            if items_of_split[x] in Mapping.keys():
                string = string.replace(items_of_split[x],Mapping[items_of_split[x]])
            else:
                string = string.replace(items_of_split[x],replace)
        string = string.split(replace)
        if Return == list:
            return string
        elif Return == str:
            return "".join(string)
        else:
            return "cannot find type"
