def GetInput(Input):
    Var = input(Input).rstrip()
    if Var == '':
        return GetInput(Input)
    else:
        return Var

def Continue():     #Function to ask if the user wants to retry input
    Var = input('Do you want to continue? (Yes / No): ').rstrip()
    if Var.capitalize() == 'Yes':
        return True
    elif Var.capitalize() == 'No':
        return False
    elif Var == '':
        print('\n')
        return Continue()
    else:
        print('Please enter Yes / No!\n')
        return Continue()

def Confirm(Input, Action, Variable):
    print(f'__________________________________________________________________________________\n')

    for i in Input[::2]:
        Var = ''
        for j in range(40- len(i)):
            Var += ' '
        print(f'            {i}{Var}:{Input[Input.index(i) + 1]}')

    print('\n__________________________________________________________________________________\n')
    Var = input(f'Are you sure you want to {Action} the following {Variable}? (Yes/No): ').rstrip()

    if Var.capitalize() == 'Yes':
        return True
    elif Var.capitalize() == 'No':
        return False
    elif Var == '':
        print('\n')
        return Confirm(Input, Action, Variable)
    else:
        print('Please enter Yes / No!\n')
        return Confirm(Input, Action, Variable)

def Integer(Quantity):
    Var = input(f'Please enter the {Quantity}: ').rstrip()
    if Var.isdigit():
        return Var
    elif Var == '':
        print('\n')
        return Integer(Quantity)
    else:
        print('Please enter an integer!\n')
        return Integer(Quantity)

def Check(Variable, File, Action = ''):
    Var = input(f'Please enter the {Variable} {Action}: ').rstrip()
    if Var == '':
        print('\n')
        return Check(Variable, File, Action)
    else:
        if 'txt' in File:
            for i in ReadFile(File):
                if Var == i[0]:
                    return Var
        else:
            for i in File:
                if Var == i[0]:
                    return Var
        print(f'{Var} is not an available {Variable}!\n')
        return Check(Variable, File, Action)

def ReadFile(file):
    file = open(file, 'r')
    File = file.readlines()
    File = [line.strip().split() for line in File]
    file.close()
    for i in File:
        for j in i:
            if '_' in j:
                File[File.index(i)][File[File.index(i)].index(j)] = File[File.index(i)][File[File.index(i)].index(j)].replace('_', ' ')
    return File

def AppendFile(file, txt):
    for i in file:
        if ' ' in i:
            i = i.replace(' ', '_')
        File = open(txt, 'a')
        File.write(i)
        File.write(' ')
    File = open(txt, 'a')
    File.write('\n')
    File.close()

def InitializeConfirm(Variable, Value):
    Var = input(f'Are you sure there are {Value} {Variable}? (Yes/No): ').rstrip()
    if Var.capitalize() == 'Yes':
        return True
    elif Var.capitalize() == 'No':
        return False
    elif Var == '':
        print('\n')
        return InitializeConfirm(Variable, Value)
    else:
        print('Please enter Yes / No!\n')
        return InitializeConfirm(Variable, Value)

def ValueCheck(Condition, Max = 999):
    if Condition == 'Receive':
        Var = input('Please enter the number of PPE item that you received: ').rstrip()
        if Var.isdigit() and int(Var) > 0:
            return Var
        elif Var == '':
            print('\n')
            return ValueCheck(Condition)
        else:
            print(f'Please enter a positive integer!\n')
            return ValueCheck(Condition)

    elif Condition == 'Distribute':
        Var = input('Please enter the number of PPE item that you want to distribute: ').rstrip()
        if Var.isdigit() and int(Var) in range(1, Max + 1):
            return Var
        elif Var == '':
            print('\n')
            return ValueCheck(Condition, Max)
        else:
            print(f'Please enter an integer between 1 to {Max}!\n')
            return ValueCheck(Condition, Max)

def SortFile(List):
    for i in range(0, len(List)):
        for j in range(0, len(List) - i - 1):
            if List[j][0] > List[j + 1][0] or (List[j][0] == List[j + 1][0] and List[j][1] > List[j + 1][1]):
                Temp = List[j]
                List[j] = List[j + 1]
                List[j + 1] = Temp
    return List

def InitializeSuppliers():
    Var = Integer('number of suppliers')
    if InitializeConfirm('suppliers', Var) == True:
        Counter = 1
        while Counter - 1 != int(Var):
            List = SupplierDetails(Counter)
            if Confirm(List, 'append', 'supplier details') == True:
                AppendFile(List[1::2], 'Suppliers.txt')
                print('The details of the supplier are recorded!\n')
                Counter += 1
        print('All suppliers are recorded!\n')
    else:
        print('\n')
        InitializeSuppliers()

