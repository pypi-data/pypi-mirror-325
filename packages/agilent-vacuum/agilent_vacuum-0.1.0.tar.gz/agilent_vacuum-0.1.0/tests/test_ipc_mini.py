import asyncio
import logging
import random
import time

import pytest
import agilent_vacuum.ipc_mini as ipc
import agilent_vacuum.commands as ac

logger = logging.getLogger("vacuum")

COM_PORT = '/dev/ttyUSB0'
ADDR = 2


@pytest.mark.asyncio
async def test_ipc_mini_serial():
    # test via RS232
    client = ipc.SerialClient(com_port=COM_PORT)
    ipc_mini = ipc.IpcMiniDriver(client, addr=ADDR)
    # ipc_mini.connect()
    response = await ipc_mini.send_request(ipc.STATUS_CMD, force=True)
    assert response.result_code is None
    client.close()


@pytest.mark.asyncio
async def test_ipc_mini_basic_commands():
    # test via LAN. ONLY READ COMMANDS
    client = ipc.SerialClient(com_port=COM_PORT)
    ipc_mini = ipc.IpcMiniDriver(client, addr=ADDR)
    await ipc_mini.connect(max_retries=1)
    status = await ipc_mini.get_status()
    logger.info(f"pump status: {status.name}")
    assert (status is ipc.PumpStatus.NORMAL) or (status is ipc.PumpStatus.STOP)

    error = await ipc_mini.get_error()
    logger.info(f"pump error: {error.name}")
    assert error is ipc.PumpErrorCode.NO_ERROR

    response = await ipc_mini.send_request(ipc.CONTROLLER_MODEL_CMD)
    logger.info(f"controller model {response.data}")
    assert len(response.data) > 4

    response = await ipc_mini.send_request(ipc.CONTROLLER_SERIAL_NO_CMD)
    logger.info(f"serial no {response.data}")
    assert len(response.data) > 4

    response = await ipc_mini.send_request(ac.SERIAL_ADDR_CMD)
    addr = int(response.data)
    assert addr >= 0
    assert addr <= 32

    response = await ipc_mini.send_request(ac.SERIAL_TYPE_CMD)
    logger.info(f"Serial type {int(response)}")
    response = await ipc_mini.send_request(ipc.MODE_CMD)
    logger.info(f"Control mode {int(response)}")

    response = await ipc_mini.send_request(ipc.UNIT_PRESSURE_CMD)
    logger.info(f"pressure unit {response.data}")
    unit = ipc_mini.PRESSURE_UNITS[int(response.data)]
    assert unit is not ipc.PressureUnit.unknown

    response = await ipc_mini.send_request(ipc.AUTO_START_CMD)
    logger.info(f"autostart is {bool(response)}")

    response = await ipc_mini.send_request(ipc.PROTECT_CMD)
    logger.info(f"Protect is {bool(response)}")

    response = await ipc_mini.send_request(ipc.STEP_CMD)
    logger.info(f"Step is {bool(response)}")

    response = await ipc_mini.send_request(ipc.DEVICE_NUM_CH1_CMD)
    logger.info(f"Device number is {int(response)}")
    assert int(response) < 21

    response = await ipc_mini.send_request(ipc.MAX_POWER_CMD)
    logger.info(f"Max power {float(response)}")
    assert float(response) >= 10
    assert float(response) <= 40

    response = await ipc_mini.send_request(ipc.V_TARGET_CH1_CMD)
    logger.info(f"V target CH1 {float(response)}")
    assert int(response) >= 3000
    assert int(response) <= 7000

    response = await ipc_mini.send_request(ipc.I_PROTECT_CH1_CMD)
    logger.info(f"I protect CH1 {float(response)}")
    assert int(response) >= 1
    assert int(response) <= 30000

    response = await ipc_mini.send_request(ipc.SET_POINT_CH1_CMD)
    logger.info(f"Set point CH1 {float(response)}")
    assert float(response) > 0

    response = await ipc_mini.send_request(ipc.TEMPERATURE_POWER_CMD)
    logger.info(f"Temperature power {float(response)}")
    assert float(response) > 0

    response = await ipc_mini.send_request(ipc.TEMPERATURE_CONTROLLER_CMD)
    logger.info(f"Temperature controller {float(response)}")
    assert float(response) > 0

    response = await ipc_mini.send_request(ipc.STATUS_SET_POINT)
    logger.info(f"Status set point {bool(response)}")

    response = await ipc_mini.send_request(ipc.V_MEASURED_CH1_CMD)
    logger.info(f"voltage measured {response.data} {float(response)}")
    assert float(response) > 3000.0

    response = await ipc_mini.send_request(ipc.I_MEASURED_CH1_CMD)
    logger.info(f"current measured {float(response)}")

    response = await ipc_mini.send_request(ipc.PRESSURE_CH1_CMD)
    logger.info(f"pressure {response.data} {float(response)}")


