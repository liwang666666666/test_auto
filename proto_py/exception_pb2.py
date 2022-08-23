# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exception.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x65xception.proto\x12\texception\"?\n\x13\x45xceptionCollection\x12(\n\nexceptions\x18\x01 \x03(\x0b\x32\x14.exception.Exception\"\x9f\x08\n\tException\x12\x1f\n\x05level\x18\x01 \x02(\x0e\x32\x10.exception.Level\x12\x39\n\x0c\x66\x63_exception\x18\x02 \x01(\x0b\x32!.exception.FlightControlExceptionH\x00\x12\x38\n\x11\x63\x61ptain_exception\x18\x03 \x01(\x0b\x32\x1b.exception.CaptainExceptionH\x00\x12\x45\n\x18\x63\x61mera_service_exception\x18\x04 \x01(\x0b\x32!.exception.CameraServiceExceptionH\x00\x12\x38\n\x11\x62\x61ttery_exception\x18\x05 \x01(\x0b\x32\x1b.exception.BatteryExceptionH\x00\x12\x30\n\rges_exception\x18\x06 \x01(\x0b\x32\x17.exception.GESExceptionH\x00\x12=\n\x0coa_exception\x18\x07 \x01(\x0b\x32%.exception.ObstacleAvoidanceExceptionH\x00\x12\x38\n\x11tracker_exception\x18\x08 \x01(\x0b\x32\x1b.exception.TrackerExceptionH\x00\x12\x36\n\x10gimbal_exception\x18\t \x01(\x0b\x32\x1a.exception.GimbalExceptionH\x00\x12\x30\n\rcpu_exception\x18\n \x01(\x0b\x32\x17.exception.CpuExceptionH\x00\x12\x32\n\x0e\x61\x64sp_exception\x18\x0b \x01(\x0b\x32\x18.exception.AdspExceptionH\x00\x12\x32\n\x0esdsp_exception\x18\x0c \x01(\x0b\x32\x18.exception.SdspExceptionH\x00\x12\x38\n\x11storage_exception\x18\r \x01(\x0b\x32\x1b.exception.StorageExceptionH\x00\x12\x32\n\x0ewifi_exception\x18\x0e \x01(\x0b\x32\x18.exception.WifiExceptionH\x00\x12\x30\n\rfpv_exception\x18\x0f \x01(\x0b\x32\x17.exception.FpvExceptionH\x00\x12\x30\n\rota_exception\x18\x10 \x01(\x0b\x32\x17.exception.OtaExceptionH\x00\x12\x38\n\x11takeoff_exception\x18\x11 \x01(\x0b\x32\x1b.exception.TakeOffExceptionH\x00\x12\x36\n\x10\x66lying_exception\x18\x12 \x01(\x0b\x32\x1a.exception.FlyingExceptionH\x00\x12\x30\n\reis_exception\x18\x13 \x01(\x0b\x32\x17.exception.EISExceptionH\x00\x42\x08\n\x06module\"\xec\x0e\n\x16\x46lightControlException\x12>\n\tcomponent\x18\x01 \x02(\x0e\x32+.exception.FlightControlException.Component\x12=\n\x04type\x18\x02 \x02(\x0e\x32/.exception.FlightControlException.ExceptionType\x12=\n\tsensor_id\x18\x03 \x01(\x0b\x32*.exception.FlightControlException.SensorId\x1a\x16\n\x08SensorId\x12\n\n\x02id\x18\x01 \x03(\r\"\xa1\x01\n\tComponent\x12\x07\n\x03IMU\x10\x00\x12\x07\n\x03GPS\x10\x01\x12\x07\n\x03VNS\x10\x02\x12\x08\n\x04\x42\x61ro\x10\x03\x12\t\n\x05Sonar\x10\x04\x12\t\n\x05Proxi\x10\x05\x12\x07\n\x03Mag\x10\x06\x12\t\n\x05Motor\x10\x07\x12\n\n\x06Params\x10\x08\x12\x0c\n\x08\x41rmcheck\x10\t\x12\t\n\x05Servo\x10\n\x12\x07\n\x03TOF\x10\x0b\x12\x0b\n\x07Remoter\x10\x0c\x12\n\n\x06Status\x10\r\"\xd7\x0b\n\rExceptionType\x12!\n\x1dMagCalibrationParamsNotExists\x10\x00\x12\x1f\n\x1bMagCalibrationParamsIsWrong\x10\x01\x12\x16\n\x12MagNeedCalibration\x10\x02\x12\x10\n\x0cMagNotUpdate\x10\x03\x12\x13\n\x0fMagAbnormalData\x10\x04\x12\x10\n\x0cGPSNotUpdate\x10\n\x12\x11\n\rGPSWeakSignal\x10\x0b\x12\x1c\n\x18MotorCommunicationFailed\x10\x14\x12\x0f\n\x0bMotorJammed\x10\x15\x12\x0f\n\x0bMotorNoLoad\x10\x16\x12\x11\n\rMotorAbnormal\x10\x17\x12\x12\n\x0eMotorSaturated\x10\x18\x12\x13\n\x0fMotorUnbalanced\x10\x19\x12\x13\n\x0fMotorShootBlade\x10\x1a\x12\x10\n\x0cVNSNotUpdate\x10\x1e\x12\x13\n\x0fVNSAbnormalData\x10\x1f\x12\x0e\n\nVNSTooDark\x10 \x12\x16\n\x12VNSNeedCalibration\x10!\x12\x12\n\x0e\x43onfigNotFound\x10(\x12\x19\n\x15\x43ontrolParamsNotFound\x10)\x12\x11\n\rBaroNotUpdate\x10\x32\x12\x14\n\x10\x42\x61roAbnormalData\x10\x33\x12\x14\n\x10\x42\x61roHeightExceed\x10\x34\x12\x1c\n\x18SonarCommunicationFailed\x10;\x12\x12\n\x0eSonarNotUpdate\x10<\x12\x15\n\x11SonarAbnormalData\x10=\x12\x11\n\rSonarSnrIsLow\x10>\x12\x15\n\x11SonarIsInDeadzone\x10?\x12\x12\n\x0eProxiNotUpdate\x10@\x12\x15\n\x11ProxiAbnormalData\x10\x41\x12\x18\n\x14ProxiNeedCalibration\x10\x42\x12\x19\n\x15SonarProxiDataUnmatch\x10\x43\x12\x0f\n\x0bProxiBroken\x10\x44\x12\x15\n\x11IMULargeVibration\x10P\x12\x15\n\x11IMUCrazyVibration\x10Q\x12\x13\n\x0fIMUBiasIsTooBig\x10R\x12\x18\n\x14IMUAccelAbnormalData\x10S\x12\x17\n\x13IMUGyroAbnormalData\x10T\x12\x0f\n\x0bIMUDiverged\x10U\x12\x16\n\x12IMUNeedCalibration\x10V\x12\x1c\n\x18IMUCalibrationParamsLost\x10W\x12\x11\n\rIMUPreheating\x10X\x12\x13\n\x0f\x44roneIsNotLevel\x10\x64\x12\x1f\n\x1bGroundTakeoffHeightAbnormal\x10\x65\x12\x1d\n\x19HandTakeoffHeightAbnormal\x10\x66\x12\x16\n\x12\x42igWindDisturbance\x10n\x12\x1c\n\x18ServoCommunicationFailed\x10x\x12#\n\x1fServoCalibrationParamsNotExists\x10y\x12!\n\x1dServoCalibrationParamsIsWrong\x10z\x12\x11\n\rServoAbnormal\x10{\x12\x0e\n\nServoStuck\x10|\x12\x15\n\x11ServoExcessiveGap\x10}\x12\x11\n\x0cTOFNotUpdate\x10\x82\x01\x12\x14\n\x0fTOFAbnormalData\x10\x83\x01\x12\x0f\n\nTOFCovered\x10\x84\x01\x12\x15\n\x10RemoterNotUpdate\x10\x8c\x01\x12\x16\n\x11StillCheckNotPass\x10\x96\x01\x12\x11\n\x0c\x46\x43Initiating\x10\x97\x01\x12\x15\n\x10\x44roneFreeFalling\x10\x98\x01\x12\x12\n\rDroneSpinning\x10\x99\x01\x12\x1b\n\x16\x44roneExcessiveAttitude\x10\x9a\x01\x12\x13\n\x0e\x44roneCollision\x10\x9b\x01\x12\x13\n\x0e\x44roneWindForce\x10\x9c\x01\x12\x11\n\x0c\x44roneOverTop\x10\x9d\x01\x12\x0e\n\tDroneFlip\x10\x9e\x01\"\xbc\x03\n\x10\x43\x61ptainException\x12\x37\n\x04type\x18\x01 \x02(\x0e\x32).exception.CaptainException.ExceptionType\"\xee\x02\n\rExceptionType\x12\x0e\n\nFCNotReady\x10\x00\x12\x0f\n\x0bGPSNotReady\x10\x14\x12\x1a\n\x16GPSTakeOffPointInvalid\x10\x15\x12\x1d\n\x19ObstacleAvoidanceNotReady\x10(\x12\x1d\n\x19ObstacleAvoidanceDetected\x10)\x12\x13\n\x0fTrackerNotReady\x10<\x12\x13\n\x0f\x42\x61tteryNotReady\x10P\x12\x1a\n\x16\x42\x61tteryLowForceLanding\x10Q\x12\x12\n\x0eGimbalNotReady\x10\x64\x12\x13\n\x0fGESForceLanding\x10y\x12\x0e\n\nGESFalling\x10z\x12\x17\n\x13GESTouchedLimitZone\x10{\x12\x14\n\x0fStorageNotReady\x10\x8d\x01\x12\x17\n\x12\x46ollowHeightTooLow\x10\xa0\x01\x12\x1b\n\x16\x46ollowDistanceTooClose\x10\xa1\x01\"\xce\x05\n\x10\x42\x61tteryException\x12\x37\n\x04type\x18\x01 \x02(\x0e\x32).exception.BatteryException.ExceptionType\"\x80\x05\n\rExceptionType\x12\x0c\n\x08\x42\x61ttNone\x10\x00\x12\x16\n\x12\x42\x61ttTemperatureLow\x10\x01\x12\x13\n\x0f\x42\x61ttOverCurrent\x10\x02\x12\x10\n\x0c\x42\x61ttOverLoad\x10\x03\x12\r\n\tBattShort\x10\x04\x12\x11\n\rBattCommError\x10\x05\x12\x12\n\x0e\x42\x61ttVoltageLow\x10\x06\x12\x12\n\x0e\x42\x61ttBrokenDown\x10\x07\x12\x12\n\x0e\x42\x61ttNonBalance\x10\x08\x12\x0f\n\x0b\x42\x61ttFuelLow\x10\t\x12\x14\n\x10\x42\x61ttFuelHeavyLow\x10\n\x12\x16\n\x12\x42\x61ttSubOverCurrent\x10\x0b\x12\x14\n\x10\x42\x61ttLevelLanding\x10\x0c\x12\x13\n\x0f\x42\x61ttLevelReturn\x10\r\x12\x10\n\x0c\x42\x61ttLevelLow\x10\x0e\x12\x15\n\x11\x42\x61ttLevelUltraLow\x10\x19\x12\x17\n\x13\x42\x61ttHighOverCurrent\x10\x0f\x12\x1d\n\x19\x42\x61ttTemperatureWarnDisarm\x10\x10\x12\x1a\n\x16\x42\x61ttTemperatureSubHigh\x10\x11\x12\x1d\n\x19\x42\x61ttOverCurrentWarnDisarm\x10\x12\x12\x12\n\x0e\x42\x61ttNonHealthy\x10\x13\x12\x1a\n\x16\x42\x61ttTemperatureHigh_50\x10\x14\x12\x1a\n\x16\x42\x61ttTemperatureHigh_65\x10\x15\x12#\n\x1f\x42\x61ttTemperatureLowCanNotTakeOff\x10\x16\x12\"\n\x1e\x42\x61ttTemperatureLowNeedSelfHeat\x10\x17\x12\x12\n\x0e\x42\x61ttLimitSpeed\x10\x18\x12\x15\n\x11\x42\x61ttInsertNotGood\x10\x1a\"\x92\x01\n\x16\x43\x61meraServiceException\x12=\n\x04type\x18\x01 \x02(\x0e\x32/.exception.CameraServiceException.ExceptionType\"9\n\rExceptionType\x12\x0e\n\nCameraNone\x10\x00\x12\x18\n\x14\x43\x61meraSelfCheckFault\x10\x01\"\x8f\x01\n\x0c\x43puException\x12\x33\n\x04type\x18\x01 \x02(\x0e\x32%.exception.CpuException.ExceptionType\"J\n\rExceptionType\x12\x0b\n\x07\x43puNone\x10\x00\x12\x14\n\x10\x43puFreqReduction\x10\x01\x12\x16\n\x12\x43puTemperatureHigh\x10\x02\"s\n\rAdspException\x12\x34\n\x04type\x18\x01 \x02(\x0e\x32&.exception.AdspException.ExceptionType\",\n\rExceptionType\x12\x0c\n\x08\x41\x64spNone\x10\x00\x12\r\n\tAdspCrash\x10\x01\"s\n\rSdspException\x12\x34\n\x04type\x18\x01 \x02(\x0e\x32&.exception.SdspException.ExceptionType\",\n\rExceptionType\x12\x0c\n\x08SdspNone\x10\x00\x12\r\n\tSdspCrash\x10\x01\"\xa3\x01\n\x10StorageException\x12\x37\n\x04type\x18\x01 \x02(\x0e\x32).exception.StorageException.ExceptionType\"V\n\rExceptionType\x12\x0f\n\x0bStorageNone\x10\x00\x12\x18\n\x14SDCardSpaceNotEnough\x10\x01\x12\x1a\n\x16InternalSpaceNotEnough\x10\x02\"\x96\x01\n\rWifiException\x12\x34\n\x04type\x18\x01 \x02(\x0e\x32&.exception.WifiException.ExceptionType\"O\n\rExceptionType\x12\x0c\n\x08WifiNone\x10\x00\x12\x16\n\x12WifiSelfCheckFault\x10\x01\x12\x18\n\x14WifiSignalQualityLow\x10\x02\"\xa9\x01\n\x0c\x46pvException\x12\x33\n\x04type\x18\x01 \x02(\x0e\x32%.exception.FpvException.ExceptionType\"d\n\rExceptionType\x12\x0b\n\x07\x46pvNone\x10\x00\x12\x15\n\x11\x46pvSelfCheckFault\x10\x01\x12\x17\n\x13\x46pvSignalQualityLow\x10\x02\x12\x16\n\x12\x46pvVersionNotMatch\x10\x03\"\xda\x01\n\x0cOtaException\x12\x33\n\x04type\x18\x01 \x02(\x0e\x32%.exception.OtaException.ExceptionType\"\x94\x01\n\rExceptionType\x12\x0b\n\x07OtaNone\x10\x00\x12\x13\n\x0fOtaGimbalFailed\x10\x01\x12\x12\n\x0eOtaSonarFailed\x10\x02\x12\x10\n\x0cOtaFPVFailed\x10\x03\x12\x14\n\x10OtaBatteryFailed\x10\x04\x12\x13\n\x0fOtaSysappFailed\x10\x05\x12\x10\n\x0cOtaBspFailed\x10\x06\"\x8d\x05\n\x10TakeOffException\x12\x37\n\x04type\x18\x01 \x02(\x0e\x32).exception.TakeOffException.ExceptionType\"\xbf\x04\n\rExceptionType\x12\x0f\n\x0bTakeOffNone\x10\x00\x12\x1b\n\x17TakeOffCanNotUseBattery\x10\x01\x12\x1a\n\x16TakeOffSdspStatusFault\x10\x02\x12\x1a\n\x16TakeOffAdspStatusFault\x10\x03\x12\x17\n\x13TakeOffCanNotUseImu\x10\x04\x12\x17\n\x13TakeOffCanNotUseMag\x10\x05\x12\x1f\n\x1bTakeOffFlightEssentialFault\x10\x06\x12\x1b\n\x17TakeOffNotEnoughBattery\x10\x07\x12\x19\n\x15TakeOffBatteryWarning\x10\x08\x12\x18\n\x14TakeOffOnGroundFault\x10\t\x12\x16\n\x12TakeOffOnHandFault\x10\n\x12\x19\n\x15TakeOffCpuStatusFault\x10\x0b\x12\x1a\n\x16TakeOffWifiStatusFault\x10\x0c\x12\x19\n\x15TakeOffFpvStatusFault\x10\r\x12\x1c\n\x18TakeOffCameraStatusFault\x10\x0e\x12!\n\x1dTakeOffBatteryHighTemperature\x10\x0f\x12 \n\x1cTakeOffBatteryLowTemperature\x10\x10\x12\x19\n\x15TakeOffInLimitFlyZone\x10\x11\x12\x1d\n\x19TakeOffCpuTemperatureHigh\x10\x12\x12\x1c\n\x18TakeOffBattInsertNotGood\x10\x13\"\x87\x01\n\x0f\x46lyingException\x12\x36\n\x04type\x18\x01 \x02(\x0e\x32(.exception.FlyingException.ExceptionType\"<\n\rExceptionType\x12\x17\n\x13\x46lyingExceptionNone\x10\x00\x12\x12\n\x0e\x46lyingNeedHeat\x10\x01\"\xf8\x03\n\x0cGESException\x12\x33\n\x04type\x18\x01 \x02(\x0e\x32%.exception.GESException.ExceptionType\"\xb2\x03\n\rExceptionType\x12\x12\n\x0eInLimitFlyZone\x10\x00\x12\x17\n\x13TouchedLimitFlyZone\x10\x01\x12\x18\n\x14\x41pproachLimitFlyZone\x10\x02\x12\x19\n\x15HasLimitFlyZoneNearby\x10\x03\x12(\n$NoGPSInDroneAndControllerInNoFlyZone\x10\x04\x12\x11\n\rInLimitHeight\x10\x05\x12\x17\n\x13\x41pproachLimitHeight\x10\x06\x12\x15\n\x11\x45xceedLimitHeight\x10\x07\x12\x1a\n\x16TouchedLimitHeightZone\x10\x08\x12\x1b\n\x17\x41pproachLimitHeightZone\x10\t\x12\x1c\n\x18HasLimitHeightZoneNearby\x10\n\x12\x16\n\x12ReachLimitDistance\x10\x0b\x12\x14\n\x10ReachLimitHeight\x10\x0c\x12\x19\n\x15ReachLimitHeightNoGPS\x10\r\x12\x1b\n\x17LoadLimitZoneDataFailed\x10\x0e\x12\x15\n\x11LoadGeoDataFailed\x10\x0f\"\xc7\x01\n\x10TrackerException\x12\x37\n\x04type\x18\x01 \x02(\x0e\x32).exception.TrackerException.ExceptionType\x12\x11\n\ttimestamp\x18\x02 \x01(\x02\"g\n\rExceptionType\x12\x14\n\x10\x43\x41NNOT_GET_IMAGE\x10\x00\x12\x16\n\x12\x43\x41NNOT_GET_FC_INFO\x10\x01\x12\x12\n\x0e\x43\x41NNOT_GET_EIS\x10\x02\x12\x14\n\x10\x43\x41NNOT_GET_PITCH\x10\x03\"\x95\x04\n\x1aObstacleAvoidanceException\x12\x41\n\x04type\x18\x01 \x02(\x0e\x32\x33.exception.ObstacleAvoidanceException.ExceptionType\"\xb3\x03\n\rExceptionType\x12\x15\n\x11\x42inocularDisabled\x10\x00\x12\x0f\n\x0bPoseTimeout\x10\x01\x12\x19\n\x15\x42inocularImageTimeout\x10\x02\x12\x19\n\x15\x42inocularAngleTimeout\x10\x03\x12\x18\n\x14PoseNavigationFailed\x10\x04\x12\x17\n\x13NoCalibrationParams\x10\x05\x12 \n\x1c\x43\x61librationParamsParseFailed\x10\x06\x12\x1a\n\x16\x42inocularControlFailed\x10\x07\x12\x1e\n\x1a\x45nvironmentLightIsTooLight\x10\x08\x12\x1d\n\x19\x45nvironmentLightIsTooDark\x10\t\x12\x10\n\x0c\x44isableBrake\x10\n\x12\x11\n\rDisableDetour\x10\x0b\x12\x17\n\x13\x42rakeBeforeObstacle\x10\x0c\x12\x15\n\x11ObstacleDetected1\x10\r\x12\x15\n\x11ObstacleDetected2\x10\x0e\x12\x12\n\x0e\x42inocularStuck\x10\x0f\x12\x14\n\x10\x42inocularNoImage\x10\x10\"\xdb\x01\n\x0fGimbalException\x12\x36\n\x04type\x18\x01 \x02(\x0e\x32(.exception.GimbalException.ExceptionType\"\x8f\x01\n\rExceptionType\x12\x0c\n\x08Overload\x10\x00\x12\x0c\n\x08ImuFault\x10\x01\x12\x0e\n\nImuOffLine\x10\x02\x12\x0f\n\x0bImuAccelErr\x10\x03\x12\x13\n\x0fImuGyroBiasHigh\x10\x04\x12\x1a\n\x16GimablOscillationLarge\x10\x05\x12\x10\n\x0cParameterErr\x10\x06\"w\n\x0c\x45ISException\x12\x33\n\x04type\x18\x01 \x02(\x0e\x32%.exception.EISException.ExceptionType\"2\n\rExceptionType\x12\x0e\n\nEisImuMiss\x10\x00\x12\x11\n\rEisImuInvalid\x10\x01**\n\x05Level\x12\x0b\n\x07Warning\x10\x00\x12\t\n\x05\x45rror\x10\x01\x12\t\n\x05\x46\x61tal\x10\x02')

