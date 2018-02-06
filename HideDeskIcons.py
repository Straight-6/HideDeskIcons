from win32gui import FindWindow, FindWindowEx, SendMessage

hWnd = FindWindowEx(0, 0, 'Progman', None)
hWnd = FindWindowEx(hWnd, 0, 'SHELLDLL_DefView', None)

SendMessage(hWnd, 0x0111, 0x7402, 0)