def SupplierDetails(Code):
    List = []
    List.append('Supplier Code')
    List.append('S0' + str(Code))
    print('\n')

    List.append('Supplier Company')
    List.append(GetInput('Please enter the supplier company: '))
    print('\n')

    List.append('Supplier Manager Name')
    List.append(GetInput('Please enter the supplier manager name: '))
    print('\n')

    List.append('Supplier Manager Contact Number')
    List.append(GetInput('Please enter the supplier manager contact number: '))
    print('\n')

    List.append('Supplier Location')
    List.append(GetInput('Please enter the supplier location: '))
    print('\n')
    return List

def InitializeHospitals():
    Var = Integer('number of hospitals')
    if InitializeConfirm('hospitals', Var) == True:
        Counter = 1
        while Counter - 1 != int(Var):
            List = HospitalDetails(Counter)
            if Confirm(List, 'append', 'hospital details') == True:
                AppendFile(List[1::2], 'Hospitals.txt')
                print('The details of the hospital are recorded!\n')
                Counter += 1
        print('All hospitals are recorded!\n')
    else:
        InitializeHospitals()

def HospitalDetails(Code):
    List = []
    List.append('Hospital Code')
    List.append('H0' + str(Code))
    print('\n')

    List.append('Hospital Company')
    List.append(GetInput('Please enter the hospital company: '))
    print('\n')

    List.append('Hospital Manager Name')
    List.append(GetInput('Please enter the hospital manager name: '))
    print('\n')

    List.append('Hospital Manager Contact Number')
    List.append(GetInput('Please enter the hospital manager contact number: '))
    print('\n')

    List.append('Hospital Location')
    List.append(GetInput('Please enter the hospital location: '))
    print('\n')
    return List

def InitializePPE():
    Var = Integer('number of PPE items')
    if InitializeConfirm('PPE items', Var) == True:
        Counter = 0
        while Counter != int(Var):
            List = PPEDetails()
            if Confirm(List, 'append', 'PPE details') == True:
                AppendFile(List[1::2], 'PPE.txt')
                print('The details of the PPE item are recorded!\n')
                Counter += 1
        print('All PPE items are recorded!\n')
    else:
        InitializePPE()

def PPEDetails():
    List = []
    List.append('Item Code')
    List.append(GetInput('Please enter the item code: '))
    print('\n')

    List.append('Item Name')
    List.append(GetInput('Please enter the item name: '))
    print('\n')

    List.append('Supplier Code')
    List.append(Check('supplier code', 'Suppliers.txt'))
    print('\n')

    List.append('Initial Quantity')
    List.append(GetInput('Please enter the initial quantity: '))
    print('\n')
    return List

def LoginUsername():
    Var = input('Please enter your username (type \'Exit\' to exit the system): ').rstrip()
    if Var.capitalize() == 'Exit':
        print('Exiting system!')
    elif Var in Admin:
        Counter = 3
        while Counter != 0:
            Status = LoginPassword(Var)
            if Status == True:
                print('Login successful!\n')
                Menu()
                break
            elif Status == False:
                Counter -= 1
                if Counter != 0:
                    print(f'You have {Counter} more attempts!\n')
                    if Continue() == False:
                        LoginUsername()
                        break
                else:
                    print('The maximum login attempts have been reached! Your account will be terminated!\n')
                    Admin.pop(Var)
                    LoginUsername()
    elif Var == '':
        print('\n')
        LoginUsername()
    else:
        print('The username is incorrect!\n')
        LoginUsername()

def LoginPassword(Username):
    Var = input('Please enter your password: ').rstrip()
    if Var == Admin[Username]:
        return True
    elif Var == '':
        print('\n')
        return LoginPassword(Username)
    else:
        return False

def Menu():
    print('''__________________________________________________________________________________\n    
                          Item Inventory Main Menu
            1) Update Details And Transactions
            2) Track PPE Items
            3) Search Distribution
            4) Display Report
            5) Log Out
\n__________________________________________________________________________________''')
    Var = input('Please enter the option that you want to proceed with (1 / 2 / 3 / 4 / 5): ').rstrip()

    if Var == '1':
        print('\n')
        Update()
    elif Var == '2':
        print('\n')
        Track()
    elif Var == '3':
        print('\n')
        Search()
    elif Var == '4':
        print('\n')
        Report()
    elif Var == '5':
        print('Logging Out!\n')
        LoginUsername()
    elif Var == '':
        print('\n')
        Menu()
    else:
        print('Please select the option between 1 to 5!\n')
        Menu()

