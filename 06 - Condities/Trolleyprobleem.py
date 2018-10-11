hendel_trekken = input('Trek aan de hendel van de wissel? (ja/nee) ')
man_duwen = input('Man van brug duwen? (ja/nee) ')
if hendel_trekken == 'ja' and man_duwen == 'ja':
    print(2)
if hendel_trekken == 'ja' and man_duwen == 'nee':
    print(1)
if hendel_trekken == 'nee' and man_duwen == 'ja':
    print(1)
if hendel_trekken == 'nee' and man_duwen == 'nee':
    print(5)

