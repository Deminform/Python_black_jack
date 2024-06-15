import shutil

logo = """
 ____  _            _     _            _    
| __ )| | __ _  ___| | __(_) __ _  ___| | __
|  _ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ /
| |_) | | (_| | (__|   < | | (_| | (__|   < 
|____/|_|\__,_|\___|_|\_\| |\__,_|\___|_|\_\\
                        /_/                 
    """

def print_centered(text):
    # Получаем ширину консоли
    terminal_width = shutil.get_terminal_size().columns
    
    # Разбиваем текст на строки
    lines = text.split('\n')
    
    for line in lines:
        # Вычисляем необходимое количество пробелов для центровки
        padding = (terminal_width - len(line)) // 2
        centered_line = ' ' * padding + line
        print(centered_line)