import os
import asyncio
import async_timeout
import binascii
import sys
sys.path.append(os.getcwd() + '/proto_py')
from proto_py import service_pb2

from bleak import discover
from bleak import BleakClient
from termcolor import colored
from rpc_request import H130_Test, Get_Parse
# os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append("/Users/zerozero/.jenkins/workspace/ota-test/ble.py")
curPath=os.path.abspath(os.path.dirname(__file__))
rootPath=os.path.split(curPath)[0]
sys.path.append(rootPath)
from bt_service import BtSevice



name_dict = {}
devices_dict = {}
devices_list = []

def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    hex_data = binascii.b2a_hex(data)
    str_data = str(hex_data).replace('\'','')[1:]
    str_data = str_data[14:-2]
    bytes_data = bytes.fromhex(str_data)
    test_proto = service_pb2.RpcResponse()
    test_proto.ParseFromString(bytes_data)
    print(colored('res_response>>>', 'yellow'))
    print(colored(test_proto,'red'))


class H130_Ble_Test(H130_Test):
    def main(self):
        data = self.cmd.SerializeToString()
        len01 = self.cmd.ByteSize()
        return data, len01

BATTERY_LEVEL_UUID = '00002902-0000-1000-8000-00805f9b34fb'
WRITE_UUID = '6e400002-b5a3-f393-e0a9-e50e24dcca9e'
GET_UUD = '6e400003-b5a3-f393-e0a9-e50e24dcca9e'

async def scan():
    dev = await discover()
    for i in range(0, len(dev)):
        print("[" + str(i) + "]" + dev[i].address, dev[i].name, dev[i].metadata["uuids"])
        name_dict[dev[i].name] = dev[i].address
        devices_dict[dev[i].address] = []
        devices_dict[dev[i].address].append(dev[i].name)
        devices_dict[dev[i].address].append(dev[i].metadata["uuids"])
        devices_list.append(dev[i].address)

async def send_data(address, hex_data=''):
    async with BleakClient(address) as client:
        print(f"BLE Connected: {client.is_connected}")
        await client.start_notify(GET_UUD, notification_handler)
        '''
        write_gatt_char
        '''
        try:
            async with async_timeout.timeout(30):
                types_data = bytes.fromhex(hex_data)
                await client.write_gatt_char(WRITE_UUID, types_data, response=True)
                # await asyncio.sleep(15.0)
                print('发送数据协程执行成功')
        except asyncio.TimeoutError as e:
            print('发送数据协程执行超时')
        await client.stop_notify(GET_UUD)

async def main(hex_data):
    await scan()
    try:
        address = name_dict[ble_name]
    except:
        print(colored('未搜索到蓝牙：{}'.format(ble_name), 'red'))
        exit()
    await send_data(address, hex_data)

if __name__ == '__main__':
    ble_name = 'liwang6'
    ble_test = H130_Ble_Test()
    Get_Parse.get_parse('H130 Ble Request POST', ble_test)

    data, len01 = ble_test.main()
    hex_data = BtSevice().BaleData(data, len01)
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(main(hex_data))