def Update():   #Update Menu
    print('''__________________________________________________________________________________\n    
                          Item Inventory Update Menu
            1) Update Supplier Details
            2) Update Hospital Details
            3) Receive PPE Items from Supplier
            4) Distribute PPE Items to Hospital
            5) Return to Main Menu     
\n__________________________________________________________________________________''')
    Var = input('Please enter the option that you want to proceed with (1 / 2 / 3 / 4 / 5): ').rstrip()

    if Var == '1':
        print('\n')
        SupplierUpdate()
    elif Var == '2':
        print('\n')
        HospitalUpdate()
    elif Var == '3':
        print('\n')
        ReceiveItems()
    elif Var == '4':
        print('\n')
        DistributeItems()
    elif Var == '5':
        print('Returning to main menu!\n')
        Menu()
    elif Var == '':
        print('\n')
        return Update()
    else:
        print('Please select the option between 1 to 5!\n')
        return Update()

def SupplierUpdate():   #Update Supplier Details
    List = []

    File = ReadFile('Suppliers.txt')
    Count = 1
    print(f'''__________________________________________________________________________________\n
                                     Suppliers
    Supplier Code   Supplier Name   Manager Name    Manager Tel     Location''')

    for i in File:
        Var = Blank = ''
        for j in range(15 - len(File[File.index(i)][1])):
            Var += ' '
        for j in range(15 - len(File[File.index(i)][2])):
            Blank += ' '
        print(f'{Count})       {File[File.index(i)][0]}          {File[File.index(i)][1]}{Var} {File[File.index(i)][2]}{Blank}{File[File.index(i)][3]}    {File[File.index(i)][4]}')
        Count += 1

    print('\n__________________________________________________________________________________')

    List.append('Supplier Code')
    List.append(Check('supplier code', 'Suppliers.txt', 'to update'))
    print('\n')

    List.append('Supplier Company')
    List.append(GetInput('Please enter the supplier company to update to: '))
    print('\n')

    List.append('Supplier Manager Name')
    List.append(GetInput('Please enter the supplier manager name to update to: '))
    print('\n')

    List.append('Supplier Manager Contact Number')
    List.append(GetInput('Please enter the supplier manager contact number to update to: '))
    print('\n')

    List.append('Supplier Location')
    List.append(GetInput('Please enter the supplier location to update to: '))
    print('\n')

    if Confirm(List, 'update', 'supplier details') == True:
        for i in List[1::2]:
            if ' ' in i:
                List[List.index(i)] = List[List.index(i)].replace(' ', '_')

        for i in File:
            if i[0] == List[1]:
                File[File.index(i)] = List[1::2]

        open('Suppliers.txt', 'w').close()
        for i in File:
            AppendFile(i, 'Suppliers.txt')

        print('The details of the supplier are updated!')
    print('Returning to update menu!\n')
    Update()

def HospitalUpdate():
    List = []

    File = ReadFile('Hospitals.txt')
    Count = 1
    print(f'''__________________________________________________________________________________\n
                                     Hospitals
    Hospital Code   Hospital Name   Manager Name    Manager Tel     Location''')

    for i in File:
        Var = Blank = ''
        for j in range(15 - len(File[File.index(i)][1])):
            Var += ' '
        for j in range(15 - len(File[File.index(i)][2])):
            Blank += ' '
        print(f'{Count})       {File[File.index(i)][0]}          {File[File.index(i)][1]}{Var} {File[File.index(i)][2]}{Blank}{File[File.index(i)][3]}    {File[File.index(i)][4]}')
        Count += 1

    print('\n__________________________________________________________________________________')

    List.append('Hospital Code')
    List.append(Check('hospital code', 'Hospitals.txt', 'to update'))
    print('\n')

    List.append('Hospital Company')
    List.append(GetInput('Please enter the hospital company to update to: '))
    print('\n')

    List.append('Hospital Manager Name')
    List.append(GetInput('Please enter the hospital manager name to update to: '))
    print('\n')

    List.append('Hospital Manager Contact Number')
    List.append(GetInput('Please enter the hospital manager contact number to update to: '))
    print('\n')

    List.append('Hospital Location')
    List.append(GetInput('Please enter the hospital location to update to: '))
    print('\n')

    if Confirm(List, 'update', 'hospital details') == True:
        for i in List[1::2]:
            if ' ' in i:
                List[List.index(i)] = List[List.index(i)].replace(' ', '_')

        for i in File:
            if i[0] == List[1]:
                File[File.index(i)] = List[1::2]

        open('Hospitals.txt', 'w').close()
        for i in File:
            AppendFile(i, 'Hospitals.txt')

        print('The details of the hospitals are updated!')
    print('Returning to update menu!\n')
    Update()

