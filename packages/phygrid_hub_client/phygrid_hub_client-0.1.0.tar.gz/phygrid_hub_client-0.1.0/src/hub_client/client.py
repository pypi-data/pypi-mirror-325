import asyncio
import os
from typing import Any, Callable, Dict, List, Optional
import socketio
from .connection import PhyHubConnection
from .types import EventPayload, ScreenTwinReportedProperties, TwinStatusEnum

class PhyHubClient:
    _instance = None

    def __init__(self, module_name: str):
        self.module_name = module_name
        self.socket: Optional[socketio.Client] = None
        self.socket_connected = False
        self.emit_queue: List[tuple] = []
        self.last_device_status_check = 0
        self.last_device_status_response = None

    @classmethod
    async def connect(
        cls,
        module_name: Optional[str] = None,
        data_residency: Optional[str] = None
    ) -> 'PhyHubClient':
        if not cls._instance:
            instance_name = module_name or os.getenv("TWIN_ID")
            if not instance_name:
                raise ValueError("Unable to initialize PhyHub client, twinId/instance name not found")
            
            cls._instance = PhyHubClient(instance_name)
            await cls._instance.initialize_connection(data_residency)
            
        return cls._instance

    async def initialize_connection(self, data_residency: Optional[str] = None) -> 'PhyHubClient':
        if self.socket:
            return self

        try:
            connection = PhyHubConnection.get_instance(data_residency)
            self.socket = await connection.get_socket_io_instance()
            self.setup_socket_listeners()
            return self
        except Exception as e:
            raise Exception(f"Failed to initialize connection: {str(e)}")

    def setup_socket_listeners(self):
        if not self.socket:
            return

        @self.socket.on('pong')
        def on_pong(data: Dict):
            asyncio.create_task(
                self.delayed_ping(data['data']['count'] + 1)
            )

        @self.socket.on('connect')
        def on_connect():
            self.socket_connected = True
            self.emit('ping', {'count': 1})
            self.process_emit_queue()

        @self.socket.on('disconnect')
        def on_disconnect():
            self.socket_connected = False

    async def delayed_ping(self, count: int):
        await asyncio.sleep(30)
        self.emit('ping', {'count': count})

    def emit(self, method: str, *args):
        if not self.socket:
            print("Socket not created")
            return

        event = self.module_name
        callback = args[-1] if args and callable(args[-1]) else None
        payload = {"method": method, **(args[0] if args else {})}
        
        emit_args = [event, payload]
        if callback:
            emit_args.append(callback)

        if not self.socket_connected:
            self.emit_queue.append(emit_args)
            return

        self.socket.emit(*emit_args)

    def process_emit_queue(self):
        if not self.socket or not self.socket_connected:
            return

        while self.emit_queue:
            args = self.emit_queue.pop(0)
            self.socket.emit(*args)

    # Add other methods (getDeviceStatus, getScreenInstance, etc.) as needed...