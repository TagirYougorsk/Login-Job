from UserModels import ReadUserModel

def age_sort_asceding(buffer_list : list[ReadUserModel]) -> list[ReadUserModel]:
    buffer_list.sort(key=lambda user: user.age)
    return buffer_list

def age_sort_desceding(buffer_list : list[ReadUserModel]) -> list[ReadUserModel]:
    buffer_list.sort(key=lambda user: user.age, reverse=True)
    return buffer_list

def name_sort_asceding(buffer_list : list[ReadUserModel]) -> list[ReadUserModel]:
    buffer_list.sort(key=lambda user: user.name)
    return buffer_list

def name_sort_desceding(buffer_list : list[ReadUserModel]) -> list[ReadUserModel]:
    buffer_list.sort(key=lambda user: user.name, reverse=True)
    return buffer_list

def gender_filter(buffer_list : list[ReadUserModel],
                    value : str | None) -> list[ReadUserModel]:
    if value == None:
        return buffer_list
    
    if value.lower() not in ["мужской", "женский"]:
        raise Exception("Некорректный пол")
    
    buffer : list[ReadUserModel] = []
    for user in buffer_list:
        if(user.gender.lower() == value.lower()):
            buffer.append(user)
    return buffer

def search(buffer_list : list[ReadUserModel],value : str | None) -> list[ReadUserModel]:
    if value is None:
        return buffer_list
    
    buffer : list[ReadUserModel] = []
    for user in buffer_list:
        if value.lower() in user.name.lower() or value.lower() in user.surname.lower() or value.lower() in user.email.lower():
            buffer.append(user)
    return buffer

def pagination(buffer_list : list[ReadUserModel],
                size : int | None, 
                num : int | None) -> list[ReadUserModel]:
    if size is None or num is None:
        return buffer_list
    
    buffer : list[ReadUserModel] = []
    start_i : int = size * num
    for i in range(start_i,start_i + size):
        if(i >= len(buffer_list)):
            break
        user : ReadUserModel = buffer_list[i]
        buffer.append(user)
    return buffer

def sort(buffer_list : list[ReadUserModel],
        field : str | None = None, 
        sort_type : int | None = None) -> list[ReadUserModel]:
    if(field is None or sort_type is None):
        return buffer_list
    if(field == "name" and sort_type == 0):
        return name_sort_asceding(buffer_list)
    if(field == "name" and sort_type == 1):
        return name_sort_desceding(buffer_list)
    if(field == "age" and sort_type == 0):
        return age_sort_asceding(buffer_list)
    if(field == "age" and sort_type == 1):
        return age_sort_desceding(buffer_list)
    raise Exception("Неожиданная ошибка в сортировке")
    