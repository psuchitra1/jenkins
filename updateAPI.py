from urllib import request
from flask_cors import CORS,cross_origin
import psycopg2
# from addserverFORM import app
from flask import Flask, request, jsonify, make_response
import requests                                   #importing the packages/modules
import psycopg2
import INSERT   #inserting the database file
from datetime import date
import data as data
import regex     #it is used to show all the matched characters which are related to the searched one
from connect2DB import *

date_today = date.today()
import datetime as datetime    #import datetime package

date_today = date.today()
date_time = datetime.datetime.now()

d = datetime.datetime.strptime('2011-06-09', '%Y-%m-%d')    # the time format
my_datetime_utc = date_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')          # here i m using this format

app = Flask(__name__)
CORS(app)

conn = connectDB()  # called the connectDB file to connect with the database
# connecting with the database
# dbase = psycopg2.connect(         #the database is assigned by dbase
#     host='localhost',
#     dbname='server111',
#     user='postgres',
#     password='root',
#     port=5433)
conn.autocommit = True  # if you commit a database, it saves all the changes till that particular point



@cross_origin()
                       #1 # adding_asset  #
@app.route('/add_asset', methods=['POST'])

def add_asset():

    try:

        if request.method == 'POST':  # using POST method to request the data
            cursor = conn.cursor()
            cursor.execute("select Asset_Id from Asset")  # [(1,),(2,)]
            res1 = cursor.fetchall()            #  fetching the data from database
            Id_alr = len(res1)                 # variable id_alr used for the length of the fetched data
            Asset_Id = Id_alr + 1           # here it is  incred with +1
            cursor.execute                # it is executed
            _json = request.json            # json format
            print("_json")


            Asset_Name=_json["Asset_Name"]
            Manufacturer = _json["Manufacturer"]
            BMC_IP = _json["BMC_IP"]
            if (len(BMC_IP) == 7):
                {
                    print("correct")
                },
            BMC_User= _json["BMC_User"]
            BMC_Password = _json["BMC_Password"]
            Asset_Location = _json["Asset_Location"]
            # Reserved = _json["Reserved"]
            # # assigned_on = _json["assigned_on"]
            # Assigned_to = _json["Assigned_to"]
            # Assigned_from=_json["Assigned_from"]
            # Assigned_by = _json["Assigned_by"]
            Created_on=date_today
            Created_by = _json["Created_by"]
            OS_IP=_json["OS_IP"]
            print("import ipaddress",len(OS_IP))
            if(len(OS_IP) == 7):
                {
                print("Verifcation ")
                },
            OS_User=_json["OS_User"]
            OS_Password=_json["OS_Password"]
            # Updated_on=_json["Updated_on"]
            # Updated_by= _json["Updated_by"]
            Purpose = _json["Purpose"]
            Cluster_Id = _json["Cluster_Id"]
            # team_id = _json["team_id"]
            Delete = "0"
            # Status = _json["Status"]
            print("server_id")
            # cursor = conn.cursor()  # created a cursor
            print("zdfrhv")
            regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
            print("reggggg",regex)

            if socket.inet_aton(OS_IP) and socket.inet_aton(BMC_IP):

                query1 = "SELECT Asset_Id FROM Asset"
                print(query1, "printing first query")
                cursor.execute(query1)
                fetch = cursor.fetchall()
                print(fetch, "fetching statement")
                lst = []
                for i in fetch:
                    for j in i:
                        lst.append(j)
                    print(lst, "listing the array")
                if Asset_Id not in lst:
                    # values to assign in the columns
                    VALUES = (Asset_Id, Asset_Name, Manufacturer, BMC_IP, BMC_User, BMC_Password,
                              Asset_Location,  # Reserved,Assigned_to,Assigned_from,Assigned_by,
                              Created_on, Created_by, OS_IP, OS_User, OS_Password,  # Updated_on,Updated_by,
                              Purpose, Cluster_Id, Delete)  # Delete,Status)
                    print("a printing msg")
                    cursor.execute(
                        'INSERT INTO Asset(Asset_Id,Asset_Name,Manufacturer,BMC_ip,BMC_User,'
                        'BMC_Password,Asset_Location,Created_on,Created_by,OS_IP,OS_User,OS_Password,Purpose,Cluster_Id,delete) '
                        'values (%s,%s, %s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', VALUES)
                    # execute the values using cursor in the server_table to store all the new data
                    print("after inserting")
                    conn.commit()
                    # conn.commit()  # commit
                    print("oook")
                    cursor.execute('select * from asset')  # to show the data in the asset_table
                    print("fjrdgchk")
                    data = cursor.fetchall()  # it will fetch all the data with variable data

                    print("_id")

                    # resp = jsonify({"message": "asset deleted successfully!", "status": "200 OK"})
                    resp = jsonify(
                        {"Status Code": "200 OK",
                         "Message": "Recorded sucessfully"})  # created a response and jsonifed it
                    resp.status_code = 200  # given a status code 200(truse) to the above response
                    return resp  # returning the response if the above condition works
                print("oooooooooooooooooooooooo")

            else:
                print("errrrrrrrrrrrrrrrrrrrrrr")
                resp = jsonify('Invalid syntax! ,status code:400 ok')  # created a response and jsonifed it
                return resp

            #     resp.status_code = 200  # given a status code 200(truse) to the above response
            #     return resp  # returning the response if the above condition works
    except Exception as exp:
            resp = jsonify('"Message": "Invalid input syntax for IP ", "Status Code": "202"')  # created a response and jsonifed it
            return resp               #return the response
    # finally:
    #     cursor.close()


                          # 2   #list_asset#

