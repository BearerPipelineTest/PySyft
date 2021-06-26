# third party
from syft.core.tensor.manager import TensorChainManager

from .fixed_precision_tensor import FixedPrecisionTensor


class FixedPrecisionTensorAncestor(TensorChainManager):
    def fix_precision(self, base=10, precision=3):

        self.child = FixedPrecisionTensor(
            base=base, precision=precision, value=self.child
        )
        return self

    def decode(self):
        if not isinstance(self.child, FixedPrecisionTensor):
            raise ValueError(f"self.child should be FPT but is {type(self.child)}")

        self.child = self.child.decode()
        return self
