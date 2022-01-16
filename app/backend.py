import os
# import pymongo
import json
import random
import psycopg2




def connector():
    # cockroachstring = "dbname='wet-dingo-838.defaultdb' user='muntaser' password='getyourownpassword' host='free-tier.gcp-us-central1.cockroachlabs.cloud' port='26257'"
    cockroachstring = os.environ.get('COCKROACHSTR')
    conn=psycopg2.connect(cockroachstring)
    return conn



def initialize(conn):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, username STRING, email STRING, userpassword STRING, useraddress STRING, lat STRING, lon STRING, usertype STRING)"
        )
        cur.execute(
            "CREATE TABLE IF NOT EXISTS doctors (id INT PRIMARY KEY, username STRING, fullname STRING, email STRING, userpassword STRING, specialty STRING, availability STRING, rate STRING)"
        )
        cur.execute(
            "CREATE TABLE IF NOT EXISTS patients (id INT PRIMARY KEY, username STRING, fullname STRING, email STRING, userpassword STRING, ethnicity STRING, gender STRING, zipcode STRING, hasinsurance STRING, premium STRING)"
        )
        cur.execute(
            "CREATE TABLE IF NOT EXISTS requests (id INT PRIMARY KEY, patientid STRING, times STRING, description STRING, video STRING, status STRING)"
        )
        cur.execute(
            "CREATE TABLE IF NOT EXISTS appointments (id INT PRIMARY KEY, doctorid STRING, patientid STRING, time STRING, status STRING)"
        )
        cur.execute(
            "CREATE TABLE IF NOT EXISTS sessions (id INT PRIMARY KEY, appointmentid STRING, doctorid STRING, patientid STRING, time STRING, duration STRING, baserate STRING, realrate STRING, billfrom STRING, payto STRING)"
        )
        cur.execute(
            "CREATE TABLE IF NOT EXISTS corporations (id INT PRIMARY KEY, name STRING, ticker STRING, donations STRING, impact STRING)"
        )
        cur.execute(
            "CREATE TABLE IF NOT EXISTS donations (id INT PRIMARY KEY, corpid STRING, amount STRING, date STRING, status STRING)"
        )
        cur.execute(
            "CREATE TABLE IF NOT EXISTS system (id INT PRIMARY KEY, donated STRING, used STRING, balance STRING, impacts STRING)"
        )
        cur.execute(
            "CREATE TABLE IF NOT EXISTS ratings (id INT PRIMARY KEY, doctorid STRING, patientid STRING, rating STRING)"
        )
        # cur.execute("UPSERT INTO users (id, email, userpassword, usertype, name) VALUES (1, 'jon@fisherman.com', 'password1', 'fisherman', 'jon stewart'), (2, 'joe@gmail.com', 'password1', 'customer', 'joe someone')")
        # logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()



def add_tasks(conn, userid, cost, price, placeid, items, tname):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM tasks")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        i = 1
        for row in rows:
            i = i + 1
        i = str(i)
        helperid = "-1"
        status = "created"
        cur.execute("UPSERT INTO tasks (id, name, userid, cost, price, placeid, items, helperid, status) VALUES (" + i +", '" + tname +"', '" + userid + "', '" + cost + "', '" + price +"', '" + placeid + "', '" + items +"', '" + helperid +"', '" + status +"')")
        # logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    return i
    # print ("user added")



def pendingtask(conn, helperid, taskid):
    newstatus = "pending"
    with conn.cursor() as cur:
        cur.execute( "UPDATE tasks SET helperid = %s , status = %s WHERE id = %s", (helperid, newstatus, taskid));
        #  "UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, frm)
        conn.commit()

    return 0


def acceptedtask(conn, taskid):
    newstatus = "accepted"
    with conn.cursor() as cur:
        cur.execute( "UPDATE tasks SET status = %s WHERE id = %s", (newstatus, taskid));
        #  "UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, frm)
        conn.commit()

    return 0


def completedtask(conn, taskid):
    newstatus = "completed"
    with conn.cursor() as cur:
        cur.execute( "UPDATE tasks SET status = %s WHERE id = %s", (newstatus, taskid));
        #  "UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, frm)
        conn.commit()

    return 0



