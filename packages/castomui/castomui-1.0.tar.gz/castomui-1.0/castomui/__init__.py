# MAKE BY Hansha
# 
# hackersam2011@gmail.com
#
# License: MIT

__all__=["inputkb"]

def _get_key():
    try:
        import getch
        char=getch.getch()
        if char=='\x1b':
            a=getch.getch()
            b=getch.getch()
            return {'[A': 'up', '[B': 'down', '[C': 'right', '[D': 'left' }[a+b]
        if ord(char) == 10:
            return  'enter'
        if ord(char) == 32:
            return  'space'
        else:
            return char
    except :
        pass
    try:
        import msvcrt
        key = msvcrt.getch()  # get keypress
        if key == b'\x1b':  # Esc key to exit
            return 'esc'
        elif key == b'\r':  # Enter key to select
            return 'enter'
        elif key == b'\x48':  # Up or Down arrow
            return  'up'
        elif key == b'\x50':  # Up or Down arrow
            return 'down'
        else:
            print(key.decode('utf-8'))
            return key.decode('utf-8')
    except:
        pass
def _get_key_str():
    try:
        import msvcrt
        key = msvcrt.getch()  # get keypress
        if key == b'\x1b':  # Esc key to exit
            return 'esc'
        elif key == b'\r':  # Enter key to select
            return 'enter'
        else:
            print(key.decode('utf-8'))
            return key.decode('utf-8')
    except:
        pass

class IntSelection():
    def __init__(self,default=0,min=0,max=100):
        self.__de=default
        self.__min=min
        self.__max=max
    def __output(self,string,select,tip):
        import os,rich
        os.system("cls" if os.name == "nt" else "clear")
        rich.print(string)
        rich.print(select)
        match tip:
            case False:
                pass
            case True:
                rich.print("\n\nUse [b red]UP[/] and [b red]DOWN[/], [b blue]ENTER[/] to continue")

    def show(self,string="",tip=True):
        import os,rich
        while True:
            
            self.__output(string,self.__de,tip)

            key = _get_key()
            if key == 'enter':  # Enter key to select 
                return self.__de
            elif key in ('up','down'):  # Up or Down arrow
                if self.__de<self.__min:
                    self.__de=self.__min
                elif self.__de>self.__max:
                    self.__de=self.__max
                else:
                    self.__de = (self.__de + (-1 if key == 'down' else 1) + self.__max % self.__max)
    
    def get(self):
        return self.__de
    
    def setdefault(self,value):
        self.__de=value

    def setmax(self,value):
        self.__max=value

    def setmin(self,value):
        self.__min=value
    
class FloatSelection():
    def __init__(self,default=0,min=0,max=10):
        self.__de=default
        self.__min=min
        self.__max=max
    def __output(self,string,select,tip):
        import os,rich
        os.system("cls" if os.name == "nt" else "clear")
        rich.print(string)
        rich.print(select)
        match tip:
            case False:
                pass
            case True:
                rich.print("\n\nUse [b red]UP[/] and [b red]DOWN[/], [b blue]ENTER[/] to continue")

    def show(self,string="",tip=True):
        import os,rich
        from decimal import Decimal
        while True:
            
            self.__output(string,self.__de,tip)

            key = _get_key()
            if key == 'enter':  # Enter key to select 
                return self.__de
            elif key in ('up','down'):  # Up or Down arrow
                if self.__de<self.__min:
                    self.__de=self.__min
                elif self.__de>self.__max:
                    self.__de=self.__max
                else:
                    self.__de = (Decimal(str(self.__de)) + (Decimal(str(-0.1)) if key == 'down' else (Decimal(str(0.1)))) + self.__max % self.__max)
    
    def get(self):
        return self.__de
    
    def setdefault(self,value):
        self.__de=value

    def setmax(self,value):
        self.__max=value

    def setmin(self,value):
        self.__min=value
    
