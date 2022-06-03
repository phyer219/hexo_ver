import os


path = './'


def ls_all(path):
    res = []
 #   print('---------', path)
    for f in os.listdir(path):
        f = path+f
        if not os.path.isdir(f):
  #          print('=======', f, os.path.isdir(f))
            res.append(f)
        else:
            res += ls_all(f+'/')
    return res


files = ls_all(path)
for f in files:
    print(f)
    if f != 'u.py' and f.endswith('.html'):
        new_content = ""
        with open(f, 'r', encoding="utf-8") as old_content:
            lines = old_content.readlines()
            print('======')
            for l in lines:
                l = l.replace("\'\\", "\'hexo_ver\\")
                l = l.replace("\"\\", "\"hexo_ver\\")
                new_content += l
        with open(f, 'w', encoding="utf-8") as old_content:
            old_content.write(new_content)
