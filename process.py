from megaverse import Cometh, Soloon, Polyanet
from constants import *

def process_element(element, row, column, delete=False):
    try:
        if element.endswith(Astral.COMETH.name):
            direction = element.split('_')[0]
            cometh = Cometh(direction.lower())
            if delete:
                cometh.callDeleteApi(row, column)
            else:
                cometh.callPostApi(row, column)
            return element
        
        elif element.endswith(Astral.SOLOON.name):
            color = element.split('_')[0]
            soloon = Soloon(color.lower())
            if delete:
                soloon.callDeleteApi(row, column)
            else:
                soloon.callPostApi(row, column)
            return element
        
        elif element == Astral.POLYANET.name:
            polyanet = Polyanet()
            if delete:
                polyanet.callDeleteApi(row, column)
            else:
                polyanet.callPostApi(row, column)
            return element
    
    except Exception as e:
        print(f"Error processing element: {e}")
    
    return None

def process_data(data, delete=False):
    return [
        [
            process_element(item, row_idx, col_idx, delete)
            for col_idx, item in enumerate(row)
        ]
        for row_idx, row in enumerate(data)
    ]



