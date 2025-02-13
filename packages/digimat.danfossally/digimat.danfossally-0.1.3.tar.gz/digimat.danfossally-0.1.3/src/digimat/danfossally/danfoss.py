# https://developer.danfoss.com/docs/ally/1/overview

# Open port 8886/TCP OUTGOING
# IP address: 3.121.210.75

import time
import logging
import logging.handlers

import pkg_resources

# import pprint
from prettytable import PrettyTable

import requests
from requests.auth import HTTPBasicAuth

# Warning : refreshing devices one by one with device.refresh() is a *lot*
# longer than refreshing the hole system with danfoss.refrehs()


class DanfossLogger(object):
    def __init__(self, title="DANFOSS"):
        self._title=title

    def create(self):
        return logging.getLogger(self._title)

    def tcp(self, level=logging.DEBUG, host='localhost'):
        logger=self.create()
        logger.setLevel(level)
        handler=logging.handlers.SocketHandler(host, logging.handlers.DEFAULT_TCP_LOGGING_PORT)
        logger.addHandler(handler)
        return logger

    def null(self):
        logger=self.create()
        logger.setLevel(logging.ERROR)
        handler=logging.NullHandler()
        logger.addHandler(handler)
        return logger


class DanfossDevice(object):
    def __init__(self, api, data):
        self._api=api
        self._did=None
        self._name=None
        self._stamp=0
        self._status=None
        self._online=False
        self.initFromData(data)

    def initFromData(self, data):
        self._did=data['id']
        self._name=data['name']
        self._type=data['device_type']
        self.logger.info('Declaring device %s:%s (%s)' % (self.did, self.name, self.type))
        try:
            self.storeStatus(data['status'])
        except:
            pass

    def isMatching(self, key):
        if self._did==key:
            return True
        if key.lower() in self._name.lower():
            return True
        if key.lower() in self._did.lower():
            return True

    def isMatchingType(self, dtype):
        try:
            if dtype.lower() in self.type.lower():
                return True
        except:
            pass
        return False

    def setOnline(self, state=True):
        self._online=state

    def isOnline(self):
        return self._online

    @property
    def api(self):
        return self._api

    @property
    def logger(self):
        return self.api.logger

    @property
    def did(self):
        return self._did

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def status(self):
        return self._status

    @property
    def fault(self):
        try:
            if self._fault:
                return True
            return False
        except:
            pass
        return False

    def isError(self):
        try:
            if not self.isOnline():
                return True
            if self._status is None or self.age()>600:
                return True
            if self._fault:
                return True
        except:
            pass
        return False

    def age(self):
        return time.time()-self._stamp

    def decodeStatus(self, code, value):
        if code=='battery_percentage':
            self._battery=float(value)
        if code=='fault':
            self._fault=False
            if int(value)>0:
                self._fault=True

    def storeStatus(self, status):
        try:
            if status:
                self._status=status
                self._stamp=time.time()
                # self.logger.debug('device %s status updated' % self.did)
                if status:
                    for data in status:
                        code=data['code']
                        value=data['value']
                        self.decodeStatus(code, value)
                return status
        except:
            self.logger.exception('storeStatus()')

    def retrieveStatus(self, force=False):
        try:
            if force or self.age()>60:
                data=self.api.doGET('devices/%s/status' % self.did)['result']
                return self.storeStatus(data)
        except:
            pass

    def refresh(self):
        self.retrieveStatus(True)

    def manager(self):
        if self.age()>5*60:
            self.refresh()

    @property
    def battery(self):
        self.manager()
        try:
            return self._battery
        except:
            pass

    def __repr__(self):
        try:
            return '<%s(name=%s, B:%d%%, %ds)>' % (self.__class__.__name__, self.name,
                    self.battery, self.age())
        except:
            return '<%s(name=%s)>' % (self.__class__.__name__, self.name)

    def table(self, key=None):
        if self._status:
            t=PrettyTable()
            t.field_names = ['property', 'value']
            t.align['property']='l'
            t.align['value']='l'

            for data in self._status:
                code=data['code']
                value=data['value']
                if key and key not in code:
                    continue
                t.add_row([code, value])

            print(t)

    def strvalue(self):
        pass


