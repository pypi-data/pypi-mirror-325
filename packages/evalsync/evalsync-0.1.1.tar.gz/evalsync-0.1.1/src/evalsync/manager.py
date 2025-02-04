import os
from evalsync.proto.sync_pb2 import StateSync, ServiceState, ExperimentCommand, ManagerMessage
import zmq
from loguru import logger

class ExperimentManager:
    def __init__(self, experiment_id: str, num_workers: int):
        self.context = zmq.Context()
        self.experiment_id = experiment_id
        self.num_workers = num_workers
        self.connected_workers = []
        
        self.socket = self.context.socket(zmq.ROUTER)
        self.socket.setsockopt(zmq.LINGER, 1000)
        self.socket.bind(f"ipc://{experiment_id}-sock")

    def cleanup(self):
        self.socket.close()
        self.context.term()
        if os.path.exists(f"{self.experiment_id}-sock"):
            os.remove(f"{self.experiment_id}-sock")

    def wait_all_workers(self):
        while len(self.connected_workers) < self.num_workers:
            message = StateSync()
            client_id, _, raw_content = self.socket.recv_multipart()
            StateSync.ParseFromString(message, raw_content)

            if client_id not in self.connected_workers and message.state == ServiceState.READY:
                self.connected_workers.append(client_id)

    def broadcast(self, message: bytes):
        for client_id in self.connected_workers:
            self.socket.send_multipart([client_id, b"", message])

    def start(self):
        self.broadcast(ManagerMessage(command=ExperimentCommand.BEGIN).SerializeToString())

    def stop(self):
        self.broadcast(ManagerMessage(command=ExperimentCommand.END).SerializeToString())

