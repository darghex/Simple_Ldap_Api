# /usr/bin/env python 2.7


def to_domain(dn):

    import re
    dn = dn.split(',')
    domain = []
    dnsearch = re.compile(r'^dc=')
    for x in dn:
        if dnsearch.search(x):
            domain.append(x)
    domain = ','.join(domain)
    return domain


def to_distinguished_name(domain_url):

    domain_url = domain_url.split('.')
    dn = []
    for x in domain_url:
        if not (x == 'www' or x == 'WWW'):
            dn.append('dc='+x)
    dn = ','.join(dn)
    return dn


def is_domain_dn(dn):

    import re
    exp = r"((dc=[a-zA-Z0-9\-]+[\,]{1})+(dc=[a-zA-Z0-9\-]+)$)"
    dnsearch = re.compile(exp)
    if dnsearch.search(dn):
        return True
    else:
        return False


def is_domain_url(domain_url):

    import re
    www = re.compile(r"(([a-zA-Z0-9\-]+[\.]{1})+([a-zA-Z0-9\-]+)$)")
    if www.search(domain_url):
        return domain_url
    else:
        return False
