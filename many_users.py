#!/usr/bin/env python
'''
@File      :many_users.py
@Copyright :luoming
@Date      :
@Desc      :
'''

user = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in user.items():
    print("\nUsername: "+username)
    full_name = user_info['first']+ " "+user_info['last']
    location = user_info['location']
    print("\nFull name: "+full_name.title())
    print("\nLocation: "+location.title())