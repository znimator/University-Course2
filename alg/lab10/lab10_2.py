import heapq

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
    files_handles = [open(file, 'r') for file in files]
    heap = []
    for i, file in enumerate(files_handles):
        line = file.readline().strip()
        if line:
            heapq.heappush(heap, (line, i))
        else:
            file.close()
    while heap:
        min_line, idx = heapq.heappop(heap)
        yield min_line + '\n'
        next_line = files_handles[idx].readline().strip()
        if next_line:
            heapq.heappush(heap, (next_line, idx))
        else:
            files_handles[idx].close()
    
    # Ensure all file handles are closed
    for file in files_handles:
        if not file.closed:
            file.close()

if __name__ == '__main__':
    external_merge_sort('alg/lab10/data.txt', 'alg/lab10/out.txt')