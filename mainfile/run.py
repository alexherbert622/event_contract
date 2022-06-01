import os
import pytest


if __name__ == '__main__':
    pytest.main(['--alluredir', './reports'])
    os.system('allure generate ./reports -o ./reports/html')
