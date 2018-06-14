# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:00:26 2018

@author: Programador1
"""

from KicadModTree import*
from shutil import copy2

#requisito fundamental:
#los array de pin deven ser multiplos de 2

footprint_name = "ATSAMD21J15"
#numeros de pines por array, empesando desde uno
array_pin = 16
pitch = 0.50
#estas medidas son tomadas para un pin en posicion vertical:
largo_pin_x = 0.30
hancho_pin_y = 1.50
#distancia g
distance_between_pads =  0.20
#medida tomada del centro de los pines:
contact_pad_spacing_c1 = 11.40
contact_pad_spacing_c2 = 11.40
#tama;o total del array
arr_size = array_pin*largo_pin_x + distance_between_pads*(array_pin - 1)
#finaliza con el centro del ultimo pin:
array_mitad = ((array_pin/2)-1)*largo_pin_x + largo_pin_x/2 + distance_between_pads*(array_pin/2 - 1) + distance_between_pads/2

# init kicad footprint
kicad_mod = Footprint(footprint_name)
kicad_mod.setDescription("Pic32")
kicad_mod.setTags("ATSAMD21J15_tag")

# set general values
kicad_mod.append(Text(type='reference', text='REF**', at=[0, 0], layer='F.SilkS'))
kicad_mod.append(Text(type='value', text=footprint_name, at=[-0.75, contact_pad_spacing_c1/2 + 1.5*hancho_pin_y], layer='F.Fab'))

# create silscreen
kicad_mod.append(RectLine(start=[-contact_pad_spacing_c1/2 + hancho_pin_y/2, contact_pad_spacing_c2/2 - hancho_pin_y/2], end=[contact_pad_spacing_c1/2 - hancho_pin_y/2, contact_pad_spacing_c2/2 - hancho_pin_y/2], layer='F.SilkS'))
kicad_mod.append(RectLine(start=[-contact_pad_spacing_c1/2 + hancho_pin_y/2, -contact_pad_spacing_c2/2 + hancho_pin_y/2], end=[contact_pad_spacing_c1/2 - hancho_pin_y/2, -contact_pad_spacing_c2/2 + hancho_pin_y/2], layer='F.SilkS'))
kicad_mod.append(RectLine(start=[contact_pad_spacing_c2/2 - hancho_pin_y/2,-contact_pad_spacing_c1/2 + hancho_pin_y/2], end=[contact_pad_spacing_c2/2 - hancho_pin_y/2 ,contact_pad_spacing_c1/2 - hancho_pin_y/2], layer='F.SilkS'))
kicad_mod.append(RectLine(start=[-contact_pad_spacing_c2/2 + hancho_pin_y/2,-contact_pad_spacing_c1/2 + hancho_pin_y/2], end=[-contact_pad_spacing_c2/2 + hancho_pin_y/2,contact_pad_spacing_c1/2 - hancho_pin_y/2 ], layer='F.SilkS'))

# create courtyard
kicad_mod.append(RectLine(start=[-contact_pad_spacing_c1/2, contact_pad_spacing_c2/2], end=[contact_pad_spacing_c1/2, contact_pad_spacing_c2/2], layer='F.CrtYd'))
kicad_mod.append(RectLine(start=[-contact_pad_spacing_c1/2, -contact_pad_spacing_c2/2], end=[contact_pad_spacing_c1/2, -contact_pad_spacing_c2/2], layer='F.CrtYd'))
kicad_mod.append(RectLine(start=[contact_pad_spacing_c2/2,-contact_pad_spacing_c1/2], end=[contact_pad_spacing_c2/2,contact_pad_spacing_c1/2], layer='F.CrtYd'))
kicad_mod.append(RectLine(start=[-contact_pad_spacing_c2/2,-contact_pad_spacing_c1/2], end=[-contact_pad_spacing_c2/2,contact_pad_spacing_c1/2 ], layer='F.CrtYd'))

#creando muesca
kicad_mod.append(RectLine(start=[-array_mitad - 0.25, contact_pad_spacing_c2/2 - hancho_pin_y], end=[-array_mitad + 0.25, contact_pad_spacing_c2/2 - hancho_pin_y], layer='F.SilkS'))

# create pads
count = 0
for i in range(0,4):   
    
    for j in range (0,array_pin): 
        count += 1
        if i==0:
            kicad_mod.append(Pad(number = count, type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT,
                         at=[-array_mitad + j*pitch,contact_pad_spacing_c2/2 ], size=[largo_pin_x, hancho_pin_y], layers=Pad.LAYERS_SMT))

        if i==1:
            kicad_mod.append(Pad(number = count, type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT,
                         at=[contact_pad_spacing_c2/2,array_mitad - j*pitch], size=[hancho_pin_y,largo_pin_x], layers=Pad.LAYERS_SMT))

        if i==2:
            kicad_mod.append(Pad(number = count, type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT,
                         at=[array_mitad - j*pitch,-contact_pad_spacing_c2/2 ], size=[largo_pin_x, hancho_pin_y], layers=Pad.LAYERS_SMT))

        if i==3:
            kicad_mod.append(Pad(number = count, type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT,
                         at=[-contact_pad_spacing_c2/2,-array_mitad + j*pitch], size=[hancho_pin_y,largo_pin_x], layers=Pad.LAYERS_SMT))


# output kicad model
file_handler = KicadFileHandler(kicad_mod)
file_handler.writeFile('Temp/'+ footprint_name + '.kicad_mod')
copy2('64 pin 10x10  TQFP.py', 'Temp/')
copy2('Libreria_dessin.xlsx', 'Temp/')
copy2('Libreria_dessin.csv', 'Temp/')


