#! /usr/bin/env python

import ldap

def main():
    server = "200.19.106.8"
    who = ""
    cred = ""
    keyword = "ryan"
    
    try:
        l = ldap.open(server)
        l.simple_bind_s(who, cred)
        print "Successfully bound to server.\n"
        print "Searching..\n"
        my_search(l, keyword)
    except ldap.LDAPError, error_message:
        print "Couldn't Connect. %s " % error_message

def my_search(l, keyword):
    base = ""
    scope = ldap.SCOPE_BASE
    #filter = "cn=" + "*" + keyword + "*"
    filter = "objectclass=*"
    retrieve_attributes = None
    count = 0
    result_set = []
    timeout = 0
    try:
        result_id = l.search(base, scope, filter, retrieve_attributes)
        while 1:
            result_type, result_data = l.result(result_id, timeout)
            if (result_data == []):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)
        if len(result_set) == 0:
            print "No Results."
            return 
        for i in range(len(result_set)):
            for entry in result_set[i]:                 
                try:
                    name = entry[1]['cn'][0]
                    email = entry[1]['mail'][0]
                    phone = entry[1]['telephonenumber'][0]
                    desc = entry[1]['description'][0]
                    count = count + 1
                    print "%d.\nName: %s\nDescription: %s\nE-mail: %s\nPhone: %s\n" %\
                           (count, name, desc, email, phone)
                except:
                    pass
    except ldap.LDAPError, error_message:
        print error_message

if __name__ == '__main__':
    main()
