## import couch
import couchdb

def printOptions():
    print('---------------------------------------------------------------');
    print('What do you want to do?');
    print('\t 0. Exit');
    print('\t 1. Show Databases');
    print('\t 2. Show Database content');
    print('\t 3. Create a new database');
    print('\t 4. Delete a database');
    print('\t 5. Add doc to a database');
    

def showDatabases(_server):
    for db in _server:
        print(db);
    
def queryDatabase(_server):
    dbName = input('Type db Name: ');
    key = input('Type the key that need to have docs: ');
    #EXAMPLE OF QUERY
    tilde = '\'';
    map_fun = '''function(doc) { var name, type; if (doc.''' + key + '''){key = doc.''' + key + '''; emit(key,doc)} }'''
    print('Using this query: ' + map_fun);
    db = _server[dbName];
    result = db.query(map_fun);
    for doc in result:
        print(doc);
    

def createDatabase(_server):
    dbName = input('Type db Name: ');
    _server.create(dbName);
    print('Created database: ' + dbName);

def deleteDatabase(_server):
    dbName = input('Type db Name: ');
    _server.delete(dbName);
    print('Deleted database: ' + dbName);

def addDoc(_server):
    dbName = input('Type db Name: ');
    dict = {};
    n = input('How many keys will have the doc?')
    for x in range(0, int(n)):
        key = input('Type key of parameter to be added: ');
        value = input('Type value of the given key: ');
        dict[key] = value;	
    db = _server[dbName];
    db.save(dict);

def main():
    ## Create a handle of server
    ## server = pycouchdb.Server('http://example.com:5984/');
    server = couchdb.Server();    ## Without arguments localhost 5984
    
    cmd = '999';
    while cmd != '0':
        printOptions();
        cmd = input('');
        if cmd == '1':
            showDatabases(server)
        elif cmd == '2':
            queryDatabase(server)
        elif cmd == '3':
            createDatabase(server);
        elif cmd == '4':
            deleteDatabase(server);
        elif cmd == '5':
            addDoc(server);

if __name__ == "__main__":
    main();
