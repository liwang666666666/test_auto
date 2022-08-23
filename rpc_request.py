import sys
import os
import inspect
import argparse
import traceback

sys.path.append(os.getcwd() + '/proto_py')
from proto_py import service_pb2


"""
python3 -m grpc_tools.protoc -I ./proto --python_out=./proto_py --grpc_python_out=./proto_py ./proto/*.proto
"""

class H130_Test(object):
    def __init__(self):
        self.cmd = service_pb2.RpcRequest()
        self.cmd.id = 123

    # // for debugging purpose
    # string echo_request;
    def echo_request(self, echo_request='thinks H130'):
        '''
        :params echo_request string // for debugging purpose
        '''
        try:
            self.cmd.echo_request = str(echo_request)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // for debugging purpose
    # string test_request;
    def test_request(self, test_request='H130'):
        '''
        :param test_request string // for debugging purpose
        '''
        try:
            self.cmd.test_request = str(test_request)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // set serial number request
    # string set_serial_number_request;
    def set_serial_number_request(self, serial_number='50901A0Z00003432'):
        '''
        :param serial_number string // set serial number request
        '''
        try:
            self.cmd.set_serial_number_request = str(serial_number)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // get serial number request
    # Empty get_serial_number_request;
    def get_serial_number_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_serial_number_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Returns code verison info
    # Empty git_request;
    def git_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.git_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set device name
    # BleName set_name_request;
    def set_name_request(self, name='H130_zzz_wifi', usb_name='H130_zzz_wifi'):
        '''
        :param name string // device name
        required string name;

        :param usb_name string // USB drive name
        optional string usb_name;
        '''
        try:
            self.cmd.set_name_request.name = str(name)
            self.cmd.set_name_request.usb_name = str(usb_name)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get device name
    # Empty get_name_request;
    def get_name_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_name_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Direct query for media count
    # // 获取媒体文件数量
    # Empty media_counts_get_request;
    def media_counts_get_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.media_counts_get_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Media request
    # // media命令请求
    # MediaRequest media_request;
    def media_request(self, request_type=7, transfer_uuid='cb477be5-29ef-459c-9f06-2fb236d2fea5', transfer_type=4, deletion_uuid='cb477be5-29ef-459c-9f06-2fb236d2fea5', mark_transferred_uuid='111',session_id = '111'):
        '''

        :param request_type {UNSET:0, LIST_AVAILABLE_MEDIA:1, GET_MEDIA_FILE:2, DELETE_MEDIA_FILE:3, START_AS_NEED_DELETION:4, MARK_TRANSFERRED:5} // Request type
        required MediaRequestType type;

        :param transfer_uuid string // Request a specific media file
        optional MediaFileTransferRequest media_file_transfer_request;

        :param transfer_type {}//MediaType type
            =UNSET=0
            =METADATA=1
            =THUMBNAIL=2
            =VIDEO=3
            =PICTURE=4
            =IMU_DATA=5
            =ANIMATED_THUMBNAIL=6

        --Range range
        // Request deletion of a specific file
        optional MediaFileDeletionRequest media_file_deletion_request = 3;
        =string uuid
        // Mark a specific file as transferred
        optional MediaFileMarkTransferredRequest media_file_mark_transferred_request = 4;
        =string uuid
        '''
        try:
            self.cmd.media_request.type = int(request_type)

            # self.cmd.media_request.media_file_transfer_request.uuid = str(transfer_uuid)
            # self.cmd.media_request.media_file_transfer_request.type = int(transfer_type)
            # # self.cmd.media_request.media_file_transfer_request.range =   //Range

            # self.cmd.media_request.media_file_deletion_request.uuid = str(deletion_uuid)
            # self.cmd.media_request.media_file_mark_transferred_request.uuid = str(mark_transferred_uuid)

            # self.cmd.media_request.session_id = session_id
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Wifi start request
    # WifiParams wifi_start_request;
    def wifi_start_request(self, res_type=1, ssid='H130_zzz_wifi', password='1234567890', frequency=1, country='CN', frequency_strategy=0):
        '''
        // wifi setting type
        required WifiSetting type = 1;
            =DISABLED_UNSET=0
            =AP=1
            =STA=2
            =P2P=3
            =SCAN=4
        // ssid
        optional string ssid = 2;
        // password
        optional string password = 3;
        // frequency
        optional uint32 frequency = 4;
        // Represents 2 byte code (i.e. US - USA, CH - Switzerland, etc.)
        optional string country = 5;
        // frequency strategy
        optional WifiFrequencyStrategy frequency_strategy = 6;
            =USE_BEST_AVAILABLE_UNSET=0
            =USE_2_4GHZ_ONLY=1 # wifi_start_request set_scheduled_update_request
        '''
        try:
            self.cmd.wifi_start_request.type = int(res_type)
            self.cmd.wifi_start_request.ssid = str(ssid)
            self.cmd.wifi_start_request.password = str(password)
            # self.cmd.wifi_start_request.frequency = int(frequency)
            self.cmd.wifi_start_request.country = str(country)
            self.cmd.wifi_start_request.frequency_strategy = int(
                frequency_strategy)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Wifi stop request
    # Empty wifi_stop_request;
    def wifi_stop_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.wifi_stop_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Battery status request
    # Empty battery_status_request;
    def battery_status_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.battery_status_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Charger state request
    # // 充电状态请求
    # Empty charger_state_request;
    def charger_state_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.charger_state_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Logs zip request
    # // 日志zip包请求，暂不实现
    # Empty logs_zip_request = 15;
    def logs_zip_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.logs_zip_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Request board ID
    # Empty board_id_request 暂不实现
    def board_id_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.board_id_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Send Location object
    # // Location信息相关请求
    # LocationData location_request
    def location_request(self, latitude=1.1, longitude=1.1, speed_mps=1, utc_time=1657765158, heading_deg=1, height_mm=1, h_acc_mm=1, v_acc_mm=1):
        '''
        // latitude
        optional float latitude = 1;
        // longitude
        optional float longitude = 2;
        // speed in meters per second
        optional uint32 speed_mps = 3;
        // utc timestamp
        optional uint64 utc_time = 4;
        // heading in degrees
        optional int32 heading_deg = 5;
        // height in meters
        optional int32 height_mm = 6;
        // horizontal accuracy
        optional uint32 h_acc_mm = 7;
        // vertical accuracy
        optional uint32 v_acc_mm = 8;
        '''
        try:
            self.cmd.location_request.latitude = float(latitude)
            self.cmd.location_request.longitude = float(longitude)
            self.cmd.location_request.speed_mps = int(speed_mps)
            # print(int(time.time()))
            # print(utc_time, type(utc_time))
            self.cmd.location_request.utc_time = int(utc_time)
            self.cmd.location_request.heading_deg = int(heading_deg)
            self.cmd.location_request.height_mm = int(height_mm)
            self.cmd.location_request.h_acc_mm = int(h_acc_mm)
            self.cmd.location_request.v_acc_mm = int(v_acc_mm)
            # return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // get temperature request
    # // 飞机温度状态请求
    # Empty get_temperature_request;
    def get_temperature_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_temperature_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // For 3PA symmetric encryption, exchange public key request. This is sent from client to device.
    # // 设置公钥请求， 暂不实现
    # KeyExchangeMessage set_pairing_public_key_request
    def set_pairing_public_key_request(self):
        '''
        // Key exchange setup related nonce
        required bytes nonce = 1;
        // Key exchange setup related public key
        required bytes public_key = 2;
        '''
        try:
            self.cmd.set_pairing_public_key_request.nonce = b''
            self.cmd.set_pairing_public_key_request.public_key = b''
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // For 3PA symmetric encryption, peer verification request. This is sent from client to device.
    # // 对等加密校验请求，暂不实现
    # PeerVerificationMessage set_peer_verification_request
    def set_peer_verification_request(self):
        '''
        // Verification message tag
        required bytes tag = 1;
        // Verification message cipher text
        required bytes ciphertext = 2;
        '''
        try:
            self.cmd.set_peer_verification_request.tag = b'111'
            self.cmd.set_peer_verification_request.ciphertext = b'111'
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Exchange nonces between client and device (BLE)
    # // in order to establish a secure channel for encrypted communication
    # // 交换通道加密nonce请求，暂不实现
    # EncryptionNonceExchange set_channel_encryption_nonce_request
    def set_channel_encryption_nonce_request(self,channel_id=1):
        '''
        // Nonce bytes
        optional bytes nonce = 1;
        // Comm channel
        optional CommChannelType channel_id = 2;
            =COMM_CHANNEL_BLE_QCA=2
            =COMM_CHANNEL_WIFI_QCA=3
            =COMM_CHANNEL_BTC_QCA=4
            =COMM_CHANNEL_HOST_TO_DEVICE=16;
        '''
        try:
            self.cmd.set_channel_encryption_nonce_request.nonce = b''
            self.cmd.set_channel_encryption_nonce_request.channel_id = channel_id
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get the status of USB import, on or off.
    # // 获取usb导出功能开启状态
    # Empty get_enable_usb_import_request
    def get_enable_usb_import_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_enable_usb_import_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set enable or disable USB import request
    # // 开启或关闭usb导出功能
    # bool set_enable_usb_import_request;
    def set_enable_usb_import_request(self, import_request='True'):
        try:
            if import_request == 'True':
                get_import_request = True
            elif import_request == 'False':
                get_import_request = False
            self.cmd.set_enable_usb_import_request = get_import_request
            # self.cmd.set_enable_usb_import_request = bool(import_request)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Clear Cheerios storage
    # // 清空飞机存储
    # Empty clear_content_request
    def clear_content_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.clear_content_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Restart Cheerios request
    # // 重启飞机
    # Empty halt_request
    def halt_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.halt_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Unpair/forget Cheerios device
    # // 取消配对
    # Empty unpair_device_request
    def unpair_device_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.unpair_device_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set time request
    # // 同步UTC时间到飞机
    # RealTimeMessage set_time_utc_request
    def set_time_utc_request(self, time_utc=1660701889, time_zone=8, time_zone_str='Asia/Shanghai'):
        '''
        // The number of seconds since 1970.
        required uint64 time_utc = 1
        // This is actually the UTC offset (e.g. -8 for Los Angeles)
        optional int32 time_zone = 2
        // This is the timezone string for Android (e.g. US/Pacific)
        optional string time_zone_str = 3
        '''
        try:
            self.cmd.set_time_utc_request.time_utc = int(time_utc)
            self.cmd.set_time_utc_request.time_zone = int(time_zone)
            self.cmd.set_time_utc_request.time_zone_str = str(time_zone_str)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Pairing timer kick request
    # // 等待用户配对中，暂不实现
    # Empty pairing_wait_for_user_request
    def pairing_wait_for_user_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.pairing_wait_for_user_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // ota update request
    # // OTA更新请求
    # OTAUpdateRequest ota_update_request
    def ota_update_request(self, request_type=0):
        '''
        // Request type
        optional OTAUpdateRequestType request_type = 1;
            =TYPE_UNSET=0
            =GET_CURRENT_VERSION=1
            =APPLY_DELTA_PATCH=2
            =APPLY_FULL_OTA=3
            =GET_CHECKSUM_MD5_SHA=4
            =CANCEL=5
            =REBOOT_AND_SWITCH_PARTITION=6
        '''
        try:
            self.cmd.ota_update_request.request_type = int(request_type)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // firmware update upload request
    # // OTA固件上传
    # FirmwareUpdateUploadRequest firmware_update_upload_request
    def firmware_update_upload_request(self):
        '''
        // Required. Should contain data to write to update file.
        // If field is not specified, an error will be returned and no filesystem changes will occur.
        optional bytes data = 1;
        // Required.
        // We will write data to file position starting at byte startPos (0 based), overwriting
        // any existing data in range [startPos, startPos + len(data)), only creating a new file if one did not exist
        // previously.
        // Preconditions if included: (Violations will result in an error returned and no filesystem changes)
        // startPos <= size of current file on disk
        // if overwriteExistingFile == true, startPos must be 0.
        optional uint32 start_pos = 2;
        // Required.
        // If true, new file will be created overwriting old one and startPos must be 0.
        // If false, new file will still be created if one does not exist.
        optional bool overwrite_existing_file = 3;
        '''
        self.cmd.firmware_update_upload_request.data = b''
        self.cmd.firmware_update_upload_request.start_pos = 111

        self.cmd.firmware_update_upload_request.overwrite_existing_file = True
        return 1

    # // dial positon request
    # // 获取当前档位
    # Empty get_flight_mode_request
    def get_flight_mode_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_flight_mode_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // flight status request
    # // 获取飞机飞行状态
    # Empty get_flight_status_request = 33;
    def get_flight_status_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_flight_status_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // abort flight request
    # // 中止飞行任务并返航
    # Empty abort_flight_request
    def abort_flight_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.abort_flight_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // storage capacity request
    # // 获取存储容量信息
    # Empty get_storage_capacity_request
    def get_storage_capacity_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_storage_capacity_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // set OTA scheduled update request
    # // 设置计划升级
    # OTAScheduledUpdate set_scheduled_update_request
    def set_scheduled_update_request(self, target_hash='111', target_version_tag='1.0', utc_time_update_window_start=1, utc_time_update_window_stop=1, is_full_update='True'):
        '''
        // target hash for scheduled update
        optional string target_hash = 1;
        // target version tag for sche+duled update
        optional string target_version_tag = 2;
        // utc time from midnight in seconds when update
        // window should begin
        optional uint32 utc_time_update_window_start = 3;
        // utc time from midnight in seconds when update
        // window should end
        optional uint32 utc_time_update_window_stop = 4;
        // flag to determine if update is full update
        optional bool is_full_update = 5;
        '''
        try:
            self.cmd.set_scheduled_update_request.target_hash = str(target_hash)
            self.cmd.set_scheduled_update_request.target_version_tag = str(target_version_tag)
            self.cmd.set_scheduled_update_request.utc_time_update_window_start = int(utc_time_update_window_start)
            self.cmd.set_scheduled_update_request.utc_time_update_window_stop = int(utc_time_update_window_stop)
            if is_full_update == 'True':
                get_is_full_update = True
            elif is_full_update == 'False':
                get_is_full_update = False
            self.cmd.set_scheduled_update_request.is_full_update = get_is_full_update
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // get OTA scheduled update request
    # // 获取计划升级信息
    # Empty get_scheduled_update_request
    def get_scheduled_update_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_scheduled_update_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // disable flight request
    # // 禁止飞行
    # DisableFlightRequest disable_flight_request
    def disable_flight_request(self, disable='True'):
        '''
        // Used to specify if flight should be enabled or disabled
        optional bool disable = 1;
        '''
        try:
            if disable == 'True':
                get_disable = True
            elif disable == 'False':
                get_disable = False
            self.cmd.disable_flight_request.disable = get_disable
            # self.cmd.disable_flight_request.disable = bool(disable)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Verifies user is allowed to pair.
    # // 配对验证请求，暂不实现
    # ValidatePairingRequest validate_pairing_request
    def validate_pairing_request(self, user_id='111'):
        '''
        // Required, the unique user id.
        optional string user_id = 1;
        '''
        try:
            self.cmd.validate_pairing_request.user_id = str(user_id)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set capture duration
    # // 设置指定轨迹模式下的采集间隔时间
    # DurationParams set_capture_duration_request
    def set_capture_duration_request(self, mode_type=1, duration=30):
        '''
        // Used to specify the flight mode being configured
        optional FlightModeConfig flight_mode = 1;
        -optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        // Used to specify the duration in seconds or orbits
        optional uint32 duration = 2;
        '''
        try:
            self.cmd.set_capture_duration_request.flight_mode.type = int(float(mode_type))
            self.cmd.set_capture_duration_request.duration = int(duration)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get capture duration
    # // 获取指定轨迹模式下的采集间隔时间
    # FlightModeConfig get_capture_duration_request
    def get_capture_duration_request(self, mode_type=1):
        '''
        // Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.get_capture_duration_request.type = int(float(mode_type))
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set video resolution
    # // 设置指定轨迹模式下的视频分辨率
    # VideoResolutionParams set_video_resolution_request
    def set_video_resolution_request(self, mode_type=1, res=1, fps=1):
        '''
        // Used to specify the flight mode being configured
        optional FlightModeConfig flight_mode = 1;
        --// Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        // Video resolution
        optional Resolution res = 2;
            // Unset
            =UNSET = 0;
            // Medium Resolution (1080p)
            =MEDIUM_RESOLUTION = 1;
            // High Resolution (2.7k)
            =HIGH_RESOLUTION = 2;
            // 1440p Resolution
            =RESOLUTION_1440P = 3;
        fps:
            // Unset
            FRAMERATE_UNSET = 0;
            FRAMERATE_30FPS = 1;
            FRAMERATE_60FPS = 2;
        '''
        try:
            self.cmd.set_video_resolution_request.flight_mode.type = int(float(mode_type))
            self.cmd.set_video_resolution_request.res = int(res)
            self.cmd.set_video_resolution_request.fps = int(fps)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get video resolution
    # // 获取指定轨迹模式下的视频分辨率
    # FlightModeConfig get_video_resolution_request
    def get_video_resolution_request(self, mode_type=1):
        '''
        // Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.get_video_resolution_request.type = int(float(mode_type))
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set flight distance
    # // 设置指定轨迹模式下的飞行距离
    # DistanceParams set_flight_distance_request
    def set_flight_distance_request(self, mode_type=2, meters=8.5): #  distance=6,
        '''
        // Used to specify the flight mode being configured
        optional FlightModeConfig flight_mode = 1;
        --// Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        // Deprecated. Floor value of meters field.

        # // Use as fallback when meters not provided.
        # optional uint32 distance = 2;

        // Float value of distance in meters
        optional float meters = 3;
        '''
        try:
            self.cmd.set_flight_distance_request.flight_mode.type = int(float(mode_type))
            # self.cmd.set_flight_distance_request.distance = int(distance)
            self.cmd.set_flight_distance_request.meters = float(meters)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get flight distance
    # // 获取指定轨迹模式下的飞行距离
    # FlightModeConfig get_flight_distance_request
    def get_flight_distance_request(self, mode_type=1):
        '''
        // Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.get_flight_distance_request.type = int(float(mode_type))
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set capture type
    # // 设置指定轨迹模式下的采集类型
    # CaptureTypeParams set_capture_type_request
    def set_capture_type_request(self, mode_type=1, capture_type=1):
        '''
        // Used to specify the flight mode being configured
        optional FlightModeConfig flight_mode = 1;
        --// Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        // Capture Type
        optional CaptureType capture_type = 2;
            // Unset
            =UNSET = 0;
            // Picture
            =PICTURE = 1;
            // Video
            =VIDEO = 2;
            // Picture and Video
            =PICTURE_AND_VIDEO = 3;
        '''
        try:
            self.cmd.set_capture_type_request.flight_mode.type = int(float(mode_type))
            self.cmd.set_capture_type_request.capture_type = int(capture_type)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get capture type
    # // 获取指定轨迹模式下的采集类型
    # FlightModeConfig get_capture_type_request = 137;
    def get_capture_type_request(self, mode_type=1):
        '''
        // Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.get_capture_type_request.type = int(float(mode_type))
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set face/body tracking
    # // 开启或关闭指定轨迹模式下的tracking
    # TrackingParams set_tracking_request
    def set_tracking_request(self, mode_type=1, tracking='True'):
        '''
        // Used to specify the flight mode being configured
        optional FlightModeConfig flight_mode = 1;
        --// Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        // Used to specify if face/body tracking is active
        optional bool tracking = 2;
        '''
        try:
            self.cmd.set_tracking_request.flight_mode.type = int(float(mode_type))
            if tracking == 'True':
                get_tracking = True
            elif tracking == 'False':
                get_tracking = False
            self.cmd.set_tracking_request.tracking = get_tracking
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get face/body tracking
    # // 获取指定轨迹模式下的tracking状态
    # FlightModeConfig get_tracking_request
    def get_tracking_request(self, mode_type=1):
        '''
        // Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''

        try:
            self.cmd.get_tracking_request.type = int(float(mode_type))
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get remaining flights info request
    # // 获取指定轨迹模式下的剩余飞行信息
    # Empty get_remaining_flights_info_request
    def get_remaining_flights_info_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_remaining_flights_info_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set video format
    # // 设置指定轨迹模式下的视频格式
    # VideoFormatParams set_video_format_request
    def set_video_format_request(self, mode_type=1, res_format=1):
        '''
        // Required. Used to specify the flight mode being configured
        optional FlightModeConfig flight_mode = 1;
        --// Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        // Required. Video format
        optional VideoFormat format = 2;
            // Unset
            =UNSET = 0;
            // AVC
            =AVC = 1;
            // HEVC
            =HEVC = 2;
        '''
        try:
            self.cmd.set_video_format_request.flight_mode.type = int(float(mode_type))
            self.cmd.set_video_format_request.format = int(res_format)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get video format
    # // 获取指定轨迹模式下的视频格式
    # FlightModeConfig get_video_format_request
    def get_video_format_request(self, mode_type=1):
        '''
        // Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.get_video_format_request.type = int(float(mode_type))
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get flight status error request
    # // 获取飞行errorcode列表
    # Empty get_flight_status_error_request
    def get_flight_status_error_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_flight_status_error_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set custom flight mode
    # // 设置custom档位的轨迹模式
    # CustomFlightMode set_custom_flight_mode_request
    def set_custom_flight_mode_request(self, mode_type=1):
        '''
        // Used to specify custom flight mode, sending "custom" will clear
        optional FlightModeConfig flight_mode = 1;
        --// Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.set_custom_flight_mode_request.flight_mode.type = int(float(mode_type))
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get custom flight mode
    # // 获取custom档位的轨迹模式
    # Empty get_custom_flight_mode_request
    def get_custom_flight_mode_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_custom_flight_mode_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get USB connection status
    # // 获取usb连接状态
    # Empty get_usb_connection_request
    def get_usb_connection_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_usb_connection_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Check if ADB is enabled
    # // 获取adb使能状态
    # Empty get_enable_adb_request
    def get_enable_adb_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_enable_adb_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Enable or disable ADB
    # // 开启或关闭adb功能
    # bool set_enable_adb_request
    def set_enable_adb_request(self, adb_request='True'):
        try:
            if adb_request == 'True':
                get_adb_request = True
            elif adb_request == 'False':
                get_adb_request = False
            self.cmd.set_enable_adb_request = get_adb_request
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set the dial position to MANUAL or not
    # // 设置档位（飞行模式）为手动或者智能轨迹
    # bool set_flight_mode_to_manual_request = 46;
    def set_flight_mode_to_manual_request(self, manual_request='True'):
        try:
            if manual_request == 'True':
                get_manual_request = True
            elif manual_request == 'False':
                get_manual_request = False
            self.cmd.set_flight_mode_to_manual_request = get_manual_request
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0
    
    # // Enable or disable the system sound
    # // 开启或关闭系统声音
    # bool set_enable_system_sound_request = 47;
    def set_enable_system_sound_request(self, sound_request='True'):
        try:
            if sound_request == 'True':
                get_sound_request = True
            elif sound_request == 'False':
                get_sound_request = False
            self.cmd.set_enable_system_sound_request = get_sound_request
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0
    
    # // Get the system sound state
    # // 获取系统声音开关
    # Empty get_enable_system_sound_request = 48;
    def get_enable_system_sound_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_enable_system_sound_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Restore factory settings
    # Empty restore_factory_settings_request = 49;
    def restore_factory_settings_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.restore_factory_settings_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set photo resolution
    # // 设置指定轨迹模式下的拍照分辨率
    # PhotoResolutionParams set_photo_resolution_request
    def set_photo_resolution_request(self, mode_type=1, res=1):
        '''
        // Used to specify the flight mode being configured
        optional FlightModeConfig flight_mode = 1;
        --// Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        // Photo resolution
        optional Resolution res = 2;
            // Unset
            UNSET = 0;
            // Medium Resolution (5MP)
            MEDIUM_RESOLUTION = 1;
            // High Resolution (12MP)
            HIGH_RESOLUTION = 2;
        '''
        try:
            self.cmd.set_photo_resolution_request.flight_mode.type = int(float(mode_type))
            self.cmd.set_photo_resolution_request.res = int(res)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get photo resolution
    # // 获取指定轨迹模式下的拍照分辨率
    # FlightModeConfig get_photo_resolution_request
    def get_photo_resolution_request(self, mode_type=1):
        '''
        // Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.get_photo_resolution_request.type = int(float(mode_type))
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Cancel scheduled update request
    # // 取消计划升级
    # Empty cancel_scheduled_update_request
    def cancel_scheduled_update_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.cancel_scheduled_update_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get log file
    # // 日志请求，暂不实现
    # LogRequest log_request
    def log_request(self, res_type=5, log_name='latest_copy.zip'):
        '''
        // Required. The type of log request.
        optional LogRequestType type = 1;
            // Unset
            =LOG_REQUEST_UNSET = 0;
            // Get debugging file list
            =DEBUGGING_FILE_LIST = 1;
            // Get a specific debugging file. The LogRequest with this type must contain LogFileTransferRequest.
            =GET_DEBUGGING_FILE = 2;
            // Delete all debugging log files
            =DELETE_DEBUGGING = 3;
            // Get analytics file list
            =ANALYTICS_FILE_LIST = 4;
            // Get a specific analytics file. The LogRequest with this type must contain LogFileTransferRequest.
            =GET_ANALYTICS_FILE = 5;
            // Delete all analytics log files
            =DELETE_ANALYTICS = 6;
        // The details of the log file to be loaded.
        optional LogFileTransferRequest log_file_transfer_request = 2;
        --// Required. The name of the requested log file.
        --optional string name = 1;
        --// Portion of log file to transfer. If not specified, the entire file is sent.
        --optional Range range = 2;
        '''
        try:
            self.cmd.log_request.type = int(float(res_type))
            self.cmd.log_request.log_file_transfer_request.name = str(log_name)
            # self.cmd.log_request.log_file_transfer_request.range = //Range
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Keep device active
    # // 保持设备活跃，暂不实现
    # KeepDeviceActiveParams keep_device_active_request
    def keep_device_active_request(self):
        try:
            self.cmd.keep_device_active_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Start IMU calibration
    # StartCalibrationRequest start_imu_calibration_request
    def start_imu_calibration_request(self):
        try:
            self.cmd.start_imu_calibration_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Stop IMU calibration
    # StopCalibrationRequest stop_imu_calibration_request
    def stop_imu_calibration_request(self):
        try:
            self.cmd.stop_imu_calibration_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Activate lost mode#
    # // 激活失联模式，暂不实现
    # ActivateLostModeRequest activate_lost_mode_request
    def activate_lost_mode_request(self):
        try:
            self.cmd.activate_lost_mode_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Deactivate lost mode
    # // 解除失联模式，暂不实现
    # DeactivateLostModeRequest deactivate_lost_mode_request
    def deactivate_lost_mode_request(self):
        try:
            self.cmd.deactivate_lost_mode_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get lost mode state
    # // 获取失联模式状态，暂不实现
    # GetLostModeStateRequest get_lost_mode_state_request
    def get_lost_mode_state_request(self):
        try:
            self.cmd.get_lost_mode_state_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Request for getting settings for all flight modes
    # // 获取所有轨迹模式的飞行配置参数
    # Empty get_all_flight_modes_settings_request
    def get_all_flight_modes_settings_request(self):
        '''
        Empty
        '''
        try:
            self.cmd.get_all_flight_modes_settings_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set Preview resolution
    # // 设置指定轨迹模式下的预览流分辨率
    # PreviewResolutionParams set_preview_resolution_request = 148;
    def set_preview_resolution_request(self, flight_mode=1, res=1):
        '''
        flight_mode:
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        res:
            // Unset
            UNSET = 0;
            // Low Resolution (720p)
            LOW_RESOLUTION = 1;
            // Medium Resolution (1080p)
            MEDIUM_RESOLUTION = 2;
        '''
        try:
            self.cmd.set_preview_resolution_request.flight_mode.type = int(float(flight_mode))
            self.cmd.set_preview_resolution_request.res = int(float(res))
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get Preview resolution
    # // 获取指定轨迹模式下的预览流分辨率
    # FlightModeConfig get_preview_resolution_request = 149;
    def get_preview_resolution_request(self, mode_type=1):
        '''
        // Flight mode type variable
        optional FlightModeType type = 1;
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.get_preview_resolution_request.type = int(float(mode_type))
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set Video HDR
    # // 开启或关闭指定轨迹模式下的HDR功能
    # HDRParams set_video_hdr_request = 150;
    def set_video_hdr_request(self, flight_mode=1, hdr_request='True'):
        '''
        flight_mode:
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.set_video_hdr_request.flight_mode.type = int(float(flight_mode))
            if hdr_request == 'True':
                get_hdr_request = True
            elif hdr_request == 'False':
                get_hdr_request = False
            self.cmd.set_video_hdr_request.hdr_enabled = get_hdr_request
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get Video HDR
    # // 获取指定轨迹模式下的HDR功能开启状态
    # FlightModeConfig get_video_hdr_request = 151;
    def get_video_hdr_request(self, mode_type=1):
        '''
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.get_video_hdr_request.type = int(mode_type)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set Photo HDR
    # // 开启或关闭指定轨迹模式下的HDR功能
    # HDRParams set_photo_hdr_request = 152;
    def set_photo_hdr_request(self, flight_mode=1, hdr_enabled='True'):
        '''
        flight_mode:
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.set_photo_hdr_request.flight_mode.type = int(float(flight_mode))
            if hdr_enabled == 'True':
                get_hdr_enable = True
            elif hdr_enabled == 'False':
                get_hdr_enable = False
            self.cmd.set_photo_hdr_request.hdr_enabled = get_hdr_enable
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get Photo HDR
    # // 获取指定轨迹模式下的HDR功能开启状态
    # FlightModeConfig get_photo_hdr_request = 153;
    def get_photo_hdr_request(self, mode_type=1):
        '''
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.get_photo_hdr_request.type = int(mode_type)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set Photo raw
    # // 开启或关闭指定轨迹模式下的raw功能
    # RAWParams set_photo_raw_request = 154;
    def set_photo_raw_request(self, flight_mode=1, raw_enabled='True'):
        '''
        flight_mode:
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.set_photo_raw_request.flight_mode.type = int(float(flight_mode))
            if raw_enabled == 'True':
                get_raw_enabled = True
            elif raw_enabled == 'False':
                get_raw_enabled = False
            self.cmd.set_photo_raw_request.raw_enabled = get_raw_enabled
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get Photo raw
    # // 获取指定轨迹模式下的raw功能开启状态
    # FlightModeConfig get_photo_raw_request = 155;
    def get_photo_raw_request(self, mode_type=1):
        try:
            self.cmd.get_photo_raw_request.type = int(mode_type)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set Photo MFNR
    # // 开启或关闭指定轨迹模式下的MFNR功能
    # MFNRParams set_photo_mfnr_request = 156;
    def set_photo_mfnr_request(self, flight_mode=1, mfnr_enabled='True'):
        '''
        flight_mode:
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.set_photo_mfnr_request.flight_mode.type = int(float(flight_mode))
            if mfnr_enabled == 'True':
                get_mfnr_enabled = True
            elif mfnr_enabled == 'False':
                get_mfnr_enabled = False
            self.cmd.set_photo_mfnr_request.mfnr_enabled = get_mfnr_enabled
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get Photo MFNR
    # // 获取指定轨迹模式下的MFNR功能开启状态
    # FlightModeConfig get_photo_mfnr_request = 157;
    def get_photo_mfnr_request(self, mode_type=1):
        try:
            self.cmd.get_photo_mfnr_request.type = int(mode_type)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set Trajectory Type
    # // 设置指定轨迹模式下的轨迹类型
    # TrajectoryTypeParams set_trajectory_type_request = 158;
    def set_trajectory_type_request(self, flight_mode=1, follow=None, overhead=None):
        '''
        flight_mode:
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        enum FollowTrajectoryType {
            // Unset
            FOLLOW_TRAJ_UNSET = 0;
            // 常规
            FOLLOW_TRAJ_NORMAL = 1;
            // 定向
            FOLLOW_TRAJ_PARALLEL = 2;
        enum OverheadTrajectoryType {
            // Unset
            OVERHEAD_TRAJ_UNSET = 0;
            // 只俯拍
            OVERHEAD_TRAJ_PICTURE = 1;
            // 俯拍+旋转
            OVERHEAD_TRAJ_PIC_ROTATE = 2;
  }
        '''
        try:
            self.cmd.set_trajectory_type_request.flight_mode.type = int(float(flight_mode))
            if follow and not overhead:
                self.cmd.set_trajectory_type_request.follow = int(float(follow))
            if overhead and not follow:
                self.cmd.set_trajectory_type_request.overhead = int(float(overhead))
            if overhead and follow:
                print("Only one of the two parameters can be set : follow | overhead")
                exit()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get Trajectory Type
    # // 获取指定轨迹模式下的轨迹类型
    # FlightModeConfig get_trajectory_type_request = 159;
    def get_trajectory_type_request(self, mode_type=3):
        try:
            self.cmd.get_trajectory_type_request.type = int(mode_type)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set main camera sensor collect framerate
    # // 设置主camera采集帧率
    # CameraFramerateParams set_main_camera_framerate_request = 160;
    def set_main_camera_framerate_request(self, flight_mode=1, fps=1):
        '''
        flight_mode:
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        fps:
            // Unset
            FRAMERATE_UNSET = 0;
            FRAMERATE_30FPS = 1;
            FRAMERATE_60FPS = 2;
        '''
        try:
            self.cmd.set_main_camera_framerate_request.flight_mode.type = int(float(flight_mode))
            self.cmd.set_main_camera_framerate_request.fps = int(float(fps))
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0


    # // Get main camera sensor collect framerate
    # // 获取主camera采集帧率
    # FlightModeConfig get_main_camera_framerate_request = 161;
    def get_main_camera_framerate_request(self, mode_type=1):
        try:
            self.cmd.get_main_camera_framerate_request.type = int(mode_type)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set height params request
    # // 设置指定轨迹模式下的高度参数
    # HeightParams set_flight_height_request = 162;
    def set_flight_height_request(self, flight_mode=5, meters=9.0):
        '''
        flight_mode:
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.set_flight_height_request.flight_mode.type = int(float(flight_mode))
            self.cmd.set_flight_height_request.meters = float(meters)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get height params request
    # // 获取指定轨迹模式下的高度参数
    # FlightModeConfig get_flight_height_request = 163;
    def get_flight_height_request(self, mode_type=2):
        try:
            self.cmd.get_flight_height_request.type = int(mode_type)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Set flight angle params request
    # // 设置指定轨迹模式下的飞行角度参数
    # AngleParams set_flight_angle_request = 164;
    def set_flight_angle_request(self, flight_mode=1, degrees=2.0):
        '''
        flight_mode:
            // Unset
            UNSET = 0;
            // Hover
            // 悬停
            HOVER = 1;
            // Reveal
            // 渐远
            REVEAL = 2;
            // Follow
            // 跟拍
            FOLLOW = 3;
            // Orbit
            // 环绕
            ORBIT = 4;
            // OverHead
            // 俯拍
            OVERHEAD = 5;
            // Custom
            CUSTOM = 6;
            // Manual
            MANUAL = 255;
        '''
        try:
            self.cmd.set_flight_angle_request.flight_mode.type = int(float(flight_mode))
            self.cmd.set_flight_angle_request.degrees = float(degrees)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Get flight angle params request
    # // 获取指定轨迹模式下的飞行角度参数
    # FlightModeConfig get_flight_angle_request = 165;
    def get_flight_angle_request(self, mode_type=1):
        try:
            self.cmd.get_flight_angle_request.type = int(mode_type)
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Request for getting settings for all camera parameters
    # // 获取所有轨迹模式的Camera配置参数
    # Empty get_all_camera_settings_request = 166;
    def get_all_camera_settings_request(self):
        try:
            self.cmd.get_all_camera_settings_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // StartSession:(should be called before other camera cmds)
    # // Generic asset file request
    # // 暂不实现
    # GetFileRequest get_generic_asset_file_request = 280;
    def get_generic_asset_file_request(self, file_identifier='111'):
        '''
        // Uri to fetch the file on device
        optional string file_identifier = 1;
        // Portion of file to transfer. If not specified, entire file is sent.
        optional Range range = 2;
        '''
        try:
            self.cmd.get_generic_asset_file_request.file_identifier = str(file_identifier)
            # self.cmd.get_generic_asset_file_request.range = //Range
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0


    # // StartSession:(should be called before other camera cmds)
    # // 1. fist time must set input sessionid = 0 to get an output sessionid from mediadb
    # // 2. In one session, if app/sRC/bRC reconnect, you should set input sessionid got from 1st step
    # // camera请求新session id, 用于媒体文件分组, 暂不实现
    def camera_start_session_request(self, session_id=0):
        '''
        // StartSession:(should be called before other camera cmds)
        // 1. fist time must set input sessionid = 0 to get an output sessionid from mediadb
        // 2. In one session, if app/sRC/bRC reconnect, you should set input sessionid got from 1st step
        '''
        try:
            self.cmd.camera_start_session_request.session_id = session_id
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Called after stopping the preview
    # // 关闭预览流时调用, 暂不实现
    def camera_stop_session_request(self):
        try:
            self.cmd.camera_stop_session_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    def camera_set_param_request(self, id=2):
        '''
        enum ID {
            FRONT   = 0;
            OPTIC   = 1;
            STEREO  = 2;
                }
        '''
        try:
            self.cmd.camera_set_param_request.id = id
            # self.cmd.camera_set_param_request.metadata.preview_resolution.width = 1
            # self.cmd.camera_set_param_request.metadata.preview_resolution.height = 1
            self.cmd.camera_set_param_request.metadata.preview_fps.fps = 1  # 预览流帧率

            # self.cmd.camera_set_param_request.metadata.preview_bitrate.bitrate = 1  # 预览流比特率

            self.cmd.camera_set_param_request.metadata.video_resolution.width = 1920  # 视频分辨率
            self.cmd.camera_set_param_request.metadata.video_resolution.height = 1080

            self.cmd.camera_set_param_request.metadata.video_fps.fps = 30  # 视频帧率

            # self.cmd.camera_set_param_request.metadata.video_bitrate.bitrate = 1  # 视频比特率

            # self.cmd.camera_set_param_request.metadata.video_file_format.AVC     = 0     #视频格式
            # self.cmd.camera_set_param_request.metadata.video_file_format.HEVC = 1

            self.cmd.camera_set_param_request.metadata.snapshot_resolution.width = 4000  # 照片分辨率
            self.cmd.camera_set_param_request.metadata.snapshot_resolution.height = 3000

            # self.cmd.camera_set_param_request.metadata.thumbnail_resolution.width = 1  # 照片缩略图分辨率
            # self.cmd.camera_set_param_request.metadata.thumbnail_resolution.height = 2

            # self.cmd.camera_set_param_request.metadata.snapshot_file_format.SnapshotFileFormatEnum fmt = 1
            # 照片格式

            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    def camera_get_param_request(self):
        try:
            self.cmd.camera_get_param_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Start/Stop the camera preview
    # // 开启或关闭预览流
    def camera_start_preview_request(self, preview_request='True'):
        try:
            if preview_request == 'True':
                get_preview_request = True
            elif preview_request == 'False':
                get_preview_request = False
            self.cmd.camera_start_preview_request = get_preview_request
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # camera_start_video_request
    # // 开启/关闭录像
    def camera_start_video_request(self, video_request='True'):
        try:
            if video_request == 'True':
                get_video_request = True
            elif video_request == 'False':
                get_video_request = False
            self.cmd.camera_start_video_request = get_video_request
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Start take a photo
    # // 开始拍照或连拍. 当手动模式下CaptureType为连拍模式，则此命令表示开始一组连拍
    # Empty camera_take_photo_request = 244;
    def camera_take_photo_request(self):
        try:
            self.cmd.camera_take_photo_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # // Stop take photo
    # // 停止连拍，暂未实现
    # Empty camera_stop_photo_request = 245;
    def camera_stop_photo_request(self):
        try:
            self.cmd.camera_stop_photo_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # heartbeat_info_request
    # // 心跳信息请求. App周期主动请求飞机心跳信息，用于判断飞机与App连接状态
    def heartbeat_info_request(self):
        try:
            self.cmd.heartbeat_info_request.SetInParent()
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    # set_udp_server_ipaddress_request
    # // 设置UDP服务端IP, 用于预览流和event主动上报App
    def set_udp_server_ipaddress_request(self, ipaddress_request='111'):
        try:
            self.cmd.set_udp_server_ipaddress_request = ipaddress_request
            return 1
        except Exception as e:
            print('traceback.format_exc():\n%s' % traceback.format_exc())
            return 0

    @classmethod
    def get_dict(cls, def_name):
        data_dict = {}
        parameter_data = inspect.signature(def_name)
        for i, item in enumerate(parameter_data.parameters.items()):
            name, param = item
            data_dict[name] = param.default
        data_dict.pop('self', None)
        return data_dict

class Get_Parse(object):
    def get_parse(parse_dp, Class_Test):
        parse = argparse.ArgumentParser(description=parse_dp)

        parse.add_argument('--echo_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.echo_request)))
        parse.add_argument('--test_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.test_request)))
        parse.add_argument('--set_serial_number_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_serial_number_request)))
        parse.add_argument('--get_serial_number_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_serial_number_request)))
        parse.add_argument('--git_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.git_request)))
        parse.add_argument('--set_name_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_name_request)))
        parse.add_argument('--get_name_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_name_request)))
        parse.add_argument('--media_counts_get_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.media_counts_get_request)))
        parse.add_argument('--media_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.media_request)))
        parse.add_argument('--wifi_start_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.wifi_start_request)))
        parse.add_argument('--wifi_stop_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.wifi_stop_request)))
        parse.add_argument('--battery_status_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.battery_status_request)))
        parse.add_argument('--charger_state_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.charger_state_request)))
        parse.add_argument('--logs_zip_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.logs_zip_request)))
        parse.add_argument('--board_id_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.board_id_request)))
        parse.add_argument('--location_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.location_request)))
        parse.add_argument('--get_temperature_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_temperature_request)))
        parse.add_argument('--set_pairing_public_key_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_pairing_public_key_request)))
        parse.add_argument('--set_peer_verification_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_peer_verification_request)))
        parse.add_argument('--set_channel_encryption_nonce_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_channel_encryption_nonce_request)))
        parse.add_argument('--get_enable_usb_import_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_enable_usb_import_request)))
        parse.add_argument('--set_enable_usb_import_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_enable_usb_import_request)))
        parse.add_argument('--clear_content_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.clear_content_request)))
        parse.add_argument('--halt_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.halt_request)))
        parse.add_argument('--unpair_device_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.unpair_device_request)))
        parse.add_argument('--set_time_utc_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_time_utc_request)))
        parse.add_argument('--pairing_wait_for_user_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.pairing_wait_for_user_request)))
        parse.add_argument('--ota_update_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.ota_update_request)))
        parse.add_argument('--firmware_update_upload_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.firmware_update_upload_request)))
        parse.add_argument('--get_flight_mode_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_flight_mode_request)))
        parse.add_argument('--get_flight_status_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_flight_status_request)))
        parse.add_argument('--abort_flight_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.abort_flight_request)))
        parse.add_argument('--get_storage_capacity_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_storage_capacity_request)))
        parse.add_argument('--set_scheduled_update_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_scheduled_update_request)))
        parse.add_argument('--get_scheduled_update_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_scheduled_update_request)))
        parse.add_argument('--disable_flight_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.disable_flight_request)))
        parse.add_argument('--validate_pairing_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.validate_pairing_request)))
        parse.add_argument('--set_capture_duration_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_capture_duration_request)))
        parse.add_argument('--get_capture_duration_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_capture_duration_request)))
        parse.add_argument('--set_video_resolution_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_video_resolution_request)))
        parse.add_argument('--get_video_resolution_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_video_resolution_request)))
        parse.add_argument('--set_flight_distance_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_flight_distance_request)))
        parse.add_argument('--get_flight_distance_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_flight_distance_request)))
        parse.add_argument('--set_capture_type_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_capture_type_request)))
        parse.add_argument('--get_capture_type_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_capture_type_request)))
        parse.add_argument('--set_tracking_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_tracking_request)))
        parse.add_argument('--get_tracking_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_tracking_request)))
        parse.add_argument('--get_remaining_flights_info_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_remaining_flights_info_request)))
        parse.add_argument('--set_video_format_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_video_format_request)))
        parse.add_argument('--get_video_format_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_video_format_request)))
        parse.add_argument('--get_flight_status_error_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_flight_status_error_request)))
        parse.add_argument('--set_custom_flight_mode_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_custom_flight_mode_request)))
        parse.add_argument('--get_custom_flight_mode_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_custom_flight_mode_request)))
        parse.add_argument('--get_usb_connection_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_usb_connection_request)))
        parse.add_argument('--get_enable_adb_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_enable_adb_request)))
        parse.add_argument('--set_enable_adb_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_enable_adb_request)))
        parse.add_argument('--set_flight_mode_to_manual_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_flight_mode_to_manual_request)))
        parse.add_argument('--set_enable_system_sound_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_enable_system_sound_request)))
        parse.add_argument('--get_enable_system_sound_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_enable_system_sound_request)))
        parse.add_argument('--restore_factory_settings_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.restore_factory_settings_request)))
        parse.add_argument('--set_photo_resolution_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_photo_resolution_request)))
        parse.add_argument('--get_photo_resolution_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_photo_resolution_request)))
        parse.add_argument('--cancel_scheduled_update_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.cancel_scheduled_update_request)))
        parse.add_argument('--log_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.log_request)))
        parse.add_argument('--keep_device_active_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.keep_device_active_request)))
        parse.add_argument('--start_imu_calibration_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.start_imu_calibration_request)))
        parse.add_argument('--stop_imu_calibration_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.stop_imu_calibration_request)))
        parse.add_argument('--activate_lost_mode_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.activate_lost_mode_request)))
        parse.add_argument('--deactivate_lost_mode_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.deactivate_lost_mode_request)))
        parse.add_argument('--get_lost_mode_state_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_lost_mode_state_request)))
        parse.add_argument('--get_all_flight_modes_settings_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_all_flight_modes_settings_request)))
        parse.add_argument('--set_preview_resolution_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_preview_resolution_request)))
        parse.add_argument('--get_preview_resolution_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_preview_resolution_request)))
        parse.add_argument('--set_video_hdr_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_video_hdr_request)))
        parse.add_argument('--get_video_hdr_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_video_hdr_request)))
        parse.add_argument('--set_photo_hdr_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_photo_hdr_request)))
        parse.add_argument('--get_photo_hdr_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_photo_hdr_request)))
        parse.add_argument('--set_photo_raw_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_photo_raw_request)))
        parse.add_argument('--get_photo_raw_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_photo_raw_request)))
        parse.add_argument('--set_photo_mfnr_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_photo_mfnr_request)))
        parse.add_argument('--get_photo_mfnr_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_photo_mfnr_request)))
        parse.add_argument('--set_trajectory_type_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_trajectory_type_request)))
        parse.add_argument('--get_trajectory_type_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_trajectory_type_request)))
        parse.add_argument('--set_main_camera_framerate_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_main_camera_framerate_request)))
        parse.add_argument('--get_main_camera_framerate_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_main_camera_framerate_request)))
        parse.add_argument('--set_flight_height_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_flight_height_request)))
        parse.add_argument('--get_flight_height_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_flight_height_request)))
        parse.add_argument('--set_flight_angle_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_flight_angle_request)))
        parse.add_argument('--get_flight_angle_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_flight_angle_request)))
        parse.add_argument('--get_all_camera_settings_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_all_camera_settings_request)))
        parse.add_argument('--get_generic_asset_file_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.get_generic_asset_file_request)))
        parse.add_argument('--camera_start_session_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.camera_start_session_request)))
        parse.add_argument('--camera_stop_session_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.camera_stop_session_request)))
        parse.add_argument('--camera_set_param_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.camera_set_param_request)))
        parse.add_argument('--camera_get_param_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.camera_get_param_request)))
        parse.add_argument('--camera_start_preview_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.camera_start_preview_request)))
        parse.add_argument('--camera_start_video_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.camera_start_video_request)))
        parse.add_argument('--camera_take_photo_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.camera_take_photo_request)))
        parse.add_argument('--camera_stop_photo_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.camera_stop_photo_request)))
        parse.add_argument('--heartbeat_info_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.heartbeat_info_request)))
        parse.add_argument('--set_udp_server_ipaddress_request', nargs="*", help=str(Class_Test.get_dict(Class_Test.set_udp_server_ipaddress_request)))

        args = parse.parse_args()

        def get_dict_data(list_data):
            if len(list_data) % 2 == 0:
                params_list_data01 = list_data[::2]
                params_list_data02 = list_data[1::2]
                params_dict_data = dict(zip(params_list_data01, params_list_data02))
                return params_dict_data
            else:
                mmyc = Exception("请输入正确的参数个数")
                raise mmyc
        
        def get_list_data(list_data):
            pass

        if args.echo_request != None:
            Class_Test.echo_request(**get_dict_data(args.echo_request))

        if args.test_request != None:
            Class_Test.test_request(**get_dict_data(args.test_request))

        if args.set_serial_number_request != None:
            Class_Test.set_serial_number_request(**get_dict_data(args.set_serial_number_request))

        if args.get_serial_number_request != None:
            Class_Test.get_serial_number_request(**get_dict_data(args.get_serial_number_request))

        if args.git_request != None:
            Class_Test.git_request(**get_dict_data(args.git_request))

        if args.set_name_request != None:
            Class_Test.set_name_request(**get_dict_data(args.set_name_request))

        if args.get_name_request != None:
            Class_Test.get_name_request(**get_dict_data(args.get_name_request))

        if args.media_counts_get_request != None:
            Class_Test.media_counts_get_request(**get_dict_data(args.media_counts_get_request))

        if args.media_request != None:
            Class_Test.media_request(**get_dict_data(args.media_request))

        if args.wifi_start_request != None:
            Class_Test.wifi_start_request(**get_dict_data(args.wifi_start_request))

        if args.wifi_stop_request != None:
            Class_Test.wifi_stop_request(**get_dict_data(args.wifi_stop_request))

        if args.battery_status_request != None:
            Class_Test.battery_status_request(**get_dict_data(args.battery_status_request))

        if args.charger_state_request != None:
            Class_Test.charger_state_request(**get_dict_data(args.charger_state_request))

        if args.logs_zip_request != None:
            Class_Test.logs_zip_request(**get_dict_data(args.logs_zip_request))

        if args.board_id_request != None:
            Class_Test.board_id_request(**get_dict_data(args.board_id_request))

        if args.location_request != None:
            Class_Test.location_request(**get_dict_data(args.location_request))

        if args.get_temperature_request != None:
            Class_Test.get_temperature_request(**get_dict_data(args.get_temperature_request))

        if args.set_pairing_public_key_request != None:
            Class_Test.set_pairing_public_key_request(**get_dict_data(args.set_pairing_public_key_request))

        if args.set_peer_verification_request != None:
            Class_Test.set_peer_verification_request(**get_dict_data(args.set_peer_verification_request))

        if args.set_channel_encryption_nonce_request != None:
            Class_Test.set_channel_encryption_nonce_request(**get_dict_data(args.set_channel_encryption_nonce_request))

        if args.get_enable_usb_import_request != None:
            Class_Test.get_enable_usb_import_request(**get_dict_data(args.get_enable_usb_import_request))

        if args.set_enable_usb_import_request != None:
            Class_Test.set_enable_usb_import_request(**get_dict_data(args.set_enable_usb_import_request))

        if args.clear_content_request != None:
            Class_Test.clear_content_request(**get_dict_data(args.clear_content_request))

        if args.halt_request != None:
            Class_Test.halt_request(**get_dict_data(args.halt_request))

        if args.unpair_device_request != None:
            Class_Test.unpair_device_request(**get_dict_data(args.unpair_device_request))

        if args.set_time_utc_request != None:
            Class_Test.set_time_utc_request(**get_dict_data(args.set_time_utc_request))

        if args.pairing_wait_for_user_request != None:
            Class_Test.pairing_wait_for_user_request(**get_dict_data(args.pairing_wait_for_user_request))

        if args.ota_update_request != None:
            Class_Test.ota_update_request(**get_dict_data(args.ota_update_request))

        if args.firmware_update_upload_request != None:
            Class_Test.firmware_update_upload_request(**get_dict_data(args.firmware_update_upload_request))

        if args.get_flight_mode_request != None:
            Class_Test.get_flight_mode_request(**get_dict_data(args.get_flight_mode_request))

        if args.get_flight_status_request != None:
            Class_Test.get_flight_status_request(**get_dict_data(args.get_flight_status_request))

        if args.abort_flight_request != None:
            Class_Test.abort_flight_request(**get_dict_data(args.abort_flight_request))

        if args.get_storage_capacity_request != None:
            Class_Test.get_storage_capacity_request(**get_dict_data(args.get_storage_capacity_request))

        if args.set_scheduled_update_request != None:
            Class_Test.set_scheduled_update_request(**get_dict_data(args.set_scheduled_update_request))

        if args.get_scheduled_update_request != None:
            Class_Test.get_scheduled_update_request(**get_dict_data(args.get_scheduled_update_request))

        if args.disable_flight_request != None:
            Class_Test.disable_flight_request(**get_dict_data(args.disable_flight_request))

        if args.validate_pairing_request != None:
            Class_Test.validate_pairing_request(**get_dict_data(args.validate_pairing_request))

        if args.set_capture_duration_request != None:
            Class_Test.set_capture_duration_request(**get_dict_data(args.set_capture_duration_request))

        if args.get_capture_duration_request != None:
            Class_Test.get_capture_duration_request(**get_dict_data(args.get_capture_duration_request))

        if args.set_video_resolution_request != None:
            Class_Test.set_video_resolution_request(**get_dict_data(args.set_video_resolution_request))

        if args.get_video_resolution_request != None:
            Class_Test.get_video_resolution_request(**get_dict_data(args.get_video_resolution_request))

        if args.set_flight_distance_request != None:
            Class_Test.set_flight_distance_request(**get_dict_data(args.set_flight_distance_request))

        if args.get_flight_distance_request != None:
            Class_Test.get_flight_distance_request(**get_dict_data(args.get_flight_distance_request))

        if args.set_capture_type_request != None:
            Class_Test.set_capture_type_request(**get_dict_data(args.set_capture_type_request))

        if args.get_capture_type_request != None:
            Class_Test.get_capture_type_request(**get_dict_data(args.get_capture_type_request))

        if args.set_tracking_request != None:
            Class_Test.set_tracking_request(**get_dict_data(args.set_tracking_request))

        if args.get_tracking_request != None:
            Class_Test.get_tracking_request(**get_dict_data(args.get_tracking_request))

        if args.get_remaining_flights_info_request != None:
            Class_Test.get_remaining_flights_info_request(**get_dict_data(args.get_remaining_flights_info_request))

        if args.set_video_format_request != None:
            Class_Test.set_video_format_request(**get_dict_data(args.set_video_format_request))

        if args.get_video_format_request != None:
            Class_Test.get_video_format_request(**get_dict_data(args.get_video_format_request))

        if args.get_flight_status_error_request != None:
            Class_Test.get_flight_status_error_request(**get_dict_data(args.get_flight_status_error_request))

        if args.set_custom_flight_mode_request != None:
            Class_Test.set_custom_flight_mode_request(**get_dict_data(args.set_custom_flight_mode_request))

        if args.get_custom_flight_mode_request != None:
            Class_Test.get_custom_flight_mode_request(**get_dict_data(args.get_custom_flight_mode_request))

        if args.get_usb_connection_request != None:
            Class_Test.get_usb_connection_request(**get_dict_data(args.get_usb_connection_request))

        if args.get_enable_adb_request != None:
            Class_Test.get_enable_adb_request(**get_dict_data(args.get_enable_adb_request))

        if args.set_enable_adb_request != None:
            Class_Test.set_enable_adb_request(**get_dict_data(args.set_enable_adb_request))

        if args.set_flight_mode_to_manual_request != None:
            Class_Test.set_flight_mode_to_manual_request(**get_dict_data(args.set_flight_mode_to_manual_request))

        if args.set_enable_system_sound_request != None:
            Class_Test.set_enable_system_sound_request(**get_dict_data(args.set_enable_system_sound_request))

        if args.get_enable_system_sound_request != None:
            Class_Test.get_enable_system_sound_request(**get_dict_data(args.get_enable_system_sound_request))

        if args.restore_factory_settings_request != None:
            Class_Test.restore_factory_settings_request(**get_dict_data(args.restore_factory_settings_request))
            
        if args.set_photo_resolution_request != None:
            Class_Test.set_photo_resolution_request(**get_dict_data(args.set_photo_resolution_request))

        if args.get_photo_resolution_request != None:
            Class_Test.get_photo_resolution_request(**get_dict_data(args.get_photo_resolution_request))

        if args.cancel_scheduled_update_request != None:
            Class_Test.cancel_scheduled_update_request(**get_dict_data(args.cancel_scheduled_update_request))

        if args.log_request != None:
            Class_Test.log_request(**get_dict_data(args.log_request))

        if args.keep_device_active_request != None:
            Class_Test.keep_device_active_request(**get_dict_data(args.keep_device_active_request))

        if args.start_imu_calibration_request != None:
            Class_Test.start_imu_calibration_request(**get_dict_data(args.start_imu_calibration_request))

        if args.stop_imu_calibration_request != None:
            Class_Test.stop_imu_calibration_request(**get_dict_data(args.stop_imu_calibration_request))

        if args.activate_lost_mode_request != None:
            Class_Test.activate_lost_mode_request(**get_dict_data(args.activate_lost_mode_request))

        if args.deactivate_lost_mode_request != None:
            Class_Test.deactivate_lost_mode_request(**get_dict_data(args.deactivate_lost_mode_request))

        if args.get_lost_mode_state_request != None:
            Class_Test.get_lost_mode_state_request(**get_dict_data(args.get_lost_mode_state_request))

        if args.get_all_flight_modes_settings_request != None:
            Class_Test.get_all_flight_modes_settings_request(**get_dict_data(args.get_all_flight_modes_settings_request))

        if args.set_preview_resolution_request != None:
            Class_Test.set_preview_resolution_request(**get_dict_data(args.set_preview_resolution_request))

        if args.get_preview_resolution_request != None:
            Class_Test.get_preview_resolution_request(**get_dict_data(args.get_preview_resolution_request))

        if args.set_video_hdr_request != None:
            Class_Test.set_video_hdr_request(**get_dict_data(args.set_video_hdr_request))

        if args.get_video_hdr_request != None:
            Class_Test.get_video_hdr_request(**get_dict_data(args.get_video_hdr_request))

        if args.set_photo_hdr_request != None:
            Class_Test.set_photo_hdr_request(**get_dict_data(args.set_photo_hdr_request))

        if args.get_photo_hdr_request != None:
            Class_Test.get_photo_hdr_request(**get_dict_data(args.get_photo_hdr_request))

        if args.set_photo_raw_request != None:
            Class_Test.set_photo_raw_request(**get_dict_data(args.set_photo_raw_request))

        if args.get_photo_raw_request != None:
            Class_Test.get_photo_raw_request(**get_dict_data(args.get_photo_raw_request))

        if args.set_photo_mfnr_request != None:
            Class_Test.set_photo_mfnr_request(**get_dict_data(args.set_photo_mfnr_request))

        if args.get_photo_mfnr_request != None:
            Class_Test.get_photo_mfnr_request(**get_dict_data(args.get_photo_mfnr_request))

        if args.set_trajectory_type_request != None:
            Class_Test.set_trajectory_type_request(**get_dict_data(args.set_trajectory_type_request))

        if args.get_trajectory_type_request != None:
            Class_Test.get_trajectory_type_request(**get_dict_data(args.get_trajectory_type_request))

        if args.set_main_camera_framerate_request != None:
            Class_Test.set_main_camera_framerate_request(**get_dict_data(args.set_main_camera_framerate_request))

        if args.get_main_camera_framerate_request != None:
            Class_Test.get_main_camera_framerate_request(**get_dict_data(args.get_main_camera_framerate_request))

        if args.set_flight_height_request != None:
            Class_Test.set_flight_height_request(**get_dict_data(args.set_flight_height_request))

        if args.get_flight_height_request != None:
            Class_Test.get_flight_height_request(**get_dict_data(args.get_flight_height_request))

        if args.set_flight_angle_request != None:
            Class_Test.set_flight_angle_request(**get_dict_data(args.set_flight_angle_request))

        if args.get_flight_angle_request != None:
            Class_Test.get_flight_angle_request(**get_dict_data(args.get_flight_angle_request))

        if args.get_all_camera_settings_request != None:
            Class_Test.get_all_camera_settings_request(**get_dict_data(args.get_all_camera_settings_request))

        if args.get_generic_asset_file_request != None:
            Class_Test.get_generic_asset_file_request(**get_dict_data(args.get_generic_asset_file_request))

        if args.camera_start_session_request != None:
            Class_Test.camera_start_session_request(**get_dict_data(args.camera_start_session_request))

        if args.camera_stop_session_request != None:
            Class_Test.camera_stop_session_request(**get_dict_data(args.camera_stop_session_request))

        if args.camera_set_param_request != None:
            Class_Test.camera_set_param_request(**get_dict_data(args.camera_set_param_request))

        if args.camera_get_param_request != None:
            Class_Test.camera_get_param_request(**get_dict_data(args.camera_get_param_request))

        if args.camera_start_preview_request != None:
            Class_Test.camera_start_preview_request(**get_dict_data(args.camera_start_preview_request))

        if args.camera_start_video_request != None:
            Class_Test.camera_start_video_request(**get_dict_data(args.camera_start_video_request))

        if args.camera_take_photo_request != None:
            Class_Test.camera_take_photo_request(**get_dict_data(args.camera_take_photo_request))

        if args.camera_stop_photo_request != None:
            Class_Test.camera_stop_photo_request(**get_dict_data(args.camera_stop_photo_request))

        if args.heartbeat_info_request != None:
            Class_Test.heartbeat_info_request(**get_dict_data(args.heartbeat_info_request))

        if args.set_udp_server_ipaddress_request != None:
            Class_Test.set_udp_server_ipaddress_request(**get_dict_data(args.set_udp_server_ipaddress_request))
