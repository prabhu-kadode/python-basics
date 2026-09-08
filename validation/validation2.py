class ValidateData:
    def __init__(self,fieldName):
        self.fieldname = fieldName
        self.isValidData = True
        self.error = []
    def required(self):
        v = str(self.fieldname).strip()
        if not v:
            err = f"this should not be empty!"
            self.error.append(err)
            return self
        return self
    def onlyString(self):
        if not isinstance(self.fieldname,str):
            err = f'This value {self.fieldname} must be only string'
            self.error.append(err)
            return self
        return self
    def onlyNumber(self):
        if not isinstance(self.fieldname,(int,float)) or isinstance(self.fieldname,bool):
            err = f'This value {self.fieldname} must be only number'
            self.error.append(err)
            return self
        return self
        
    def minmax(self,minv,maxv):            
        if len(str(self.fieldname))>=minv and len(str(self.fieldname))<=maxv:
            return self
        
        err = f'The length of {self.fieldname} must be between  {minv} and  {maxv}'
        self.error.append(err)
        return self  
    def length(self,lenthn):            
        if len(str(self.fieldname))==lenthn:
            return self
        
        err = f'The length of {self.fieldname} must be {lenthn}'
        self.error.append(err)
        return self  
    def isBoolean(self):

        if isinstance(self.fieldname,bool):
            return self
        
        err = f'This {self.fieldname} type must be boolean'
        self.error.append(err)
        return self  
        

    def isValid(self):
        if len(self.error)>0:
            self.isValidData = False

        return {
            "isValidData":self.isValidData,
            "error":self.error
        }
        
validate = ValidateData(23232323233232).required().onlyNumber().length(20).isValid()
print(validate)
for i in validate['error']:
    print(i)

# validate1= ValidateData(True).isBoolean().isValid()
# print(validate1)
    