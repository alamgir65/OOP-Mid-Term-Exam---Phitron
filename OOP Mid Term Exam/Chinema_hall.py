class Star_chinema:
    __hall_list = []
    # def __init__(self) -> None:
    #     pass
    def entry_hall(self,hall_details):
        self.__hall_list.append(hall_details)
    
class Hall(Star_chinema):
    def __init__(self,row,col,hall_no) -> None:
        self.__row = row
        self.__col = col
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        super().entry_hall(self)
    
    def entryShow(self,movie_name,id,time):
        movieTPl = (movie_name ,id,time)
        self.__show_list.append(movieTPl)
        seat = []
        for i in range(self.__row):
            tmpSeat = []
            for j in range(self.__col):
                tmpSeat.append('.')
            seat.append(tmpSeat)
        self.__seats[id]=seat
        
    
    def book_Seats(self,show_id,show_seats):
        if show_id not in self.__seats:
            print("THERE IS NO SEAT WITH THIS ID")
            return
        
        for show_seat in (show_seats):
            if (show_seat[0]<0 or show_seat[0]>= self.__row) or (show_seat[1]<0 or show_seat[1]>=self.__col):
                print("THE SEAT NUMBER IS INVALID")
            elif self.__seats[show_id][show_seat[0]][show_seat[1]] == '#':
                print("THIS SEAT IS ALREADY BOOKED")
            else:
                print("SEAT BOOKING SUCCESSFULL")
                self.__seats[show_id][show_seat[0]][show_seat[1]] = '#'
    
    
    def view_show_list(self):
        print("SHOW LIST IS : ")
        
        for x in self.__show_list:
            print(f"MOVIE NAME: {x[0]},SHOW ID: {x[1]},TIME: {x[2]}")
    
    
    def view_available_seats(self,id):
        if id not in self.__seats:
            print("THIS MOVIE ID IS INVALID")
            return -1
        cnt = 0
        print("'.' INDICATE THIS SEAT STILL AVAILABLE : ")
        for i,row in enumerate(self.__seats[id]):
            for j,col in enumerate(row):
                if col=='.':
                    cnt += 1
                if j==0 :
                    print("[",col,end=' ')
                elif j == len(self.__seats[id])-1 :
                    print(col,"]")
                else:
                    print(f'{col}',end=' ')
            # print()
        return cnt
                        
                    
    
    
SonyHall = Hall(10,10,1)
SonyHall.entryShow('JAWAN','100','16/02/24 FRIDAY 8:00 AM')
SonyHall.entryShow('PUSHPA','101','15/02/24 FRIDAY 8:00 AM')
SonyHall.entryShow('TIGER','102','17/02/24 FRIDAY 8:00 AM')
SonyHall.entryShow('LEO','103','06/02/24 FRIDAY 8:00 AM')
SonyHall.entryShow('BIJAY','104','26/03/24 FRIDAY 8:00 AM')


while True:
    print("CHOOSE YOUR OPTION : ")
    print()
    print("Option 1: VIEW ALL RUNNING SHOW.")
    print("Option 2: VIEW AVAILABLE SEATS.")
    print("Option 3: BOOK TICKET.")
    print("Option 4: Exit.")
    print()
    option = int(input("ENTER YOUR OPTION : "))
    
    if option == 1:
        SonyHall.view_show_list()
    elif option == 2:
        id = input("ENTER SHOW ID : ")
        ans = SonyHall.view_available_seats(id)
        print(f"NUMBER OF TOTAL AVAILABLE SEAT: {ans}")
    elif option == 3:
        id = input("ENTER SHOW ID : ")
        FreeSeat = SonyHall.view_available_seats(id)
        
        if FreeSeat == -1:
            print("INVALID SHOW ID")
        else:
            seats = []
            number = int(input("Number of Ticket : "))
            
            if number > FreeSeat:
                print(f"{number} of seat not available")
                continue
            
            for _ in range(number):
                s_row = int(input("ENTER SEAT ROW : "))
                s_col = int(input("ENTER SEAT COLUM : "))
                s_col -= 1
                s_row -= 1
                # print()
                seat = (s_row,s_col)
                seats.append(seat)
            SonyHall.book_Seats(id,seats)
    elif option == 4:
        break
    else:
        print("INVALID OPTION")
        break