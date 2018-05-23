import numpy as np
import sys
import cv2
from ctypes import *
from ctypes.wintypes import *
from define import *

class TUCAM_INIT(Structure):
    _fields_ = [('uiCamCount',c_uint),('pstrConfigPath',c_char_p)]
	
class TUCAM_OPEN(Structure):
    _fields_ = [('uiIdxOpen',c_uint),('hIdxTUCam',HANDLE)]
	
class TUCAM_FRAME(Structure):
    _fields_ = [('szSignature',c_char_p),
               ('usHeader',c_ushort),
               ('usOffset',c_ushort),
               ('usWidth',c_ushort),
               ('usHeight',c_ushort),
               ('uiWidthStep',c_uint),
               ('ucDepth',c_ubyte),
               ('ucFormat',c_ubyte),
               ('ucChannels',c_ubyte),
               ('ucElemBytes',c_ubyte),
               ('ucFormatGet',c_ubyte),
               ('uiIndex',c_uint),
               ('uiImgSize',c_uint),
               ('uiRsdSize',c_uint),
               ('uiHstSize',c_uint),
               ('pBuffer',c_void_p)]
func_type={
'TUCAM_Api_Init':(c_int,[POINTER(TUCAM_INIT)]),
'TUCAM_Dev_Open':(c_int,[POINTER(TUCAM_OPEN)]),
'TUCAM_Buf_Alloc':(c_int,[HANDLE, POINTER(TUCAM_FRAME)]),
'TUCAM_Cap_Start':(c_int,[HANDLE, c_uint]),
'TUCAM_Buf_WaitForFrame':(c_int,[HANDLE, POINTER(TUCAM_FRAME)]),
'TUCAM_Buf_CopyFrame':(c_int,[HANDLE,POINTER(TUCAM_FRAME)]),
'TUCAM_Buf_AbortWait':(c_int,[HANDLE]),
'TUCAM_Cap_Stop':(c_int,[HANDLE]),
'TUCAM_Buf_Release':(c_int,[HANDLE]),
'TUCAM_Dev_Close':(c_int,[HANDLE]),
'TUCAM_Api_Uninit':(None,None),
'memcpy':(None,[c_void_p,c_void_p,c_uint])
}

def specify_type(f,key):
	ret_type,args_type=func_type[key]
	if ret_type!=None:
		f.restype=ret_type
	if args_type!=None:
		f.argtypes=args_type
	return f
	
parser_error=lambda x:hex(pow(2,32)+x)
dlib=CDLL('TUCam.dll')
libc=cdll.msvcrt
memcpy = specify_type(libc.memcpy,'memcpy')
TUCAM_Api_Init = specify_type(dlib.TUCAM_Api_Init,'TUCAM_Api_Init')
TUCAM_Dev_Open = specify_type(dlib.TUCAM_Dev_Open,'TUCAM_Dev_Open')
TUCAM_Buf_Alloc = specify_type(dlib.TUCAM_Buf_Alloc,'TUCAM_Buf_Alloc')
TUCAM_Cap_Start = specify_type(dlib.TUCAM_Cap_Start,'TUCAM_Cap_Start')
TUCAM_Buf_WaitForFrame = specify_type(dlib.TUCAM_Buf_WaitForFrame,'TUCAM_Buf_WaitForFrame')
TUCAM_Buf_CopyFrame = specify_type(dlib.TUCAM_Buf_CopyFrame,'TUCAM_Buf_CopyFrame')
TUCAM_Buf_AbortWait = specify_type(dlib.TUCAM_Buf_AbortWait,'TUCAM_Buf_AbortWait')
TUCAM_Cap_Stop = specify_type(dlib.TUCAM_Cap_Stop,'TUCAM_Cap_Stop')
TUCAM_Buf_Release = specify_type(dlib.TUCAM_Buf_Release,'TUCAM_Buf_Release')
TUCAM_Dev_Close = specify_type(dlib.TUCAM_Dev_Close,'TUCAM_Dev_Close')
TUCAM_Api_Uninit = specify_type(dlib.TUCAM_Api_Uninit,'TUCAM_Api_Uninit')
#libc.memcpy(img_ctypes_ptr,mframe.pBuffer+mframe.usOffset,mframe.uiImgSize)
class ccd:
	def __init__(self):
		
		#initiate the device
		workpath=c_char_p(b"")
		itApi=TUCAM_INIT(0,workpath)
		ret=TUCAM_Api_Init(byref(itApi))
		assert(ret==1)
		#open the camera
		opCam = TUCAM_OPEN(0,0)
		ret = TUCAM_Dev_Open(byref(opCam))
		assert(ret == 1)
		# allocate the buffer memory
		signature = (c_char*8)()
		signature = cast(signature,c_char_p)
		mframe = TUCAM_FRAME(signature,0,0,0,0,0,0,0,0,0,TUFRM_FMT_RGB888,0,0,1,0,cast(0,c_void_p))
		ret = TUCAM_Buf_Alloc(opCam.hIdxTUCam,byref(mframe))
		assert(ret==1)
		
		ret = TUCAM_Cap_Start(opCam.hIdxTUCam,TUCCM_SEQUENCE)
		assert(ret == 1)
		
		self.mframe = mframe
		self.hIdxTUCam = opCam.hIdxTUCam
		
	def read(self):
		img = np.zeros((1728,2304,3),dtype=np.uint8)
		if not img.flags['C_CONTIGUOUS']:
			img = np.ascontiguous(img, dtype=img.dtype)
		img_ctypes_ptr = cast(img.ctypes.data,c_void_p) 
		ret=TUCAM_Buf_WaitForFrame(self.hIdxTUCam,byref(self.mframe))
		assert(ret == 1)
		
		ret=TUCAM_Buf_CopyFrame(self.hIdxTUCam,byref(self.mframe))
		assert(ret == 1)
		
		memcpy(img_ctypes_ptr,self.mframe.pBuffer+self.mframe.usOffset,self.mframe.uiImgSize)
		return img
	
	def stop(self):
		TUCAM_Buf_AbortWait(self.hIdxTUCam)
		TUCAM_Cap_Stop(self.hIdxTUCam)
		TUCAM_Buf_Release(self.hIdxTUCam)
		TUCAM_Dev_Close(self.hIdxTUCam)
		TUCAM_Api_Uninit()
		
		
		
