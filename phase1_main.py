from megaverse import Polyanet


# for phase 1, we create polyanet object and call api method to update the mail.
polyanet = Polyanet()
start_row, start_col = 2, 2  
end_row, end_col = 8, 8
for i in range(start_row, end_row+1):
    try:
        polyanet.callPostApi(i, start_col + i - start_row)
        polyanet.callPostApi(i, end_col - (i - start_row))
    except Exception as e:
        print(f"Error calling api: {e}")