class api:
    import webbrowser
    import requests
    import time
    cid = '50682'
    secret = ''
    actoken = ''
    retoken = ''
    athid = 0
    exptime = 0
    def __init__(self):
        self.webbrowser.open('http://www.strava.com/oauth/authorize?client_id='+self.cid+'&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read',new = 0)
        print('http://www.strava.com/oauth/authorize?client_id='+self.cid+'&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read')
        code = input()
        data1 =dict(client_id=self.cid,client_secret=self.secret,code=code,grant_type='authorization_code')
        r = self.requests.post('https://www.strava.com/api/v3/oauth/token',data = data1)
        re = r.json()
        self.actoken = re['access_token']
        self.exptime = re['expires_at']
        self.retoken = re['refresh_token']
        self.athid = re['athlete']['id']

    def refresh(self):
        if(self.exptime-self.time.time()<0 or True):
            print('refreshing')
            data =dict(client_id=self.cid,client_secret=self.secret,refresh_token=self.retoken,grant_type='refresh_token')
            response = self.requests.post('https://www.strava.com/api/v3/oauth/token',data = data)
            js = response.json()
            self.actoken = js['access_token']
            self.exptime = js['expires_at']
            self.retoken = js['refresh_token']
        else:
            print('no refresh needed')
    def getMiles(self):
        data = {'Authorization':'Bearer '+self.actoken}
        r = self.requests.get('https://www.strava.com/api/v3/athletes/'+str(self.athid)+'/stats',headers=data)
        js = r.json()
        return(int(js['all_ride_totals']['distance']/1609))
    
