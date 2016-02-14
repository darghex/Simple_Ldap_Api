def show_profile():
    return ['displayName', 'mail', 'telephoneNumber', 'physicalDeliveryOfficeName']


def show_mail():
    return ['mail']


def show_name():
    return ['Name']


def show_dn():
    return ['distinguishedName']


def show_sensitive_data():
    return ['userPrincipalName', 'primaryGroupID', 'sAMAccountType', 'userPrincipalName']


def show_member_of():
    return ['memberOf']
