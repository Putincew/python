from jinja2 import Environment, FileSystemLoader
tit = 'Домашнее задание'
page = 'Страница с домашним заданием'
compl = 'домашнее задание выполнено'


file_loader=FileSystemLoader('template')
env=Environment(loader=file_loader)
tm=env.get_template('main.html')
msg=tm.render(tit=tit, page=page, compl=compl)
print(msg)
