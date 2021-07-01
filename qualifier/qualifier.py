from typing import Any, List, Optional, NewType
import copy

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    "chars to draw table"
    longest_sample = copy.copy(rows[0])
    table = ''

    vertical_line = '│'
    horizontal_line = '─'
    top_left = '┌'
    top_right = '┐'
    middle_left = '├'
    middle = '┼'
    middle_right = '┤'
    top_tee = '┬'
    inverted_tee = '┴'
    bottom_left = '└'
    bottom_right = '┘'

    class Fruit:
        def __init__(self, fruit: str):
            self.fruit = fruit
        
        def __len__(self):
            return len(self.fruit)

        def __str__(self):
            return self.fruit

        def __repr__(self):
            return f'Fruit <{self.fruit}>'
    
    # Check One Dimensional Array
    if len(longest_sample) == 1:
        longest_length = len(longest_sample[0])
        for x in range(len(rows)):
            # find longest word
            new_sample = rows[x]
            if len(longest_sample[0]) < len(new_sample[0]):
                longest_sample = new_sample
                longest_length = len(new_sample[0])
        i = 0
        # Print 1-D Array
        buffer_spaces = longest_length
        table += str(f'{top_left}{horizontal_line}{horizontal_line * longest_length}{horizontal_line}{top_right}\n')
        # Check if single column table has a label
        if labels:
            if centered is True:
                table += str(f'{vertical_line} {labels[0]:^{buffer_spaces}} {vertical_line}\n')
            else:
                table += str(f'{vertical_line} {labels[0]:<{buffer_spaces}} {vertical_line}\n')
            table += str(f'{middle_left}{horizontal_line}{horizontal_line * longest_length}{horizontal_line}{middle_right}\n')
        while i < len(rows):
            if centered is True:
                table += str(f'{vertical_line} {rows[i][0]:^{buffer_spaces}} {vertical_line}\n')
            else:
                table += str(f'{vertical_line} {rows[i][0]:<{buffer_spaces}} {vertical_line}\n')

            i += 1
        table += str(f'{bottom_left}{horizontal_line}{horizontal_line * longest_length}{horizontal_line}{bottom_right}\n')
    else:
        longest_length = []
        longest = []
        # Build temp list with longest & biggest elements
        for obj in rows:
            x = 0
            for item in obj:
                try:
                    if item == None:
                        if len(str(longest_sample[x])) <= len(str(item)):
                            longest_sample[x] = str(item)
                    elif isinstance(item, int) or isinstance(item, float):
                        if longest_sample[x] <= item:
                            longest_sample[x] = item
                    elif isinstance(item, complex):
                        if len(str(longest_sample[x])) <= len(str(item)):
                            longest_sample[x] = str(item)
                    elif len(longest_sample[x]) <= len(item):
                        longest_sample[x] = item
                except:
                    longest_sample[x] = Fruit(str(item))

                x += 1

        for i in longest_sample:
            if isinstance(i, int) or isinstance(i, float):
               longest_length.append(len(str(i)))
            else:
               longest_length.append(len(i))
        if labels:
            for x in range(len(labels)):
                if isinstance(labels[x], int) or labels[x] == None or isinstance(labels[x], float) or isinstance(labels[x], complex):
                    if len(str(labels[x])) > longest_length[x]:
                        longest_length[x] = len(str(labels[x]))
                if len(str(labels[x])) > longest_length[x]:
                    longest_length[x] = len(str(labels[x]))

        # print top lines for table
        table += str(f'{top_left}')
        for i in range(len(longest_length)):
            table += str(f'{horizontal_line}{horizontal_line * longest_length[i]}')
            if len(longest_length) > i+1:
                table += str(f'{horizontal_line}{top_tee}')
        table += str(f'{horizontal_line}{top_right}\n')
        
        # If labels exist format accordingly
        if labels:
            table += str(f'{vertical_line}')    
            if centered is True:
                for ix in range(len(labels)):
                    if labels[ix] == None:
                        table += str(f' {str(labels[ix]):^{longest_length[ix]}} {vertical_line}')
                    else:
                        table += str(f' {labels[ix]:^{longest_length[ix]}} {vertical_line}')
            else:
                for ix in range(len(labels)):
                    table += str(f' {labels[ix]:<{longest_length[ix]}} {vertical_line}')
            table += str(f'\n{middle_left}')
            for i in range(len(longest_length)):
                table += str(f'{horizontal_line}{horizontal_line * longest_length[i]}')
                if len(longest_length) > i+1:
                    table += str(f'{horizontal_line}{middle}')
            table += str(f'{horizontal_line}{middle_right}\n')

        for idx in rows:
            table += str(f'{vertical_line}')
            for ix in range(len(idx)):
                if centered is True:
                    table += str(f' {str(idx[ix]):^{longest_length[ix]}} {vertical_line}')
                else:
                    table += str(f' {str(idx[ix]):<{longest_length[ix]}} {vertical_line}')
            table += str('\n')

        # print bottom lines for table
        table += str(f'{bottom_left}')
        for i in range(len(longest_length)):
            table += str(f'{horizontal_line}{horizontal_line * longest_length[i]}')
            if len(longest_length) > i+1:
                table += str(f'{horizontal_line}{inverted_tee}')
        table += str(f'{horizontal_line}{bottom_right}\n')
    
    return table