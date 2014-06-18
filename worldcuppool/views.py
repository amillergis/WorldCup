from django.shortcuts import render

from worldcuppool.models import User, Team


def get_picks(request, userID):
    user = User.objects.get(userID=userID)
    picks = []
    picks.append(("16pt",user.pick16.name))
    picks.append(("15pt",user.pick15.name))
    picks.append(("14pt",user.pick14.name))
    picks.append(("13pt",user.pick13.name))
    picks.append(("12pt",user.pick12.name))
    picks.append(("11pt",user.pick11.name))
    picks.append(("10pt",user.pick10.name))
    picks.append(("9pt",user.pick9.name))
    picks.append(("8pt",user.pick8.name))
    picks.append(("7pt",user.pick7.name))
    picks.append(("6pt",user.pick6.name))
    picks.append(("5pt",user.pick5.name))
    picks.append(("4pt",user.pick4.name))
    picks.append(("3pt",user.pick3.name))
    picks.append(("2pt",user.pick2.name))
    picks.append(("1pt",user.pick1.name))

    return render(request, 'picks_table.html', {'picks':picks})

def get_standings(request):
    users = User.objects.all()
    standings_table = {}
    points = {}
    for user in users:      
        points[user] = _calculate_points(user)
    
    rank = 0
    for key, value in sorted(points.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        rank += 1
        standings_table[rank] = (key.userID, key, value)

    return render(request, 'standings_table.html', {'standings_table':standings_table})


def _calculate_points(user):
    points = 0
    if user.pick1.advanced == True:
        points += 5
    points += user.pick1.knockout_wins * 1
    if user.pick2.advanced == True:
        points += 5
    points += user.pick2.knockout_wins * 2
    if user.pick3.advanced == True:
        points += 5
    points += user.pick3.knockout_wins * 3
    if user.pick4.advanced == True:
        points += 5
    points += user.pick4.knockout_wins * 4
    if user.pick5.advanced == True:
        points += 5
    points += user.pick5.knockout_wins * 5
    if user.pick6.advanced == True:
        points += 5
    points += user.pick6.knockout_wins * 6
    if user.pick7.advanced == True:
        points += 5
    points += user.pick7.knockout_wins * 7
    if user.pick8.advanced == True:
        points += 5
    points += user.pick8.knockout_wins * 8
    if user.pick9.advanced == True:
        points += 5
    points += user.pick9.knockout_wins * 9
    if user.pick10.advanced == True:
        points += 5
    points += user.pick10.knockout_wins * 10
    if user.pick11.advanced == True:
        points += 5
    points += user.pick11.knockout_wins * 11
    if user.pick12.advanced == True:
        points += 5
    points += user.pick12.knockout_wins * 12
    if user.pick13.advanced == True:
        points += 5
    points += user.pick13.knockout_wins * 13
    if user.pick14.advanced == True:
        points += 5
    points += user.pick14.knockout_wins * 14
    if user.pick15.advanced == True:
        points += 5
    points += user.pick15.knockout_wins * 15
    if user.pick16.advanced == True:
        points += 5
    points += user.pick16.knockout_wins * 16
    return points