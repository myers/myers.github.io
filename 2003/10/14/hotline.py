#!/usr/bin/python

__copyright__ = 'Copyright (c) 2003, Myers "icepick" Carpenter'
__license__ = "LGPL <http://www.gnu.org/copyleft/lesser.html>"
__author__ = "icepick <icepick@icepick.info>"

from twisted.python import log
from twisted.internet.defer import Deferred
from twisted.internet.protocol import ClientFactory, ClientCreator
from twisted.internet.protocol import Protocol
from twisted.internet.app import Application
from twisted.internet import reactor
from twisted.internet.error import ConnectionDone

import cStringIO as StringIO
import sys, struct, os, pprint
import urllib, urlparse

class Error(Exception):
    pass

class ServerError(Exception):
    """
    The server told us about an error
    """
    pass


def parseHotlineURL(url):
    """
    @returns: ( (hostname, port,), kws, )
    """
    
    urlparse.uses_netloc.append('hotline')
    schema, host, path, query, fragment = urlparse.urlsplit(url)
    assert schema == 'hotline'
    assert query == ''
    assert fragment == ''
    kws = {}
    if host.count('@'):
        userstr, host = urllib.splituser(host)
        kws['username'], kws['password'] = urllib.splittype(userstr)
    kws['cwd'] = path
    return ( urllib.splitnport(host, 5500), kws,)

def openHotlineURL(url, nickname=None):
    hostTuple, kws = parseHotlineURL(url)
    if nickname:
        kws['nickname'] = nickname

    cc = ClientCreator(reactor, HotlineClient, **kws)
    dd = cc.connectTCP(*hostTuple)
    return dd


def openHotlineURL(url, nickname=None):
    urlparse.uses_netloc.append('hotline')
    schema, host, path, query, fragment = urlparse.urlsplit(url)
    assert schema == 'hotline'
    assert query == ''
    assert fragment == ''
    kws = {}
    if nickname:
        kws['nickname'] = nickname
    if host.count('@'):
        userstr, host = urllib.splituser(host)
        kws['username'], kws['password'] = urllib.splittype(userstr)
    kws['cwd'] = path
    cc = ClientCreator(reactor, HotlineClient, **kws)
    dd = cc.connectTCP(*urllib.splitnport(host, 5500))
    return dd

def cleanFilename(filename):
    return filename.replace('\xa5', '-')

