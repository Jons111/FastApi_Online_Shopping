from math import ceil

def pageination(form,page,limit):
    return {"currentt_page":page,"limit":limit,"pages":ceil(form.count() /limit),"data":form.offset((page -1)*limit).limit(limit).all()}