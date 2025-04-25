Products = ["Laptop","Telephone","Robot hoover"]

Robots_hoover = ["ECOVACS","IROBOT"]
Telephones = ["Samsung","Apple"]
Laptops = ["ASUS","Mac"]

Apple_telefons = ["iPhone 15 Max", "iPhone 15 ultra"]
Samsung_telefons = ["Galaxy s25 ultra", "Z flip 6"]

Robots_hoover_ECOVACS = ["Deebot Y1 Pro","Deebot N20 Pro"]
Robots_hoover_IROBOT = ["Roomba i7", "iRobot Roomba"]

Laptops_ASUS = ["Zenbook", "Zenbook Duo"]
Laptops_Mac = ["MacBook", "MacBook Pro"]

choice = input('Что вы хотите ' + Products)

if choice == "Laptop":
    choice_of_laptop_marks = input('ввидите марку из' + Laptops)
    if choice_of_laptop_marks == "Laptop":
        print("вы выбрали" + choice_of_laptop_marks)

if choice == "Telephone":
    choice_of_telephones_marks = input('ввидите марку из' + Telephones)
    if choice_of_telephones_marks == "Laptop":
        print("вы выбрали" + choice_of_telephones_marks)

if choice == "Robot hoover":
    choice_of_robot_hoover_marks = input('ввидите марку из' + Robots_hoover)
    if choice_of_robot_hoover_marks == "Laptop":
        print("вы выбрали" + choice_of_robot_hoover_marks)