@app.route('/list_asset', methods=["GET"])
def view_server():
    # conn = connectDB()
    try:
        print(conn,"kkkkkk")

        cursor = conn.cursor()
        # conn.autocommit = True

        if request.method == 'GET':  # GET method is used here
            cursor.execute("select * from asset WHERE delete =B'0'")  # store inserver_table

            data = cursor.fetchall()  # crusor fetchs all the data
            serverl = []  # serverlist for get method with variable serverl
            for serverData in data:


                jsonData =  {"Asset_ID": serverData[0],"Asset_Name":serverData[1],"Manufacturer": serverData[2],"BMC_IP": serverData[3], "BMC_User": serverData[4],
                        # "BMC_password": serverData[4],
                        "Asset_Location": serverData[6],"Reserved": serverData[7],"OS_IP":serverData[15],"Assigned_to": serverData[8],"Assigned_from":serverData[9],"Assigned_by": serverData[10],
            "OS_User":serverData[16],
                        "Created_on":serverData[11],"Created_by":serverData[12],"Updated_on":serverData[13],"Updated_by":serverData[14],
                             "Purpose":serverData[18],"Cluster_Id":serverData[19] ,
                         "Delete":serverData[20],
                    "Status":serverData[21]}
                serverl.append(jsonData)  # it will show all the data stored in the database with key:value
        a = []
        for i in serverl:

            cursor.execute("select email_id from users where user_id=%s", [i['Assigned_to']])              # select the email id from user table a it is sameas assigned to
            res = cursor.fetchall()                                # it will fetch all the data
            print(res)
            for j in res:
                i.update({"Assigned_to": j[0].split("@")[0]})              #it will split the email id and print the first name only
            a.append(i)
        datavar = []
        for i in serverl:
            if i["Created_on"]:
                created_date = i["Created_on"]                         #here changing the format to "2022-10-03T00:00:00Z"
                date_time_obj = created_date.isoformat() + 'Z'
                i.update({"Created_on": date_time_obj})
            if i["Updated_on"]:
                Updated_date = i["Updated_on"]
                date_time_obj1 = Updated_date.isoformat() + 'Z'
                i.update({"Updated_on": date_time_obj1})
            if i["Assigned_from"]:
                Updated_date = i["Assigned_from"]
                date_time_obj1 = Updated_date.isoformat() + 'Z'
                i.update({"Assigned_from": date_time_obj1})
            datavar.append(i)
            # print("datauserrr", datavar)
        return jsonify({"message":"listing all assets","status code": '200 OK',"ListAsset":datavar[::-1]})           # response message
    except Exception as e:
        print(e)
    finally:
        cursor.close()

                                                 # 3 # delete_asset#

