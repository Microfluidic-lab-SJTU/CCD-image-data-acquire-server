# typedef enum the capture mode
TUCCM_SEQUENCE              = 0x00
TUCCM_TRIGGER_STANDARD      = 0x01
TUCCM_TRIGGER_SYNCHRONOUS   = 0x02
TUCCM_TRIGGER_GLOBAL        = 0x03
TUCCM_TRIGGER_SOFTWARE      = 0x04

# typedef enum the frame formats
TUFRM_FMT_RAW               = 0x10            #// The raw data
TUFRM_FMT_USUAl             = 0x11            #// The usually data
TUFRM_FMT_RGB888            = 0x12            #// The RGB888 data for drawing

#typedef enum the capture mode
TUCCM_SEQUENCE              = 0x00           #// capture start sequence mode
TUCCM_TRIGGER_STANDARD      = 0x01           #// capture start trigger standard mode
TUCCM_TRIGGER_SYNCHRONOUS   = 0x02           #// capture start trigger synchronous mode
TUCCM_TRIGGER_GLOBAL        = 0x03          #// capture start trigger global
TUCCM_TRIGGER_SOFTWARE      = 0x04           #// capture start trigger software

#// typedef enum the image formats
TUFMT_RAW                   = 0x01          #// The format RAW
TUFMT_TIF                   = 0x02          #// The format TIFF
TUFMT_PNG                   = 0x04           #// The format PNG
TUFMT_JPG                   = 0x08           #// The format JPEG
TUFMT_BMP                   = 0x10           #// The format BMP
	
#//  typedef enum information id
TUIDI_BUS                   = 0x01           #// the bus type USB2.0/USB3.0
TUIDI_VENDOR                = 0x02          #// the vendor id
TUIDI_PRODUCT               = 0x03          #// the product id 
TUIDI_VERSION_API           = 0x04          #// the API version    
TUIDI_VERSION_FRMW          = 0x05           #// the firmware version
TUIDI_VERSION_FPGA          = 0x06           #// the FPGA version
TUIDI_VERSION_DRIVER        = 0x07           #// the driver version
TUIDI_TRANSFER_RATE         = 0x08          #// the transfer rate
TUIDI_CAMERA_MODEL          = 0x09           #// the camera model (string)
TUIDI_CURRENT_WIDTH         = 0x0A           #// the camera image data current width(must use TUCAM_Dev_GetInfoEx and after calling TUCAM_Buf_Alloc)
TUIDI_CURRENT_HEIGHT        = 0x0B           #// the camera image data current height(must use TUCAM_Dev_GetInfoEx and after calling TUCAM_Buf_Alloc)
TUIDI_CAMERA_CHANNELS       = 0x0C           #// the camera image data channels
TUIDI_BCDDEVICE             = 0x0D          #// the USB bcdDevice
TUIDI_ENDINFO               = 0x0E          #// the string id end
	
TUIDC_RESOLUTION            = 0x00           #// id capability resolution
TUIDC_PIXELCLOCK            = 0x01          #// id capability pixel clock
TUIDC_BITOFDEPTH            = 0x02          #// id capability bit of depth
TUIDC_ATEXPOSURE            = 0x03           #// id capability automatic exposure time  
TUIDC_HORIZONTAL            = 0x04          #// id capability horizontal
TUIDC_VERTICAL              = 0x05           #// id capability vertical
TUIDC_ATWBALANCE            = 0x06           #// id capability automatic white balance
TUIDC_FAN_GEAR              = 0x07           #// id capability fan gear
TUIDC_ATLEVELS              = 0x08             #// id capability automatic levels
TUIDC_SHIFT                 = 0x09             #// (The reserved) id capability shift(15~8, 14~7, 13~6, 12~5, 11~4, 10~3, 9~2, 8~1, 7~0) [16bit]
TUIDC_HISTC                 = 0x0A             #// id capability histogram statistic
TUIDC_CHANNELS              = 0x0B             #// id capability current channels(Only color camera support:0-RGB,1-Red,2-Green,3-Blue. Used in the property levels, see enum TUCHN_SELECT)
TUIDC_ENHANCE               = 0x0C             #// id capability enhance
TUIDC_DFTCORRECTION         = 0x0D             #// id capability defect correction (0-not correction, 1-calculate, 3-correction)
TUIDC_ENABLEDENOISE         = 0x0E             #// id capability enable denoise (TUIDP_NOISELEVEL effective)
TUIDC_FLTCORRECTION         = 0x0F             #// id capability flat field correction (0-not correction, 1-grab frame, 2-calculate, 3-correction)
TUIDC_RESTARTLONGTM         = 0x10             #// id capability restart long exposure time (only CCD camera support)
TUIDC_DATAFORMAT            = 0x11             #// id capability the data format(only YUV format data support 0-YUV 1-RAW)
TUIDC_DRCORRECTION          = 0x12             #// (The reserved)id capability dynamic range of correction
TUIDC_VERCORRECTION         = 0x13             #// id capability vertical correction(correction the image data show vertical, in windows os the default value is 1)
TUIDC_MONOCHROME            = 0x14             #// id capability monochromatic
TUIDC_BLACKBALANCE          = 0x15             #// id capability black balance
TUIDC_ENDCAPABILITY         = 0x16             #// id capability end 

