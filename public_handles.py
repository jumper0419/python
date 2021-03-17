"""
这是“public_handles.py"模块， 提供公共方法处理的函数。
- handle_list()：这个函数的作用是为了输出列表中的元素，列表可以嵌套也可以不嵌套
"""


def handle_list(list_name, level=0, indent=False):
	'''
	:param list_name: 列表的名字
	:return:
	'''
	for item in list_name:
		if isinstance(item, list):
			handle_list(item, level=level+1, indent=indent)
		else:
			if indent:
				for tab_num in range(level):
					print("\t", end="")
			print(item)