def ReceiveItems():
    List = []
    Record = []

    File = ReadFile('Suppliers.txt')
    Count = 1
    print(f'''__________________________________________________________________________________\n
                               Suppliers
            Supplier Code                    Supplier Name''')

    for i in File:
        print(f'{Count})               {File[File.index(i)][0]}                           {File[File.index(i)][1]}')
        Count += 1

    print('\n__________________________________________________________________________________')

    List.append('Supplier Code')
    List.append(Check('supplier code', 'Suppliers.txt', 'to receive PPE items from'))
    print('\n')

    File = ReadFile('PPE.txt')
    for i in File:    #Append all available item code of the supplier code into Record
        if i[2] == List[1]:
            Record.append([i[0], i[1]])

    Count = 1
    print(f'''\n__________________________________________________________________________________\n
                           PPE Items
              Item Code                 Item Name''')

    for i in Record:
        print(f'{Count})               {i[0]}                    {i[1]}')
        Count += 1

    print('\n__________________________________________________________________________________\n')

    List.append('Item Code')
    List.append(Check('item code', Record, 'of the PPE item that you received'))
    print('\n')

    List.append('Quantity Received')
    List.append(ValueCheck('Receive'))
    print('\n')

    if Confirm(List, 'make', 'transaction') == True:
        List.append('Date')
        from datetime import date
        List.append(str(date.today()))

        AppendFile(List[1::2], 'Distribution.txt')

        open('PPE.txt', 'w').close()
        for i in File:  #Increment quantity of PPE item
            if i[0] == List[3]:
                i[3] = str(int(i[3]) + int(List[5]))
            AppendFile(i, 'PPE.txt')

        print('The transaction is successful!')
    print('Returning to update menu!\n')
    Update()

def DistributeItems():
    List = []

    File = ReadFile('Hospitals.txt')
    Count = 1
    print(f'''__________________________________________________________________________________\n
                               Hospitals
            Hospital Code                    Hospital Name''')

    for i in File:
        print(f'{Count})               {File[File.index(i)][0]}                           {File[File.index(i)][1]}')
        Count += 1

    print('\n__________________________________________________________________________________')

    List.append('Hospital Code')
    List.append(Check('hospital code', 'Hospitals.txt', 'to distribute PPE items to'))

    File = ReadFile('PPE.txt')
    Count = 1
    print('''\n__________________________________________________________________________________\n
                                    PPE Items
            Item Code               Item Name               Quantity''')

    for i in File:
        Var = ''
        for j in range(15 - len(File[File.index(i)][1])):
            Var += ' '
        print(f'{Count})             {File[File.index(i)][0]}                  {File[File.index(i)][1]}{Var}            {File[File.index(i)][3]}')
        Count += 1

    print('\n__________________________________________________________________________________')

    List.append('Item Code')
    List.append(Check('item code', 'PPE.txt', 'of the PPE item that you want to distribute'))
    print('\n')

    Var = ''
    for i in ReadFile('PPE.txt'):
        if i[0] == List[3]:
            Var = i[3]

    if Var == '0':
        print('There is no stock for the PPE item!')
        print('Please restock the PPE item to distribute!')
    else:
        List.append('Quantity Received')
        List.append(ValueCheck('Distribute', int(Var)))
        print('\n')

        if Confirm(List, 'make', 'transaction') == True:
            List.append('Date')
            from datetime import date
            List.append(str(date.today()))

            AppendFile(List[1::2], 'Distribution.txt')

            open('PPE.txt', 'w').close()
            for i in File:  # Decrement quantity of PPE item
                if i[0] == List[3]:
                    i[3] = str(int(i[3]) - int(List[5]))
                AppendFile(i, 'PPE.txt')

            print('The transaction is successful!')
    print('Returning to update menu!\n')
    Update()

