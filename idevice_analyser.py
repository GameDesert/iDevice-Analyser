# Developed by GameDesert. Intended for educational use, but no-one's stopping you from doing anything else with it.

from os import system
from tkinter import *
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
from subprocess import check_output as cmd
from random import randint
import json

sudo_password = bytes(input("Please enter sudo password: ")+"\n", 'utf-8')



producttype_to_phone = {
"iPhone1,1":"iPhone",
"iPhone1,2":"iPhone 3G",
"iPhone2,1":"iPhone 3GS",
"iPhone3,1":"iPhone 4",
"iPhone3,2":"iPhone 4",
"iPhone3,3":"iPhone 4",
"iPhone4,1":"iPhone 4s",
"iPhone5,1":"iPhone 5",
"iPhone5,2":"iPhone 5",
"iPhone5,3":"iPhone 5c",
"iPhone5,4":"iPhone 5c",
"iPhone6,1":"iPhone 5s",
"iPhone6,2":"iPhone 5s",
"iPhone7,2":"iPhone 6",
"iPhone7,1":"iPhone 6 Plus",
"iPhone8,1":"iPhone 6s",
"iPhone8,2":"iPhone 6s Plus",
"iPhone8,4":"iPhone SE (1st generation)",
"iPhone9,1":"iPhone 7",
"iPhone9,3":"iPhone 7",
"iPhone9,2":"iPhone 7 Plus",
"iPhone9,4":"iPhone 7 Plus",
"iPhone10,1":"iPhone 8",
"iPhone10,4":"iPhone 8",
"iPhone10,2":"iPhone 8 Plus",
"iPhone10,5":"iPhone 8 Plus",
"iPhone10,3":"iPhone X",
"iPhone10,6":"iPhone X",
"iPhone11,8":"iPhone XR",
"iPhone11,2":"iPhone XS",
"iPhone11,6":"iPhone XS Max",
"iPhone11,4":"iPhone XS Max",
"iPhone12,1":"iPhone 11",
"iPhone12,3":"iPhone 11 Pro",
"iPhone12,5":"iPhone 11 Pro Max",
"iPhone12,8":"iPhone SE (2nd generation)",
"iPhone13,1":"iPhone 12 mini",
"iPhone13,2":"iPhone 12",
"iPhone13,3":"iPhone 12 Pro",
"iPhone13,4":"iPhone 12 Pro Max"
}

def pair():
	try:
		cmd("sudo usbmuxd -f",shell=True,input=sudo_password)
	finally:
		try:
			cmd("idevicepair pair",shell=True)
		except:
			print("The device has already been paired (both commands returned errors).")
