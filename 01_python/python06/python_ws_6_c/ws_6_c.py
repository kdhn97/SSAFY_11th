data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
# data를 순회한다
for item in data:
    # print(item['name'], key)
    # 순회중인 key로 조회해봤을 때, 해당하는 키가 없다면(None)
    for key in key_list:
        if data.get(key) == None:
            item.setdefault(key, 'uknown')
        print(f'{key}은/는 {item[key]}입니다')
    # item 하나하나마다 공백으로 구분
    print()