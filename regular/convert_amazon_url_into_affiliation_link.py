def generate_affiliation_link(url):
    _, sep, suffix = url.partition('/dp/')
    if sep != '/dp/':
        raise ValueError('Invalid affiliation url')

    asin = suffix.partition('/')[0]
    return f'http://www.amazon.com/dp/{asin}/?tag=pyb0f-20'