def add_appt(conn, pid, time, did):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM appointments")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        i = 1
        for row in rows:
            i = i + 1
        i = str(i)

        st = "scheduled"
        
        cur.execute("UPSERT INTO appointments (id, doctorid, patientid, time, status) VALUES (" + i +", '" + did + "', '" + pid + "', '" + time +"', '" + st +"')")
        # logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    return i
    # print ("user added")

def add_request(conn, pid, times, description, video):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM requests")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        i = 1
        for row in rows:
            i = i + 1
        i = str(i)

        st = "open"
        
        cur.execute("UPSERT INTO requests (id, patientid, times, description, video, status) VALUES (" + i +", '" + pid + "', '" + times + "', '" + description +"', '" + video + "', '"  + st +"')")
        # logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    return i
    # print ("user added")


def acceptrequest(conn, rid):
    newstatus = "accepted"
    with conn.cursor() as cur:
        cur.execute( "UPDATE requests SET status = %s WHERE id = %s", (newstatus, rid));
        #  "UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, frm)
        conn.commit()

    return 0


def completerequest(conn, rid):
    newstatus = "conpleted"
    with conn.cursor() as cur:
        cur.execute( "UPDATE requests SET status = %s WHERE id = %s", (newstatus, rid));
        #  "UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, frm)
        conn.commit()

    return 0




def add_donation(conn, corpid, amount, date):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM donations")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        i = 1
        for row in rows:
            i = i + 1
        i = str(i)

        st = "donated"
        
        cur.execute("UPSERT INTO donations (id, corpid, amount, date, status) VALUES (" + i +", '" + corpid + "', '" + amount + "', '" + date +"', '"  + st +"')")
        conn.commit()

        cur.execute("SELECT id, donations FROM corporations")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()

        newdon = amount

        for row in rows:
            if row[0] == corpid:
                oldon = int(row[1])
                nd = oldon + int(amount)
                newdon =  str(nd)

        cur.execute( "UPDATE corporations SET donations = %s WHERE id = %s", (newdon, corpid));
        # logging.debug("create_accounts(): status message: %s", cur.statusmessage)

        cur.execute("SELECT id, donated, balance FROM system")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()

        newdon = amount
        newbal = amount

        for row in rows:
            if row[0] == "0":
                oldon = int(row[1])
                oldbal = int(row[2])
                nd = oldon + int(amount)
                newdon =  str(nd)
                ob = oldbal + int(amount)
                newbal = str(ob)

        cur.execute( "UPDATE system SET donated = %s WHERE id = %s", (newdon, "0"));
        conn.commit()
        cur.execute( "UPDATE system SET balance = %s WHERE id = %s", (newbal, "0"));
        conn.commit()
            



    conn.commit()
    return i
    # print ("user added")



def add_places(conn, pname, paddress, lat, lon, ptype, image):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM places")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        i = 1
        for row in rows:
            i = i + 1
        i = str(i)
        
        cur.execute("UPSERT INTO places (id, name, placeaddress, lat, lon, type, img) VALUES (" + i +", '" + pname + "', '" + paddress + "', '" + lat +"', '" + lon + "', '" + ptype +"', '" + image +"')")
        # logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    return i
    # print ("user added")



def add_users(conn, uname, pw, utype, uemail, lat, lon, uaddress):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        i = 1
        for row in rows:
            i = i + 1
        i = str(i)
        
        cur.execute("UPSERT INTO users (id, email, userpassword, usertype, username, lat, lon, useraddress) VALUES (" + i +", '" + uemail + "', '" + pw + "', '" + utype +"', '" + uname + "', '" + lat +"', '" + lon +"', '" + uaddress +"')")
        # logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    return i
    # print ("user added")



def add_doctor(conn, uname, fn, uemail, pw, sp, av, rate):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM doctors")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        i = 1
        for row in rows:
            i = i + 1
        i = str(i)
        
        cur.execute("UPSERT INTO doctors (id, email, password, fullname, username, specialty, availability, rate) VALUES (" + i +", '" + uemail + "', '" + pw + "', '" + fn +"', '" + uname + "', '" + sp +"', '" + av +"', '" + rate+"')")
        # logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    return i
    # print ("user added")


