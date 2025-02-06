from .base import SpecBase

try:
    import yaml
except ImportError:
    raise ImportError("Required yaml package. Install it with `pip install pyyaml`")


class YamlSpec(SpecBase):
    def load(self, stream):
        self._spec = yaml.safe_load(stream)
