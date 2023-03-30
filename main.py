import menu
import tokenGen as tg
import sop

while(True):
    menu.displayMenu()
    selection = tg.ask("choose option","num")
    match(int(selection)):
        case 0:  sop.generateMeetingUpdate()
        case 2:  sop.generateBoldPoints()
        case 3:  sop.generateTicket()
        case 9:  sop.happenings()
        case 10: sop.quit()