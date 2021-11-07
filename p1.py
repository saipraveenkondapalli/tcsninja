key = input()
keys = ['break', 'case', 'continue','default', 'defer', 'else', 'for','func', 'goto','if','map', 'range','return','struct','type','var' ]

if key in keys:
    print(f"{key} is a keyword")
else:
    print(f"{key} is not a keyword")
