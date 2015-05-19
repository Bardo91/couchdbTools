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
    
def showDatabaseContent(_server):
    dbName = input('Type db Name: ');
    #EXAMPLE OF QUERY
    map_fun = '''function(doc) { if (doc.type == 'Person') emit(doc.name, null); }'''
    db = _server[dbName];
    db.query(map_fun);
    for doc in db:
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
    print('Not implemeted now');

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
            showDatabaseContent(server)
        elif cmd == '3':
            createDatabase(server);
        elif cmd == '4':
            deleteDatabase(server);
        elif cmd == '5':
            addDoc(server);

if __name__ == "__main__":
    main();
