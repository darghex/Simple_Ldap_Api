"""
++++++++++++++++++++++++++++++++++++
search for ldapsearch function
++++++++++++++++++++++++++++++++++++
"""


def search_by_mail(mail):
    """search_by_mail(mail) -> String """
    return 'mail='+mail


def search_by_number(number):
    """search_by_number(number) -> String """
    return 'telephoneNumber='+number


def search_by_name(name):
    """search_by_name(name) -> String """
    return 'name='+name