class Prompt():
    NORMAL='NORMAL'
    PASSWORD='PASSWORD'
    NCPASSWORD='NCPASSWORD'
    def __init__(self,default="",max=10):
        self.__de=default
        self.__max=max
    def __output(self,string,select,tip,content,mode):
        import os,rich
        os.system("cls" if os.name == "nt" else "clear")
        rich.print(string)
        match mode:
            case 'NORMAL':
                rich.print(select)
            case 'PASSWORD':
                rich.print("*" * len(select))
            case 'NCPASSWORD':
                if self.__de=="":
                    rich.print("")
                else:
                    rich.print("*" * (len(select)-1) + f"[b green]{select[-1]}[/]")
        match content:
            case False:
                pass
            case True:
                rich.print("\n\n\t%s"%str(self.__max-len(select)))
        match tip:
            case False:
                pass
            case True:
                rich.print("Use [b red]ESC[/] to clear, [b blue]ENTER[/] to continue")

    def show(self,string="",tip=True,content=True,mode=NORMAL):
        import os,rich
        from decimal import Decimal
        while True:
            
            self.__output(string,self.__de,tip,content,mode)

            key = _get_key_str()
            if key == 'enter':  # Enter key to select 
                return self.__de
            elif key == 'esc':  # Enter key to select 
                self.__de=""
            else:
                if len(self.__de)==self.__max:
                    pass
                else:
                    self.__de+=key
    
    def get(self):
        return self.__de

    def setmax(self,value:int):
        self.__max=value
    
    def setdefault(self,value):
        self.__de=value

class RegexPrompt():
    def __init__(self,default="",max=10):
        self.__de=default
        self.__max=max
    def __output(self,string,select,tip,content,regex):
        import os,rich
        os.system("cls" if os.name == "nt" else "clear")
        rich.print(string)
        
        import re

        matchobjx=re.compile(regex,re.I)
        matchobj=matchobjx.match(select)
        try:
            if matchobj:
                for i in range(len(matchobj.group())):
                    select=select.replace(matchobj.group(i),f"[red]{matchobj.group(i)}[/]",1)
                selectx=select
            else:
                selectx=select
        except:
            selectx=select
        rich.print(selectx)
        match content:
            case False:
                pass
            case True:
                rich.print("\n\n\t%s"%str(self.__max-len(select)))
        match tip:
            case False:
                pass
            case True:
                rich.print("Use [b red]ESC[/] to clear, [b blue]ENTER[/] to continue")

    def show(self,string="",tip=True,content=True,regex=r""):
        import os,rich
        from decimal import Decimal
        while True:
            
            self.__output(string,self.__de,tip,content,regex)

            key = _get_key_str()
            if key == 'enter':  # Enter key to select 
                return self.__de
            elif key == 'esc':  # Enter key to select 
                self.__de=""
            else:
                if len(self.__de)==self.__max:
                    pass
                else:
                    self.__de+=key
    
    def get(self):
        return self.__de

    def setmax(self,value:int):
        self.__max=value
    
    def setdefault(self,value):
        self.__de=value



