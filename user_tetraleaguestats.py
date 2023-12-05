import requests

names=(input ('Tetrio username (for multiple people, put space inbetween names): ')) #tetrio usernames, make sure username is exactly correct
list= names.split() #makes input into list 


for user in list: 
    try:
        response= requests.get('https://ch.tetr.io/api/users/'+user) #finds api
        userstats= response.json() #makes into library (i think)
        userrank= str(userstats['data']['user']['league']['rank'])#finds rank in api
        if userrank=='z': 
            userrank=userrank.replace ('z','?') #people with no current tl rank (rd is over 100) will be marked as z but made as question mark as is more commonly known
        userrating= str(round((userstats['data']['user']['league']['rating']),2))#finds tr
        userpps= (userstats['data']['user']['league']['pps'])#finds pieces per second
        userapm= (userstats['data']['user']['league']['apm'])#finds attack per minute
        uservs= str(userstats['data']['user']['league']['vs'])#finds vs score
        userapp= str(round((userapm/userpps/60),3))#calculates attack per piece and rounds to 3 decimal palces
        
        print (f'{user}: {userrank.upper()}, {userrating}TR, {str(userpps)}pps, {str(userapm)}apm, {uservs}vs, {userapp}APP')
    except: print('TL stats for '+ user + ' unavailable.') #for errors (mistyped name or user doesn't have tetra league stats)