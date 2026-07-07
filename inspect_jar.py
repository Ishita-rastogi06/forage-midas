import zipfile
jar = 'services/transaction-incentive-api.jar'
with zipfile.ZipFile(jar) as z:
    names = [n for n in z.namelist() if n.endswith('.class') and ('Controller' in n or 'Incentive' in n or 'Transaction' in n)]
    print('\n'.join(names[:200]))
    print('---')
    for name in z.namelist():
        if name.endswith('SerializableTransaction.class'):
            print(name)
            break