def getdoctorbyid(conn, did):
    with conn.cursor() as cur:
        cur.execute("SELECT id, email, specialty, fullname, availability, rate FROM doctors")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        for row in rows:
            # print(row)
            # print (type(row))
            if row[0] == int(uid):
                # print ("found")
                return True, row[0], row[1], row[2], row[3], row[4], row[5]
        return False, 'none', 'none', '-1', '-1', '-1', '-1'


def add_patient(conn, uname, fn, uemail, pw, eth, gen, zp, ins, pre):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM patients")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        i = 1
        for row in rows:
            i = i + 1
        i = str(i)
        
        cur.execute("UPSERT INTO patients (id, email, password, fullname, username, ethnicity, gender, zipcode, hasinsurance, premium) VALUES (" + i +", '" + uemail + "', '" + pw + "', '" + fn +"', '" + uname + "', '" + eth +"', '" + gen +"', '" + zp +"', '" + ins +"', '" + pre+"')")
        # logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    return i
    # print ("user added")



def login(conn, uemail, pw):
    with conn.cursor() as cur:
        cur.execute("SELECT id, email, userpassword, usertype, username, lat, lon, useraddress FROM users")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        for row in rows:
            # print(row)
            # print (type(row))
            if row[1] == uemail and row[2] == pw:
                # print ("found")
                return True, row[0], row[3], row[4], row[5], row[6], row[7]
        return False, 'none', 'none', '-1', '-1', '-1', '-1', '-1', '-1' 


def getuserbyid(conn, uid):
    with conn.cursor() as cur:
        cur.execute("SELECT id, email, userpassword, usertype, username, lat, lon, useraddress FROM users")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        for row in rows:
            # print(row)
            # print (type(row))
            if row[0] == int(uid):
                # print ("found")
                return True, row[0], row[1], row[3], row[4], row[5], row[6], row[7]
        return False, 'none', 'none', '-1', '-1', '-1', '-1', '-1', '-1' , '-1'





def gettasks(conn, userid):
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, userid, cost, price, items, helperid, status FROM tasks")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        tasks = []

        for row in rows:
            if row[2] != userid:
                continue
             
            place = {}
            place['id'] = row[0]
            place['name'] = row[1]
            place['userid'] = row[2]
            place['cost'] = row[3]
            place['price'] = row[4]
            place['items'] = row[5]
            place['helperid'] = row[6]
            place['status'] = row[7]

            tasks.append(place)

        return tasks 










