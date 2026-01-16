def NULL_not_found(object: any) -> int:
    obj_type = type(object)

    if object is None:
        print(f"Nothing: None {obj_type}")
        return 0
    elif obj_type == float and object != object:
        print(f"Cheese: nan {obj_type}")
        return 0
    elif obj_type == bool:
        print(f"Fake: {object} {obj_type}")
        return 0
    elif obj_type == int:
        print(f"Zero: {object} {obj_type}")
        return 0
    elif obj_type == str and object == "":
        print(f"Empty: {obj_type}")
        return 0
    else:
        print("Type not Found")
        return 1
