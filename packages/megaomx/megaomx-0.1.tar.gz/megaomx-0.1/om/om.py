import requests
import json 
import time 
import datetime 

from enum import Enum 
class ECod( Enum ):
    Stage=1
    Alignment=2
    Measure=3
    Wafer_a=4
    Wafer_m=5

class OMX():

    CAMERA_MEAS="量测相机"
    CAMERA_ALIGN="定位相机"

    def __init__(self,host,port):
        
        self._url = f"http://{host}:{port}"
        
        pass 

    # base 
    def GET( self, path, args=None ):
        resp = requests.get(url=f"{self._url}/{path}",
                            headers={"content-Type":"application/json"},verify=False,
                            params=args )
                            
        return resp.text
                            
    def POST( self, path, **args ):
        resp = requests.post( url=f"{self._url}/{path}", 
                            headers={"content-Type":"application/json"},verify=False,
                            params=args )
        # print( args )
        return resp.text
    
    # calis 
    def getAbc( self ):
        
        return self.GET("calis/abc")
        
    def setAbc( self, v ):
        
        # requests.post( url=f"{self._url}/calis/abc", headers={"content-Type":"application/json"}, json={"ab":v} )
        
        return self.POST("calis/abc", ab=v)
        
    def prtScr( self, brief:str, fName:str ):
        self.POST( "calis/CaptureScr", brief=f"{brief}", fName=f"{fName}" )
        pass 
        
        
    def capture( self, brief:str, fName:str ):
        self.POST( "calis/CaptureCam", brief=f"{brief}", fName=f"{fName}" ) 
    
    def GetBgCnt( self ):
        
        a = self.GET("calis/GetBgCnt")
        # print( a )
        d = json.loads( a )
        
        return d
        
    def GetError( self ):
        
        a = self.GET("calis/GetError")
        # print( a )
        d = json.loads( a )
        
        return d
        
    def GetError2( self ):
        
        a = self.GET("wapi/GetError")
        # print( a )
        d = json.loads( a )
        
        return d
        
    def ClrError( self ):
        
        self.POST("calis/ClrErr")

    def GetPos( self ):
        
        a = self.GET("calis/GetPos")

        # print( a )
        d = json.loads( a )
        
        return d
    
    def Home( self ):
        
        self.POST("calis/Home")

    def PmCam( self ):
        
        self.POST("calis/PmCam")

    def MeasLight( self, na, fltId, attenId ):
        """
        na: 0,1,2
        flt: 0~7
        atten: 0~8
        """
        self.POST("calis/measlight", na=f"{na}", fltId=f"{fltId}",attenId=f"{attenId}")

    def Sharp( self, rng=0.8 ):
        a = self.GET("calis/sharp",args=f"rng={rng}")

        d = json.loads( a )
        
        return d
    
    def GetCorner( self, w=100, h=100):
        a = self.GET("calis/GetCorners",args=f"w={w}&h={h}" )

        d = json.loads( a )
        
        return d

    def PztMove( self, p, vMax:int=0 ):
        self.POST("calframe/PztMove", p=f"{p}", vMax=f"{vMax}" )

    # calframe
    def SwitchCam( self, cam ):
        self.POST("calframe/SwitchCam", cam=f"{cam}" )
        
    def GetCam( self ):
        a = self.GET("calframe/GetCam")
        # print( a )
        d = json.loads( a )
        
        return d
        
    def GetFrameId( self ):
        a = self.GET("calframe/GetFrameID")
        # print( a )
        d = json.loads( a )
        
        return d
    
    def SetMExposure( self, expo:float ):
        """
        in us unit
        """
        self.POST("calframe/SetMExposure",expo=expo )

    def SetNA( self, na:int ):
        """
        na: 0,1,2
        """
        self.POST("calframe/SetNA",naId=f"{na}")

    def SetLightAtten( self, iAtten:int ):
        """
        iAtten: 0,1,2,...40
        """
        self.POST("calframe/SetLightAtten",iAtten=f"{iAtten}")

    def SetAExposure( self, expo:float ):
        """
        expo: us unit
        """
        self.POST("calframe/SetAExposure",expo=expo )

    def SetDLight( self, dLight:int ):
        """
        dLight: 0~255
        """
        self.POST("calframe/SetDLight",dLight=f"{dLight}")
        
    def LZFocus( self ):
        self.POST("calframe/LZFocus")
        
    def SZFocus( self ):
        self.POST("calframe/SZFocus") 
        
    def ZFocus0( self ):
        self.POST("calframe/ZFocus0") 

    def LPztFocus( self ):
        self.POST("calframe/LPztFocus")
        
    def SPztFocus( self ):
        self.POST("calframe/SPztFocus") 

    def PztFocus0( self ):
        self.POST("calframe/PztFocus0") 

    def SetURoi( self, cx:int, cy:int, w:int, h:int ):
        self.POST("calframe/SetURoi", cx=cx, cy=cy, w=w, h=h )

    def GetURoi( self ):
        a = self.GET("calframe/GetURoi")
        d = json.loads( a )
        
        return d
    def ClrURoi( self ):
        self.POST("calframe/ClrURoi")
    
    # hori 
    def getGis( self ):
    
        a = self.GET("horimanual/GetGis")
        # print( a )
        d = json.loads( a )
        
        return d  
        
    def mov( self, p:tuple, cod:ECod=ECod.Wafer_a ):
        """
        cod="Stage"/"Alignment","Measure","Wafer_a", "Wafer_m"
        """
        
        self.POST( "horimanual/move", tp=f"{cod.name}", x=p[0], y=p[1] )
    
        pass 

    def movz( self, z ):
        
        
        self.POST( "horimanual/movez", z=f"{z}" )
    
        pass 

    def movpzt( self, pzt ):
        self.POST( "horimanual/movepzt", pzt=f"{pzt}" )
    
        pass 

    def rot( self, ang):
        # rot the data
        self.POST( "horimanual/rrot", ang=ang )    

    def trot( self, angle ):
        """
        only rotate t
        """
        self.POST( "horimanual/trot", angle=angle ) 

    def Sync( self, tmo=120, tick=0.05 ):
        """
        wait bg = 0 or error 
        """
        
        while tmo > 0:
            time.sleep( tick )
            
            tmo = tmo - tick 
            
            bg = self.GetBgCnt()
            err = self.GetError()
            
            if err != 0 :
                assert False, f"error {err}"
            
            if bg == 0:
                return 
                
        # timeout     
        assert False, f"wait tmo {bg} {err}"
        
        pass 
       