def getplaces(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, placeaddress, lat, lon, type, img FROM places")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        places = []

        for row in rows:
            place = {}
            place['id'] = row[0]
            place['name'] = row[1]
            place['address'] = row[2]
            place['lat'] = row[3]
            place['lon'] = row[4]
            place['type'] = row[5]
            place['image'] = row[6]

            places.append(place)

        return places 


def delete_users(conn):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM defaultdb.users")
        # logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    with conn.cursor() as cur:
        cur.execute("DROP TABLE users")
        # logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    conn.commit()

    print ("users table deleted")


def purgedb(conn):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM defaultdb.users")
        # logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    with conn.cursor() as cur:
        cur.execute("DROP TABLE users")
        # logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    conn.commit()

    print ("users table deleted")



def dummy(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if request.method == 'OPTIONS':
        # Allows GET requests from origin https://mydomain.com with
        # Authorization header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    }

    request_json = request.get_json()
    conn = connector()
    initialize(conn)

    retjson = {}

    action = request_json['action']
    if action == "createuser" :
        uname = request_json['name']
        pw = request_json['password']
        utype = request_json['type']
        uaddress = request_json['address']
        lat = request_json['lat']
        lon = request_json['lon']
        uemail = request_json['email']

        pid = add_users(conn, uname, pw, utype, uemail, lat, lon, uaddress)

        retjson['status'] = "successfully added"
        retjson['id'] = pid

        return json.dumps(retjson)



    if action == "adddoctor" :
        uname = request_json['username']
        pw = request_json['password']
        fn = request_json['fullname']
        uemail = request_json['email']
        sp = request_json['speciality']
        av = request_json['availability']
        rate = request_json['rate']

        did = add_doctor(conn, uname, fn, uemail, pw, sp, av, rate)

        # pid = add_users(conn, uname, pw, utype, uemail, lat, lon, uaddress)

        retjson['status'] = "successfully added"
        retjson['id'] = did

        return json.dumps(retjson)


    if action == "addappt" :
        pid = request_json['patientid']
        time = request_json['time']
        description = request_json['description']
        video = request_json['video']

        rid = add_request(conn, pid, times, description, video)

        # pid = add_users(conn, uname, pw, utype, uemail, lat, lon, uaddress)

        retjson['status'] = "successfully added"
        retjson['id'] = rid

        return json.dumps(retjson)


    if action == "acceptappt" :
        rid = request_json['appointmentid']
        did = request_json['doctorid']
        pid = request_json['patientid']
        time = request_json['time']
        
        res = acceptrequest(conn, rid)

        res = add_appt(conn, pid, time, did)

        
        retjson['status'] = "scheduled"
        retjson['aid'] = res

        return json.dumps(retjson)



    if action == "createtask" :
        userid = request_json['userid']
        cost = request_json['cost']
        price = request_json['price']
        placeid = request_json['placeid']
        items = request_json['items']
        tname= request_json['name']

        tid = add_tasks(conn, userid, cost, price, placeid, items, tname)
        
        

        retjson['status'] = "successfully added"
        retjson['id'] = tid

        return json.dumps(retjson)


    if action == "createplace" :
        pname = request_json['name']
        ptype = request_json['type']
        paddress = request_json['address']
        lat = request_json['lat']
        lon = request_json['lon']
        image = request_json['image']


        pid = add_places(conn, pname, paddress, lat, lon, ptype, image)

        retjson['status'] = "successfully added"
        retjson['id'] = pid

        return json.dumps(retjson)
    
    if action == "getplaces" :
        places = getplaces(conn)
        
        retjson['status'] = "successfully retrieved"
        retjson['id'] = places

        return json.dumps(retjson)
    

    if action == "gettasksbyhelpee" :
        userid = request_json['userid']
        tasks = gettasks(conn, userid)
        
        retjson['status'] = "successfully retrieved"
        retjson['tasks'] = tasks

        return json.dumps(retjson)



    if action == "pickuptask" :
        helperid = request_json['helperid']
        taskid = request_json['taskid']
        
        res = pendingtask(conn, helperid, taskid)
        retjson['status'] = "task successfully picked up"

        return json.dumps(retjson)
    
    if action == "accepttask" :
        taskid = request_json['taskid']

        res = acceptedtask(conn, taskid)
        
        retjson['status'] = "task successfully accepted"

        return json.dumps(retjson)   


    if action == "completetask" :
        taskid = request_json['taskid']

        res = completedtask(conn, taskid)
        
        retjson['status'] = "task successfully accepted"

        return json.dumps(retjson)    

    

    if action == 'login':
        uemail = request_json['email']
        pw = request_json['password']

        res = login(conn, uemail, pw)

        retjson['status'] = str(res[0])
        retjson['id'] = str(res[1])
        retjson['type'] = str(res[2])
        retjson['name'] = str(res[3])
        retjson['lat'] = str(res[4])
        retjson['lon'] = str(res[5])
        retjson['address'] = str(res[6])
        

        return json.dumps(retjson)



    if action == 'getuserbyid':
        uid = request_json['uid']

        res = getuserbyid(conn, uid)

        retjson['status'] = str(res[0])
        retjson['id'] = str(res[1])
        retjson['email'] = str(res[2])
        retjson['type'] = str(res[3])
        retjson['name'] = str(res[4])
        retjson['lat'] = str(res[5])
        retjson['lon'] = str(res[6])
        retjson['address'] = str(res[7])
        

        return json.dumps(retjson)


    retstr = "action not done"

    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return retstr