def Track():    #Track Menu
    List = []
    print('''__________________________________________________________________________________\n
                        Item Inventory Tracking Menu
            1) Display all PPE Item\'s with their Quantity
            2) Display all PPE Item\'s that are low on stock (< 25 boxes)
            3) Return to Main Menu
\n__________________________________________________________________________________''')
    Var = input('Please enter the option that you want to proceed with (1 / 2 / 3): ').rstrip()

    if Var == '1':
        List = SortFile(ReadFile('PPE.txt'))
        Count = 1
        print('''\n__________________________________________________________________________________\n
                                  PPE Items
        Item Code        Item Name        Supplier Code       Quantity''')

        for i in List:
            Var = ''
            for j in range(15 - len(List[List.index(i)][1])):
                Var += ' '
            print(f'{Count})         {List[List.index(i)][0]}           {List[List.index(i)][1]}{Var}        {List[List.index(i)][2]}               {List[List.index(i)][3]}')
            Count += 1

        print('\n__________________________________________________________________________________')
        print('Returning to track menu!\n')
        Track()
    elif Var == '2':
        for i in SortFile(ReadFile('PPE.txt')):
            if int(i[3]) < 25:
                List.append(i)

        if List == []:
            print('There are no PPE items that has stock less than 25!\n')
        else:
            Count = 1
            print('''\n__________________________________________________________________________________\n
                        PPE Items With Stock Less Than 25
        Item Code        Item Name        Supplier Code       Quantity''')

            for i in List:
                Var = ''
                for j in range(15 - len(List[List.index(i)][1])):
                    Var += ' '
                print(f'{Count})         {List[List.index(i)][0]}           {List[List.index(i)][1]}{Var}        {List[List.index(i)][2]}               {List[List.index(i)][3]}')
                Count += 1

            print('\n__________________________________________________________________________________')
        print('Returning to track menu!\n')
        Track()
    elif Var == '3':
        print('Returning to main menu!\n')
        Menu()
    elif Var == '':
        print('\n')
        Track()
    else:
        print('Please select the option between 1 to 3!\n')
        Track()

def Search():
    List = []
    Record = []

    for i in ReadFile('PPE.txt'):
        List.append(i[0])
        List.append(i[1])

    Count = 1
    print(f'''__________________________________________________________________________________\n
                           PPE Items
              Item Code                 Item Name''')

    for i in List[::2]:
        print(f'{Count})               {List[List.index(i)]}                    {List[List.index(i) + 1]}')
        Count += 1

    print('\n__________________________________________________________________________________\n')

    List = []
    Var = Check('PPE item code', 'PPE.txt', 'that you want to search')
    for i in ReadFile('Distribution.txt'):
        if 'H' in i[0] and Var == i[1]:
            if i[0] + i[1] in Record:
                for j in List:
                    if i[0] == j[0] and i[1] == i[1]:
                        j[2] = str(int(j[2]) + int(i[2]))
            else:
                List.append([i[0], i[1], i[2]])
                Record.append(i[0] + i[1])

    for i in ReadFile('PPE.txt'):
        if Var == i[0]:
            Var = i[1]

    if List == []:
        print(f'There are no {Var.lower()}\'s distributed!')
    else:
        Count = 1
        print(f'''__________________________________________________________________________________\n
                        {Var} Distribution
            Hospital Code                Quantity''')

        for i in SortFile(List):
            print(f'{Count})               {List[List.index(i)][0]}                       {List[List.index(i)][2]}')
            Count += 1

        print('\n__________________________________________________________________________________')
    print('Returning to main menu!\n')
    Menu()

def Report():   #Report Menu
    print('''__________________________________________________________________________________\n
                        Item Inventory Report Menu
            1) Supplier Receive Report
            2) Hospital Distribution Report
            3) Overall Transaction Report for a Selected Month
            4) Return to Main Menu
\n__________________________________________________________________________________''')
    Var = input('Please enter the option that you want to proceed with (1 / 2 / 3 / 4): ').rstrip()

    if Var == '1':
        print('\n')
        SupplierReport()
    elif Var == '2':
        print('\n')
        HospitalReport()
    elif Var == '3':
        print('\n')
        OverallReport()
    elif Var == '4':
        print('Returning to main menu!\n')
        Menu()
    elif Var == '':
        print('\n')
        Report()
    else:
        print('Please select the option between 1 to 4!\n')
        Report()

