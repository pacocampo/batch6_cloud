config = {
    'CONTEXT': 'We are in project context',
    'ProjectName': 'Silly Naming project',
    'ProjectId': 'qwerty123456',
    'ProjectOwner': 'Me, myself and I',
    'ProjectAbbreviation': 'SNP',
    'InstanceMin': '1',
    'InstanceMax': '3',
    # This in an example which would not work with simple dictionary.update() NOTE: use in depth recursive merge in helper class.
    'HQ_Address': {
        'City': 'Edinburgh'
    }
}