_LEVEL = DESCRIPTOR.enum_types_by_name['Level']
Level = enum_type_wrapper.EnumTypeWrapper(_LEVEL)
Warning = 0
Error = 1
Fatal = 2


_EXCEPTIONCOLLECTION = DESCRIPTOR.message_types_by_name['ExceptionCollection']
_EXCEPTION = DESCRIPTOR.message_types_by_name['Exception']
_FLIGHTCONTROLEXCEPTION = DESCRIPTOR.message_types_by_name['FlightControlException']
_FLIGHTCONTROLEXCEPTION_SENSORID = _FLIGHTCONTROLEXCEPTION.nested_types_by_name['SensorId']
_CAPTAINEXCEPTION = DESCRIPTOR.message_types_by_name['CaptainException']
_BATTERYEXCEPTION = DESCRIPTOR.message_types_by_name['BatteryException']
_CAMERASERVICEEXCEPTION = DESCRIPTOR.message_types_by_name['CameraServiceException']
_CPUEXCEPTION = DESCRIPTOR.message_types_by_name['CpuException']
_ADSPEXCEPTION = DESCRIPTOR.message_types_by_name['AdspException']
_SDSPEXCEPTION = DESCRIPTOR.message_types_by_name['SdspException']
_STORAGEEXCEPTION = DESCRIPTOR.message_types_by_name['StorageException']
_WIFIEXCEPTION = DESCRIPTOR.message_types_by_name['WifiException']
_FPVEXCEPTION = DESCRIPTOR.message_types_by_name['FpvException']
_OTAEXCEPTION = DESCRIPTOR.message_types_by_name['OtaException']
_TAKEOFFEXCEPTION = DESCRIPTOR.message_types_by_name['TakeOffException']
_FLYINGEXCEPTION = DESCRIPTOR.message_types_by_name['FlyingException']
_GESEXCEPTION = DESCRIPTOR.message_types_by_name['GESException']
_TRACKEREXCEPTION = DESCRIPTOR.message_types_by_name['TrackerException']
_OBSTACLEAVOIDANCEEXCEPTION = DESCRIPTOR.message_types_by_name['ObstacleAvoidanceException']
_GIMBALEXCEPTION = DESCRIPTOR.message_types_by_name['GimbalException']
_EISEXCEPTION = DESCRIPTOR.message_types_by_name['EISException']
_FLIGHTCONTROLEXCEPTION_COMPONENT = _FLIGHTCONTROLEXCEPTION.enum_types_by_name['Component']
_FLIGHTCONTROLEXCEPTION_EXCEPTIONTYPE = _FLIGHTCONTROLEXCEPTION.enum_types_by_name['ExceptionType']
_CAPTAINEXCEPTION_EXCEPTIONTYPE = _CAPTAINEXCEPTION.enum_types_by_name['ExceptionType']
_BATTERYEXCEPTION_EXCEPTIONTYPE = _BATTERYEXCEPTION.enum_types_by_name['ExceptionType']
_CAMERASERVICEEXCEPTION_EXCEPTIONTYPE = _CAMERASERVICEEXCEPTION.enum_types_by_name['ExceptionType']
_CPUEXCEPTION_EXCEPTIONTYPE = _CPUEXCEPTION.enum_types_by_name['ExceptionType']
_ADSPEXCEPTION_EXCEPTIONTYPE = _ADSPEXCEPTION.enum_types_by_name['ExceptionType']
_SDSPEXCEPTION_EXCEPTIONTYPE = _SDSPEXCEPTION.enum_types_by_name['ExceptionType']
_STORAGEEXCEPTION_EXCEPTIONTYPE = _STORAGEEXCEPTION.enum_types_by_name['ExceptionType']
_WIFIEXCEPTION_EXCEPTIONTYPE = _WIFIEXCEPTION.enum_types_by_name['ExceptionType']
_FPVEXCEPTION_EXCEPTIONTYPE = _FPVEXCEPTION.enum_types_by_name['ExceptionType']
_OTAEXCEPTION_EXCEPTIONTYPE = _OTAEXCEPTION.enum_types_by_name['ExceptionType']
_TAKEOFFEXCEPTION_EXCEPTIONTYPE = _TAKEOFFEXCEPTION.enum_types_by_name['ExceptionType']
_FLYINGEXCEPTION_EXCEPTIONTYPE = _FLYINGEXCEPTION.enum_types_by_name['ExceptionType']
_GESEXCEPTION_EXCEPTIONTYPE = _GESEXCEPTION.enum_types_by_name['ExceptionType']
_TRACKEREXCEPTION_EXCEPTIONTYPE = _TRACKEREXCEPTION.enum_types_by_name['ExceptionType']
_OBSTACLEAVOIDANCEEXCEPTION_EXCEPTIONTYPE = _OBSTACLEAVOIDANCEEXCEPTION.enum_types_by_name['ExceptionType']
_GIMBALEXCEPTION_EXCEPTIONTYPE = _GIMBALEXCEPTION.enum_types_by_name['ExceptionType']
_EISEXCEPTION_EXCEPTIONTYPE = _EISEXCEPTION.enum_types_by_name['ExceptionType']
ExceptionCollection = _reflection.GeneratedProtocolMessageType('ExceptionCollection', (_message.Message,), {
  'DESCRIPTOR' : _EXCEPTIONCOLLECTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.ExceptionCollection)
  })
