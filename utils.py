def remove_item(datas):
    if type(datas) == type([]):
        for data in datas:
            remove_item(data)
    if type(datas) == type({}):
        if datas.has_key('TotalCost'):
            datas.pop('TotalCost')
        if datas.has_key('StartupCost'):
            datas.pop('StartupCost')
        if datas.has_key('PlanRows'):
            datas.pop('PlanRows')
        if datas.has_key('PlanWidth'):
            datas.pop('PlanWidth')
        if datas.has_key('Plan'):
            remove_item(datas['Plan'])
        if datas.has_key('Plans'):
            remove_item(datas['Plans'])
        if datas.has_key('IndexCond'):
            remove_item(datas['IndexCond'])
        if datas.has_key('Filter'):
            remove_item(datas['Filter'])
