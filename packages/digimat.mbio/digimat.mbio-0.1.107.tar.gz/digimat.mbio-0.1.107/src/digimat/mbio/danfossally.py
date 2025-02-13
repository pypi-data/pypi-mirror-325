#!/bin/python

from .task import MBIOTask
from .xmlconfig import XMLConfig


from digimat.danfossally import DanfossAlly


class MBIOTaskDanfossAlly(MBIOTask):
    def initName(self):
        return 'ally'

    def onInit(self):
        self._danfoss=DanfossAlly(logger=self.logger)
        self._devices={}
        self._sensors={}
        self._radiators={}
        self._icons={}

        self.config.set('refreshperiod', 60)
        self.config.set('key')
        self.config.set('secret')
        self._timeoutRefresh=0
        self.valueDigital('comerr', default=False)

    def onLoad(self, xml: XMLConfig):
        self.config.update('refreshperiod', xml.getInt('refresh', vmin=60))

        self.config.set('key', self.pickleRead('key'))
        self.config.update('key', xml.get('key'))
        self.pickleWrite('key', self.config.key)

        self.config.set('secret', self.pickleRead('secret'))
        self.config.update('secret', xml.get('secret'))
        self.pickleWrite('secret', self.config.secret)

        items=xml.children('sensor')
        if items:
            for item in items:
                name=item.get('name')
                if name and not self._devices.get(name):
                    did=item.get('id') or name
                    data={'id': did}
                    data['t']=self.value('%s_t' % name, unit='C', resolution=0.1)
                    data['hr']=self.value('%s_hr' % name, unit='%', resolution=1)
                    data['bat']=self.value('%s_bat' % name, unit='%', resolution=1)
                    self._devices[name]=data
                    self._sensors[did]=data

        items=xml.children('radiator')
        if items:
            for item in items:
                name=item.get('name')
                if name and not self._devices.get(name):
                    did=item.get('id') or name
                    data={'id': did}
                    data['t']=self.value('%s_t' % name, unit='C', resolution=0.1)
                    data['sp']=self.value('%s_sp' % name, unit='C', resolution=0.1, writable=True)
                    data['bat']=self.value('%s_bat' % name, unit='%', resolution=1)
                    data['heat']=self.valueDigital('%s_heat' % name)
                    self._devices[name]=data
                    self._radiators[did]=data

        items=xml.children('icon2')
        if items:
            for item in items:
                name=item.get('name')
                if name and not self._devices.get(name):
                    did=item.get('id') or name
                    data={'id': did}
                    data['t']=self.value('%s_t' % name, unit='C', resolution=0.1)
                    data['sp']=self.value('%s_sp' % name, unit='C', resolution=0.1, writable=True)
                    data['bat']=self.value('%s_bat' % name, unit='%', resolution=1)
                    data['heat']=self.valueDigital('%s_heat' % name)
                    self._devices[name]=data
                    self._icons[did]=data

    def refresh(self):
        if self._danfoss.refresh():
            self._timeoutRefresh=self.timeout(self.config.refreshperiod)
            return True

        self._timeoutRefresh=self.timeout(15)
        return False

    def poweron(self):
        self._danfoss.auth(self.config.key, self.config.secret)
        return True

    def poweroff(self):
        return True

    def run(self):
        # sync
        for item in self._radiators.values():
            self.microsleep()
            value=item['sp']
            if value.isPendingSync():
                device=self._danfoss.radiator(item['id'])
                if device:
                    device.sp=value.toReachValue
                    value.clearSyncAndUpdateValue()

        for item in self._icons.values():
            self.microsleep()
            value=item['sp']
            if value.isPendingSync():
                device=self._danfoss.icon2(item['id'])
                if device:
                    device.sp=value.toReachValue
                    value.clearSyncAndUpdateValue()

        # refresh
        if self.isTimeout(self._timeoutRefresh):
            self.refresh()

            error=False

            for item in self._sensors.values():
                self.microsleep()
                device=self._danfoss.sensor(item['id'])
                if device and not device.isError():
                    item['t'].updateValidValue(device.t)
                    item['hr'].updateValidValue(device.hr)
                    item['bat'].updateValidValue(device.battery)
                else:
                    item['t'].setError(True)
                    item['hr'].setError(True)
                    item['bat'].setError(True)
                    error=True

            for item in self._radiators.values():
                self.microsleep()
                device=self._danfoss.radiator(item['id'])
                if device and not device.isError():
                    item['t'].updateValidValue(device.tref)
                    item['sp'].updateValidValue(device.sp)
                    item['bat'].updateValidValue(device.battery)
                    item['heat'].updateValidValue(device.isHeating())
                else:
                    item['t'].setError(True)
                    item['sp'].setError(True)
                    item['bat'].setError(True)
                    item['heat'].setError(True)
                    error=True

            for item in self._icons.values():
                self.microsleep()
                device=self._danfoss.icon2(item['id'])
                if device and not device.isError():
                    item['t'].updateValidValue(device.t)
                    item['sp'].updateValidValue(device.sp)
                    item['bat'].updateValidValue(device.battery)
                    item['heat'].updateValidValue(device.isHeating())
                else:
                    item['t'].setError(True)
                    item['sp'].setError(True)
                    item['bat'].setError(True)
                    item['heat'].setError(True)
                    error=True

            self.values.comerr.updateValue(error)

        return 5.0


if __name__ == "__main__":
    pass