_sym_db.RegisterMessage(ExceptionCollection)

Exception = _reflection.GeneratedProtocolMessageType('Exception', (_message.Message,), {
  'DESCRIPTOR' : _EXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.Exception)
  })
_sym_db.RegisterMessage(Exception)

FlightControlException = _reflection.GeneratedProtocolMessageType('FlightControlException', (_message.Message,), {

  'SensorId' : _reflection.GeneratedProtocolMessageType('SensorId', (_message.Message,), {
    'DESCRIPTOR' : _FLIGHTCONTROLEXCEPTION_SENSORID,
    '__module__' : 'exception_pb2'
    # @@protoc_insertion_point(class_scope:exception.FlightControlException.SensorId)
    })
  ,
  'DESCRIPTOR' : _FLIGHTCONTROLEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.FlightControlException)
  })
_sym_db.RegisterMessage(FlightControlException)
_sym_db.RegisterMessage(FlightControlException.SensorId)

CaptainException = _reflection.GeneratedProtocolMessageType('CaptainException', (_message.Message,), {
  'DESCRIPTOR' : _CAPTAINEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.CaptainException)
  })
_sym_db.RegisterMessage(CaptainException)

BatteryException = _reflection.GeneratedProtocolMessageType('BatteryException', (_message.Message,), {
  'DESCRIPTOR' : _BATTERYEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.BatteryException)
  })
