#!/usr/bin/env python3


import json, collections


class Publisher:

    topic = {
        'frontend' : 'com.opentrons.frontend',
        'driver' : 'com.opentrons.driver',
        'labware' : 'com.opentrons.labware',
        'bootloader' : 'com.opentrons.bootloader'
    }

    def __init__(self, session=None):
        """
        """
        print('publisher.__init__ called')
        print('\tsession: '+str(session))
        self.caller = None
        if session is not None:
            self.caller = session


    def set_caller(self, session):
        """
        """
        print('publisher.set_caller called')
        print('\tsession: '+str(session))
        self.caller = session


    def publish(self,topic,type_,name,message,param):
        """
        """
        print('publisher.publish called:')
        print('\ttopic: '+str(topic))
        print('\ttype_: '+str(type_))
        print('\tname: '+str(name))
        print('\tmessage: '+str(message))
        print('\tparam: '+str(param))
        if self.caller is not None and topic is not None and type_ is not None:
            if name is None:
                name = 'None'
            if message is None:
                message = ''
            if param is None:
                param = ''
            if self.caller._myAppSession is not None:
                msg = {'type':type_,'data':{'name':name,'message':{message:param}}}
                try:
                    self.caller._myAppSession.publish(self.topic.get(topic),json.dumps(msg))
                except:
                    print('publisher.py - publish - error: '+sys.exc_info()[0])
                    raise
            else:
                print('publisher.py - publish - error: caller._myAppSession is None')
        else:
            print('publisher.py - publish - error: calller, topic, or type_ is None')

