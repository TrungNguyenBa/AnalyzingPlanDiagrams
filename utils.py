def remove_item(datas):
    if type(datas) == type([]):
        for data in datas:
            remove_item(data)
    if type(datas) == type({}):
        if datas.get('TotalCost',0):
            datas.pop('TotalCost')
        if datas.get('StartupCost',0):
            datas.pop('StartupCost')
        if datas.get('PlanRows',0):
            datas.pop('PlanRows')
        if datas.get('PlanWidth',0):
            datas.pop('PlanWidth')
        if datas.get('Plan',0):
            remove_item(datas['Plan'])
        if datas.get('Plans',0):
            remove_item(datas['Plans'])
        if datas.get('IndexCond',0):
            datas.pop('IndexCond')
        if datas.get('Filter',0):
            datas.pop('Filter')
