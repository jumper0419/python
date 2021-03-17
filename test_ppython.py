import sys
print(sys.path)
import public_handles
list1 = ['aaaa', 123, 'bbb', ['ccc', 234, ['ddd'], 'eee'], 235, 'ggg']
public_handles.handle_list(list1)
public_handles.handle_list(list1, indent=True)