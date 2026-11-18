bl_info = {
    "name": 'Rigi-All-里吉-奥尔-荣枯汉化',
    "description": "Speeds up the Rigify process",
    "author": "hisanimations",
    "version": (1, 6, 0),
    "blender": (4, 1, 0),
    "location": "View3D > Rigi-All",
    "warning": "", # used for warning icon and text in addons panel
    "doc_url": "https://github.com/hisprofile/rigi-all/tree/main",
    "support": "COMMUNITY",
    "category": "Rigging",
}

from . import (
    main,
    operators,
    operators_ambidextrous,
    operators_cleanup,
    operators_miscellaneous,
    panel
)

def register():
    operators_ambidextrous.register()
    main.register()
    operators.register()
    operators_cleanup.register()
    operators_miscellaneous.register()
    panel.register()

def unregister():
    operators_ambidextrous.unregister()
    main.unregister()
    operators.unregister()
    operators_cleanup.unregister()
    operators_miscellaneous.unregister()
    panel.unregister()

if __name__ == '__main__':
    register()

# RONGCOOL_LOCALIZATION_BEGIN
from . import rongcool_i18n as _rongcool_i18n

_rongcool_original_register = globals().get("register")
_rongcool_original_unregister = globals().get("unregister")


def register():
    _rongcool_i18n.register()
    if _rongcool_original_register is not None:
        _rongcool_original_register()


def unregister():
    if _rongcool_original_unregister is not None:
        _rongcool_original_unregister()
    _rongcool_i18n.unregister()
# RONGCOOL_LOCALIZATION_END

