import datetime


class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class AddRequest:
    def __init__(self, requestFrom, requestTo, date):
        self.requestFrom = requestFrom
        self.requestTo = requestTo
        self.date = date
        self.request = []

    def get_requestFrom(self):
        return self.requestFrom

    def set_requestFrom(self, requestFrom):
        self.requestFrom = requestFrom

    def get_requestTo(self):
        return self.requestTo

    def set_requestTo(self, requestTo):
        self.requestTo = requestTo

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def add_request(self):
        self.request.append(self.requestTo)
        return self.request


class Message:
    def __init__(self, messageFrom, messageTo, date, message):
        self.messageFrom = messageFrom
        self.messageTo = messageTo
        self.date = date
        self.message = message
        self.request = []

    def get_messageFrom(self):
        return self.messageFrom

    def set_requestFrom(self, messageFrom):
        self.messageFrom = messageFrom

    def get_messageTo(self):
        return self.messageTo

    def set_requestTo(self, messageTo):
        self.messageTo = messageTo

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def set_message(self, message):
        self.message = message

    def get_message(self):
        return self.message


class GroupChat:
    pass


class Messenger:

    def __init__(self):
        self.database = {}


    def make_online(self, name):
        new_user = User(name)
        if name not in self.database:
            self.database[name] = {'name': new_user,'sent_request':[],'received_request':[],
                                  'sent_message':[],'received_message':[] ,'Accept':{},'Reject':{}}
        print(name, "User is Online")
        # print(self.database)

    def AddRequest(self, requestFrom, requestTo, date):
        new_request = AddRequest(requestFrom, requestTo, date)
        self.database[requestFrom]['sent_request'].append(new_request)
        self.database[requestTo]['received_request'].append(new_request)
        print(requestFrom+" send request to " + requestTo)

    def get_message(self,message):
        for i in message:
            return i.get_message()

    def send_message(self, messageFrom, messageTo, date, message):
        if self.database[messageTo]['Accept'][messageFrom]=='YES':
            new_message = Message(messageFrom, messageTo, date, message)
            self.database[messageFrom]['sent_message'].append(new_message)
            self.database[messageTo]['received_message'].append(new_message)
            print(messageFrom +" message ",self.get_message(self.database[messageTo]['received_message'])+ " to", messageTo)
        elif self.database[messageTo]['Accept'][messageFrom]=='NO':
                print("request not been accepted!! message is not sent")
        else:
            print("request is still pending. cannot send the message")



    def get_request_deatils(self, name):
        if self.database[name]:
            request = (self.database[name]['sent_request'].get_requestTo())
            message = (self.database[name]['sent_message'].get_message())
            return ("Request sent to",  request + " and the message is ",message)

    def accept_request(self,name1,name2):
        if self.database[name1]:
            for i in self.database[name1]['received_request']:
                if i.get_requestFrom()== name2:
                    self.database[name1]['Accept'][name2]="YES"
                    print(name1 +" accepred request of "+ name2)


    def reject_request(self,name1,name2):
        if self.database[name1]:
            for i in self.database[name1]['received_request']:
                if i.get_requestFrom()== name2:
                    self.database[name1]['Accept'][name2]="NO"
                    print(name1 + " rejected request " + name2)





myObj = Messenger()

myObj.make_online("Elsy")
myObj.make_online("Aaron")
myObj.make_online("Akhil")
myObj.AddRequest("Aaron", "Elsy", datetime.datetime.now())
myObj.AddRequest("Aaron", "Akhil", datetime.datetime.now())
myObj.AddRequest("Akhil", "Elsy", datetime.datetime.now())
myObj.accept_request("Elsy","Akhil")
myObj.reject_request("Elsy","Aaron")
myObj.send_message("Akhil", "Elsy", datetime.datetime.now(), "Hi how are you!!!")
myObj.send_message("Aaron", "Elsy", datetime.datetime.now(), "Hi how are you!!!")