@app.route('/delete_asset', methods=['PUT'])
def delete_ser():  # created a function for deleting user with their corresponding
    try:

        _json = request.json  # converting the request to json
        Asset_Id = _json['Asset_Id']
        print(Asset_Id, "Asset_Id")

        conn = connectDB()  # connecting to the database
        cursor = conn.cursor()  # created a cursor function and giving cursor_factory=RealDictCursor
        curs = conn.cursor()
        cursor.execute("SELECT * FROM asset  WHERE Asset_Id=%s",
                       (Asset_Id,))  # qurey for selecting the datas with the given id
        # and given to the cursor and it will execute
        db22 = cursor.fetchall()  # fetching all the datas of that corresponding id
        print(db22, "db22")

        if len(db22) != 0:  # checking condition if the user is not null
            cursor.execute("UPDATE  asset SET DELETE ='1',Reserved= False,Updated_on=%s WHERE Asset_Id =%s", [date.today() ,(Asset_Id,)])  # qurey for deleting and it will
            # work only the value is not equal to null
            curs.execute(
                "SELECT Asset_Id,Assigned_to,Assigned_from,Updated_on,Updated_by FROM ASSET WHERE Asset_Id =%s",
            (Asset_Id,))
            print("axydt cgbi; kn/on'i")
            data = curs.fetchall()  # fetching all the datas of that corresponding id
            print(data, "dattttaa")
            remarks = "remark"

            lst = []
            for i in data:
                for j in i:
                    lst.append(j)
                    # lst.append()
            print(lst, "lsssttttt")  # it will print the list lst
            print(lst[0], "ppppp")
            # print(lst[1],"qqqq")
            # print(lst[2],"ooo")
            # print(lst[3],"333")
            # print(lst[4],"44")
            lst2 = lst + [remarks]  # creating another list to add the string format REMARK with that list lst
            print(lst2, "l222")

            query = (lst2[0], lst2[1], lst2[2], lst2[3], lst2[4],
                     lst2[5])  # query to get all the fields starting from index 0 to 5
            # print(query,"qqq")
            # print(lst[0],"1lst")
            # print(lst[0],"9999")
            curs.execute(
                'INSERT INTO  historic_details(Asset_Id,Assigned_to,Assigned_from,Updated_on,Updated_by,remarks)values (%s, %s ,%s ,%s ,%s,%s)',
                query)  # insert query

            print(query, "queryyyyyyyyy")  # it will print the query



            conn.commit()
            resp = jsonify({"message": "asset deleted successfully!", "status": "200 OK"})

            # resp = jsonify('User deleted successfully!')  # response is jsonifying
            resp.status_code = 200  # giving status code as 200 (true)
            return resp  # if the above condition works thengive the response as 200



        else:
            resp = jsonify({"message": "ASSET_ID IS NOT THERE!", "status": "400 Bad Request"})
            # res = jsonify("User not available with  id ", User_Id)  # if the user is null then this response works
            resp.status_code = 400  # error response
            return resp

    except Exception as e:
        print(e)
    finally:
        cursor.close()

  #if assigned from is null ,then it will show error like violates not null constraint
  #in postman it is showing like this -
#   The view function for 'delete_ser' did not return a valid response. The function either returned None or ended without a return statement


                                                  #4 #platform_profile#

@app.route('/platformProfile', methods=['GET'])
def getfile():
        print("vgsduofwedj")


        with open("platformprofile.json", "r+") as f:
            data = f.read()
        return data

                            #5 #update the request_form (infra_admin)#