_sym_db.RegisterMessage(BatteryException)

CameraServiceException = _reflection.GeneratedProtocolMessageType('CameraServiceException', (_message.Message,), {
  'DESCRIPTOR' : _CAMERASERVICEEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.CameraServiceException)
  })
_sym_db.RegisterMessage(CameraServiceException)

CpuException = _reflection.GeneratedProtocolMessageType('CpuException', (_message.Message,), {
  'DESCRIPTOR' : _CPUEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.CpuException)
  })
_sym_db.RegisterMessage(CpuException)

AdspException = _reflection.GeneratedProtocolMessageType('AdspException', (_message.Message,), {
  'DESCRIPTOR' : _ADSPEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.AdspException)
  })
_sym_db.RegisterMessage(AdspException)

SdspException = _reflection.GeneratedProtocolMessageType('SdspException', (_message.Message,), {
  'DESCRIPTOR' : _SDSPEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.SdspException)
  })
_sym_db.RegisterMessage(SdspException)

StorageException = _reflection.GeneratedProtocolMessageType('StorageException', (_message.Message,), {
  'DESCRIPTOR' : _STORAGEEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.StorageException)
  })
_sym_db.RegisterMessage(StorageException)

WifiException = _reflection.GeneratedProtocolMessageType('WifiException', (_message.Message,), {
  'DESCRIPTOR' : _WIFIEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.WifiException)
  })
