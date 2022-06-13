import subprocess
import logging
import psutil
from .exceptions import ProxyIsAlreadyRunningError

logger = logging.getLogger(__name__)

PROCESS_NAME = "mitmweb"


class Client(object):
    """ Class responsible to interact with MitmProxy"""

    def is_installed(self):
        result = subprocess.run(["which", "mitmweb"])

        if result.returncode == 0:
            return True

        return False

    def is_running(self):
        """ Check if Mitmweb is running by looking into running processes"""
        proc = self.get_process()

        if proc is not None:
            return True

        return False

    def get_process(self):
        """ Returns the process for mitmweb"""
        for proc in psutil.process_iter():
            try:
                if PROCESS_NAME in proc.name().lower():
                    return proc
            except (psutil.NoSuchProcess, psutil.AccessDenied,
                    psutil.ZombieProcess):
                pass

        return None

    def start(self, proxy_port, web_port):
        """ Starts mitmweb with the specified ports"""

        if self.get_process() is not None:
            raise ProxyIsAlreadyRunningError()

        cmd = [
            "mitmweb", "--listen-port={}".format(proxy_port),
            "--web-port={}".format(web_port)
        ]

        try:
            p = subprocess.Popen(cmd,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 universal_newlines=True)
            output = p.stdout.readline().strip()

            if "Web server listening at" not in output:
                raise RuntimeError("Failed to start Proxy server")

        except subprocess.CalledProcessError as e:
            logger.error("Failed to start mitmweb server: %s", e)
            raise RuntimeError("Failed to start mitmweb server: %s", e)

    def stop(self):
        """ Stops the mitmweb process"""
        p = self.get_process()

        if p is None:
            return

        p.terminate()