@app.route('/update_ia_comments', methods=['PUT'])
def UpdateRequest():  # created a function for deleting user with their corresponding
    try:
        conn = connectDB()
        if request.method == 'PUT':
            _json = request.json                #the put method withjson format
            ID = _json["ID"]

            # Infraadmin_Comments   =  _json["Infraadmin_Comments"]
            Infraadmin_Comments = _json["Infraadmin_Comments"]
            Request= _json["Request"]

            cursor = conn.cursor()            # cursor used

            data = ( ID, Infraadmin_Comments,Request)      #value
            cursor.execute("SELECT * FROM server_request  WHERE ID=%s", (ID,))       # execute query with id
            print("show selected id")

            cursor.execute("UPDATE  server_request SET Request= %s WHERE ID =%s",
                           (Request, ID))  # qurey for updating the request column using id
            print(request,"id")
            #
            # cursor.execute("UPDATE server_request SET Infraadmin_Comments = array_prepend( %s, Infraadmin_Comments) where ID=%s", [ str(Infraadmin_Comments).split(', '),str(my_datetime_utc).split(', '), ID ])
            # print("infra_comments",sq)

            cursor.execute("UPDATE server_request SET Infraadmin_Comments = array_prepend( %s, Infraadmin_Comments) WHERE ID=%s",
                [ str(my_datetime_utc)+str(Infraadmin_Comments), ID]) # updating thecomment section with today date and time
            # print(Infraadmin_Comments .splitlines())
            conn.commit()           #commit
            cursor.execute('select * from server_request where ID = %s', (ID,))
            data = cursor.fetchall()         # it fetches all the data
            print("data")
            print(Infraadmin_Comments,"printing the comments")
            conn.commit()
            resp = jsonify({"message": "updated successfully!", "status": "200 OK"})

            # resp = jsonify('User deleted successfully!')  # response is jsonifying
            resp.status_code = 200  # giving status code as 200 (true)
            return resp

    except Exception as e:
        print(e)
    finally:
        cursor.close()
            # 7. create request...