import sys         
if __name__=="__main__":

    aObj=OMX( "127.0.0.1", 5000 )
    
    err = aObj.GetError2()
    print( err )
    
    exit(0)
    
    aObj.ClrError()
    aObj.Sync()
    
    if True:
        for i in range( 100 ):
            aObj.mov( (-57.4518,4.5157), ECod.Stage )
            aObj.Sync()
            
            aObj.capture(f"{i}",f"a_cor_{i}")
            time.sleep( 0.5 )
            
            aObj.mov( (0,0), ECod.Stage )
            aObj.Sync()

    if False:
        # aObj.SetMExposure( 260 )
        # aObj.Sync()
        # aObj.SetNA( 0 )
        # aObj.Sync()
        # aObj.SetLightAtten( 3 )

        aObj.MeasLight( 0, 0, 0 )
        
        aObj.Sync()

        # aObj.SetAExposure( 200 )
        # aObj.Sync()
        # aObj.SetDLight( 64 )
        aObj.Sync()
        sys.exit(0)

    # v = aObj.GetURoi()
    # print( v )

    aObj.SetURoi( 1, 2, 200, 100 )

    v = aObj.GetURoi()
    print( v )

    aObj.ClrURoi()
    v = aObj.GetURoi()
    print( v )

    exit(0)

    cCam = aObj.GetCam()
    print( f"current cam {cCam}" )

    # aObj.SwitchCam(OMX.CAMERA_ALIGN)
    # aObj.Sync()

    # aObj.SwitchCam(OMX.CAMERA_MEAS)
    # aObj.Sync()


    aObj.PztFocus0()
    aObj.Sync()

    for i in range( 1000 ):
        ts = datetime.datetime.now()
        print( f"{ts} {i}>>>" )

        aObj.LPztFocus()
        # aObj.LZFocus()
        aObj.Sync()

        time.sleep( 0.1 )
        aObj.prtScr( f"{ts}",f"{i}_L" )
        
        print("sfocus")
        aObj.SPztFocus()
        # aObj.SZFocus()
        aObj.Sync()

        time.sleep( 0.1 )
        ts = datetime.datetime.now()
        aObj.prtScr( f"{ts}",f"{i}_S" )

        print( f"{i}<<<" )

    # v = aObj.getAbc()
    # print( v )
    
    # v = aObj.setAbc("df" )
    
    # v = aObj.prtScr( "bf", "123" )
    
    # v = aObj.capture( "dd", "456" )
    
    # v = aObj.getGis()
    # print( v )
    
    # aObj.mov( "")
    
    # a=ECod.Stage 
    # print( a, f"{a.name}" )
    
    # aObj.mov( (1,3), ECod.Wafer_a )

    pass 