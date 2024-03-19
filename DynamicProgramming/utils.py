def print_table(table):
  for column in table:
    print_str = ''
    for cell in column:
        print_str+=(str(cell)+'\t')
    print(print_str)