def analyse():
	raw_device_info = str(cmd("ideviceinfo", shell=True))
	json_device_info = "{" + raw_device_info.replace('b\'ActivationState: ','"activationstate":"').replace('\\nActivationStateAcknowledged: ','","activationstateacknowledged":"').replace('\\nBasebandActivationTicketVersion: ','","basebandactivationticketversion":"').replace('\\nBasebandCertId: ','","basebandcertid":"').replace('\\nBasebandChipID: ','","basebandchipid":"').replace('\\nBasebandFactoryMasterKeyHash: ','","basebandfactorymasterkeyhash":"').replace('\\nBasebandKeyHashInformation: ','","basebandkeyhashinformation":{"').replace('\\n AKeyStatus: ','akeystatus":"').replace('\\n SKeyHash: ','","skeyhash":"').replace('\\n SKeyStatus: ','","skeystatus":"').replace('\\nBasebandMasterKeyHash: ','"},"basebandmasterkeyhash":"').replace('\\nBasebandRegionSKU: ','","basebandregionsku":"').replace('\\nBasebandSerialNumber: ','","basebandserialnumber":"').replace('\\nBasebandStatus: ','","basebandstatus":"').replace('\\nBasebandVersion: ','","basebandversion":"').replace('\\nBluetoothAddress: ','","bluetoothaddress":"').replace('\\nBoardId: ','","boardid":"').replace('\\nBrickState: ','","brickstate":"').replace('\\nBuildVersion: ','","buildversion":"').replace('\\nCPUArchitecture: ','","cpuarchitecture":"').replace('\\nCarrierBundleInfoArray[1]: ','","carrierbundleinfoarray":{"').replace('\\nCarrierBundleInfoArray[0]: ','","carrierbundleinfoarray0":{"":"').replace('\\n 0: ','0":"').replace('\\n  CFBundleIdentifier: ','","cfbundleidentifier":"').replace('\\n  CFBundleVersion: ','","cfbundleversion":"').replace('\\n  GID1: ','","gid1a":"').replace('\\n  IntegratedCircuitCardIdentity: ','","integratedcircuitcardidentitya":"').replace('\\n  InternationalMobileSubscriberIdentity: ','","internationalmobilesubscriberidentity":"').replace('\\n  MCC: ','","mcc":"').replace('\\n  MNC: ','","mnc":"').replace('\\n  MobileEquipmentIdentifier: ','","mobileequipmentidentifier":"').replace('\\n  SIMGID1: ','","simgid1a":"').replace('\\n  Slot: ','","slot":"').replace('\\n  kCTPostponementInfoAvailable: ','","kctpostponementinfoavailable":"').replace('\\nCertID: ','"},"certid":"').replace('\\nChipID: ','","chipid":"').replace('\\nChipSerialNo: ','","chipserialno":"').replace('\\nDeviceClass: ','","deviceclass":"').replace('\\nDeviceColor: ','","devicecolor":"').replace('\\nDeviceName: ','","devicename":"').replace('\\nDieID: ','","dieid":"').replace('\\nEthernetAddress: ','","ethernetaddress":"').replace('\\nFirmwareVersion: ','","firmwareversion":"').replace('\\nFusingStatus: ','","fusingstatus":"').replace('\\nGID1: ','","gid1":"').replace('\\nHardwareModel: ','","hardwaremodel":"').replace('\\nHardwarePlatform: ','","hardwareplatform":"').replace('\\nHasSiDP: ','","hassidp":"').replace('\\nHostAttached: ','","hostattached":"').replace('\\nIntegratedCircuitCardIdentity: ','","integratedcircuitcardidentity":"').replace('\\nInternationalMobileEquipmentIdentity: ','","internationalmobileequipmentidentity":"').replace('\\nInternationalMobileEquipmentIdentity2: ','","internationalmobileequipmentidentity2":"').replace('\\nInternationalMobileSubscriberIdentity: ','","internationalmobilsesubscriberidentity":"').replace('\\nInternationalMobileSubscriberIdentityOverride: ','","internationalmobilsesubscriberidentityoverride":"').replace('\\nMLBSerialNumber: ','","mlbserialnumber":"').replace('\\nMobileEquipmentIdentifier: ','","mobileequipmentidentifier":"').replace('\\nMobileSubscriberCountryCode: ','","mobilesubscribercountrycode":"').replace('\\nMobileSubscriberNetworkCode: ','","mobilesubscribernetworkcode":"').replace('\\nModelNumber: ','","modelnumber":"').replace('\\nNonVolatileRAM: ','","nonvolatileram":"').replace('\\n IONVRAM-SYNCNOW-PROPERTY: ','","ionvramsyncnowproperty":"').replace('\\n auto-boot: ','","autoboot":"').replace('\\n backlight-level: ','","backlightlevel":"').replace('\\n backlight-nits: ','","backlightnits":"').replace('\\n boot-args: ','","bootargs":"').replace('\\n com.apple.System.tz0-size: ','","comapplesystemtz0size":"').replace('\\n oblit-begins: ','","oblitbegins":"').replace('\\n obliteration: ','","obliteration":"').replace('\\n ota-controllerVersion: ','","otacontrollerversion":"').replace('\\n bootdelay: ','","bootdelay":"').replace('\\n usbcfwflasherResult: ','","usbcfwflasherresult":"').replace('\\nPRIVersion_Major: ','","priversionmajor":"').replace('\\nPRIVersion_Minor: ','","priversionminor":"').replace('\\nPRIVersion_ReleaseNo: ','","priversionreleaseno":"').replace('\\nPartitionType: ','","partitiontype":"').replace('\\nPasswordProtected: ','","passwordprotected":"').replace('\\nPhoneNumber: ','","phonenumber":"').replace('\\nPkHash: ','","pkhash":"').replace('\\nProductName: ','","productname":"').replace('\\nProductType: ','","producttype":"').replace('\\nProductVersion: ','","productversion":"').replace('\\nProductionSOC: ','","productionsoc":"').replace('\\nProtocolVersion: ','","protocolversion":"').replace('\\nProximitySensorCalibration: ','","proximitysensorcalibration":"').replace('\\nRegionInfo: ','","regioninfo":"').replace('\\nSIM1IsEmbedded: ','","sim1isembedded":"').replace('\\nSIMGID1: ','","simgid1":"').replace('\\nSIMStatus: ','","simstatus":"').replace('\\nSIMTrayStatus: ','","simtraystatus":"').replace('\\nSerialNumber: ','","serialnumber":"').replace('\\nSoftwareBehavior: ','","softwarebehaviour":"').replace('\\nSoftwareBundleVersion: ','","softwarebundleversion":"').replace('\\nSupportedDeviceFamilies[1]: ','","supporteddevicefamilies":{"').replace('\\n 0: ','","0":"').replace('\\nTelephonyCapability: ','"},"telephonycapability":"').replace('\\nTimeIntervalSince1970: ','","timeintervalsince1970":"').replace('\\nTimeZone: ','","timezone":"').replace('\\nTimeZoneOffsetFromUTC: ','","timezoneoffsetfromutc":"').replace('\\nTrustedHostAttached: ','","trustedhostattached":"').replace('\\nUniqueChipID: ','","uniquechipid":"').replace('\\nUniqueDeviceID: ','","uniquedeviceid":"').replace('\\nUntrustedHostBUID: ','","untrustedhostbuid":"').replace('\\nUseRaptorCerts: ','","useraptorcerts":"').replace('\\nUses24HourClock: ','","uses24hourclock":"').replace('\\nWiFiAddress: ','","wifiaddress":"').replace('\\nWirelessBoardSerialNumber: ','","wirelessboardserialnumber":"').replace('\\nkCTPostponementInfoPRLName: ','","kctpostponementinfoprlname":"').replace('\\nkCTPostponementInfoPRIVersion: ','","kctpostponementinfopriversion":"').replace('\\nkCTPostponementInfoServiceProvisioningState: ','","kctpostponementinfoserviceprovisioningstate":"').replace('\\nkCTPostponementStatus: ','","kctpostponementstatus":"').replace("\\n'",'"').replace('\\','\\\\') + '}'
	parsed_device_info = json.loads(json_device_info)
	try:
		product_title = producttype_to_phone[parsed_device_info["producttype"]]
	except:
		product_title = "Unidentified Apple Device" 
	phonename = Label(text=".", fg="Black", font=("Helvetica", 18))
	phonename.master.destroy
	phonename = Label(text=product_title, fg="Black", font=("Helvetica", 18))
	phonename.place(x=20,y=60)
	
	passwordprotection = Label(text=".", fg="Black", font=("Helvetica", 18))
	passwordprotection.master.destroy
	passwordprotection = Label(text="Password Protected: " + parsed_device_info["passwordprotected"], fg="Black", font=("Helvetica", 14))
	passwordprotection.place(x=20,y=90)
	
	try:
		phonenum = Label(text=".", fg="Black", font=("Helvetica", 18))
		phonenum.master.destroy
		phonenum = Label(text="Phone Number: " + parsed_device_info["phonenumber"], fg="Black", font=("Helvetica", 14))
		phonenum.place(x=20,y=120)
	except:
		phonenum = Label(text=".", fg="Black", font=("Helvetica", 18))
		phonenum.master.destroy
		phonenum = Label(text="Phone Number: N/A                          ", fg="Black", font=("Helvetica", 14))
		phonenum.place(x=20,y=120)
	
	os = Label(text=".", fg="Black", font=("Helvetica", 18))
	os.master.destroy
	os = Label(text="Operating System: " + parsed_device_info["productname"] + " " + parsed_device_info["productversion"], fg="Black", font=("Helvetica", 14))
	os.place(x=20,y=150)
	
	addresses = Label(text=".", fg="Black", font=("Helvetica", 18))
	addresses.master.destroy
	addresses = Label(text="Addresses:", fg="Black", font=("Helvetica", 16))
	addresses.place(x=20,y=200)
	
	wifiaddress = Label(text=".", fg="Black", font=("Helvetica", 18))
	wifiaddress.master.destroy
	wifiaddress = Label(text="Wi-Fi Address: " + parsed_device_info["wifiaddress"], fg="Black", font=("Helvetica", 14))
	wifiaddress.place(x=20,y=230)
	
	ethernetaddress = Label(text=".", fg="Black", font=("Helvetica", 18))
	ethernetaddress.master.destroy
	ethernetaddress = Label(text="Ethernet Address: " + parsed_device_info["ethernetaddress"], fg="Black", font=("Helvetica", 14))
	ethernetaddress.place(x=20,y=260)
	
	bluetoothaddress = Label(text=".", fg="Black", font=("Helvetica", 18))
	bluetoothaddress.master.destroy
	bluetoothaddress = Label(text="Bluetooth Address: " + parsed_device_info["bluetoothaddress"], fg="Black", font=("Helvetica", 14))
	bluetoothaddress.place(x=20,y=290)
	
	ids = Label(text=".", fg="Black", font=("Helvetica", 18))
	ids.master.destroy
	ids = Label(text="Identifiers:", fg="Black", font=("Helvetica", 16))
	ids.place(x=20,y=340)
	
	imei = Label(text=".", fg="Black", font=("Helvetica", 18))
	imei.master.destroy
	imei = Label(text="IMEI: " + parsed_device_info["internationalmobileequipmentidentity"], fg="Black", font=("Helvetica", 14))
	imei.place(x=20,y=370)
	
	serial = Label(text=".", fg="Black", font=("Helvetica", 18))
	serial.master.destroy
	serial = Label(text="Serial Number: " + parsed_device_info["serialnumber"], fg="Black", font=("Helvetica", 14))
	serial.place(x=20,y=400)
	
	modelnumber = Label(text=".", fg="Black", font=("Helvetica", 18))
	modelnumber.master.destroy
	modelnumber = Label(text="Model Number: " + parsed_device_info["modelnumber"] + parsed_device_info["regioninfo"], fg="Black", font=("Helvetica", 14))
	modelnumber.place(x=20,y=430)
	
	try:	
		icci = Label(text=".", fg="Black", font=("Helvetica", 18))
		icci.master.destroy
		icci = Label(text="ICCI: " + parsed_device_info["integratedcircuitcardidentity"], fg="Black", font=("Helvetica", 14))
		icci.place(x=20,y=460)
	except:
		icci = Label(text=".", fg="Black", font=("Helvetica", 18))
		icci.master.destroy
		icci = Label(text="ICCI: N/A                          ", fg="Black", font=("Helvetica", 14))
		icci.place(x=20,y=460)
	
	ids = Label(text=".", fg="Black", font=("Helvetica", 18))
	ids.master.destroy
	ids = Label(text="Time:", fg="Black", font=("Helvetica", 16))
	ids.place(x=20,y=510)
	
	zone = Label(text=".", fg="Black", font=("Helvetica", 18))
	zone.master.destroy
	zone = Label(text="Time Zone: " + parsed_device_info["timezone"], fg="Black", font=("Helvetica", 14))
	zone.place(x=20,y=540)
	
	tfhr = Label(text=".", fg="Black", font=("Helvetica", 18))
	tfhr.master.destroy
	tfhr = Label(text="24-Hour Clock: " + parsed_device_info["uses24hourclock"], fg="Black", font=("Helvetica", 14))
	tfhr.place(x=20,y=570)
	


root = Tk()
app = Window(root)
root.geometry("700x800")

root.wm_title("iDevice Analyser")

pairButton = Button(text="Pair Device", command=pair)
pairButton.place(x=0, y=0)
analyseButton = Button(text="Analyse Device", command=analyse)
analyseButton.place(x=100, y=0)
info = Label(text="Connect device to computer via lightning cable and press the Analyse button.", fg="Black", font=("Helvetica", 10))
info.place(x=10,y=730)
info2 = Label(text="If an error is returned, restart the program and before analysing, press Pair and enter the passcode on the device.", fg="Black", font=("Helvetica", 10))
info2.place(x=10,y=750)
info3 = Label(text="Once the device is paired, press Analyse to get a printout of the basic device info.", fg="Black", font=("Helvetica", 10))
info3.place(x=10,y=770)


# show windowc
root.mainloop()
