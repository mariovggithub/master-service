from nameko.rpc import rpc

class MasterService:
    name = "master-service"

    @rpc
    def hello(self, name):
        return f"Hello {name}"