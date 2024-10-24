def external_merge_sort(input_file, output_file):
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()
    chunks = [lines[i:i+10] for i in range(0, len(lines), 10)]
    for i, chunk in enumerate(chunks):
        with open(f'{input_file}-{i}', 'w') as f_out:
            f_out.writelines(sorted(chunk))
    with open(output_file, 'w') as f_out:
        f_out.writelines(merge_files([f'{input_file}-{i}' for i in range(len(chunks))]))


def merge_files(files):
    lines = []
    files_handles = [open(file, 'r') for file in files]
    for i, file in enumerate(files_handles):
        line = file.readline().strip()
        if line:
            lines.append((line, i))
        else:
            files_handles[i].close()
    while lines:
        min_line = min(lines)
        yield min_line[0] + '\n'
        idx = min_line[1]
        line = files_handles[idx].readline().strip()
        if line:
            lines[idx] = (line, idx)
        else:
            files_handles[idx].close()
            lines.pop(idx)

if __name__ == '__main__':
    external_merge_sort('alg/lab10/data.txt', 'alg/lab10/out.txt')

