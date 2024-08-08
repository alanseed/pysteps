"""Implementations of deterministic and ensemble nowcasting methods."""

from pysteps.nowcasts.interface import get_method

try:
    from dgmr_module_plugin import dgmr
except ImportError:
    dgmr=None