class HotlineClient(Protocol):
    def __init__(self, username='guest', password='', nickname='Twisted Hotline', icon=101, cwd='/'):
        self.username = username
        self.password = password
        self.nickname = nickname
        self.icon = icon
        self.cwd = cwd

        self.pathSeparator = '/'
        
        self.loggedInDeferred = Deferred()

        self.taskCounter = 0
        self.buffer = StringIO.StringIO()
        self.tasks = {}
        
    def chdir(self, path):
        if path is None or path == '.':
            return
        elif path == '..':
            raise NotImplemented
        elif path[0] != '/':
            self.cwd = os.path.normpath(os.path.join(self.cwd, path))
        else:
            self.cwd = path
        
    def connectionMade(self):
        self.sentLogin = False
        # tell the server we are a hotline client can deal with version 1 - 2
        self.transport.write('TRTPHOTL' + encodeShort(1) + encodeShort(2))

    def startTransaction(self, id, objects, *args):
        self.taskCounter += 1
        trans = assembleTransaction(
            objects = objects,
            id = id, type = 0, taskNumber = self.taskCounter)
        self.tasks[self.taskCounter] = Deferred()
        self.transport.write(trans)
        return self.tasks[self.taskCounter]

    def extractErrorMsg(self, transaction):
        assert len(transaction['objects']) == 1
        transaction['objects'][0][0] == 100
        return ServerError(transaction['objects'][0][3])
    
    def handleTransaction(self, transaction):
        # it's a reply to a query we sent
        if transaction['id'] == 0 and transaction['type'] == 1:
            if self.tasks.has_key(transaction['taskNumber']):
                if transaction['errorCode']:
                    
                    self.tasks[transaction['taskNumber']].errback(self.extractErrorMsg(transaction))
                else:
                    self.tasks[transaction['taskNumber']].callback(transaction)
                del self.tasks[transaction['taskNumber']]
            else:
                raise Error("no callback for this task number: %r" % transaction)
        elif hasattr(self, 'handleRaw' + transaction['name']):
            apply(getattr(self, 'handleRaw' + transaction['name']), (transaction,))
        else:
            log.debug("don't know how to handle transaction %r" % transaction['name'])

    def dataReceived(self, data):
        if not self.sentLogin:
            assert data == SERVER_HELLO, "data: %r != SERVER_HELLO: %r" % (data, SERVER_HELLO,)
            self.sendLogin()
            return

        self.buffer.write(data)
        
        self.parseBuffer()
    
    def parseBuffer(self): 
        """ 
        Examine data in self.buffer and pull out and parse transactions. 
        Leave incomplete data in self.buffer
        
        @returns: number of transactions found
        """
        counter = 0
        while len(self.buffer.getvalue()) > 16:
            self.buffer.seek(0)

            transaction = {}
            transaction['type'] = decodeShort(self.buffer.read(2))
            transaction['id'] = decodeShort(self.buffer.read(2))
            if transactionTypes.has_key(transaction['id']):
                transaction['name'] = transactionTypes[transaction['id']]
            else:
                transaction['name'] = None
            transaction['taskNumber'] = decodeLong(self.buffer.read(4))
            transaction['errorCode'] = decodeLong(self.buffer.read(4))
            data_block_len = decodeLong(self.buffer.read(4))
            # skip repeated len
            self.buffer.seek(4, 1)
            
            # Check if we have the complete data block
            if len(self.buffer.getvalue()) - self.buffer.tell() < data_block_len:
                log.debug("waiting for more data for this transaction: should be %s is %s" % (data_block_len, len(self.buffer.getvalue()) - self.buffer.tell()))
                break

            number_of_objects = decodeShort(self.buffer.read(2))
            transaction['objects'] = []
            for ii in xrange(number_of_objects):
                type = decodeShort(self.buffer.read(2))
                if object_types.has_key(type):
                    type_str = object_types[type]
                else:
                    type_str = None
                size = decodeShort(self.buffer.read(2))
                data = self.buffer.read(size)
                transaction['objects'].append( (type, type_str, size, data) )
            self.handleTransaction(transaction)
            counter += 1
            new_buffer = StringIO.StringIO()
            new_buffer.write(self.buffer.read())
            self.buffer = new_buffer
                
        # move to the end of the buffer
        self.buffer.seek(0, 2)
        return counter 
        
    def sendLogin(self):
        username = assembleObject(105, self.username)
        password = assembleObject(106, self.password)
        nickname = assembleObject(102, self.nickname)
        icon = assembleObject(104, self.icon)
        
        log.debug("sending login")
        dd = self.startTransaction(107, (username, password, nickname, icon,))
        self.sentLogin = True
        dd.chainDeferred(self.loggedInDeferred)
        del self.loggedInDeferred
        return dd

    def handleRawUserlist(self, transaction):
        log.debug("got userlist")
        
    def handleRawDisconnected(self, transaction):
        assert len(transaction['objects']) == 1
        assert transaction['objects'][0][0] == 101

        log.debug("Disconnected: %r" % transaction['objects'][0][3])
        
    def handleRawAgreement(self, transaction):
        log.debug('handleRawAgreement')
        assert len(transaction['objects']) == 1
    
    def _createPathObject(self, path):
        """
        Build a path object
         - short (directory levels)
         - one or more directory levels:
             - short (0)  not sure what it's for
             - byte (length of dir name)
             - string (dir name)
        """
        ret = []

        # make path absolute
        if len(path) == 0 or path[0] != self.pathSeparator:
            path = os.path.join(self.cwd, path)
        dirs = path[1:].split(self.pathSeparator)

        # for the root directory we don't send any objects *weird*
        if len(dirs) == 0:
            return ret 
            
        data = StringIO.StringIO()
        data.write(encodeShort(len(dirs)))
        for ii in dirs:
            data.write(encodeShort(0))
            data.write(encodeChar(len(ii)))
            data.write(ii)
        ret.append(assembleObject(202, data.getvalue()))
    
        return ret 

    def listFolder(self, path=None):
        log.debug('path = %r' % path)

        if path is None or path == '.':
            path = self.cwd
        log.debug("listing %r" % path)
        
        objects = self._createPathObject(path)
        
        dd = self.startTransaction(200, objects)
        dd.addCallback(self.parseFilelist)
        return dd
        
    def parseFilelist(self, transaction):
        ret = {}
        
        for obj in transaction['objects']:
            info = {}
            if obj[0] != 200:
                log.debug('unknown object: %r' % obj)
                continue
            info['type'] = obj[3][:4]
            if info['type'] == 'fldr':
                assert decodeLong(obj[3][4:8]) == 0
                info['count'] = decodeLong(obj[3][8:12])
                assert decodeLong(obj[3][12:16]) == 0
            else:
                info['creator'] = obj[3][4:8]
                info['size'] = decodeLong(obj[3][8:12])
                assert decodeLong(obj[3][12:16]) == 0
            assert decodeLong(obj[3][16:20]) == len(obj[3][20:])
            
            ret[obj[3][20:]] = info           
        
        return ret
   

    def retrieveFile(self, path, protocol):
        """
        Retrieve a file from the given path

        The file is fed into the given Protocol instance.
        
        @param path: path to file that you wish to receive.
        @param protocol: a L{Protocol} instance.

        @returns: L{Deferred}
        """
        log.msg("retrieveFile: %r" % path)
        
        path, filename = os.path.split(path)
        objects = [assembleObject(201, filename)]
        objects.extend(self._createPathObject(path))
        
        dd = self.startTransaction(202, objects)
        dd.addCallback(self._startFileXfer, protocol=protocol)
        return dd


    def _startFileXfer(self, transaction, protocol):
        xferID = None
        xfersize = None
        
        assert transaction['type'] == 1, "This isn't a server response"
        for obj in transaction['objects']:
            if obj[0] == 107:
                xferID = decodeLong(obj[3])
            elif obj[0] == 108:
                xfersize = decodeLong(obj[3])
        assert xferID is not None, "Didn't find xferID object: " + pprint.pformat(transaction)
        assert xfersize is not None, "Didn't find xfersize object"
                
                
        finishedDeferred = Deferred()
        cc = ClientCreator(reactor, HotlineDownload, xferID, xfersize, protocol, finishedDeferred)
        cc.connectTCP(self.transport.realAddress[0], 5501)
        return finishedDeferred
                
        
