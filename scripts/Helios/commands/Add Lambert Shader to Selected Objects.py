sel = mc.ls(sl=True)
shader = mel.eval('createRenderNodeCB -asShader "surfaceShader" lambert "";')
mc.select(sel)
mel.eval('sets -e -forceElement ' + shader + 'SG;')
mc.select(shader)