class SecondCheckPrompt():
    NORMAL='NORMAL'
    PASSWORD='PASSWORD'
    NCPASSWORD='NCPASSWORD'

    RULE_COMMON='RULE_COMMON'
    RULE_HAVENUMBER='RULE_HAVENUMBER'

    CHECKMODE_SINGLE='CM_SINGLE'
    CHECKMODE_DOUBLE='CM_DOUBLE'
    def __init__(self,default="",max=10):
        self.__de=default
        self.__currect=""
        self.__max=max
    def __output(self,string,select,currect,tip,content,mode,err,p1,p2,sel):
        import os,rich
        os.system("cls" if os.name == "nt" else "clear")
        rich.print(string)
        match mode:
            case 'NORMAL':
                rich.print(p1+select)
                rich.print(p2+currect)
            case 'PASSWORD':
                rich.print(p1+"*" * len(select))
                rich.print(p2+"*" * len(currect))
            case 'NCPASSWORD':
                if self.__de=="":
                    rich.print(p1+"")
                else:
                    rich.print(p1+"*" * (len(select)-1) + f"[b yellow]{select[-1]}[/]")
                if self.__currect=="":
                    rich.print(p2+"")
                else:
                    rich.print(p2+"*" * (len(currect)-1) + f"[b green]{currect[-1]}[/]")
        match content:
            case False:
                pass
            case True:
                match sel:
                    case 0:
                        rich.print("\n\n\t%s"%str(self.__max-len(select)))
                    case 1:
                        rich.print("\n\n\t%s"%str(self.__max-len(currect)))
        match tip:
            case False:
                pass
            case True:
                rich.print("Use [b red]ESC[/] to clear, [b blue]ENTER[/] to continue")

        rich.print(f"[i red]{err}[/]")

    def show(self,string="",park1="",park2="",tip=True,content=True,mode=NORMAL,rule=RULE_COMMON,checkmode=CHECKMODE_SINGLE):
        import os,rich
        from decimal import Decimal
        now_sel=0
        err=""
        while True:
            
            self.__output(string,self.__de,self.__currect,tip,content,mode,err,park1,park2,now_sel)

            key = _get_key_str()
            if key == 'enter':  # Enter key to select
                if now_sel==0:
                    match rule:
                        case 'RULE_COMMON':
                            err=""
                            now_sel=1
                        case 'RULE_HAVENUMBER':
                            have=0
                            for i in range(len(self.__de)):
                                cc=self.__de[i]
                                if cc.isdigit()==True:
                                    have+=1
                            if have!=0:
                                err=""
                                now_sel=1
                            else:
                                err="Error: No number in the input"
                elif now_sel==1:
                    match rule:
                        case 'RULE_COMMON':
                            err=""
                        case 'RULE_HAVENUMBER':
                            have=0
                            for i in range(len(self.__currect)):
                                cc=self.__currect[i]
                                if cc.isdigit()==True:
                                    have+=1
                            if have!=0:
                                err=""
                            else:
                                err="Error: No number in the input"

                    match checkmode:
                        case 'CM_SINGLE':
                            err=""
                            return self.__de
                        case 'CM_DOUBLE':
                            if self.__de==self.__currect:
                                err=""
                                return self.__de
                            else: err="Error: The input does not match"
                         
            elif key == 'esc':  # Enter key to select 
                match now_sel:
                    case 0:
                        self.__de=""
                    case 1:
                        if self.__currect!="":
                            self.__currect=""
                        else:
                            self.__de=""
                            now_sel=0
            else:
                match now_sel:
                    case 0:
                        if len(self.__de)==self.__max:
                            pass
                        else:
                            self.__de+=key
                    case 1:
                        if len(self.__currect)==self.__max:
                            pass
                        else:
                            self.__currect+=key
                        
                
    
    def get(self):
        return self.__de

    def setmax(self,value:int):
        self.__max=value
    
    def setdefault(self,value):
        self.__de=value

class Selection():
    def __init__(self,value=[],default=0):
        self.__de=default
        self.__val=value
    def __output(self,string,select,tip):
        import os,rich
        os.system("cls" if os.name == "nt" else "clear")
        rich.print(string)
        rich.print(select)
        match tip:
            case False:
                pass
            case True:
                rich.print("\n\nUse [b red]UP[/] and [b red]DOWN[/], [b blue]ENTER[/] to continue")

    def show(self,string="",tip=True):
        import os,rich
        while True:
            
            self.__output(string,self.__val[self.__de],tip)
            key = _get_key()
            if key == 'enter':  # Enter key to select 
                return self.__de
            elif key in ('up','down'):  # Up or Down arrow
                if self.__de<0:
                    self.__de=(len(self.__val)-2)
                elif self.__de>(len(self.__val)-2):
                    self.__de=0
                else:
                    self.__de = (self.__de + (1 if key == 'down' else -1) + len(self.__val) % len(self.__val))
    
    def get(self):
        return self.__val[self.__de]
    
    def setdefault(self,value):
        self.__de=value

    def getlength(self):
        return len(self.__val)
    
    def setselection(self,value):
        self.__val=value
    
class DirectedSelection():
    def __init__(self,value=[],default=0,prompt='>'):
        self.__de=default
        self.__val=value
        self.__pomt=prompt
    def __output(self,string,select,tip):
        import os,rich
        os.system("cls" if os.name == "nt" else "clear")
        rich.print(string)
        rich.print("\n")
        for i in range(len(self.__val)):
            if i==self.__de:
                if len(self.__pomt)==1:
                    rich.print(f"[b #FF7F50]{self.__pomt}[/] [b #4169E1]{self.__val[i]}[/]")
                else:
                    rich.print(f"[b #FF7F50]>[/] [b #4169E1]{self.__val[i]}[/]")
            else:
                rich.print(f"  {self.__val[i]}")
        match tip:
            case False:
                pass
            case True:
                rich.print("\n\nUse [b red]UP[/] and [b red]DOWN[/], [b blue]ENTER[/] to continue")

    def show(self,string="",tip=True):
        import os,rich
        while True:
            
            self.__output(string,self.__val[self.__de],tip)
            key = _get_key()
            if key == 'enter':  # Enter key to select 
                return self.__de
            elif key in ('up','down'):  # Up or Down arrow
                if self.__de<0:
                    self.__de=(len(self.__val)-2)
                elif self.__de>(len(self.__val)-2):
                    self.__de=0
                else:
                    self.__de = (self.__de + (1 if key == 'down' else -1) + len(self.__val) % len(self.__val))
    
    def get(self):
        return self.__val[self.__de]
    
    def setdefault(self,value):
        self.__de=value

    def getlength(self):
        return len(self.__val)
    
    def setprompt(self,value):
        self.__pomt=value

    def setselection(self,value):
        self.__val=value