_sym_db.RegisterMessage(WifiException)

FpvException = _reflection.GeneratedProtocolMessageType('FpvException', (_message.Message,), {
  'DESCRIPTOR' : _FPVEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.FpvException)
  })
_sym_db.RegisterMessage(FpvException)

OtaException = _reflection.GeneratedProtocolMessageType('OtaException', (_message.Message,), {
  'DESCRIPTOR' : _OTAEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.OtaException)
  })
_sym_db.RegisterMessage(OtaException)

TakeOffException = _reflection.GeneratedProtocolMessageType('TakeOffException', (_message.Message,), {
  'DESCRIPTOR' : _TAKEOFFEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.TakeOffException)
  })
_sym_db.RegisterMessage(TakeOffException)

FlyingException = _reflection.GeneratedProtocolMessageType('FlyingException', (_message.Message,), {
  'DESCRIPTOR' : _FLYINGEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.FlyingException)
  })
_sym_db.RegisterMessage(FlyingException)

GESException = _reflection.GeneratedProtocolMessageType('GESException', (_message.Message,), {
  'DESCRIPTOR' : _GESEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.GESException)
  })
_sym_db.RegisterMessage(GESException)

TrackerException = _reflection.GeneratedProtocolMessageType('TrackerException', (_message.Message,), {
  'DESCRIPTOR' : _TRACKEREXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.TrackerException)
  })