# radiator
class DanfossThermostat(DanfossDevice):
    def decodeStatus(self, code, value):
        super().decodeStatus(code, value)
        if code=='temp_current':
            self._temperature=float(value)/10
        elif code=='temp_set':
            self._setpoint=float(value)/10
        elif code=='mode':
            self._mode=value
        elif code=='window_state':
            self._window=True
            if value=='close':
                self._window=False
        elif code=='room_sensor':
            self._roomsensor=bool(value)
        elif code=='ext_measured_rs':
            value=float(value)/100
            self._tref=value
        elif code=='work_state':
            self._workstate=value

    @property
    def temperature(self):
        self.manager()
        try:
            return self._temperature
        except:
            pass

    @temperature.setter
    def temperature(self, value):
        try:
            value=int(float(value)*10)
            data={'commands': [{'code': 'temp_set', 'value': value}]}
            self.api.doPOST('devices/%s/commands' % self.did, data)
        except:
            pass

    @property
    def t(self):
        if self.tref is not None:
            return self.tref
        return self.temperature

    @t.setter
    def t(self, value):
        self.temperature=value

    @property
    def sp(self):
        try:
            return self._setpoint
        except:
            pass

    @sp.setter
    def sp(self, value):
        self.temperature=value

    @property
    def tref(self):
        self.manager()
        try:
            if self._tref>0:
                return self._tref
        except:
            pass

    @property
    def mode(self):
        self.manager()
        try:
            return self._mode
        except:
            pass

    def isModeComfort(self):
        try:
            if self.mode=='at_home':
                return True
        except:
            pass
        return False

    def isModePause(self):
        try:
            if self.mode=='pause':
                return True
        except:
            pass
        return False

    @property
    def state(self):
        self.manager()
        try:
            return self._workstate
        except:
            pass

    def isHeating(self):
        try:
            if self.state=='Heat':
                return True
        except:
            pass
        return False

    @property
    def window(self):
        self.manager()
        try:
            return self._window
        except:
            pass

    def __repr__(self):
        try:
            return '<%s(name=%s, t=%.01f/SP=%.01f, comfort=%d, %d%%, %ds)>' % (self.__class__.__name__, self.name,
                    self.t, self.setpoint, self.isModeComfort(),
                    self.battery, self.age())
        except:
            return '<%s(name=%s)>' % (self.__class__.__name__, self.name)

    def strvalue(self):
        value=''
        if self.t is not None:
            value+='%.01fC' % (self.t)
        if self.isHeating():
            value+='+'
        if self.battery<20:
            value+='!'
        if self.isError():
            value+='E'
        return value


class DanfossIcon2Thermostat(DanfossThermostat):
    pass


class DanfossRoomSensor(DanfossDevice):
    def decodeStatus(self, code, value):
        super().decodeStatus(code, value)
        # self.logger.warning("%s %s" % (code, value))
        if code=='temp_current':
            self._temperature=float(value)/10
        elif code=='humidity_value':
            self._humidity=float(value)/10

    @property
    def temperature(self):
        self.manager()
        try:
            return self._temperature
        except:
            pass

    @property
    def t(self):
        return self.temperature

    @property
    def humidity(self):
        self.manager()
        try:
            return self._humidity
        except:
            pass

    @property
    def hr(self):
        return self.humidity

    def __repr__(self):
        try:
            return '<%s(name=%s, t=%.01f, h=%d%%, B:%d%%, %ds)>' % (self.__class__.__name__, self.name,
                    self.temperature, self.humidity, self.battery, self.age())
        except:
            return '<%s(name=%s)>' % (self.__class__.__name__, self.name)

    def strvalue(self):
        value=''
        if self.temperature is not None:
            value += '%.01fC' % (self.temperature)
        if self.isError():
            value += 'E'
        return value


