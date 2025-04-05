from datetime import datetime
import logging
from typing import Any
import asyncio

from pygryfsmart.api import GryfApi
from pygryfsmart.gryfexpert import GryfExpert
from pygryfsmart.const import (
    COMMAND_FUNCTION_COVER,
    COMMAND_FUNCTION_PONG,
    COMMAND_FUNCTION_PWM,
    COMMAND_FUNCTION_TEMP,
    CONF_OUT,
    CONF_TEMPERATURE,
    OUTPUT_STATES,
    COMMAND_FUNCTION_IN,
    COMMAND_FUNCTION_OUT,
    SCHUTTER_STATES,
)

_LOGGER = logging.getLogger(__name__)

class _GryfDevice:
    _name: str
    _id: int
    _pin: int
    _api: GryfApi

    def __init__(self,
                 name: str,
                 id: int,
                 pin: int,
                 api: GryfApi
                 ) -> None:
        self._name = name
        self._id = id
        self._pin = pin
        self._api = api

        now = datetime.now()
        self._api.feedback.data[COMMAND_FUNCTION_PONG][self._id] = now.strftime("%H:%M") 

    @property
    def available(self):
        return self._api.avaiable_module(self._id)

class _GryfOutput(_GryfDevice):
    def __init__(
        self,
        name: str,
        id: int,
        pin: int,
        api: GryfApi,
    ):
        super().__init__(name,
                         id,
                         pin,
                         api)

    def subscribe(self , update_fun_ptr):
        self._api.subscribe(self._id , self._pin, COMMAND_FUNCTION_OUT , update_fun_ptr)

    @property
    def name(self):
        return f"{self._name}"

    async def turn_on(self):
        await self._api.set_out(self._id, self._pin, OUTPUT_STATES.ON)

    async def turn_off(self):
        await self._api.set_out(self._id, self._pin, OUTPUT_STATES.OFF)

    async def toggle(self):
        await self._api.set_out(self._id, self._pin, OUTPUT_STATES.TOGGLE)

class _GryfInput(_GryfDevice):

    def __init__(self,
                 name: str,
                 id: int,
                 pin: int,
                 api: GryfApi,
                 ) -> None:
        super().__init__(name,
                         id,
                         pin,
                         api)

    def subscribe(self , update_fun_ptr):
        self._api.subscribe(self._id , self._pin, COMMAND_FUNCTION_IN , update_fun_ptr)

    @property
    def name(self):
        return f"{self._name}"

class _GryfTemperature(_GryfDevice):
    
    def __init__(self,
                 name: str,
                 id: int,
                 pin: int,
                 api: GryfApi,
                 ) -> None:
        super().__init__(name, 
                         id, 
                         pin, 
                         api)

    def subscribe(self , update_fun_ptr):
        self._api.subscribe(self._id , self._pin, COMMAND_FUNCTION_TEMP , update_fun_ptr)

    @property
    def name(self):
        return f"{self._name}"

class _GryfPwm(_GryfDevice):
    
    _last_level = 70
    _is_on: bool

    def __init__(self,
                 name: str,
                 id: int,
                 pin: int,
                 api: GryfApi,
                 ) -> None:
        super().__init__(name, 
                         id, 
                         pin, 
                         api)
        self._last_level = 0
        self._is_on = False

    def subscribe(self , update_fun_ptr):
        self._api.subscribe(self._id , self._pin, COMMAND_FUNCTION_PWM , update_fun_ptr)

    async def set_level(self , level: int):
        if level > 0:
            self._last_level = level
        await self._api.set_pwm(self._id , self._pin , level)
        await asyncio.sleep(1)
        await self._api.send_data(f"stateLED={self._id}\n\r")

    async def turn_on(self):
        await self._api.set_pwm(self._id , self._pin , self._last_level)
        self._is_on = True

    async def turn_off(self):
        await self._api.set_pwm(self._id , self._pin , 0)
        self._is_on = False

    async def toggle(self):
        if self._is_on:
            await self.turn_off()
        else:
            await self.turn_on()

    @property
    def name(self):
        return f"{self._name}"

class _GryfInputLine(_GryfDevice):
    
    def __init__(self,
                 name: str,
                 api: GryfApi,
                 ) -> None:
        super().__init__(name, 
                         0, 
                         0, 
                         api)

    def subscribe(self , update_fun_ptr):
        self._api.subscribe_input_message(update_fun_ptr)

    @property
    def name(self):
        return f"{self._name}"

class _GryfOutputLine(_GryfDevice):
    
    def __init__(self,
                 name: str,
                 api: GryfApi,
                 ) -> None:
        super().__init__(name, 
                         0, 
                         0, 
                         api)

    def subscribe(self , update_fun_ptr):
        self._api.subscribe_output_message(update_fun_ptr)

    @property
    def name(self):
        return f"{self._name}"

