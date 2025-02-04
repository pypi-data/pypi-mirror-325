from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


DEFAULT_STEEV_CFG = """
alert_rules:
  metrics: # Add metrics name to monitor
    - name: loss
    - name: grad_norm
  actions:
    notify_user: true
"""


def chcek_steev_cfg(steev_cfg: "Path") -> bool:
    if not steev_cfg.exists():
        return False
    return True


def make_default_steev_cfg(steev_cfg: "Path") -> None:
    if not steev_cfg.exists():
        steev_cfg.touch()
        steev_cfg.write_text(DEFAULT_STEEV_CFG)
