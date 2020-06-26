def multsplit(str, items_of_split):
    if len(items_of_split) == 1:
        return "need more than one item for split"
    elif len(items_of_split) == 0:
        return "list is empty"
    else:
        try:
            for x in range(len(items_of_split)):
                str = str.replace(items_of_split[x],'œ')
            str = str.split('œ')
            return str
        except Exception as e:
            print(str(e))
        
