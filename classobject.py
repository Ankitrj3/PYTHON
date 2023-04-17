class ankit:
    def __init__(self,name,processor,ram):
        self.name=name
        self.processor=processor
        self.ram=ram

    def configuration(self):
        print('configuration of laptop is' , self.name , self.processor , self.ram)

obj=ankit('hp laptop','i9 processor','16 gb ram')

obj.configuration()