def SupplierReport():
    List = []
    Record = []

    for i in ReadFile('Distribution.txt'):
        if 'S' in i[0]:
            if i[0] + i[1] in Record:
                for j in List:
                    if i[0] == j[0] and i[1] == i[1]:
                        j[2] = str(int(j[2]) + int(i[2]))
            else:
                List.append([i[0], i[1], i[2]])
                Record.append(i[0] + i[1])

    if List == []:
        print('There are no PPE items received from suppliers!')
    else:
        Count = 1
        print('''__________________________________________________________________________________\n
                           Supplier Receive Report
        Supplier Code             Item Code              Quantity''')

        for i in SortFile(List):
            print(f'{Count})           {List[List.index(i)][0]}                     {List[List.index(i)][1]}                    {List[List.index(i)][2]}')
            Count += 1

        print('\n__________________________________________________________________________________')
    print('Returning to report menu!\n')
    Report()

def HospitalReport():
    List = []
    Record = []

    for i in ReadFile('Distribution.txt'):
        if 'H' in i[0]:
            if i[0] + i[1] in Record:
                for j in List:
                    if i[0] == j[0] and i[1] == i[1]:
                        j[2] = str(int(j[2]) + int(i[2]))
            else:
                List.append([i[0], i[1], i[2]])
                Record.append(i[0] + i[1])

    if List == []:
        print('There are no PPE items distributed to hospitals!')
    else:
        Count = 1
        print('''__________________________________________________________________________________\n
                        Hospital Distribution Report
        Hospital Code             Item Code              Quantity''')

        for i in SortFile(List):
            print(f'{Count})           {List[List.index(i)][0]}                     {List[List.index(i)][1]}                    {List[List.index(i)][2]}')
            Count += 1

        print('\n__________________________________________________________________________________')
    print('Returning to report menu!\n')
    Report()

def OverallReport():
    List = []
    Record = []
    File = []

    for i in range(1, 13):
        File.append(str(i))
        from datetime import datetime
        File.append(datetime.strptime(str(i), '%m').strftime('%B'))
        File.append(datetime.strptime(str(i), '%m').strftime('%B').lower())

    Var = Check('month', File, 'of the report that you want to see')

    File = []
    for i in range(1, 13):
        File.append(str(i))

    if Var in File:
        from datetime import datetime
        Var = datetime.strptime(Var, '%m').strftime('%B')

    for i in ReadFile('Distribution.txt'):
        from datetime import datetime
        if datetime.strptime(i[3], '%Y-%m-%d').strftime('%B') == Var.capitalize():
            if i[0] + i[1] in Record:
                for j in List:
                    if i[0] == j[0] and i[1] == i[1]:
                        j[2] = str(int(j[2]) + int(i[2]))
            else:
                List.append([i[0], i[1], i[2]])
                Record.append(i[0] + i[1])

    if List == []:
        print(f'There are no transactions in {Var.capitalize()}!')
    else:
        if 'S' in SortFile(List)[-1][0]:
            Count = 1
            print(f'''__________________________________________________________________________________\n
                         {Var.capitalize()} Supplier Receive Report
        Supplier Code             Item Code              Quantity''')

            for i in SortFile(List):
                if 'S' in i[0]:
                    print(f'{Count})           {List[List.index(i)][0]}                     {List[List.index(i)][1]}                    {List[List.index(i)][2]}')
                    Count += 1

            print('\n__________________________________________________________________________________\n')
        else:
            print(f'There are no PPE items received from suppliers in {Var.capitalize()}!\n')

        if 'H' in SortFile(List)[0][0]:
            Count = 1
            print(f'''__________________________________________________________________________________\n
                        {Var.capitalize()} Hospital Distribution Report
        Hospital Code             Item Code              Quantity''')

            for i in SortFile(List):
                if 'H' in i[0]:
                    print(f'{Count})           {List[List.index(i)][0]}                     {List[List.index(i)][1]}                    {List[List.index(i)][2]}')
                    Count += 1

            print('\n__________________________________________________________________________________')
        else:
            print(f'There are no PPE items distributed to hospitals in {Var.capitalize()}!')
    print('Returning to report menu!\n')
    Report()

print('Welcome to Inventory Management System for Personal Protective Equipment(PPE)')

'''print('Proceeding to initializing suppliers\n')
InitializeSuppliers()
print('Proceeding to initializing hospitals\n')
InitializeHospitals()
print('Proceeding to initializing PPE items\n')
InitializePPE()'''
Admin = {'Admin1': 'Password1#', 'Admin2': 'Password2#', 'Admin3': 'Password3#', 'Admin4': 'Password4#'}
LoginUsername()