from evalsync.proto.sync_pb2 import StateSync, ServiceState, ManagerMessage, ExperimentCommand
from loguru import logger
import zmq
from zmq.utils.monitor import recv_monitor_message

class ExperimentWorker:
    def __init__(self, experiment_id: str, client_id: str):
        self.context = zmq.Context()
        self.experiment_id = experiment_id
        self.client_id = client_id
        self.state = ServiceState.INIT

        # we pub on the worker channel and sub on the manager channel
        self.socket = self.context.socket(zmq.DEALER)
        self.socket.setsockopt(zmq.LINGER, 1000)
        self.socket.setsockopt(zmq.IDENTITY, f"Client-{client_id}".encode())
        self.socket.connect(f"ipc://{experiment_id}-sock")

        self.metadata = {}

    def cleanup(self):
        self.socket.close()
        self.context.term()

    def notify_manager(self, msg: str) -> bool:
        message = StateSync(state=self.state, error_message=msg, metadata=self.metadata).SerializeToString()
        self.socket.send_multipart([b"", message])
        return True

    def ready(self) -> bool:
        if self.state == ServiceState.INIT:
            self.state = ServiceState.READY
            self.notify_manager("ready")
            return True
        else:
            return False

    def wait_for_start(self) -> bool:
        if self.state == ServiceState.READY:
            while self.state != ServiceState.RUNNING:
                _, raw_message = self.socket.recv_multipart()
                message = ManagerMessage()

                ManagerMessage.ParseFromString(message, raw_message)
                match message.command:
                    case ExperimentCommand.BEGIN:
                        self.state = ServiceState.RUNNING
                        self.notify_manager("running")
                        return True
                    case ExperimentCommand.END | ExperimentCommand.ABORT:
                        self.state = ServiceState.ERROR
                        self.notify_manager("error")
                        return False

        return False

    def end(self):
        if self.state == ServiceState.RUNNING:
            self.state = ServiceState.DONE
            self.notify_manager("done")
            return True
        else:
            return False

    def wait_for_stop(self):
        if self.state == ServiceState.RUNNING:
            while self.state != ServiceState.DONE:
                _, raw_message = self.socket.recv_multipart()
                message = ManagerMessage()
                ManagerMessage.ParseFromString(message, raw_message)
                match message.command:
                    case ExperimentCommand.END:
                        self.state = ServiceState.DONE
                        self.notify_manager("done")
                        return True
                    case ExperimentCommand.BEGIN | ExperimentCommand.ABORT:
                        self.state = ServiceState.ERROR
                        self.notify_manager("error")
                        return True
        return False