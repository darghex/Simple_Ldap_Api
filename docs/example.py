"""
+++++++++++++++++++++
Examples
+++++++++++++++++++++

Need connect a ip and user with dn type....  then add a password, also can use a alternative port myinstance(ip - DN_user - Pass - alternative port)

* Instance = myldap('192.168.10.28', 'cn=Administrador,cn=Users,dc=ITFIPSALAS,dc=LOCAL', 'Itfip2015')

Save in a varible with the returned data of our search, when want search use a key for example a mail, user, number ... etc could use search_this functions
ldapsearch method help us to get data, Instance.ldapsearch(search_by_mail('mail-to-search@hotmail.com') - alternative domain)
the alternative domain, is default your domain that you used construct the connection

* query = Instance.ldapsearch(search_by_name('admin'),domain='ITFIPSALAS.LOCAL')

 or

* query = Instance.ldapsearch(search_by_name('admin'),domain='dc=ITFIPSALAS,dc=local')

now should extract data of our query, will use getsearch function, should put the query and then the data to search

* getsearch(query, data to search) > for search data use the show_this functions

another thing that you must know, the obtained data of getsearch is easily manageable with indices example[0][1][0]..... more indices..

* print Instance.getsearch(query,show_mail())
"""