class HotlineDownload(Protocol):
    def __init__(self, xferID, xfersize, protocol, finishedDeferred):
        self.xferID = xferID
        self.xfersize = xfersize
        self.protocol = protocol
        self.finishedDeferred = finishedDeferred
                
        self.buffer = StringIO.StringIO()
        self.nextWatermark = 40
        self.watermarkHandler = self.parseHeader

        self.inData = False
        self.dataLen = 0
        self.dataCounter = 0 
        
    def connectionMade(self):
        self.transport.write('HTXF' + encodeLong(self.xferID) + encodeLong(0) + encodeLong(0))

    def connectionLost(self, reason):
        if reason.type == ConnectionDone:
            self.finishedDeferred.callback(None)
        else:
            self.finishedDeferred.callback(reason)
        
    def dataReceived(self, data):
        if self.inData:
            # check to see if we have all the data
            if len(data) + self.dataCounter <= self.dataLen:
                self.protocol.dataReceived(data)
                return                
            else:
                restOfDataLen = self.dataLen - self.dataCounter
                self.protocol.dataReceived(data[:restOfDataLen])
                self.buffer.seek(0)
                self.buffer.truncate(0)
                self.buffer.write(data[restOfDataLen:])
                self.watermarkHandler = self.parseRscrBlock
                self.nextWatermark = 16
                self.inData = False
                
        readpos = self.buffer.tell()
        self.buffer.seek(0, 2)
        self.buffer.write(data)
        writepos = self.buffer.tell()
        self.buffer.seek(readpos)
        
        while 1:
            if writepos < self.nextWatermark:
                break
            self.watermarkHandler()

    def parseHeader(self):
        self.watermarkHandler = self.parseInfoBlock

        assertEquals(self.buffer.read(4), 'FILP')
        assertEquals(self.buffer.read(2), '\x00\x01')
        self.buffer.read(2) #'\x00\x00'
        self.buffer.read(4) #'\x00\x00\x00\x00' 
        self.buffer.read(4) #'\x00\x00\x00\x00' 
        self.buffer.read(4) #'\x00\x00\x00\x00' 
        self.buffer.read(4) #'\x00\x00\x00\x03' 
        assertEquals(self.buffer.read(4), 'INFO')
        self.buffer.read(4) #'\x00\x00\x00\x00' 
        self.buffer.read(4) #'\x00\x00\x00\x00' 
        # infoblock + header of data block
        self.nextWatermark += decodeLong(self.buffer.read(4)) + (4 * 4)

    def parseInfoBlock(self):
        self.watermarkHandler = self.parseRscrBlock

        assertEquals(self.buffer.read(4), 'AMAC')
        self.protocol.filetype = self.buffer.read(4)
        self.protocol.creator = self.buffer.read(4)
        
        #read over longs that might be flags
        self.buffer.read(4 * 10)
        #creation date, format unknown
        self.buffer.read(8)
        #modification date, format unknown
        self.buffer.read(8)
        assertEquals(self.buffer.read(2), '\x00\x00')

        self._filenameLen = decodeShort(self.buffer.read(2))
        self.protocol.filename = self.buffer.read(self._filenameLen)

        self._commentLen = decodeShort(self.buffer.read(2))
        self.protocol.comment = self.buffer.read(self._commentLen)

        assertEquals(self.buffer.read(4), 'DATA')
        self.buffer.read(4 + 4)
        self.dataLen = decodeLong(self.buffer.read(4))
        self.inData = True

        # put the rest of the buffer into the protocol
        self.protocol.dataReceived(self.buffer.read())
        # this will never be reached, we just don't want the watermark handling 
        # code to be invoked.  dataLen + header of Rscr block
        self.nextWatermark += self.dataLen + 16
        
    def parseRscrBlock(self):
        log.debug('self.parseRscrBlock')
                
