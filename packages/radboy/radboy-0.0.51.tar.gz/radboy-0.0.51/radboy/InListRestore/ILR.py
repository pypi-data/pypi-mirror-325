from . import *


class InListRestoreUI:
    def sf2l(self):
        with Session(ENGINE) as session:
            results=session.query(Entry).filter(Entry.InList==True).all()
            Comments=Prompt.__init2__(None,func=FormBuilderMkText,ptext="what Comments need to be said about this Restore List?",helpText="Comments",data="string")
            if Comments in ['d',]:
                Comments=''
            elif Comments in [None,]:
                return
            Note=Prompt.__init2__(None,func=FormBuilderMkText,ptext="what is the Note for this Restore List?",helpText="Note",data="string")
            if Note in ['d',]:
                Note=''
            elif Note in [None,]:
                return
            Description=Prompt.__init2__(None,func=FormBuilderMkText,ptext="what is the Description of this Restore List?",helpText="Description",data="string")
            if Description in ['d',]:
                Description=''
            elif Description in [None,]:
                return
            Name=Prompt.__init2__(None,func=FormBuilderMkText,ptext="What Name Do you want to call this Restore List?",helpText="Name",data="string")
            if Name in [None,'d']:
                print("Name cannot be empty, or user cancelled!")
                return
            InList=True
            if len(results) < 1:
                print("No results were found to use!")
                return
            for num,entry in enumerate(results):
                ilr=InListRestore(Name=Name,InList=InList,Description=Description,Note=Note,Comments=Comments,EntryId=entry.EntryId)
                session.add(ilr)
                if num % 10 == 0:
                    session.commit()
            session.commit()

    def listRestoreNames(self,ALL=False):
        Name=Prompt.__init2__(None,func=FormBuilderMkText,ptext="What Do you want look for by Name?",helpText="Name",data="string")
        if Name in [None,]:
            print("Name cannot be empty, or user cancelled!")
            return
        elif Name in ['d',]:
            Name=''
        with Session(ENGINE) as session:
            results=session.query(InListRestore).filter(InListRestore.Name.icontains(Name)).group_by(InListRestore.Name).all()
            ct=len(results)
            mtext=[]
            for num, i in enumerate(results):
                if not ALL:
                    msg=f"""{Fore.light_cyan}{num}/{Fore.light_yellow}{num+1} of {Fore.light_red}{ct} -> {Fore.grey_70}Name: {Fore.light_steel_blue}{i.Name}{Style.reset}"""
                else:
                    msg=f"""{Fore.light_cyan}{num}/{Fore.light_yellow}{num+1} of {Fore.light_red}{ct} -> {i}"""
                mtext.append(msg)
            mtext='\n'.join(mtext)
            print(mtext)
            print(f"{Fore.light_steel_blue}{ct}{Fore.orange_red_1} Total Results{Style.reset}")

    def RestoreFromName(self):
        Name=Prompt.__init2__(None,func=FormBuilderMkText,ptext="What Do you want look for by Name?",helpText="Name",data="string")
        if Name in [None,]:
            print("Name cannot be empty, or user cancelled!")
            return
        elif Name in ['d',]:
            Name=''
        with Session(ENGINE) as session:
            results=session.query(InListRestore).filter(InListRestore.Name.icontains(Name)).group_by(InListRestore.Name).all()
            ct=len(results)
            mtext=[]
            for num, i in enumerate(results):
                msg=f"{Fore.light_cyan}{num}/{Fore.light_yellow}{num+1} of {Fore.light_red}{ct} -> {Fore.grey_70}Name: {Fore.light_steel_blue}{i.Name}{Style.reset}"
                mtext.append(msg)
            mtext='\n'.join(mtext)
            while True:
                try:
                    print(mtext)
                    print(f"{Fore.light_steel_blue}{ct}{Fore.orange_red_1} Total Results{Style.reset}")
                    which=Prompt.__init2__(None,func=FormBuilderMkText,ptext="Which index?",helpText="an integer",data="integer")
                    if which in [None,'d']:
                        return
                    if which >= 0 and which < ct:
                        zerod=session.query(Entry).update({'InList':False})
                        session.commit()
                        restore=session.query(InListRestore).filter(InListRestore.Name==results[which].Name).all()
                        for num,i in enumerate(restore):
                            x=session.query(Entry).filter(Entry.EntryId==i.EntryId).update({'InList':i.InList})
                            if num % 10 == 0:
                                session.commit()
                        session.commit()
                        break
                except Exception as e:
                    print(e)

    def DeleteFromName(self):
        Name=Prompt.__init2__(None,func=FormBuilderMkText,ptext="What Do you want look for by Name?",helpText="Name",data="string")
        if Name in [None,]:
            print("Name cannot be empty, or user cancelled!")
            return
        elif Name in ['d',]:
            Name=''
        with Session(ENGINE) as session:
            results=session.query(InListRestore).filter(InListRestore.Name.icontains(Name)).group_by(InListRestore.Name).all()
            ct=len(results)
            mtext=[]
            for num, i in enumerate(results):
                msg=f"{Fore.light_cyan}{num}/{Fore.light_yellow}{num+1} of {Fore.light_red}{ct} -> {Fore.grey_70}Name: {Fore.light_steel_blue}{i.Name}{Style.reset}"
                mtext.append(msg)
            mtext='\n'.join(mtext)
            while True:
                try:
                    print(mtext)
                    print(f"{Fore.light_steel_blue}{ct}{Fore.orange_red_1} Total Results{Style.reset}")
                    which=Prompt.__init2__(None,func=FormBuilderMkText,ptext="Which index?",helpText="an integer",data="integer")
                    if which in [None,'d']:
                        return
                    if which >= 0 and which < ct:
                        restore=session.query(InListRestore).filter(InListRestore.Name==results[which].Name).delete()
                        session.commit()
                        break
                except Exception as e:
                    print(e)


    def __init__(self):
        '''Store A List of EntryId's whose InList==True being set to True will allow for speedier on-the-floor use of the List Maker.'''
        cmds={
            'save2list':{
            'cmds':['save2list','s2l',],
            'exec':self.sf2l,
            'desc':"save all current Entries with InList=True to InListRestore"
            },
            'list names':{
            'cmds':['lrn','list restore names'],
            'exec':self.listRestoreNames,
            'desc':"List Restore Names",
            },
            'list all names':{
            'cmds':['sarn','show all restore names'],
            'exec':lambda self=self:self.listRestoreNames(ALL=True),
            'desc':"List Restore Names, but show everything",
            },
            'restore list':{
            'cmds':['restore','restore list','rl','lr'],
            'exec':self.RestoreFromName,
            'desc':"Restore Entry's to InList==True by Restore Name",
            },
            'delete list':{
            'cmds':['del','delete','remove','rem','rm',],
            'exec':self.DeleteFromName,
            'desc':"Delete a Restore list by Name",
            },
        }
        helpText=[]
        for m in cmds:
            helpText.append(f"{cmds[m]['cmds']} - {cmds[m]['desc']}")
        helpText='\n'.join(helpText)
        while True:
            doWhat=Prompt.__init2__(None,func=FormBuilderMkText,ptext=f"InListRestore@{Fore.light_green}Menu{Fore.light_yellow}",helpText=helpText,data="string")
            if doWhat in [None,]:
                return
            elif doWhat in ['d',]:
                print(helpText)
                continue
            for cmd in cmds:
                check=[i.lower() for i in cmds[cmd]['cmds']]
                if doWhat.lower() in check:
                    try:
                        cmds[cmd]['exec']()
                        break
                    except Exception as e:
                        print(e)