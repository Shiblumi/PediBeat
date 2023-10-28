import data_stream as ds

if __name__ == '__main__':
    buffer_stream = ds.DataStream('', 5, 10, 15)
    for i in range(50):
        buffer_stream.feed_buffers(i, i, i)
    buffer_stream.display()