#success
TUCAMRET_SUCCESS            = 0x00000001       # no error, general success code, app should check the value is positive   
TUCAMRET_FAILURE            = 0x80000000       # error    

#initialization error
TUCAMRET_NO_MEMORY          = 0x80000101       # not enough memory
TUCAMRET_NO_RESOURCE        = 0x80000102       # not enough resource except memory    
TUCAMRET_NO_MODULE          = 0x80000103       # no sub module
TUCAMRET_NO_DRIVER          = 0x80000104       # no driver
TUCAMRET_NO_CAMERA          = 0x80000105       # no camera
TUCAMRET_NO_GRABBER         = 0x80000106       # no grabber  
TUCAMRET_NO_PROPERTY        = 0x80000107       # there is no alternative or influence id, or no more property id

TUCAMRET_FAILOPEN_CAMERA    = 0x80000110       #fail open the camera
TUCAMRET_FAILOPEN_BULKIN    = 0x80000111       #fail open the bulk in endpoint
TUCAMRET_FAILOPEN_BULKOUT   = 0x80000112       #fail open the bulk out endpoint
TUCAMRET_FAILOPEN_CONTROL   = 0x80000113       #fail open the control endpoint
TUCAMRET_FAILCLOSE_CAMERA   = 0x80000114       #fail close the camera

TUCAMRET_FAILOPEN_FILE      = 0x80000115       #fail open the file

#status error
TUCAMRET_INIT               = 0x80000201       #API requires has not initialized state.
TUCAMRET_BUSY               = 0x80000202      #API cannot process in busy state.
TUCAMRET_NOT_INIT           = 0x80000203       #API requires has initialized state.
TUCAMRET_EXCLUDED           = 0x80000204       #some resource is exclusive and already used.
TUCAMRET_NOT_BUSY           = 0x80000205      #API requires busy state.
TUCAMRET_NOT_READY          = 0x80000206       #API requires ready state.
    
#wait error
TUCAMRET_ABORT              = 0x80000207       #abort process
TUCAMRET_TIMEOUT            = 0x80000208      #timeout
TUCAMRET_LOSTFRAME          = 0x80000209      #frame data is lost
TUCAMRET_MISSFRAME          = 0x8000020A      #frame is lost but reason is low lever driver's bug

#calling error
TUCAMRET_INVALID_CAMERA     = 0x80000301       #invalid camera
TUCAMRET_INVALID_HANDLE     = 0x80000302      #invalid camera handle
TUCAMRET_INVALID_OPTION     = 0x80000303       #invalid the option value of structure
TUCAMRET_INVALID_IDPROP     = 0x80000304      #invalid property id
TUCAMRET_INVALID_IDCAPA     = 0x80000305      #invalid capability id
TUCAMRET_INVALID_IDPARAM    = 0x80000306       #invalid parameter id
TUCAMRET_INVALID_PARAM      = 0x80000307       #invalid parameter
TUCAMRET_INVALID_FRAMEIDX   = 0x80000308       #invalid frame index
TUCAMRET_INVALID_VALUE      = 0x80000309      #invalid property value
TUCAMRET_INVALID_EQUAL      = 0x8000030A      #invalid property value equal 
TUCAMRET_INVALID_CHANNEL    = 0x8000030B      #the property id specifies channel but channel is invalid
TUCAMRET_INVALID_SUBARRAY   = 0x8000030C       #the combination of subarray values are invalid. e.g. TUCAM_IDPROP_SUBARRAYHPOS + TUCAM_IDPROP_SUBARRAYHSIZE is greater than the number of horizontal pixel of sensor.
TUCAMRET_INVALID_VIEW       = 0x8000030D       #invalid view window handle
TUCAMRET_INVALID_PATH       = 0x8000030E      #invalid file path

TUCAMRET_NO_VALUETEXT       = 0x80000310       #the property does not have value text
TUCAMRET_OUT_OF_RANGE       = 0x80000311       #value is out of range

TUCAMRET_NOT_SUPPORT        = 0x80000312       #camera does not support the function or property with current settings
TUCAMRET_NOT_WRITABLE       = 0x80000313       #the property is not writable	
TUCAMRET_NOT_READABLE       = 0x80000314       #the property is not readable

             
TUCAMRET_WRONG_HANDSHAKE    = 0x80000410       #this error happens TUCAM get error code from camera unexpectedly
TUCAMRET_NEWAPI_REQUIRED    = 0x80000411       #old API does not support the value because only new API supports the value
 
TUCAMRET_ACCESSDENY         = 0x80000412       #the property cannot access during this TUCAM status

TUCAMRET_NO_CORRECTIONDATA  = 0x80000501       #not take the dark and shading correction data yet.

TUCAMRET_INVALID_PRFSETS    = 0x80000601       #the profiles set name is invalid

TUCAMRET_DECODE_FAILURE     = 0x80000701       #the image decoding raw data to rgb data failure
TUCAMRET_COPYDATA_FAILURE   = 0x80000702       #the image data copying failure

#camera or bus trouble
TUCAMRET_FAIL_READ_CAMERA   = 0x83001001      #fail read from camera  
TUCAMRET_FAIL_WRITE_CAMERA  = 0x83001002      #fail write to camera
TUCAMRET_OPTICS_UNPLUGGED   = 0x83001003      #optics part is unplugged s
