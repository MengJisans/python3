#!/usr/bin/python3

a = [1,4,2,3,1]
sorted(a,reverse=True)

a = [{'name':'xiaoming','age':18,'gender':'male'},
       {'name':'xiaohong','age':20,'gender':'female'}]
#按 age升序
sorted(a,key=lambda x: x['age'],reverse=False)