"""
++++++++++++++++++++++++++++++++++++
show for getsearch function
++++++++++++++++++++++++++++++++++++
"""


def show_profile():
    """show_profile() -> array """
    return ['displayName', 'mail', 'telephoneNumber', 'physicalDeliveryOfficeName']


def show_mail():
    """show_mail() -> array """
    return ['mail']


def show_name():
    """show_name() -> array """
    return ['Name']


def show_dn():
    """show_dn() -> array """
    return ['distinguishedName']


def show_sensitive_data():
    """show_sensitive_data() -> array """
    return ['userPrincipalName', 'primaryGroupID', 'sAMAccountType', 'userPrincipalName']


def show_member_of():
    """show_member_of() -> array """
    return ['memberOf']
