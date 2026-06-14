"""
Hospital Management System
Entity
- Patient     (pid,pname,page,pgender,pcontact,problem)
- Doctor      (did,dname,dspec,active)
- Appointment

1- Add Patient Information
2- View All Patients
3- Update Patient Information
4- Delete A Patient
5- Add Doctor Information
6- View All Doctors Information
7- Active/Inactive Doctor
8- Book An Appointment
9- View All Appointments
0- Exit


"""
# IMPORTING REQUIRED LIBRARIES
import pickle

# A METHOD TO ADD PATIENT INFORMATION
def addPatient():
    pid = input("\n\tEnter Patient ID : ")
    pname = input("\tEnter Patient Name : ")
    page = input("\tEnter Patient Age : ")
    pgender = input("\tEnter Patient Gender : ")
    pmob = input("\tEnter Patient Mobile No : ")
    pdisease = input("\tExplain Disease/Problem : ")
    data = {pid:[pname,page,pgender,pmob,pdisease]}
    file = open('patient.bin','ab')
    pickle.dump(data,file)
    file.close()
    print("\n\t\tPatient Added Successfully!")

# A METHOD TO VIEW ALL PATIENTS
def viewAllPatients():
    file = open('patient.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            for pid,info in data.items():
                print("\n\tPatient ID :",pid)
                print("\tPatient Name :",info[0])
                print("\tPatient Age :",info[1])
                print("\tPatient Gender :",info[2])
                print("\tPatient Contact :",info[3])
                print("\tPatient's Problem :",info[4])
                print("\t-----------------------------------")
    except:
        print("\n\tHere is your all patients")
    file.close()

# A METHOD TO GET PATIENT INFORMATION
def getAllPatients():
    file = open('patient.bin','rb')
    pat = dict()
    try:
        while True:
            pat.update(pickle.load(file))
    except:
        pass
    file.close()
    return pat

# A METHOD TO UPDATE PATIENT's INFORMATIOn
def updatePatient():
    pid = input("\n\tEnter Patient ID To Update Info : ")
    pat = getAllPatients()
    res = pat.get(pid,False)
    if res:
        print("\tCustomer Name :",res[0])
        print("\tCustomer Age :",res[1])
        print("\tCustomer Gender :",res[2])
        print("\tOld Contact Number :",res[3])
        cont = input("\tEnter New Contact : ")
        print("\tOld Patient Problem :",res[4])
        prob = input("\tEnter New Problem if Any : ")
        pat.update({pid:[res[0],res[1],res[2],cont,prob]})
        file = open('patient.bin','wb')
        for pid,info in pat.items():
            pickle.dump({pid:info},file)
        file.close()
        print("\tPatient Updated Successfully!")
    else:
        print("\tNo Patient Found on this ID")

# A METHOD TO DELETE A PATIENT
def deletePatient():
    pid = input("\n\tEnter Patient ID To Delete : ")
    pat = getAllPatients()
    res = pat.get(pid,False)
    if res:
        print("\tPatient Name :",res[0])
        print("\tPatient Age :",res[1])
        print("\tPatient Gender :",res[2])
        print("\tPatient Contact :",res[3])
        print("\tPatient's Problem :",res[4])
        ch = input("\n\tDo You Want To Delete(Y/n) :")
        if ch in "Yy":
            pat.pop(pid)
            file = open('patient.bin','wb')
            for pid,info in pat.items():
                pickle.dump({pid:info},file)
            file.close()
            print("\tPatient Deleted Successfully!")
        else:
            print("\tPatient's Information Not Deleted!")
    else:
        print("\n\tPatient Not Found!")

# A METHOD TO ADD A DOCTOR's INFORMATION
def addDoctor():
    did = input("\n\tEnter New Docter ID : ")
    dname = input("\tEnter Doctor Name : ")
    dspec = input("\tEnter Doctor Speciality : ")
    active = 1
    data = {did:[dname,dspec,active]}
    file = open('doctor.bin','ab')
    pickle.dump(data,file)
    print(f"\n\tDoctor {dname} Added Successfully!")
    file.close()
    file = open('appointment.bin','ab')
    data = {did:{'1PM':0,'2PM':0,'3PM':0,'4PM':0}}
    pickle.dump(data,file)
    file.close()
    
# A METHOD TO GET ALL THE DOCTORS INFORMATION
def getAllDoctors():
    doc = dict()
    file = open('doctor.bin','rb')
    try:
        while True:
            doc.update( pickle.load(file) )
    except:
        pass
    file.close()
    return doc

# A METHOD TO GET ALL APPOINTMENTS
def getAllAppointments():
    app = dict()
    file = open('appointment.bin','rb')
    try:
        while True:
            app.update( pickle.load(file) )
    except:
        pass
    file.close()
    return app

# A METHOD TO MARK ACTIVE/INACTIVE TO A DOCTOR
def activeDoctor():
    did = input("\n\tEnter Doctor ID To Mark A/In :")
    doc = getAllDoctors()
    d = doc.get(did,False)
    if d:
        print(f"\n\tDoctor {d[0]} is",'Active' if d[2]==1 else 'Inactive')
        if d[2]==1:
            ch = input("\tDo You Want To Mark Inactive (Y/n) :")
            if ch in "yY":
                d[2] = 0
                print(f"\tDoctor {d[0]} is Inactive Now!")
            else:
                print(f"\tDoctor {d[0]} is stil",'Active' if d[2]==1 else 'Inactive')
        else:
            ch = input("\tDo You Want To Mark Active (Y/n) :")
            if ch in "yY":
                d[2] = 1
                print(f"\tDoctor {d[0]} is Active Now!")
            else:
                print(f"\tDoctor {d[0]} is stil",'Active' if d[2]==1 else 'Inactive')
        doc.update({did:d})
        file = open('doctor.bin','wb')
        for did,info in doc.items():
            pickle.dump({did:info},file)
        file.close()
    else:
        print("\n\tDoctor Not Found!")

# A METHOD TO BOOK AN APPOINMENT
def bookAnAppointment():
    pid = input("\n\tEnter Patient ID : ")
    pat = getAllPatients().get(pid,False)
    if pat:
        print("\n\tPatient Name : ",pat[0])
        print("\tPatient Age : ",pat[1])
        print("\tPatient Disease : ",pat[4])
        did = input("\n\tEnter Doctor ID : ")
        doc = getAllDoctors().get(did,False)
        if doc:
            if doc[2]==1:
                print("\tDoctor Name : ",doc[0])
                print("\tDoctor Speciality : ",doc[1])
                doc = getAllAppointments()
                app = doc.get(did)
                print("\tAll Slots")
                i = 1
                li = []
                for k,v in app.items():
                    print(f'\t{i}.',k,'\tAvailable' if v==0 else '\tBooked')
                    i = i+1
                    li.append(k)
                ch = int(input("\n\tSelect Your Slot(1-4) : "))
                if app.get(li[ch-1])==0:
                    app[li[ch-1]]=1
                    print("\n\tApponitment Booked!")
                else:
                    print("\n\tSlot Already Booked!")
                doc.update({did:app})
                file = open('appointment.bin','wb')
                for k,v in doc.items():
                    pickle.dump({k:v},file)
                file.close()
            else:
                print("\tDoctor is Inactive! Not Available!")
        else:
            print("\n\tDoctor Not Found!")
    else:
        print("\n\tPatient Not Found!")

# A METHOD TO VIEW ALL APPOINTMENTS
def viewAllAppointments():
    app = getAllAppointments()
    for did,slots in app.items():
        doc = getAllDoctors().get(did)
        print("\n\tDoctor Name :",doc[0])
        print("\tDoctor Speciality :",doc[1])
        for k,v in slots.items():
            if v==1:
                print(f'\t{k}\tBooked!')

# DASHBOARD
while True:
    print("\n\t\tHospital Management System")
    print('''
        1- Add Patient Information
        2- View All Patients
        3- Update Patient Information
        4- Delete A Patient
        5- Add Doctor Information
        6- View All Doctors Information
        7- Active/Inactive Doctor
        8- Book An Appointment
        9- View All Appointments
        0- Exit''')
    ch = int(input("\n\tEnter Your Choice : "))
    if ch==0:
        print("\t\tBye-Bye Admin!")
        break
    elif ch==1:
        addPatient()
        input("\n\t\tPress Enter To Continue...")
    elif ch==2:
        viewAllPatients()
        input("\n\t\tPress Enter To Continue...")
    elif ch==3:
        updatePatient()
        input("\n\t\tPress Enter To Continue...")
    elif ch==4:
        deletePatient()
        input("\n\t\tPress Enter To Continue...")
    elif ch==5:
        addDoctor()
        input("\n\t\tPress Enter To Continue...")
    elif ch==6:
        viewAllDoctors()
        input("\n\t\tPress Enter To Continue...")
    elif ch==7:
        activeDoctor()
        input("\n\t\tPress Enter To Continue...")
    elif ch==8:
        bookAnAppointment()
        input("\n\t\tPress Enter To Continue...")
    elif ch==9:
        viewAllAppointments()
        input("\n\t\tPress Enter To Continue...")
    else:
        input("\n\tWrong Entered\n\tTry Again!")
