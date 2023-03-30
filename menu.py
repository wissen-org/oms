import utilities
import jsonController


## CONSTANTS
FONT1 = "courier-sans"
FONT2 = "bold-aerial"
FONT3 = ""


def displayMenu():
    print("🤝 𝔚𝔢𝔩𝔠𝔬𝔪𝔢 𝔱𝔬 𝕾𝖙𝖚𝖉𝖊𝖓𝖙 𝕺𝖗𝖌𝖆𝖓𝖎𝖟𝖆𝖙𝖎𝖔𝖓, 𝖂𝖎𝖘𝖘𝖊𝖓 𝕸𝖆𝖓𝖆𝖌𝖊𝖒𝖊𝖓𝖙 𝕾𝖔𝖋𝖙𝖜𝖆𝖗𝖊")
    menuList = jsonController.getMenuList()
    for i in range(0,len(menuList)):
        print("🔸",utilities.changeFont(str(i),FONT2),utilities.changeFont(menuList[i],FONT1),end="\n")



def displayTageeMenu():
    pass