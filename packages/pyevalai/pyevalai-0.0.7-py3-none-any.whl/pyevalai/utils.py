import json
import base64
import numpy as np
import torch

# Custom Encoder to Serialize NumPy and PyTorch objects
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return {"__type__": "numpy", "data": base64.b64encode(obj.tobytes()).decode('utf-8'), "dtype": str(obj.dtype), "shape": obj.shape}
        elif isinstance(obj, torch.Tensor):
            return {"__type__": "torch", "data": base64.b64encode(obj.numpy().tobytes()).decode('utf-8'), "dtype": str(obj.numpy().dtype), "shape": obj.size()}
        return super().default(obj)

# Decoder to Reconstruct NumPy and PyTorch Objects
def custom_decoder(dct):
    if "__type__" in dct:
        if dct["__type__"] == "numpy":
            data = base64.b64decode(dct["data"])
            return np.frombuffer(data, dtype=dct["dtype"]).reshape(dct["shape"])
        elif dct["__type__"] == "torch":
            data = base64.b64decode(dct["data"])
            array = np.frombuffer(data, dtype=dct["dtype"]).reshape(dct["shape"])
            return torch.from_numpy(array)
    return dct