class _GryfThermostat(_GryfDevice):

    _t_state: float
    _o_state = False

    def __init__(
        self,
        name: str,
        id: int,
        pin: int,
        temperature_id: int,
        temperature_pin: int,
        differential: int,
        api: GryfApi,
    ):
        super().__init__(name,
                         id,
                         pin,
                         api)
        self._t_id = temperature_id
        self._t_pin = temperature_pin
        self._update_fun_ptr = None | Any
        self._target_temperature = 0
        self._enable = False
        self._differential = differential

    def subscribe(self , update_fun_ptr):
        self._api.subscribe(self._id , self._pin, COMMAND_FUNCTION_OUT , self.update_out)
        self._api.subscribe(self._t_id , self._t_pin, COMMAND_FUNCTION_TEMP , self.update_temperature)
        self._update_fun_ptr = update_fun_ptr

    async def update_temperature(self , state):
        self._t_state = state

        data = {
            CONF_TEMPERATURE: self._t_state,
            CONF_OUT: self._o_state
        }
        
        if self._enable:
            if self._t_state > self._target_temperature + self._differential:
                await self._api.set_out(self._id , self._pin , OUTPUT_STATES.OFF)
            elif self._t_state < self._target_temperature - self._differential: 
                await self._api.set_out(self._id , self._pin , OUTPUT_STATES.ON)

        await self._update_fun_ptr(data)

    def enable(self , enable):
        self._enable = enable
        
    def set_target_temperature(self , temperature):
        self._target_temperature = temperature

    async def update_out(self , state):
        self._o_state = state

        data = {
            CONF_TEMPERATURE: self._t_state,
            CONF_OUT: self._o_state
        }

        await self._update_fun_ptr(data)

    @property
    def name(self):
        return f"{self._name}"

class _GryfCover(_GryfDevice):

    def __init__(
        self,
        name: str,
        id: int,
        pin: int,
        time: int,
        api: GryfApi,
    ):
        super().__init__(name,
                         id,
                         pin,
                         api)

        self._time = time

    def subscribe(self , update_fun_ptr):
        self._api.subscribe(self._id , self._pin, COMMAND_FUNCTION_COVER , update_fun_ptr)

    @property
    def name(self):
        return f"{self._name}"

    async def turn_on(self):
        await self._api.set_cover(self._id , self._pin , self._time , SCHUTTER_STATES.OPEN)

    async def turn_off(self):
        await self._api.set_cover(self._id , self._pin , self._time , SCHUTTER_STATES.CLOSE)

    async def toggle(self):
        await self._api.set_cover(self._id , self._pin , self._time , SCHUTTER_STATES.STEP_MODE)

    async def stop(self):
        await self._api.set_cover(self._id , self._pin , self._time , SCHUTTER_STATES.STOP)

class _GryfPCover(_GryfDevice):

    def __init__(self,
                 name: str,
                 id: int,
                 pin: int,
                 time: int,
                 api: GryfApi
                 ) -> None:
        super().__init__(
            name,
            id,
            pin,
            api,
        )

        self._opening_time = time
        self._current_postion = 0
        self._expected_postion = 0
        self._one_interval_position_move = 500 / time
        self._timer_en = False
        self._timer_task = None
        self._opening_postion = 0
        self._opening_postion_en = False
        self._operation = SCHUTTER_STATES.STOP
        self._time_to_sleep = 0.0

    async def turn_on(self):
        await self._api.set_cover(self._id , self._pin , self._opening_time , SCHUTTER_STATES.OPEN)

    async def turn_off(self):
        await self._api.set_cover(self._id , self._pin , self._opening_time , SCHUTTER_STATES.CLOSE)

    async def toggle(self):
        await self._api.set_cover(self._id , self._pin , self._opening_time , SCHUTTER_STATES.STEP_MODE)

    async def stop(self):
        await self._api.set_cover(self._id , self._pin , 0, SCHUTTER_STATES.STOP)

    async def __timer(self):
        self._timer_en = True

        while abs(self._current_postion - self._expected_postion) > 1:

            if self._expected_postion > self._current_postion:
                self._current_postion += self._one_interval_position_move
            elif self._expected_postion < self._current_postion:
                self._current_postion -= self._one_interval_position_move
 
            _LOGGER.debug("%s" , self._current_postion)

            if not self._opening_postion_en:
                await self.__send_postion_to_move()
                self._opening_postion_en = True
                self._opening_postion = self._expected_postion

            if abs(self._expected_postion - self._opening_postion) > 2:
                if self._opening_postion > self._current_postion and self._current_postion > self._expected_postion:
                    await self.stop()
                    await self.__send_postion_to_move()
                elif self._expected_postion > self._current_postion and self._current_postion > self._opening_postion:
                    await self.stop()
                    await self.__send_postion_to_move()

            await asyncio.sleep(0.5)

        await asyncio.sleep(self._time_to_sleep)
        self._time_to_sleep = 0.0
        await self.stop()

        self._timer_en = False
        self._opening_postion_en = False

    async def __send_postion_to_move(self):
        self._operation = SCHUTTER_STATES.OPEN if self._current_postion < self._expected_postion else SCHUTTER_STATES.CLOSE
        time_to_move = int((abs(self._current_postion - self._expected_postion) * self._opening_time) / 100)

        await self._api.set_cover(self._id , self._pin , time_to_move , self._operation)

        if time_to_move > 10:
            self._time_to_sleep += 0.5

    def set_current_postion(self , current_postion: int):
        self._current_postion = current_postion

    async def set_position(self , position: int):

        self._expected_postion = position

        if not self._timer_en:
            self._opening_postion = 0
            self._opening_postion_en = False
            self._timer_task = asyncio.create_task(self.__timer())

class _GryfReset(_GryfDevice):
    
    def __init__(
        self,
        api: GryfApi,
    ) -> None:
        super().__init__("Gryf RST",
                         0,
                         0,
                         api)
    
    @property
    def name(self):
        return "Gryf RST"

    async def reset_all(self):
        await self._api.reset(0 , True)

    async def reset_single_module(self , module):
        await self._api.reset(module , True)

class _GryfExpert(_GryfDevice):
    
    _expert: GryfExpert

    def __init__(self , api: GryfApi) -> None:
        super().__init__("Gryf Expert" , 0 , 0 , api)

    async def start(self):

        self._expert = GryfExpert(self._api)
        await self._expert.start_server()

    async def stop(self):

        await self._expert.stop_server()