@pytest.mark.asyncio
async def test_ipc_mini_high_level():
    # test via LAN
    # Rewrite this to not switch on ion pump

    async def on_connect_cb():
        nonlocal on_connect_called
        on_connect_called = True

    on_connect_called = False
    client = ipc.SerialClient(com_port=COM_PORT)
    ipc_mini = ipc.IpcMiniDriver(client, addr=ADDR)
    ipc_mini.on_connect = on_connect_cb
    await ipc_mini.connect()
    assert on_connect_called is True
    status = await ipc_mini.get_status()
    assert status is not ipc.PumpStatus.FAIL
    await ipc_mini.stop()
    await asyncio.sleep(1.0)
    status = await ipc_mini.get_status()
    assert status is ipc.PumpStatus.STOP
    pressure = await ipc_mini.read_pressure()
    logger.info(f"STOP pressure {pressure}")

    await ipc_mini.start()
    await asyncio.sleep(1.0)
    status = await ipc_mini.get_status()
    assert status is ipc.PumpStatus.NORMAL
    unit = await ipc_mini.get_pressure_unit()
    # assert unit is PressureUnit.mBar
    pressure = await ipc_mini.read_pressure()
    logger.info(f"pressure {pressure} {unit.name}")
    assert pressure < 1e-5

    auto_start_backup = await ipc_mini.get_autostart() is False
    await ipc_mini.set_autostart(False)
    assert await ipc_mini.get_autostart() is False
    await ipc_mini.set_autostart(True)
    assert await ipc_mini.get_autostart() is True
    await ipc_mini.set_autostart(auto_start_backup)

    protect_backup = await ipc_mini.get_protect()
    await ipc_mini.set_protect(False)
    assert await ipc_mini.get_protect() is False
    await ipc_mini.set_protect(True)
    assert await ipc_mini.get_protect() is True
    await ipc_mini.set_protect(protect_backup)

    step_backup = await ipc_mini.get_step()
    await ipc_mini.set_step(False)
    assert await ipc_mini.get_step() is False
    await ipc_mini.set_step(True)
    assert await ipc_mini.get_step() is True
    await ipc_mini.set_step(step_backup)

    device_number = await ipc_mini.get_device_num()
    assert device_number > 0
    assert device_number < 25
    await ipc_mini.set_device_num(device_number)

    v_target = await ipc_mini.get_v_target()
    assert v_target >= 3000
    await ipc_mini.set_v_target(v_target)

    voltage = await ipc_mini.read_voltage()
    logger.info(f"voltage: {voltage}")
    assert voltage > 2000

    current = await ipc_mini.read_current()
    logger.info(f"current: {current}")
    assert current > 0


@pytest.mark.asyncio
async def test_ipc_mini_set_current_protect():
    client = ipc.SerialClient(com_port=COM_PORT)
    ipc_mini = ipc.IpcMiniDriver(client, addr=ADDR)
    await ipc_mini.connect()
    current_backup = await ipc_mini.get_current_protect()
    setting = random.randrange(1, 100) / 10.0
    await ipc_mini.set_current_protect(setting)
    assert await ipc_mini.get_current_protect() == pytest.approx(setting)
    # await ipc_mini.set_current_protect(current_backup)
    await ipc_mini.set_current_protect(20)
    await ipc_mini.set_protect(True)
    await ipc_mini.set_step(False)


@pytest.mark.asyncio
async def test_ipc_mini_temperatures():
    client = ipc.SerialClient(com_port=COM_PORT)
    ipc_mini = ipc.IpcMiniDriver(client, addr=ADDR)
    await ipc_mini.connect()
    assert 20 < await ipc_mini.read_power_temp() < 100
    assert 20 < await ipc_mini.read_controller_temp() < 100


@pytest.mark.asyncio
async def test_ipc_mini_protect_off():
    # Protect on/off does not work
    client = ipc.SerialClient(com_port=COM_PORT)
    ipc_mini = ipc.IpcMiniDriver(client, addr=ADDR)
    await ipc_mini.connect()
    await ipc_mini.stop()
    await ipc_mini.set_protect(False)
    assert await ipc_mini.get_protect() is False


@pytest.mark.asyncio
async def test_ipc_mini_protect_on():
    # Protect on/off does not work
    client = ipc.SerialClient(com_port=COM_PORT)
    ipc_mini = ipc.IpcMiniDriver(client, addr=ADDR)
    await ipc_mini.connect()
    await asyncio.sleep(0.5)
    await ipc_mini.set_protect(True)
    await asyncio.sleep(0.5)
    assert await ipc_mini.get_protect() is True
    logger.info(f"protect I {await ipc_mini.send_request(ipc.I_PROTECT_CH1_CMD)}")
    await ipc_mini.start()


@pytest.mark.asyncio
async def test_rate_limit():
    client = ipc.SerialClient(com_port=COM_PORT)
    ipc_mini = ipc.IpcMiniDriver(client, addr=ADDR)
    await ipc_mini.connect()
    start = time.time()
    for i in range(100):
        await ipc_mini.get_status()
    logger.info(f"Rate limit test. 100 calls in {time.time() - start}")


@pytest.mark.asyncio
async def test_rate_limit():
    client = ipc.SerialClient(com_port=COM_PORT)
    ipc_mini = ipc.IpcMiniDriver(client, addr=ADDR)
    await ipc_mini.connect(max_retries=0)


@pytest.mark.asyncio
async def test_long_run():
    client = ipc.SerialClient(com_port=COM_PORT)
    ipc_mini = ipc.IpcMiniDriver(client, addr=ADDR)
    await ipc_mini.connect()
    start = time.time()
    while ipc_mini.is_connected is True:
        pressure = await ipc_mini.read_pressure()
        voltage = await ipc_mini.read_voltage()
        logger.info(f"pressure {pressure} voltage {voltage} time {time.time()}")
        await asyncio.sleep(0.25)