_sym_db.RegisterMessage(TrackerException)

ObstacleAvoidanceException = _reflection.GeneratedProtocolMessageType('ObstacleAvoidanceException', (_message.Message,), {
  'DESCRIPTOR' : _OBSTACLEAVOIDANCEEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.ObstacleAvoidanceException)
  })
_sym_db.RegisterMessage(ObstacleAvoidanceException)

GimbalException = _reflection.GeneratedProtocolMessageType('GimbalException', (_message.Message,), {
  'DESCRIPTOR' : _GIMBALEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.GimbalException)
  })
_sym_db.RegisterMessage(GimbalException)

EISException = _reflection.GeneratedProtocolMessageType('EISException', (_message.Message,), {
  'DESCRIPTOR' : _EISEXCEPTION,
  '__module__' : 'exception_pb2'
  # @@protoc_insertion_point(class_scope:exception.EISException)
  })
_sym_db.RegisterMessage(EISException)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LEVEL._serialized_start=7847
  _LEVEL._serialized_end=7889
  _EXCEPTIONCOLLECTION._serialized_start=30
  _EXCEPTIONCOLLECTION._serialized_end=93
  _EXCEPTION._serialized_start=96
  _EXCEPTION._serialized_end=1151
  _FLIGHTCONTROLEXCEPTION._serialized_start=1154
  _FLIGHTCONTROLEXCEPTION._serialized_end=3054
  _FLIGHTCONTROLEXCEPTION_SENSORID._serialized_start=1370
  _FLIGHTCONTROLEXCEPTION_SENSORID._serialized_end=1392
  _FLIGHTCONTROLEXCEPTION_COMPONENT._serialized_start=1395
  _FLIGHTCONTROLEXCEPTION_COMPONENT._serialized_end=1556
  _FLIGHTCONTROLEXCEPTION_EXCEPTIONTYPE._serialized_start=1559
  _FLIGHTCONTROLEXCEPTION_EXCEPTIONTYPE._serialized_end=3054
  _CAPTAINEXCEPTION._serialized_start=3057
  _CAPTAINEXCEPTION._serialized_end=3501
  _CAPTAINEXCEPTION_EXCEPTIONTYPE._serialized_start=3135
  _CAPTAINEXCEPTION_EXCEPTIONTYPE._serialized_end=3501
  _BATTERYEXCEPTION._serialized_start=3504
  _BATTERYEXCEPTION._serialized_end=4222
  _BATTERYEXCEPTION_EXCEPTIONTYPE._serialized_start=3582
  _BATTERYEXCEPTION_EXCEPTIONTYPE._serialized_end=4222
  _CAMERASERVICEEXCEPTION._serialized_start=4225
  _CAMERASERVICEEXCEPTION._serialized_end=4371
  _CAMERASERVICEEXCEPTION_EXCEPTIONTYPE._serialized_start=4314
  _CAMERASERVICEEXCEPTION_EXCEPTIONTYPE._serialized_end=4371
  _CPUEXCEPTION._serialized_start=4374
  _CPUEXCEPTION._serialized_end=4517
  _CPUEXCEPTION_EXCEPTIONTYPE._serialized_start=4443
  _CPUEXCEPTION_EXCEPTIONTYPE._serialized_end=4517
  _ADSPEXCEPTION._serialized_start=4519
  _ADSPEXCEPTION._serialized_end=4634
  _ADSPEXCEPTION_EXCEPTIONTYPE._serialized_start=4590
  _ADSPEXCEPTION_EXCEPTIONTYPE._serialized_end=4634
  _SDSPEXCEPTION._serialized_start=4636
  _SDSPEXCEPTION._serialized_end=4751
  _SDSPEXCEPTION_EXCEPTIONTYPE._serialized_start=4707
  _SDSPEXCEPTION_EXCEPTIONTYPE._serialized_end=4751
  _STORAGEEXCEPTION._serialized_start=4754
  _STORAGEEXCEPTION._serialized_end=4917
  _STORAGEEXCEPTION_EXCEPTIONTYPE._serialized_start=4831
  _STORAGEEXCEPTION_EXCEPTIONTYPE._serialized_end=4917
  _WIFIEXCEPTION._serialized_start=4920
  _WIFIEXCEPTION._serialized_end=5070
  _WIFIEXCEPTION_EXCEPTIONTYPE._serialized_start=4991
  _WIFIEXCEPTION_EXCEPTIONTYPE._serialized_end=5070
  _FPVEXCEPTION._serialized_start=5073
  _FPVEXCEPTION._serialized_end=5242
  _FPVEXCEPTION_EXCEPTIONTYPE._serialized_start=5142
  _FPVEXCEPTION_EXCEPTIONTYPE._serialized_end=5242
  _OTAEXCEPTION._serialized_start=5245
  _OTAEXCEPTION._serialized_end=5463
  _OTAEXCEPTION_EXCEPTIONTYPE._serialized_start=5315
  _OTAEXCEPTION_EXCEPTIONTYPE._serialized_end=5463
  _TAKEOFFEXCEPTION._serialized_start=5466
  _TAKEOFFEXCEPTION._serialized_end=6119
  _TAKEOFFEXCEPTION_EXCEPTIONTYPE._serialized_start=5544
  _TAKEOFFEXCEPTION_EXCEPTIONTYPE._serialized_end=6119
  _FLYINGEXCEPTION._serialized_start=6122
  _FLYINGEXCEPTION._serialized_end=6257
  _FLYINGEXCEPTION_EXCEPTIONTYPE._serialized_start=6197
  _FLYINGEXCEPTION_EXCEPTIONTYPE._serialized_end=6257
  _GESEXCEPTION._serialized_start=6260
  _GESEXCEPTION._serialized_end=6764
  _GESEXCEPTION_EXCEPTIONTYPE._serialized_start=6330
  _GESEXCEPTION_EXCEPTIONTYPE._serialized_end=6764
  _TRACKEREXCEPTION._serialized_start=6767
  _TRACKEREXCEPTION._serialized_end=6966
  _TRACKEREXCEPTION_EXCEPTIONTYPE._serialized_start=6863
  _TRACKEREXCEPTION_EXCEPTIONTYPE._serialized_end=6966
  _OBSTACLEAVOIDANCEEXCEPTION._serialized_start=6969
  _OBSTACLEAVOIDANCEEXCEPTION._serialized_end=7502
  _OBSTACLEAVOIDANCEEXCEPTION_EXCEPTIONTYPE._serialized_start=7067
  _OBSTACLEAVOIDANCEEXCEPTION_EXCEPTIONTYPE._serialized_end=7502
  _GIMBALEXCEPTION._serialized_start=7505
  _GIMBALEXCEPTION._serialized_end=7724
  _GIMBALEXCEPTION_EXCEPTIONTYPE._serialized_start=7581
  _GIMBALEXCEPTION_EXCEPTIONTYPE._serialized_end=7724
  _EISEXCEPTION._serialized_start=7726
  _EISEXCEPTION._serialized_end=7845
  _EISEXCEPTION_EXCEPTIONTYPE._serialized_start=7795
  _EISEXCEPTION_EXCEPTIONTYPE._serialized_end=7845
# @@protoc_insertion_point(module_scope)
