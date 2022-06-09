import xlrd


def read_data_from_excel(path, sheet_name="", row_number=0, col_number=0, everything=None, element_name=None,
                         locator_type=False, locator_value=True):
    """If everything property is set True, this function will return list of rows in
    a single list"""
    if element_name and not everything:
        wb = xlrd.open_workbook(path)
        sh = wb.sheet_by_name(sheet_name)
        for i in range(1, sh.nrows):
            gen_row_obj = sh.row_values(i)
            if element_name in gen_row_obj:
                if locator_type:
                    return gen_row_obj[1]
                elif locator_value:
                    return gen_row_obj[2]
                else:
                    return gen_row_obj[2]

    elif everything:
        final_list_data = []
        wb = xlrd.open_workbook(path)
        sh = wb.sheet_by_name(sheet_name)
        for i in range(1, sh.nrows):
            temp_list = []
            for j in range(sh.ncols):
                temp_list.append(sh.cell_value(i, j))
            final_list_data.append(temp_list)
        return final_list_data

    else:
        wb = xlrd.open_workbook(path)
        sh = wb.sheet_by_name(sheet_name)
        data = sh.cell_value(row_number, col_number)
        return data
