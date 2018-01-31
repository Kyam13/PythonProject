PASSWORDS = {'email':'F7alksjdfajoew',
            'blog':'a;lkjfanoewnflkasngflaw',
            'luggale':'12345'
            }

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方：python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

account = sys.argv[1]#最初のコマンドライン引数がアカウント名

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをクリップボードにコピーしました')
else:
    print(account+'というパスワードはありません')