class KeyboardPrompt():
    NORMAL='NORMAL'
    PASSWORD='PASSWORD'
    NCPASSWORD='NCPASSWORD'
    def __init__(self,default="",max=10):
        self.__de=default
        self.__max=max
        self.__x=0
        self.__y=0
        self.__temp=""
    def __output(self,string,select,tip,content,mode,keyboard:list):
        import os,rich
        os.system("cls" if os.name == "nt" else "clear")
        rich.print(string)
        match mode:
            case 'NORMAL':
                rich.print(select)
            case 'PASSWORD':
                rich.print("*" * len(select))
            case 'NCPASSWORD':
                if self.__de=="":
                    rich.print("")
                else:
                    rich.print("*" * (len(select)-1) + f"[b yellow]{select[-1]}[/]")
        match content:
            case False:
                pass
            case True:
                rich.print("\n\n\t[i green]%s[/]"%str(self.__max-len(select)))

        rich.print("\n")
        for i in range(len(keyboard)):
            for j in range(len(keyboard[i])):
                if self.__x==j and self.__y==i:
                    rich.print(f"[b #FF7F50]{keyboard[i][j]} [/]",end='')
                else:
                    rich.print(f"{keyboard[i][j]} ",end='')
            rich.print("\n")
        match tip:
            case False:
                pass
            case True:
                rich.print("\nUse [b red]LEFT[/]/[b red]RIGHT[/]/[b red]UP[/]/[b red]DOWN[/] to move, [b blue]ENTER[/] to continue")

    def show(self,string="",tip=True,content=True,mode=NORMAL,keyboard=[["1","2","3","4","5","6","7","8","9","0","+","-","(",")","CLEAR"],["BACKSPACE","SPACE","ENTER"]]):
        import os,rich
        from decimal import Decimal
        while True:
            

            

            self.__output(string,self.__de,tip,content,mode,keyboard)


            key = _get_key()
            if key == 'up':
                if self.__y<1:
                    pass
                else:
                    self.__y-=1
                    if self.__x>(len(keyboard[self.__y])-2):
                        self.__x=len(keyboard[self.__y])-1
            elif key == 'down':
                if self.__y>(len(keyboard)-2):
                    pass
                else:
                    self.__y+=1
                    if self.__x>(len(keyboard[self.__y])-2):
                        self.__x=len(keyboard[self.__y])-1
            elif key == 'M':
                if self.__x>(len(keyboard[self.__y])-2):
                    pass
                else:
                    self.__x+=1
            elif key == 'K':
                if self.__x<1:
                    pass
                else:
                    self.__x-=1
            elif key == 'enter':
                getkey=keyboard[self.__y][self.__x]
                if getkey=="BACKSPACE":
                    self.__de=self.__de[:-1]
                    self.__temp=self.__temp[:-1]
                elif getkey=="ENTER":
                    return self.__de
                elif getkey=="CLEAR":
                    self.__de=""
                    self.__temp=""
                else:
                    if len(self.__de)>=self.__max:
                        pass
                    else:
                        if getkey=="SPACE":
                            self.__de+=" "
                            self.__temp=""
                        else:
                            self.__de+=getkey
                            self.__temp+=getkey

    
    def get(self):
        return self.__de

    def setmax(self,value:int):
        self.__max=value
    
    def setdefault(self,value):
        self.__de=value

def copyright():
    return """
Make by Hansha

MIT License
"""

def demo():
    demols=DirectedSelection(value=["Selection 1","Selection 2","Selection 3","Selection 4","Selection 5","Selection 6","Selection 7","Support me?"])
    demols.show()
    print(demols.get())
