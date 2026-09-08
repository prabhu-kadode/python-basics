class ValidateData:
    def __init__(self,fieldName):
        self.fieldname = fieldName
        self.isValidData = True
        self.error= ""
        print(self.fieldname)
    def notEmpty(self):
        if self.isValidData==False:
            return self
            
        if self.fieldname=="":
            self.isValidData = False
            self.error = 'should not be empty'
            return self
        return self
    def onlyString(self):
        if self.isValidData==False:
            return self

        if isinstance(self.fieldname,str) is False:
            self.isValidData = False
            self.error = f'This feild {self.fieldname} should be only string'
            return self
        return self
    def onlyNumber(self):
        if self.isValidData==False:
            return self

        if isinstance(self.fieldname,str) is False:
            self.isValidData = False
            self.error = f'This feild {self.fieldname} should be only string'
            return self
        return self
        
    def min(self,minv,maxv):
        if self.isValidData == False:
            return self
            
        if len(self.fieldname)>minv and len(self.fieldname)<=maxv:
            return self
        else:
            self.isValidData = False
            self.error = f'This feild {self.fieldname} length should be minimum {minv} and max should be {maxv}'
            
        return self  
    def isValid(self):
        return {
            "isValidData":self.isValidData,
            "error":self.error
        }
        
validate = ValidateData("hipppppp").notEmpty().onlyString().min(2,9).isValid()
print(validate)
    