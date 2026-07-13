import time

death_count = 0

def scary_pause(text, delay=0.5):
    print(f"\n{text}")
    time.sleep(delay)

def start_game():
    global death_count
    
    if death_count == 0:
        scary_pause("="*50)
        scary_pause("   ПРИКЛЮЧЕНИЕ В ЗАБРОШЕННОМ ЗАМКЕ ")
        scary_pause("="*50)
        scary_pause("\nВы стоите перед старым замком. Дверь приоткрыта...")
    elif death_count == 1:
        scary_pause("="*50)
        scary_pause("   ...СНОВА ЭТОТ ЗАМОК... ")
        scary_pause("="*50)
        scary_pause("\nВы снова здесь. Как вы сюда попали?..")
    elif death_count == 2:
        scary_pause("="*50)
        scary_pause("   ОПЯТЬ... ОПЯТЬ... ОПЯТЬ... ")
        scary_pause("="*50)
        scary_pause("\nСтены шепчут ваше имя. Вы не можете уйти.")
    else:
        scary_pause("="*50)
        scary_pause("   БЕЗЫСХОДНОСТЬ ")
        scary_pause("="*50)
        scary_pause("\nЗамок жив. Он питается лишь Вами.")
    
    scary_pause("\nЧто делать?")
    scary_pause("  1 - Войти")
    scary_pause("  2 - Уйти (попытаться...)")
    
    choice = input("\nВаш выбор (1-2): ").strip()
    
    if choice in ["1", "войти"]:
        enter_castle()
    elif choice in ["2", "уйти"]:
        if death_count >= 2:
            scary_pause("\nВы бежите, но дорога ведет обратно к замку...")
            scary_pause("Вы снова стоите перед дверью.")
            time.sleep(1)
            enter_castle()
        else:
            scary_pause("\nВы развернулись и пошли прочь...")
            scary_pause("Но через час снова оказались у ворот замка.")
            death_count += 1
            time.sleep(1)
            enter_castle()
    else:
        scary_pause("\nТемнота поглотила вас...")
        death_count += 1
        time.sleep(1)
        start_game()

def enter_castle():
    global death_count
    
    scary_pause("\nВы входите в замок. Дверь захлопнулась за спиной.")
    scary_pause("Темный коридор разветвляется...")
    scary_pause("Налево — запах крови. Направо — мертвая тишина.")
    
    scary_pause("\nКуда пойти?")
    scary_pause("  1 - Налево")
    scary_pause("  2 - Направо")
    
    choice = input("\nВаш выбор (1-2): ").strip()
    
    if choice in ["1", "налево"]:
        treasure_room()
    elif choice in ["2", "направо"]:
        staircase()
    else:
        scary_pause("\nТени схватили вас...")
        death_count += 1
        time.sleep(1)
        start_game()

def treasure_room():
    global death_count
    
    scary_pause("\nВы нашли комнату с потайным сундуком!")
    scary_pause("Но в углу что-то движется...")
    scary_pause("Кошка? Нет... это...")
    
    scary_pause("\nЧто сделать?")
    scary_pause("  1 - Взять сундук")
    scary_pause("  2 - Убежать")
    scary_pause("  3 - Открыть сундук")
    
    choice = input("\nВаш выбор (1-3): ").strip()
    
    if choice in ["1", "взять"]:
        scary_pause("\nСущество обернулось. У него нет лица.")
        scary_pause("Оно знает ваше имя.")
        scary_pause("ВЫ МЕРТВЫ.")
        death_count += 1
        time.sleep(1.5)
        start_game()
    elif choice in ["2", "убежать"]:
        scary_pause("\nВы бежите, но коридор ведет обратно...")
        if death_count >= 2:
            scary_pause("Вы понимаете - выхода нет.")
            scary_pause("ВЫ МЕРТВЫ.")
            death_count += 1
            time.sleep(1.5)
            start_game()
        else:
            scary_pause("Вы нашли другую дверь...")
            time.sleep(1)
            staircase()
    elif choice in ["3", "открыть"]:
        chest_ending()
    else:
        scary_pause("\nСущество поглотило вас.")
        death_count += 1
        time.sleep(1)
        start_game()

def chest_ending():
    global death_count
    
    scary_pause("\nВы подходите к сундуку и медленно открываете крышку...")
    time.sleep(1)
    scary_pause("Внутри лежит тело.")
    scary_pause("Ваше тело.")
    time.sleep(1)
    scary_pause("\nГлаза трупа резко открываются.")
    scary_pause("Они смотрят прямо на вас.")
    time.sleep(1)
    scary_pause("\nХолодные руки хватают вас за горло.")
    scary_pause("Вы пытаетесь кричать, но воздух не проходит...")
    time.sleep(1)
    scary_pause("Сознание угасает...")
    time.sleep(2)
    scary_pause("\n...")
    time.sleep(1)
    scary_pause("\nВы открываете глаза.")
    scary_pause("Темный сырой подвал.")
    scary_pause("Где-то вдалеке капает вода.")
    time.sleep(1)
    scary_pause("\nВы живы. Но надолго ли?")
    death_count += 1
    time.sleep(1.5)
    start_game()

def staircase():
    global death_count
    
    scary_pause("\nВы нашли лестницу вниз...")
    scary_pause("Оттуда доносится шепот: 'помоги-и... помоги-и-и мне...'")
    
    scary_pause("\nСпуститься?")
    scary_pause("  1 - Да, я за движ")
    scary_pause("  2 - Нет, вернуться")
    
    choice = input("\nВаш выбор (1-2): ").strip()
    
    if choice in ["1", "да"]:
        if death_count >= 3:
            scary_pause("\nВ подвале вы нашли... СЕБЯ?")
            scary_pause("Мертвеца. С такими же глазами.")
            scary_pause("ВЫ МЕРТВЫ.")
            time.sleep(2)
            scary_pause("\n...или нет?")
            time.sleep(1)
            death_count = 0
            start_game()
        else:
            scary_pause("\nВ подвале вы нашли выход!")
            scary_pause("Свет...")
            scary_pause("\nПОБЕДА! Вы сбежали из замка!")
            scary_pause("\n...но будете ли вы спать спокойно?")
    elif choice in ["2", "нет"]:
        scary_pause("\nВы повернули назад, однако... дверь исчезла.")
        scary_pause("Стены сжимаются...")
        scary_pause("ВЫ МЕРТВЫ.")
        death_count += 1
        time.sleep(1.5)
        start_game()
    else:
        scary_pause("\nЛестница обрушилась под вами.")
        death_count += 1
        time.sleep(1)
        start_game()

if __name__ == "__main__":
    start_game()