def assertEquals(val1, val2):
    assert val1 == val2, "val1: %r vs val2: %r" % (val1, val2,)

def encodeShort(short):
    binshort = struct.pack('>h', short)
    return binshort

def encodeChar(data):
    return struct.pack('>b', data)
    
def decodeShort(data):
    assert len(data) == 2
    return struct.unpack('>h', data)[0]

def encodeLong(long):
    binlong = struct.pack('>l', long)
    return binlong
    
def decodeLong(data):
    assert len(data) == 4
    return struct.unpack('>l', data)[0]
    
def encodeString(string):
    eodstring = ''
    for ii in range(len(string)):
        eodstring = eodstring + chr(255 - ord(string[ii]))
    return eodstring


def assembleObject(id, data):
    ret = StringIO.StringIO()
    ret.write(encodeShort(id))
    
    if objectEncodings.has_key(id) and objectEncodings[id]:
        data = objectEncodings[id](data)
    
    ret.write(encodeShort(len(data)))
    ret.write(data)

    return ret.getvalue()


def assembleTransaction(objects, id, type, taskNumber, errorCode = 0):
    # first the data block so we know it's size for the header block
    dataBlock = ''.join(objects)

    ret = StringIO.StringIO()
    # header block
    ret.write(encodeShort(type))
    ret.write(encodeShort(id))
    ret.write(encodeLong(taskNumber))
    ret.write(encodeLong(errorCode))

    # dataBlockLen is 1 short representing the number of objects in the
    # data + len of data
    dataBlockLen = len(encodeShort(len(objects))) + len(dataBlock) 
    ret.write(encodeLong(dataBlockLen))
    ret.write(encodeLong(dataBlockLen))

    # data block 
    # number of objects 
    ret.write(encodeShort(len(objects)))
    ret.write(dataBlock)
    
    return ret.getvalue()

SERVER_HELLO = 'TRTP\x00\x00\x00\x00'


object_types = {
    100: 'errormsg',
    101: 'message',
    102: 'nick',
    103: 'socket',
    104: 'icon',
    105: 'login',
    106: 'password',
    107: 'xferID',
    108: 'xfersize',
    109: 'parameter',
    110: 'privs',
    112: 'status',
    113: 'ban',
    114: 'chatwindow',
    115: 'subject',
    200: 'fileentry',
    201: 'filename',
    202: 'path',
    203: 'resumeinfo',
    204: 'resumeflag',
    205: 'infolongtype',
    206: 'infocreator',
    207: 'infosize',
    208: 'infocreated',
    209: 'infomodified',
    210: 'comment',
    211: 'newfilename',
    212: 'targetpath',
    213: 'infotype',
    214: 'Quote',
    300: 'userlistentry',
    320: 'newsfolderitem',
    321: 'catlist',
    322: 'category',
    325: 'newspath',
    326: 'threadID',
    327: 'newstype',
    328: 'newssubject',
    329: 'author',
    330: 'newsdate',
    331: 'prevthread',
    332: 'nextthread',
    333: 'newsdata',
}

objectEncodings = {
    102:    None,
    104:    encodeShort,
    105:    encodeString,
    106:    encodeString,
#    201:    encodeString,
}

transactionTypes = {
    101: 'GetNews',
    102: 'NewPost',
    103: 'PostNews',
    104: 'PrivateMessage',
    105: 'SendChat',
    106: 'RelayChat',
    107: 'Login',
    108: 'SendPM',
    109: 'Agreement',
    110: 'Kick',
    111: 'Disconnected',
    112: 'CreatePchatWith',
    113: 'AddToPchat',
    114: 'RejectPchat',
    115: 'RequestJoinPchat',
    116: 'LeavingPchat',
    117: 'JoinedPchat',
    118: 'LeftPchat',
    119: 'ChangedSubject',
    120: 'RequestChangeSubject',
    200: 'FolderList',
    202: 'Download',
    203: 'Upload',
    204: 'MoveToTrash',
    205: 'CreateFolder',
    206: 'GetFileInfo',
    207: 'SetFileInfo',
    208: 'MoveFile',
    209: 'MakeAlias',
    300: 'GetUserList',
    301: 'UserChange',
    302: 'UserLeave',
    303: 'GetUserInfo',
    304: 'ChangeNickIcon',
    350: 'CreateUser',
    351: 'DeleteUser',
    352: 'OpenUser',
    353: 'ModifyUser',
    354: 'Userlist',
    370: 'NewsDirlist',
    371: 'NewsCatList',
    380: 'DeleteNewsDirCat',
    381: 'MakeNewsDir',
    382: 'MakeCategory',
    400: 'GetThread',
    410: 'PostThread',
    411: 'DeleteThread'
}

    