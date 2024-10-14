def noteEntity(item)->dict:
    return{
        "_id":str(item["_id"]),
        "title":item["title"],
        "note":item["note"]

    }

def notesEntity(items)->list:
    return [noteEntity(item) for item in items]