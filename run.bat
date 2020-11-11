cd  D:\learn\pytestApi\tc
pytest  -sq --alluredir=..\report\tmp
allure generate  ..\report\tmp -o ..\report\report --clean