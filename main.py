import webbrowser
repetitions = int(input('''How many barcodes you want,
remember that the program each time generates 10 barcodes: '''))
data = '123400000001%0A123400000002%0A123400000003%0A123400000004%0A123400000005%0A123400000006%0A123400000007%0A123400000008%0A123400000009%0A123400000010'
data = (data.split('%0A'))
i = 0
for time in range(repetitions):
    new_link = 'https://barcode.tec-it.com/barcode.ashx?data='
    for item in data:
        item = int(item)
        item += i
        item = str(item)
        #print(item)
        new_link += item+'%0A'
    new_link = new_link[:-3]
    i += 10
    new_link += '&code=EAN13&multiplebarcodes=true&unit=Fit&dpi=600&imagetype=Jpg&modulewidth=0.254&download=true'
    webbrowser.open(new_link)