@app.route('/create_request', methods=['POST'])
def create_request():
    try:
        conn = connectDB()
        cursor = conn.cursor()  # created a cursor
        print(cursor, "cursoor")

        cursor.execute("select Id from Server_Request")  # [(1,),(2,)]
        res1 = cursor.fetchall()
        Id_alr = len(res1)
        Id = Id_alr + 1

        _json = request.json  # converting to json
        # Id = _json['Id']
        # print(Id, "Id")
        User_No = _json['User_No']
        print(User_No, "User_No")
        Creator = _json['Creator']
        print(Creator, "Creator")
        Start_Date = _json['Start_Date']
        print(Start_Date, "Start_Date")
        End_Date = _json['End_Date']
        print(End_Date, "End_Date")
        Manufacturer = _json['Manufacturer']
        print(Manufacturer, "Manufacturer")
        # Created_on = date_today
        # print(Created_on, "Created_on")
        Number_Of_Servers = _json['Number_Of_Servers']
        print(Number_Of_Servers, "Number_Of_Servers")
        Operating_System = _json['Operating_System']
        print(Operating_System, "Operating_System")
        # Updated_on = date_today
        # print(Updated_on, "Updated_on")
        Cpu_model = _json['Cpu_model']
        print(Cpu_model, "Cpu_model")
        CPU_Sockets = _json['CPU_Sockets']
        print(CPU_Sockets, "CPU_Sockets")
        DIMM_Size = _json['DIMM_Size']
        print(DIMM_Size, "DIMM_Size")
        DIMM_Capacity = _json['DIMM_Capacity']
        # delete = dele.encode()
        print(DIMM_Capacity, "DIMM_Capacity")
        Storage_Vendor = _json['Storage_Vendor']
        print(Storage_Vendor, "Storage_Vendor")
        Storage_Controller = _json['Storage_Controller']
        print(Storage_Controller, "Storage_Controller")
        Storage_Capacity = _json['Storage_Capacity']
        print(Storage_Capacity, "Storage_Capacity")
        Network_Type = _json['Network_Type']
        print(Network_Type, "Network_Type")
        Network_speed = _json['Network_speed']
        print(Network_speed, "Network_speed")
        Number_Of_Network_Ports = _json['Number_Of_Network_Ports']
        print(Number_Of_Network_Ports, "Number_Of_Network_Ports")
        Special_Switching_Needs = _json['Special_Switching_Needs']
        print(Special_Switching_Needs, "Special_Switching_Needs")
        Infraadmin_Comments = _json['Infraadmin_Comments']
        print(Infraadmin_Comments, "Infraadmin_Comments")
        User_Comments = _json['User_Comments']
        print(User_Comments, "User_Comments")
        Request = _json['Request']
        print(User_Comments, "Request")

        # validate the received values
        if Id and User_No and Creator and Start_Date and End_Date and Manufacturer and \
                Number_Of_Servers and Operating_System and Cpu_model and CPU_Sockets and DIMM_Size and \
                DIMM_Capacity and Storage_Vendor and Storage_Controller and Storage_Capacity and \
                Network_Type and Network_speed and Number_Of_Network_Ports and \
                Special_Switching_Needs and Infraadmin_Comments and \
                User_Comments and Request and request.method == 'POST':  # giving condition whether the method is post

            query1 = ("SELECT Id FROM Server_Request ")  # qurey for selecting userid id from the usertable
            print(query1, "q1111")
            cursor.execute(query1)  # executing the qurey
            db224 = cursor.fetchall()  # fetching the qurey
            print(db224, "db224")
            usrid = []  # created an empty list for adding the user ids
            for i in db224:  # iterating the fetched values
                for j in i:  # iterating the tuples
                    print(usrid, "useridd")
                    usrid.append(j)  # appending the values in to the list
                print(usrid, "idddddd")

            query2 = ("SELECT User_Id FROM Users ")
            print(query2, "qqq2222222222222222")
            cursor.execute(query2)
            dbq2 = cursor.fetchall()
            print(dbq2, "dbq2")
            usid = []
            for i in dbq2:
                for j in i:
                    print(usid, "usid")
                    usid.append(j)
                print(usid, "usssssssssss")

            if User_No not in usid:  # checking the user id is present in the list
                resp = jsonify({"Message": "No current Requests!",
                                "Status": "400 Bad Request"})  # if the userid is present in the list it will show response as this
                resp.status_code = 400  # status code made as 400
                return resp  # this response will work if this condition works

            else:

                sql = "INSERT INTO Server_Request(Id,User_No, Creator, Start_Date,End_Date ,Manufacturer ," \
                      " Number_Of_Servers ,Operating_System, Cpu_model , CPU_Sockets, DIMM_Size," \
                      "DIMM_Capacity,Storage_Vendor,Storage_Controller,Storage_Capacity," \
                      "Network_Type,Network_speed," \
                      "Number_Of_Network_Ports,Special_Switching_Needs,Infraadmin_Comments,User_Comments,Request)" \
                      " VALUES(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s,%s,%s,%s,%s,%s,%s)"  # qurey for inserting values to the sql
                print(sql, "sqlll")
                data = (
                Id, User_No, Creator, Start_Date, End_Date, Manufacturer, Number_Of_Servers, Operating_System,
                Cpu_model,
                CPU_Sockets, DIMM_Size, DIMM_Capacity, Storage_Vendor, Storage_Controller, Storage_Capacity,
                Network_Type, Network_speed,
                Number_Of_Network_Ports, Special_Switching_Needs, Infraadmin_Comments, User_Comments,
                Request)  # passing the variables from frondend to data
                print(data, "dataa")
                # connecting to psql

                cursor.execute(sql, data)  # executed the cursor with the sql qurey and the datas inserting
                conn.commit()  # commited the conn
                resp = jsonify(
                    {"Message": "Request added successfully!",
                     "Status": "200 OK"})  # created a response and jsonifed it
                return resp
            # resp.status_code = 200  # given a status code 200(truse) to the above response
            # return resp  # returning the response if the above condition works

        else:
            res = jsonify(
                {
                    "Message": "Request is not added please check the error below!"})
            res.status_code = 400  # giving error status
            return res

    except Exception as e:
        print(e)
    finally:
        cursor.close()


if __name__ == '__main__':
    # app.app_context()
    app.run(host="0.0.0.0",port=5000,debug=True)