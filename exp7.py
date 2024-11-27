class Students:
    def __init__(self):
        self.name = ''
        self.rollNum = ''
        self.totalFee = ''
        self.feePaid = 0
        
    def getStudentDetails(self):
        self.name = input('Enter Student Name: ')
        self.rollNum = input('Enter Roll Nu: ')
        self.totalFee = input('Enter total fee: ')
        self.feePaid = input('Enter amount paid: ')
    
    def showData(self):
        print('Student Data')
        print(f'Student Name: {self.name}')
        print(f'Student Roll No: {self.rollNum}')
        print(f'Student Total Fee: {self.totalFee}')
        print(f'Student Fee paid: {self.feePaid}')
        
    def updatePaidFee(self):
        self.feePaid = input('Enter new data of paid fee: ')
        print(f'Paid fee: {self.feePaid}')
        
el = Students()
el.getStudentDetails()
el.showData()
el.updatePaidFee()