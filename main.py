import sys
sys.path.append('src/')
import data_stream as ds

if __name__ == '__main__':
    d_stream = ds.DataStream(5, 10, 15)
    d_stream.initialize_csv('col1', 'col2', 'col3')
    for i in range(50):
        d_stream.feed_buffers(i, i, i)
    d_stream.display()
    d_stream.flush_all_to_csv()
    
# if __name__ == '__main__':
#     d_stream = ds.DataStream(5, 10, 15, csv_file_path='./data/test.csv', save_rate=10)
#     for i in range(50):
#         d_stream.feed_buffers(i, i, i)
#     d_stream.display()