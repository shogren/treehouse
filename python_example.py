import mandrill
mandrill_client = mandrill.Mandrill('API-KEY-GOES-HERE')

m = mandrill.Mandrill('API-KEY-GOES-HERE')

try:
    mandrill_client = mandrill.Mandrill('API-KEY-GOES-HERE')
    message = {
        'from_email': 'jonshogren@mac.com',
        'from_name': 'Jon Shogren',
        'headers': {'Reply-To': 'jonshogren@mac.com'},
        'html': '<p>Man I hope this works!</p>',
        'subject': 'Test Send from Python',
        'text': 'Man I hope this works!',
        'to': [{'email': 'jonathanshogren@gmail.com',
                'name': 'Jonathan Shogren',
                'type': 'to'}],
        }     
    result = mandrill_client.messages.send(message=message, async=False,send_at='1437055128'))
    '''
    [{'_id': 'abc123abc123abc123abc123abc123',
        'email': 'recipient.email@example.com',
        'reject_reason': 'hard-bounce',
        'status': 'sent'}]
    '''

except mandrill.Error, e:
    # Mandrill errors are thrown as exceptions
    print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
    # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'    
    raise
