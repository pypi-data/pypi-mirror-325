from siliconcompiler.tools.klayout import show as klayout_show
from siliconcompiler.tools.klayout import screenshot as klayout_screenshot
from siliconcompiler.tools.openroad import show as openroad_show
from siliconcompiler.tools.openroad import screenshot as openroad_screenshot
from siliconcompiler.tools.vpr import show as vpr_show
from siliconcompiler.tools.vpr import screenshot as vpr_screenshot
from siliconcompiler.tools.yosys import screenshot as yosys_screenshot
from siliconcompiler.tools.gtkwave import show as gtkwave_show


def setup(chip):
    chip.register_showtool('gds', klayout_show)
    chip.register_showtool('gds', klayout_screenshot)
    chip.register_showtool('oas', klayout_show)
    chip.register_showtool('oas', klayout_screenshot)
    chip.register_showtool('lef', klayout_show)
    chip.register_showtool('lef', klayout_screenshot)
    chip.register_showtool('lyrdb', klayout_show)
    chip.register_showtool('ascii', klayout_show)

    chip.register_showtool('odb', openroad_show)
    chip.register_showtool('odb', openroad_screenshot)
    chip.register_showtool('def', openroad_show)
    chip.register_showtool('def', openroad_screenshot)

    chip.register_showtool('route', vpr_show)
    chip.register_showtool('route', vpr_screenshot)
    chip.register_showtool('place', vpr_show)
    chip.register_showtool('place', vpr_screenshot)

    chip.register_showtool('v', yosys_screenshot)
    chip.register_showtool('vg', yosys_screenshot)

    chip.register_showtool('vcd', gtkwave_show)