class DanfossAlly(object):
    API_URL='https://api.danfoss.com'

    def __init__(self, key=None, secret=None, logger=None, debug=False):
        requests.packages.urllib3.disable_warnings()
        self._debug=debug
        if logger is None:
            logger=DanfossLogger().tcp()
        self._logger=logger
        self._key=None
        self._secret=None
        self._token=None
        self._timeoutToken=0

        self._devices=[]
        self._devicesById={}
        self._devicesByName={}
        self._devicesByType={}

        self.auth(key, secret)

    def debug(self, state=True):
        self._debug=state

    def nodebug(self):
        self.debug(False)

    def isDebug(self):
        if self._debug:
            return True
        return False

    def getVersion(self):
        try:
            distribution=pkg_resources.get_distribution('digimat.danfossally')
            return distribution.parsed_version
        except:
            pass

    @property
    def version(self):
        return self.getVersion()

    @property
    def logger(self):
        return self._logger

    def token(self):
        if not self._key or not self._secret:
            return None

        if not self._token or time.time()>self._timeoutToken:
            payload={'grant_type': 'client_credentials'}
            # payload={'grant_type': 'client_credentials', 'client_id': self._key, 'client_secret': self._secret}

            try:
                self.logger.info('Acquiring OAUTH2 token (%s)...' % self._key)
                r=requests.post('%s/oauth2/token' % self.API_URL,
                    auth=HTTPBasicAuth(self._key, self._secret),
                    data=payload)
                if r and r.ok:
                    data=r.json()
                    self._token=data['access_token']
                    self._timeoutToken=time.time()+int(data['expires_in'])-60
                    self.logger.debug('Access token is %s', self._token)
                else:
                    self.logger.error('Unable to retrieve token')
            except:
                self.logger.exception('token()')

        return self._token

    def reset(self):
        self.logger.info('Reset access token')
        self._token=None

    def auth(self, key=None, secret=None):
        self.logger.info('auth()')
        if key:
            self._key=key
            if secret:
                self._secret=secret

        self.reset()
        if self.token():
            return True
        return False

    def url(self, path=None):
        url='%s/ally' % self.API_URL
        if path:
            url+='/%s' % path
        return url

    def headers(self):
        return {'Accept': 'application/json',
            'Authorization': 'Bearer %s' % self.token()}

    def doGET(self, path, retry=3):
        try:
            while retry>0:
                url=self.url(path)
                self.logger.debug('GET %s' % (url))
                r=requests.get(url, headers=self.headers())
                if r:
                    if r.ok:
                        data=r.json()
                        return data

                self.logger.error(r.content)
                self.reset()
                retry-=1
                time.sleep(0.3)
        except:
            self.logger.exception('get()')

    def doPOST(self, path, data, retry=3):
        try:
            while retry>0:
                url=self.url(path)
                self.logger.debug('POST %s %s' % (url, data))
                r=requests.post(url, headers=self.headers(), json=data)
                if r:
                    if r.ok:
                        data=r.json()
                        return data

                self.logger.error(r.content)
                self.reset()
                retry-=1
                time.sleep(0.3)
        except:
            self.logger.exception('post()')

    def device(self, did):
        try:
            return self._devicesById[did]
        except:
            pass
        try:
            return self._devicesByName[did]
        except:
            pass

        if self._devices:
            for device in self._devices:
                if device.isMatching(did):
                    return device

    # FIXME: useful ?
    # def __getitem__(self, key):
        # return self.device(key)

    def devices(self):
        return self._devices

    def getDevicesFromType(self, dtype, key=None):
        devices=[]
        if self._devices:
            for device in self._devices:
                if device.isMatchingType(dtype):
                    if not key or device.isMatching(key):
                        devices.append(device)
        return devices

    def getDevicesSensor(self, key=None):
        return self.getDevicesFromType('room sensor', key)

    def sensor(self, key):
        try:
            return self.getDevicesSensor(key)[0]
        except:
            pass

    def getDevicesRadiatorThermostat(self, key=None):
        return self.getDevicesFromType('radiator thermostat', key)

    def radiator(self, key):
        try:
            return self.getDevicesRadiatorThermostat(key)[0]
        except:
            pass

    def getDevicesIcon2Thermostat(self, key=None):
        return self.getDevicesFromType('icon2 rt', key)

    def icon2(self, key):
        try:
            return self.getDevicesIcon2Thermostat(key)[0]
        except:
            pass

    def all(self):
        return self.devices()

    def refresh(self):
        self.retrieveDevices()

    def count(self):
        return len(self._devices)

    def retrieveDevices(self):
        try:
            data=self.doGET('devices')['result']
        except:
            return None

        for devdata in data:
            # import pprint
            # pprint.pprint(devdata)
            did=devdata['id']
            device=self.device(did)
            online=devdata['online']

            if not device:
                if devdata['status']:
                    dtype=devdata['device_type']

                    device=None
                    if 'Radiator Thermostat' in dtype:
                        device=DanfossThermostat(self, devdata)
                    elif 'Room Sensor' in dtype:
                        device=DanfossRoomSensor(self, devdata)
                    elif 'Icon2 RT' in dtype:
                        device=DanfossIcon2Thermostat(self, devdata)
                    else:
                        self.logger.warning('No class found to handle device type %s, using generic one' % dtype)
                        device=DanfossDevice(self, devdata)

                    if device:
                        device.setOnline(online)
                        self._devices.append(device)
                        self._devicesById[did]=device
                        self._devicesByName[device.name]=device
                        if device.type not in self._devicesByType:
                            self._devicesByType[device.type]=[]
                        self._devicesByType[device.type].append(device)
            else:
                try:
                    device.storeStatus(devdata['status'])
                    device.setOnline(online)
                except:
                    pass

        return self._devices

    def __repr__(self):
        return '<%s(%d devices)>' % (self.__class__.__name__, self.count())

    def table(self, key=None):
        if self._devices:
            t=PrettyTable()
            t.field_names = ['device', 'type', 'id', 'name', 'strvalue', 'age']
            t.align['device']='l'
            t.align['type']='l'
            t.align['id']='l'
            t.align['name']='l'

            for device in self._devices:
                if key and not device.isMatching(key):
                    continue

                age='%.01fs' % device.age()
                t.add_row([device.__class__.__name__,
                           device.type,
                           device.did,
                           device.name,
                           device.strvalue(),
                           age])

            print(t)


if __name__ == "__main__":
    pass
