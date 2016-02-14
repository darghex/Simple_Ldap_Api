# /usr/bin/env python 2.7

import ldap

from functions.convert import *
from functions.show_this import *
from functions.search_this import *


class myldap(object):
    attributedb = ['displayName','company','mail','telephoneNumber']
    domain = ''
    generaldn = ''

    def __init__(self, ip, dn, password, port='389'):
        myldap.domain = to_domain(dn)
        myldap.generaldn = dn
        self.__connect(ip,dn,password,port)

    def __connect(self, ip, dn, password, port):
        """

        ip should be a string
        dn shouldn't have spaces
        password you must specify
        """
        try:
            self.conn=ldap.initialize("ldap://"+ip+":"+port)
            self.conn.simple_bind(dn, password)  # simple bind changed
            print self.conn.whoami_s()
        except:
            print('Error al conectar a ldap')

    def ldapsearch(self, attributeandsearch, **kwargs):
        """

        ldapsearch(self,attributeandsearch, **kwargs) -> dict

        This method return a dict with the information wich will be extracted with another method

        atrributeandsearch: is a tuple (x=n) where x is the attribute and n the value for search.. For example
        I want search (mail=narvaez@hotmail.com) or you can use, the 'search methods' stored in search_methods module...
        with methods only should write, search_by_mail(narvaez@hotmail.com)...according select function

        **kwargs could specify the domain that you want use, for example, ... domain='dc=itfip,dc=local'
        or anything url, domain='www.myexample.com'
        """
        try:
            self.conn.protocol_version = ldap.VERSION3
            self.conn.set_option(ldap.OPT_REFERRALS,0)
            if kwargs.has_key('domain'):  # if found the parameter 'domain'
                if is_domain_dn(kwargs['domain']):  # verify if is a valid domain
                    base = kwargs['domain']  # change default domain which is specified at the beginning
                elif is_domain_url(kwargs['domain']):
                    newdn = to_distinguished_name(kwargs['domain'])
                    print(newdn)
                    base = newdn
                else:
                    raise NameError('Has escrito un dominio invalido, asegurate de no tener espacios, por ejemplo dc=ejemplo,dc=com')
            else:
                base = myldap.domain  # default domain
            criteria = attributeandsearch
            result = self.conn.search_s(base,ldap.SCOPE_SUBTREE,criteria)
            results = [entry for dn,entry in result if isinstance(entry,dict)]
            if not results:  # if is empty return 0 because not found the search... similar that, "if results == []"
                return 0
            return results[0]
        finally:
            pass
            #self.conn.unbind(), changed because need the conections for ldapadd

    def ldapadd(self, domain = ''):
        #experimental
        user_info = {'uid':'barney123',
                    'givenname':'Barney',
                    'cn':'barney123',
                    'sn':'Smith',
                    'telephonenumber':'123-4567',
                    'facsimiletelephonenumber':'987-6543',
                    'objectclass':('Remote-Address','person', 'Top'),
                    'physicaldeliveryofficename':'Services',
                    'mail':'fred123@company.com',
                    'title':'programmer',
                    }

        mymodlist = {"objectClass": ["inetOrgPerson",
                                   "posixAccount", "shadowAccount"],
                                   "uid": ["maarten"],
                                   "sn": ["De Paepe"],
                                   "givenName": ["Maarten"],
                                   "cn": ["Maarten De Paepe"],
                                   "displayName": ["Maarten De Paepe"],
                                   "uidNumber": ["5000"],
                                   "gidNumber": ["10000"],
                                   "loginShell": ["/bin/bash"],
                                   "homeDirectory": ["/home/maarten"]}
        attrs = {}
        attrs['objectclass'] = ['top','organizationalRole','simpleSecurityObject']
        attrs['cn'] = 'replica'
        attrs['userPassword'] = 'aDifferentSecret'
        attrs['description'] = 'User object for replication using slurpd'

        add_record = [
         ('objectclass', ['person','organizationalperson','inetorgperson']),
         ('uid', ['francis']),
         ('cn', ['Francis Bacon']),
         ('sn', ['Bacon']),
         ('userpassword', ['secret']),
         ('ou', ['estudiantes'])
        ]

        data = [(x,v) for x,v in user_info.items()]
        dn='cn=Users,dc=ITFIPSALAS,dc=LOCAL'
        #self.conn.add_s('uid=Administrador,cn=Users,dc=ITFIPSALAS,dc=LOCAL','uid=Administrador,cn=Users,dc=ITFIPSALAS,dc=LOCAL')
        #ldif = modlist.addModlist(data)
        self.conn.add_s('uid=francis,ou=estudiantes,dc=ITFIPSALAS,dc=LOCAL', add_record)
        #modlist.addModlist(user_info)
        #self.conn.unbind()

    #@staticmethod
    def getsearch(self, ldapsearch, attributetosearch = attributedb):  # method(), ['mail','displayName','is you want, you can use another attributes that you specified in the ldapsearch method']
        """

        getsearch(self, ldapsearch, attributetosearch=attributedb) -> array

        this method can return a array with the found information in the search, but need to ldapsearch data,
        and another parameter for obtain the information

        for example:
        x=[['mail', ['narvaez@hotmail.com']], ['displayName', ['B2-E1']]]

        where X is the result and you can use X[0][1][0]
        and it should print the mail.. as narvaez@hotmail.com


        attributetosearch: should be a array, and you must specify the attribute what want you search, for example
        ['displayName'], but you could use, the 'show methods', stored in show_methods module
        """
        separador = ldapsearch
        if separador != 0:
            foundit = []
            for key, x in separador.iteritems():
                for atrib in attributetosearch:
                    if key.lower() == atrib.lower():  # convert to lower for insensitive case
                        foundit.append([key, x])
            return foundit
        else:
            print 'Lo sentimos lo que has buscado no ha sido encontrado'


#Nop = myldap('192.168.10.28', 'cn=Administrador,cn=Users,dc=ITFIPSALAS,dc=LOCAL', 'Itfip2015')
#print('fin')
#consulta = Nop.ldapsearch(search_by_name('admin'),domain='WWW.ITFIPSALAS.LOCAL')
#print Nop.getsearch(consulta,show_mail())


#Nop.ldapadd()
